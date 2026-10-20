## 4. Introduction to Machine Learning

**Judul:** Prediksi Penjualan Harian Menggunakan Data Transaksi Ritel.

### A. Latar Belakang

Perusahaan ritel perlu memperkirakan permintaan produk untuk mengurangi risiko kelebihan atau kekurangan stok. Machine Learning dapat mempelajari pola hubungan antara karakteristik waktu dan jumlah penjualan berdasarkan data historis. Studi kasus ini menggunakan dataset Online Retail dari UCI yang memuat transaksi ritel historis sebuah perusahaan di Inggris pada 2010–2011.

### B. Metode dan Implementasi Python

Program membersihkan data transaksi, menghapus faktur pembatalan dan kuantitas yang tidak valid, lalu mengagregasi penjualan per hari. Fitur yang digunakan mencakup hari dalam minggu, bulan, tanggal, penjualan hari sebelumnya, dan penjualan tujuh hari sebelumnya. Model DummyRegressor dibandingkan dengan RandomForestRegressor menggunakan MAE dan RMSE. Pembagian data dilakukan berdasarkan urutan waktu.

### C. Hasil dan Manfaat

Program menghasilkan data penjualan harian dan perbandingan kesalahan prediksi antara model baseline dan Random Forest. Hasil tersebut dapat membantu menilai apakah model mampu mempelajari pola penjualan historis dan berpotensi mendukung perencanaan persediaan. Namun, performa pada satu dataset tidak otomatis berlaku untuk bisnis lain atau kondisi pasar saat ini.
