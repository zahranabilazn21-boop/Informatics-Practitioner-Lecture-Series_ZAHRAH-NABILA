# Informatics-Practitioner-Lecture-Series_ZAHRAH-NABILA

Python implementations of six Informatics seminar case studies covering Data Analytics, Credit Risk Prediction, GIS using real-world public datasets, Machine Learning, High Performance Computing (HPC), Interactive Data Visualization, and Forest Fire Analysis.

# Penjelasan Enam Studi Kasus Informatics Practitioner Lecture Series

## 1. Make Sense of Data with Analysis and AI

**Judul:** Analisis Risiko Kredit Menggunakan Data Analytics dan Logistic Regression.

### A. Latar Belakang

Pemberian kredit memiliki risiko gagal bayar yang dapat memengaruhi kondisi keuangan lembaga pemberi kredit. Analisis data dapat membantu mengidentifikasi karakteristik nasabah yang berkaitan dengan risiko tersebut. Studi kasus ini menggunakan dataset Default of Credit Card Clients dari UCI Machine Learning Repository, yang berisi data historis nasabah kartu kredit di Taiwan.

### B. Metode dan Implementasi Python

Analisis dilakukan melalui pembersihan data, pemeriksaan nilai kosong, dan analisis deskriptif untuk mengetahui distribusi nasabah serta proporsi gagal bayar. Analisis diagnostik digunakan untuk mengeksplorasi hubungan antara karakteristik nasabah dan status pembayaran. Selanjutnya, Logistic Regression digunakan untuk memprediksi probabilitas gagal bayar, dengan evaluasi menggunakan precision, recall, F1-score, dan ROC-AUC.

### C. Hasil dan Manfaat

Program menghasilkan ringkasan karakteristik nasabah, distribusi status gagal bayar, serta evaluasi performa model. Hasil analisis dapat membantu menjelaskan bagaimana data historis digunakan untuk mengidentifikasi risiko kredit dan mendukung penentuan prioritas peninjauan nasabah. Namun, hasil dari dataset Taiwan tidak dapat langsung digeneralisasi untuk perusahaan Indonesia tanpa pengujian menggunakan data yang sesuai.

## 2. Global Infrastructure to Address Local Challenge with HPC

**Judul:** Perbandingan Komputasi Serial dan Paralel untuk Pengolahan Data Kualitas Udara.

### A. Latar Belakang

Data lingkungan dapat memiliki banyak pengamatan dan variabel yang membutuhkan pengolahan berulang. Pemrosesan paralel memungkinkan pekerjaan dibagi ke beberapa proses untuk meningkatkan efisiensi komputasi. Studi kasus ini menggunakan dataset Air Quality dari UCI yang berisi pengukuran historis sensor kualitas udara di Italia.

### B. Metode dan Implementasi Python

Program menghitung statistik deskriptif pada kolom numerik menggunakan dua pendekatan, yaitu komputasi serial dan komputasi paralel dengan ProcessPoolExecutor. Waktu eksekusi kedua metode dibandingkan untuk menghitung speedup dan menilai efisiensi pembagian pekerjaan.

### C. Hasil dan Manfaat

Program menghasilkan ringkasan statistik kualitas udara, waktu eksekusi, dan perbandingan kinerja kedua metode. Hasilnya dapat digunakan untuk memahami manfaat serta keterbatasan komputasi paralel. Pada dataset kecil, komputasi paralel bisa lebih lambat karena biaya pembuatan proses dan pemindahan data. Pengujian ini menggambarkan kinerja komputer yang digunakan, bukan performa supercomputer.

## 3. Career and Competition in Industrial Era with GIS

**Judul:** Pemetaan dan Analisis Fasilitas Publik Menggunakan OpenStreetMap dan Python.

### A. Latar Belakang

Informasi geografis diperlukan untuk memahami persebaran fasilitas publik, seperti rumah sakit, klinik, sekolah, dan apotek. GIS memungkinkan data lokasi dikumpulkan dan dianalisis untuk mendukung perencanaan wilayah. Studi kasus ini menggunakan OpenStreetMap sebagai sumber data geografis terbuka.

### B. Metode dan Implementasi Python

Program menggunakan OSMnx untuk mengambil data fasilitas berdasarkan wilayah dan kategori yang dipilih. Data kemudian diolah menggunakan Pandas untuk menghitung jumlah fasilitas menurut jenis, menampilkan sampel lokasi, dan menyimpan koordinat lintang serta bujur ke dalam file CSV. Untuk fasilitas berbentuk poligon, program menggunakan titik pusat geometri sebagai representasi lokasi.

### C. Hasil dan Manfaat

Program menghasilkan daftar fasilitas publik yang ditemukan pada wilayah pilihan, ringkasan jumlah fasilitas berdasarkan jenis, dan koordinat yang dapat digunakan untuk analisis spasial lanjutan. Hasilnya dapat membantu mengidentifikasi persebaran fasilitas serta menjadi dasar awal analisis aksesibilitas. Namun, kelengkapan OpenStreetMap berbeda antarwilayah sehingga data perlu diverifikasi sebelum digunakan dalam keputusan resmi.

## 4. Introduction to Machine Learning

**Judul:** Prediksi Penjualan Harian Menggunakan Data Transaksi Ritel.

### A. Latar Belakang

Perusahaan ritel perlu memperkirakan permintaan produk untuk mengurangi risiko kelebihan atau kekurangan stok. Machine Learning dapat mempelajari pola hubungan antara karakteristik waktu dan jumlah penjualan berdasarkan data historis. Studi kasus ini menggunakan dataset Online Retail dari UCI yang memuat transaksi ritel historis sebuah perusahaan di Inggris pada 2010–2011.

### B. Metode dan Implementasi Python

Program membersihkan data transaksi, menghapus faktur pembatalan dan kuantitas yang tidak valid, lalu mengagregasi penjualan per hari. Fitur yang digunakan mencakup hari dalam minggu, bulan, tanggal, penjualan hari sebelumnya, dan penjualan tujuh hari sebelumnya. Model DummyRegressor dibandingkan dengan RandomForestRegressor menggunakan MAE dan RMSE. Pembagian data dilakukan berdasarkan urutan waktu.

### C. Hasil dan Manfaat

Program menghasilkan data penjualan harian dan perbandingan kesalahan prediksi antara model baseline dan Random Forest. Hasil tersebut dapat membantu menilai apakah model mampu mempelajari pola penjualan historis dan berpotensi mendukung perencanaan persediaan. Namun, performa pada satu dataset tidak otomatis berlaku untuk bisnis lain atau kondisi pasar saat ini.

## 5. Human-Computer Interaction & Data Visualization

**Judul:** Pengembangan Dashboard Interaktif untuk Analisis Kualitas Udara.

### A. Latar Belakang

Data sensor lingkungan sering disajikan dalam bentuk tabel yang sulit digunakan untuk membandingkan pola dan perubahan dari waktu ke waktu. Visualisasi data membantu pengguna memahami informasi dengan lebih cepat, sedangkan prinsip Human-Computer Interaction (HCI) memastikan antarmuka mudah dipahami dan digunakan.

### B. Metode dan Implementasi Python

Dashboard dibuat menggunakan Streamlit dan Pandas dengan fitur pemilihan variabel sensor, indikator jumlah pengukuran valid, rata-rata dan median, grafik, serta tabel data. Nilai hilang yang ditandai dengan kode khusus pada dataset juga ditangani sebelum visualisasi.

### C. Hasil dan Manfaat

Dashboard memungkinkan pengguna mengeksplorasi pengukuran kualitas udara secara interaktif tanpa memeriksa seluruh tabel secara manual. Grafik membantu mengidentifikasi pola, sedangkan indikator dan tabel mendukung pemeriksaan data secara lebih terarah. Penerapan HCI terlihat pada penggunaan label yang jelas, kontrol pengguna, dan umpan balik antarmuka. Data yang ditampilkan merupakan pengukuran historis, bukan kondisi kualitas udara secara real-time.

## 6. Analisis Lingkungan dan Kebakaran Hutan Menggunakan AI

**Judul:** Analisis Faktor Lingkungan yang Berkaitan dengan Luas Kebakaran Hutan Menggunakan Random Forest.

### A. Latar Belakang

Kebakaran hutan dapat berkaitan dengan kondisi lingkungan, seperti suhu, kelembapan, angin, dan curah hujan. Analisis data dapat membantu mengidentifikasi pola yang berkaitan dengan luas area terbakar. Studi kasus ini menggunakan dataset Forest Fires dari UCI yang berisi pengamatan meteorologis dan luas kebakaran hutan di Portugal.

### B. Metode dan Implementasi Python

Program memeriksa distribusi luas area terbakar, menganalisis korelasi antarvariabel, dan membangun model RandomForestRegressor untuk memprediksi luas kebakaran dengan transformasi logaritmik. Evaluasi model menggunakan MAE, RMSE, dan \(R^2\).

### C. Hasil dan Manfaat

Program menghasilkan statistik deskriptif, korelasi antarvariabel, dan metrik evaluasi model. Hasilnya membantu memahami bagaimana Machine Learning dapat digunakan untuk mempelajari pola data lingkungan dan memperkirakan luas area terbakar. Namun, hubungan statistik tidak membuktikan sebab-akibat. Dataset ini juga bukan data citra satelit, sehingga tidak dapat digunakan untuk menyimpulkan penyebab langsung deforestasi.
