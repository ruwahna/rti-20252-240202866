# Tahap 2 — Uji Deskriptif & Visualisasi

**Status:** Selesai  
**Tujuan:** Menyajikan ringkasan statistik deskriptif dari data usability (SUS Score) dan memvisualisasikan persebaran data serta perbandingannya.

---

## 1. Statistik Deskriptif Rata-rata
Metrik deskriptif dihitung menggunakan pustaka Python `pandas` dan `numpy` pada script `generate_output.py`.

- **SIGNAL (n = 97):**
  - Rata-rata (*Mean*): 76.90
  - Standar Deviasi (*SD*): 12.79
- **New Sakpole (n = 97):**
  - Rata-rata (*Mean*): 67.16
  - Standar Deviasi (*SD*): 12.03

Hasil deskriptif disimpan dalam bentuk tabel markdown pada [descriptive_stats.md](../06-output/tables/descriptive_stats.md).

## 2. Pembuatan Figure Visualisasi
Dihasilkan dua berkas gambar visualisasi menggunakan pustaka `matplotlib` untuk dimasukkan ke laporan dan draf manuskrip:

1. **Bar Chart Perbandingan Rata-rata (`fig_sus_comparison.png`):**
   - Menampilkan rata-rata skor SUS untuk SIGNAL dan New Sakpole.
   - Dilengkapi *error bars* berbasis standar deviasi.
   - Menambahkan garis putus-putus merah horizontal pada skor **68** sebagai indikator batas rata-rata kelayakan minimum usability industri.
   - Output: [fig_sus_comparison.png](../06-output/figures/fig_sus_comparison.png)

2. **Box Plot Persebaran Skor (`fig_sus_distribution.png`):**
   - Menampilkan kuartil, median, dan persebaran sebaran data mentah dari responden untuk melihat apakah terdapat anomali setelah pembersihan.
   - Output: [fig_sus_distribution.png](../06-output/figures/fig_sus_distribution.png)
