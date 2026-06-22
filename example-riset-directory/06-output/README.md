# 06-output

Folder ini dikhususkan untuk menyimpan hasil akhir dari proses pengolahan data mentah. Semua *file* berupa angka metrik perhitungan, visualisasi grafik, dan tabel yang nantinya akan dicantumkan di naskah laporan akan bermuara dan bermukim di folder ini.

## Struktur dan Isi yang Diharapkan

### Folder `tables/` (Tabel Statistik)
Berisi *file* berupa *spreadsheet* (seperti CSV atau Excel) yang merekapitulasi hasil akhir perhitungan statistik.
- `descriptive_stats.csv` — Tabel rekap nilai *Mean*, *Standard Deviation* (SD), dan ukuran sampel (n) dari pengujian skor SUS SIGNAL dan Sakpole.
- `t_test_results.csv` — Tabel yang menyimpan angka eksak hasil uji hipotesis (seperti nilai *t-statistic*, *p-value*, derajat kebebasan, dan besaran *Cohen's d*).

### Folder `figures/` (Grafik Visual)
Berisi *file* gambar (PNG/JPG/SVG) hasil visualisasi pengolahan data.
- `fig_sus_comparison.png` — Diagram batang (*bar chart*) yang membandingkan rata-rata skor SUS SIGNAL dengan Sakpole secara visual, dilengkapi dengan *error bar* untuk mendemonstrasikan ketidakpastian/standar deviasi.
- `fig_sus_distribution.png` — Grafik persebaran data (*box plot* atau kurva lonceng) yang secara visual memperlihatkan rentang pemberian skor oleh 194 responden.

## Catatan Penting
File yang berada di dalam folder `06-output` ini murni merupakan aset hasil akhir (bukan bahan baku eksperimen). Idealnya, seluruh *file* di sini diproduksi secara otomatis dengan mengeksekusi *script* yang ada di folder `05-kode/`, yang mengambil sumber datanya langsung dari folder `04-data/`.
