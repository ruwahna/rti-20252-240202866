# Tahap 1 — Validasi Data & Preprocessing

**Status:** Selesai  
**Tujuan:** Memastikan integritas dan kualitas data mentah hasil kuesioner sebelum dilakukan analisis statistik deskriptif dan inferensial.

---

## 1. Validasi Kelengkapan (Completeness)
- **Sumber Data:** Kuesioner online yang disebarkan kepada pengguna SIGNAL dan New Sakpole.
- **Data Masuk Awal:** 200 responden.
- **Pengecekan:** Mengidentifikasi data kosong atau tidak lengkap (missing values).
- **Temuan:** Terdapat 5 data kosong (2 pada SIGNAL, 3 pada New Sakpole) disebabkan responden menutup formulir sebelum mengirim.
- **Keputusan:** Diterapkan *listwise deletion* (menghapus baris kosong) karena tingkat data hilang sangat rendah (2.5% < 5%) dan diasumsikan terjadi secara acak (*Missing Completely at Random* - MCAR).

## 2. Validasi Range & Logika (Range & Logic Check)
- **Pengecekan:** Memastikan nilai skor berada dalam rentang valid instrumen SUS (0 s/d 100).
- **Temuan:** Ditemukan 1 baris data dengan skor SUS bernilai 120.0 (outlier/anomaly ekstrem). Skor SUS secara teoritis memiliki batas maksimal 100.
- **Keputusan:** Data dibuang karena diidentifikasi sebagai kesalahan pengetikan (*typo*) dari responden yang tidak dapat diperbaiki.

## 3. Hasil Akhir Data Bersih (Cleaned Data)
- **SIGNAL:** 97 responden valid.
- **New Sakpole:** 97 responden valid.
- **Total Valid (n):** 194 responden.
- **Penyimpanan:** Data bersih disimpan dalam berkas [survey_data_signal_sakpole.csv](../04-data/survey_data_signal_sakpole.csv).
