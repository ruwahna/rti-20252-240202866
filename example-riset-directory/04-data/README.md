# 04-data

Folder ini adalah tempat khusus di mana saya menyimpan seluruh kumpulan data mentah (*raw data*) yang diperoleh langsung dari proses pengumpulan data di lapangan, sebelum data tersebut dimanipulasi atau dianalisis.

## Isi yang Diharapkan

- **Data Mentah (*Raw Data*):** File hasil *export* kuesioner dari *platform survey* (seperti Google Form) dalam format CSV atau Excel.
- **Data Hasil Pembersihan (*Cleaned Data*):** Salinan data yang telah dibersihkan dari nilai pencilan (*outlier* ekstrem), data ganda (*duplikat*), dan data kosong (*missing values*), sehingga siap untuk diuji secara statistik.
- **Kamus Data (*Data Dictionary*):** Penjelasan singkat mengenai deskripsi setiap kolom (misalnya penjelasan apa arti dari kolom `SUS_Score`).

## Catatan Penting

Data di dalam folder ini harus selalu dijaga orisinalitasnya. Segala bentuk *output* berupa grafik visualisasi (*bar chart*) atau nilai hasil uji statistik (*p-value* T-Test) tidak boleh diletakkan di sini, melainkan akan saya simpan di folder *output* khusus agar tidak tercampur secara historis dengan sumber *dataset*.

## Berkas Terkait

- `survey_data_signal_sakpole.csv` — Kumpulan data mentah asli yang memuat data dari 200 responden awal terkait pengujian aplikasi SIGNAL dan Sakpole.
