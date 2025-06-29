from flask import Flask, render_template, request, send_from_directory
import numpy as np
import tensorflow as tf
import os
import time
from PIL import Image
from info_daun import get_info_daun
from tensorflow.keras.applications.efficientnet import preprocess_input

# Inisialisasi interpreter model
interpreter = tf.lite.Interpreter(model_path="static/EfficientNetB0_24.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Daftar kelas
classes = ["bandotan", "gympie", "jelatang", "kelor", "kemangi", "mint", "saga", "sirih"]

# Inisialisasi Flask
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/upload"
COUNT = 0
ERROR_COUNT = 0
TOTAL_COUNT = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home():
    global COUNT, ERROR_COUNT, TOTAL_COUNT

    file = request.files['image']
    filename = f"{COUNT}.jpg"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    try:
        # Timer mulai
        start_time = time.time()

        # Preprocessing EfficientNetB0
        image = Image.open(filepath).convert('RGB')
        image = image.resize((224, 224))
        image_array = np.array(image, dtype=np.float32)
        image_array = preprocess_input(image_array)
        input_data = np.expand_dims(image_array, axis=0)

        # Inference dengan TFLite
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])[0]

        # klasifikasi & fail-safe
        top2 = prediction.argsort()[-2:][::-1]
        confidence_top = prediction[top2[0]] * 100
        confidence_gap = confidence_top - prediction[top2[1]] * 100
        fail_safe = confidence_top < 60 or confidence_gap < 10
        predicted_class = classes[top2[0]]

        # Hitung waktu & error
        inference_time = round(time.time() - start_time, 3)
        TOTAL_COUNT += 1
        if fail_safe:
            ERROR_COUNT += 1
        error_rate = f"{(ERROR_COUNT / TOTAL_COUNT) * 100:.2f}%" if TOTAL_COUNT > 0 else "0%"

        # Ambil info daun
        info = get_info_daun(predicted_class)

        data = {
            'kelas': predicted_class.capitalize(),
            'kategori': info['kategori'],
            'akurasi': f"{confidence_top:.2f}%",
            'deskripsi': info['deskripsi'],
            'solusi': info['solusi'],
            'nama_lengkap': info['nama_lengkap'],
            'filename': filename,
            'inference_time': inference_time,
            'fail_safe': fail_safe,
            'error_rate': error_rate
        }

        COUNT += 1
        return render_template('deteksi.html', data=data)

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {str(e)}")
        return render_template('deteksi.html', data={
            'kelas': 'Tidak Diketahui',
            'kategori': 'Tidak Tersedia',
            'akurasi': '0%',
            'deskripsi': 'Terjadi kesalahan saat memproses gambar.',
            'solusi': 'Pastikan gambar jelas dan sesuai format.',
            'nama_lengkap': 'Unknown',
            'filename': filename,
            'inference_time': '-',
            'fail_safe': True,
            'error_rate': '100%'
        })

@app.route('/load_img/<filename>')
def load_img(filename):
    return send_from_directory('static/upload', filename)

if __name__ == '__main__':
    app.run(debug=True)
