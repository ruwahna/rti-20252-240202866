# 05-kode

Folder ini merupakan ruang penyimpanan utama untuk seluruh skrip (*script*) atau kode sumber (*source code*) pemrograman yang saya susun dan saya gunakan selama pelaksanaan riset komparatif *usability* ini.

## Struktur dan Isi yang Diharapkan

- **Skrip Pembersihan Data (*Data Cleaning*):** Kode pemrograman (seperti bahasa Python atau R) yang berfungsi untuk membuang pencilan skor (*outlier* > 100), membersihkan data kosong (*missing value*), dan memastikan dataset final valid untuk diuji.
- **Skrip Pengujian Statistik:** Kode otomatisasi untuk menghitung rumusan *Independent T-Test*, memperoleh *p-value*, serta menghitung besaran efek (*Cohen's d*) dari dataset yang telah dibersihkan.
- **Skrip Visualisasi:** Kode tambahan (seperti Matplotlib/Seaborn) untuk membangun diagram grafik pendukung (misalnya *bar chart* yang dilengkapi *error bar*).

## Berkas Terkait

- `check_data.py` — Skrip utama berbasis Python (menggunakan kepustakaan Pandas dan SciPy) yang secara khusus saya buat untuk meninjau data mentah, mendeteksi anomali/outlier skor SUS responden, sekaligus mengeksekusi perhitungan T-Test secara komputasi otomatis.
