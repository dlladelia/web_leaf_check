def get_info_daun(nama_daun):
    info = {
        "bandotan": {
            "nama_lengkap": "Bandotan (Ageratum conyzoides L.)",
            "kategori": "Tanaman Beracun",
            "deskripsi": "Bandotan (Ageratum conyzoides L.) meskipun umumnya aman berdasarkan penelitian toksisitas, tetap perlu diwaspadai karena dapat menimbulkan efek samping pada hati, ginjal, parameter hematologi, dan jantung jika dikonsumsi berlebihan.",
            "solusi": "Hindari konsumsi berlebihan dan jauhi dari anak-anak."
        },
        "gympie": {
            "nama_lengkap": "Gympie-Gympie (Dendrocnide moroides)",
            "kategori": "Tanaman Beracun",
            "deskripsi": "Gympie-Gympie (Dendrocnide moroides) jika terkena batang atau daunnya, dapat menyebabkan iritasi ringan hingga neuropati parah. Pembengkakan bisa mereda dalam sejam atau bertahan 24 jam, tetapi nyeri dan gatal bisa berbulan-bulan.",
            "solusi": "Gunakan sarung tangan dan hindari kontak langsung dengan tanaman ini."
        },
        "jelatang": {
            "nama_lengkap": "Jelatang (Laportea interrupta L.)",
            "kategori": "Tanaman Beracun",
            "deskripsi": "Jelatang (Laportea interrupta L.) dikategorikan sebagai tumbuhan beracun karena kontak langsung dengan trikomanya menimbulkan reaksi berupa bintik merah, rasa gatal, dan sensasi panas pada kulit yang terpapar.",
            "solusi": "Cuci dengan air sabun dan oleskan salep antihistamin bila perlu."
        },
        "kelor": {
            "nama_lengkap": "Kelor (Moringa oleifera)",
            "kategori": "Tanaman Herbal",
            "deskripsi": "Daun Kelor (Moringa oleifera) digunakan sebagai antidiabetes dan antioksidan. Bagian biji, daun, dan kayunya bermanfaat untuk menurunkan tekanan darah, melancarkan sirkulasi, serta memiliki sifat antitumor, antibakteri, dan antiinflamasi.",
            "solusi": "Dapat dikonsumsi secara rutin sebagai suplemen alami."
        },
        "kemangi": {
            "nama_lengkap": "Kemangi (Ocimum basilicum L.)",
            "kategori": "Tanaman Herbal",
            "deskripsi": "Kemangi (Ocimum basilicum L.) terkenal dengan sifat antibakterinya, menunjukkan aktivitas antijamur, antioksidan, anti-penuaan, anti-inflamasi, serta membantu pengobatan tradisional seperti sakit kepala, stres, sembelit, dan gangguan ginjal.",
            "solusi": "Dapat dikonsumsi sebagai lalapan atau teh herbal."
        },
        "mint": {
            "nama_lengkap": "Mint (Mentha Spicata)",
            "kategori": "Tanaman Herbal",
            "deskripsi": "Daun Mint (Mentha Spicata) mengandung mentol yang membantu melancarkan sirkulasi darah serta meredakan mual, kembung, dan kram. Kandungan tanin dan flavonoidnya juga berpotensi meningkatkan fungsi sistem pencernaan.",
            "solusi": "Dapat digunakan sebagai minuman dingin atau aromaterapi."
        },
        "saga": {
            "nama_lengkap": "Saga Rambat (Abrus precatorius)",
            "kategori": "Tanaman Beracun",
            "deskripsi": "Saga Rambat (Abrus precatorius) memiliki daun dan biji yang mengandung abrin, protein sangat beracun yang menghambat sintesis protein dan menyebabkan kerusakan hati, ginjal, serta limpa, bahkan dapat menimbulkan kematian jika dikonsumsi.",
            "solusi": "Jauhkan dari anak-anak dan hindari konsumsi."
        },
        "sirih": {
            "nama_lengkap": "Sirih (Piper betle L.)",
            "kategori": "Tanaman Herbal",
            "deskripsi": "Daun Sirih (Piper betle L.) sering digunakan karena mengandung kalsium, vitamin, dan senyawa bioaktif seperti fenolat dan minyak atsiri, yang berfungsi sebagai antibakteri, antiseptik, anti-inflamasi, dan pereda gatal maupun batuk.",
            "solusi": "Dapat digunakan untuk pengobatan alami luka dan bau mulut."
        }
    }
    return info.get(nama_daun, {
        "nama_lengkap": "Tidak Diketahui",
        "kategori": "Tidak Diketahui",
        "deskripsi": "Informasi tidak tersedia.",
        "solusi": "-"
    })


