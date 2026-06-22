# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

### 1. Completeness
- [x] Semua skenario tercakup
- [ ] Jumlah run sesuai rencana (Ada responden yang tidak lengkap)
- [x] Tidak ada file output hilang
- **Missing:** 5 dari 200 data points

### 2. Format Consistency
- [x] Semua file format sama (CSV)
- [x] Header konsisten
- [x] Tipe data konsisten (numerik tetap numerik)

### 3. Range & Logic
- [ ] Nilai dalam range masuk akal
- [x] Tidak ada waktu negatif
- [ ] Metrik 0–100%, tidak di luar range
- **Anomali ditemukan:** Ada 1 skor SUS > 100 (kesalahan input/ketik responden)

### 4. Cross-Validation
- [x] Run identik → hasil mendekati
- [x] Trend konsisten dengan ekspektasi teori

### 5. Keputusan
- [ ] Data siap analisis
- [x] **Perlu cleaning** (Hapus missing data & outlier, simpan ulang sebagai `cleaned_data.csv`)
- [ ] Perlu re-run (skenario: -)

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Uji SUS SIGNAL | 100 responden | 98 | 2 | User menutup browser sebelum selesai |
| Uji SUS New Sakpole | 100 responden | 97 | 3 | User menutup browser sebelum selesai |

**Total expected:** 200 | **Total actual:** 195 | **Missing:** 5

**Keputusan untuk data missing:**
> Data missing akan dihapus (listwise deletion) karena jumlahnya sangat kecil (<5%) dan tidak memengaruhi keseimbangan distribusi data secara signifikan.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Responden ID | Skor SUS SIGNAL |
|-----|-------------|
| 001 | 75.0 |
| 002 | 80.5 |
| 003 | 120.0 |
| 004 | 78.5 |
| 005 | 72.0 |

**Deteksi outlier:**
- Q1 = 73.5 | Q3 = 80.5 | IQR = 7.0
- Batas bawah (Q1 - 1.5×IQR) = 63.0
- Batas atas (Q3 + 1.5×IQR) = 91.0
- Outlier terdeteksi: Responden 003 (Skor 120.0)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Responden 003 | 120.0 | Kesalahan logika / typo input (Skor SUS maksimal absolut adalah 100) | Hapus (drop) data baris ini karena secara teori nilai SUS tidak mungkin di atas 100 |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 97.5% data terkumpul (195 dari 200)
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: -
**3. Range check (anomali):** Ditemukan 1 outlier dengan skor SUS > 100
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: -

**Kesimpulan:** [ ] Data siap analisis / [x] Perlu tindakan: Data Cleaning (menghapus baris missing value dan nilai > 100, lalu di-save menjadi `cleaned_data.csv`).

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> **Data yang benar** adalah data yang tercatat jujur apa adanya dari responden. Sedangkan **Data yang dipercaya** adalah data yang sudah divalidasi keabsahannya (tidak ada typo nilai ekstrem, format benar, lengkap) sehingga layak dianalisis secara statistik. Validasi formal tetap wajib dilakukan karena form otomatis tidak 100% kebal dari human-error seperti *user* yang asbun (asal bunyi) atau error saat ekspor CSV.
