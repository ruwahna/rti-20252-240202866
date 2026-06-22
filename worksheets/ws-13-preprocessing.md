# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

**PREPROCESSING LOG**

**Dataset           :** `survey_data_signal_sakpole.csv`
**Jumlah data awal  :** 200 baris (records)

**Cleaning:**

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 5           | Listwise deletion (Drop baris) | Missing rate < 5% (2.5%), diasumsikan random (user tutup browser). |
| Duplikat| 0           | -          | Tidak ada data duplikat yang terdeteksi. |
| Error   | 1           | Drop baris | Skor SUS > 100 tidak masuk akal secara teori, ini pasti error input / typo responden. |

**Transformation:**

| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Tidak ada   | -        | -      | Data SUS sudah numerik dan tidak butuh transformasi khusus untuk analisis *mean comparison*. |

**Normalization:**
- **Metode    :** Tidak dilakukan
- **Alasan    :** Skor SUS sudah memiliki standar *bounded range* (0 sampai 100), sehingga analisis statistik dasar (seperti T-test atau ANOVA) bisa langsung diaplikasikan tanpa perlu normalisasi.
- **Parameter :** -

**Leakage Check:**
- [x] Parameter normalisasi dari training set saja (N/A)
- [x] Tidak ada informasi test set dalam preprocessing (N/A)
- [x] Cross-validation dilakukan setelah split (N/A)

**Jumlah data akhir :** 194 baris
**Script tersedia   :** [x] Ya → path: `data_validation/check_data.py` | [ ] Belum

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing values pada skor SUS | 5 dari 200 (2.5%) | Listwise deletion (menghapus baris) | Persentase missing < 5%, distribusi dianggap random, tidak signifikan merusak variabilitas. |
| Error / Outlier skor SUS > 100 | 1 dari 200 (0.5%) | Menghapus baris | Skor SUS maksimal secara absolut adalah 100. Data ini cacat secara logika. |

**Jumlah data sebelum cleaning:** 200
**Jumlah data setelah cleaning:** 194
**Persentase data yang hilang/berubah:** 3%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| SUS_Score | 0 – 100 | Asumsi normal | Sudah dibersihkan | Tidak perlu | Sudah berada di dalam skala standar 0-100 yang konsisten. Tidak perlu menggunakan algoritma berbasis distance yang butuh range [0,1]. |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Data penelitian ini berfokus pada analisis perbandingan *mean* skor System Usability Scale (SUS) antar aplikasi. Karena SUS sudah merupakan metrik dengan *range* paten 0-100, melakukan normalisasi (seperti Z-score atau Min-Max) justru akan menghilangkan interpretabilitas bisnis dari skor itu sendiri (misalnya, batas skor 68 sebagai skor wajar).

**Leakage check:**
- [x] Parameter dihitung dari training set saja (N/A)
- [x] Normalisasi diterapkan setelah train-test split (N/A)

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

**PREPROCESSING SUMMARY**

1. Dataset: `survey_data_signal_sakpole.csv`
2. Data awal: 200 records, 11 features
3. Cleaning:
   - Missing values: 5 kasus, metode: Listwise deletion (drop)
   - Duplikat: 0 kasus, tindakan: -
   - Error: 1 kasus (SUS > 100), tindakan: Dihapus
4. Transformation: Tidak ada transformasi variabel (data original dipertahankan).
5. Normalisasi: Tidak dilakukan, parameter dari N/A (skor SUS langsung digunakan).
6. Data akhir: 194 records, 11 features
7. Leakage check: [x] Lulus / [ ] Ada masalah (Tidak rentan leakage karena bukan pemodelan prediktif)

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, seringkali di tutorial Machine Learning diajarkan untuk mem-fit StandardScaler (Z-score) pada semua kolom numerik tanpa berpikir panjang. Risiko *over-preprocessing* adalah hilangnya makna atau konteks asli dari data (interpretabilitas). Misalnya, mengubah skor SUS 75 menjadi nilai z-score 0.4 membuat kita sulit menjelaskan hasilnya secara intuitif, karena nilai patokan "baik/buruk" pada kuesioner SUS menjadi hilang.
