## 2. Global Infrastructure to Address Local Challenge with HPC

**Judul:** Perbandingan Komputasi Serial dan Paralel untuk Pengolahan Data Kualitas Udara.

### A. Latar Belakang

Data lingkungan dapat memiliki banyak pengamatan dan variabel yang membutuhkan pengolahan berulang. Pemrosesan paralel memungkinkan pekerjaan dibagi ke beberapa proses untuk meningkatkan efisiensi komputasi. Studi kasus ini menggunakan dataset Air Quality dari UCI yang berisi pengukuran historis sensor kualitas udara di Italia.

### B. Metode dan Implementasi Python

Program menghitung statistik deskriptif pada kolom numerik menggunakan dua pendekatan, yaitu komputasi serial dan komputasi paralel dengan ProcessPoolExecutor. Waktu eksekusi kedua metode dibandingkan untuk menghitung speedup dan menilai efisiensi pembagian pekerjaan.

### C. Hasil dan Manfaat

Program menghasilkan ringkasan statistik kualitas udara, waktu eksekusi, dan perbandingan kinerja kedua metode. Hasilnya dapat digunakan untuk memahami manfaat serta keterbatasan komputasi paralel. Pada dataset kecil, komputasi paralel bisa lebih lambat karena biaya pembuatan proses dan pemindahan data. Pengujian ini menggambarkan kinerja komputer yang digunakan, bukan performa supercomputer.
