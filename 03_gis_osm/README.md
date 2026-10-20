## 3. Career and Competition in Industrial Era with GIS

**Judul:** Pemetaan dan Analisis Fasilitas Publik Menggunakan OpenStreetMap dan Python.

### A. Latar Belakang

Informasi geografis diperlukan untuk memahami persebaran fasilitas publik, seperti rumah sakit, klinik, sekolah, dan apotek. GIS memungkinkan data lokasi dikumpulkan dan dianalisis untuk mendukung perencanaan wilayah. Studi kasus ini menggunakan OpenStreetMap sebagai sumber data geografis terbuka.

### B. Metode dan Implementasi Python

Program menggunakan OSMnx untuk mengambil data fasilitas berdasarkan wilayah dan kategori yang dipilih. Data kemudian diolah menggunakan Pandas untuk menghitung jumlah fasilitas menurut jenis, menampilkan sampel lokasi, dan menyimpan koordinat lintang serta bujur ke dalam file CSV. Untuk fasilitas berbentuk poligon, program menggunakan titik pusat geometri sebagai representasi lokasi.

### C. Hasil dan Manfaat

Program menghasilkan daftar fasilitas publik yang ditemukan pada wilayah pilihan, ringkasan jumlah fasilitas berdasarkan jenis, dan koordinat yang dapat digunakan untuk analisis spasial lanjutan. Hasilnya dapat membantu mengidentifikasi persebaran fasilitas serta menjadi dasar awal analisis aksesibilitas. Namun, kelengkapan OpenStreetMap berbeda antarwilayah sehingga data perlu diverifikasi sebelum digunakan dalam keputusan resmi.
