# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

### 1. Execution Plan

| Run # | Skenario | Seed | Parameter | Status | Waktu Eksekusi | Output File |
|---|---|---|---|---|---|---|
| **1** | Uji Normalitas (Shapiro-Wilk) | 42 | Alpha = 0.05 | Planned | *TBD* | `shapiro_out.txt` |
| **2** | Uji Beda SUS (Mann-Whitney U) | 42 | Alpha = 0.05 | Planned | *TBD* | `mwu_sus_out.txt` |
| **3** | Uji Beda UEQ per dimensi | 42 | Alpha = 0.05 | Planned | *TBD* | `mwu_ueq_out.txt` |
| **4** | Bootstrapping SUS (Iterasi 1) | 123 | n = 1000 | Planned | *TBD* | `boot_123.csv` |
| **5** | Bootstrapping SUS (Iterasi 2) | 456 | n = 1000 | Planned | *TBD* | `boot_456.csv` |

- **Jumlah runs per skenario:** 1 (untuk uji dasar), 2 (untuk bootstrapping)
- **Total runs:** 5

### 2. Data Log (Hasil Eksekusi)

- **Run ID:** `run-sus-mannwhitney-01`
- **Timestamp:** `2026-06-22T21:55:10`
- **Skenario:** Uji Beda SUS SIGNAL vs New Sakpole
- **Input:** `survey_data_signal_sakpole.csv` (N=100 sampel)
- **Output:** `p_value_sus.txt` (p=0.014) & `sus_boxplot.png`
- **Anomali:** Data skor SUS tidak berdistribusi normal berdasarkan uji Shapiro-Wilk (p = 0.031).
- **Catatan:** Karena anomali data yang tidak normal tersebut, uji beda dialihkan menggunakan metode Non-parametrik (Mann-Whitney U). Hasil uji beda menunjukkan p-value < 0.05, sehingga terbukti ada perbedaan usability yang signifikan antara SIGNAL dan New Sakpole.

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Uji Normalitas (Shapiro-Wilk) | 42 | Alpha = 0.05 | Planned |
| 2 | Uji Beda SUS (Mann-Whitney U) | 42 | Alpha = 0.05 | Planned |
| 3 | Uji Beda UEQ per dimensi | 42 | Alpha = 0.05 | Planned |
| 4 | Bootstrapping SUS 1000 iterasi | 123 | n=1000, seed=123 | Planned |
| 5 | Bootstrapping SUS 1000 iterasi | 456 | n=1000, seed=456 | Planned |

**Total skenario:** 3 Skenario Uji Dasar + 1 Skenario Bootstrapping
**Run per skenario:** 1x untuk uji dasar, 2x (beda seed) untuk bootstrapping
**Total run keseluruhan:** 5 run utama

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-sus-mannwhitney-01 |
| Timestamp | 2026-06-25T14:30:00 |
| Skenario | Uji Beda SUS SIGNAL vs New Sakpole |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Alpha | 0.05 |
| Dataset Version | raw_data_v1.csv |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| P-Value | float | 0.0 – 1.0 |
| Z-Score | float | -10.0 – 10.0 |
| Kesimpulan | string | "Signifikan" / "Tidak Signifikan" |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Error TypeError saat load CSV (misal: ada sel kosong) | Dokumentasi error, sanitasi data dengan fungsi fillna() atau dropna(), lalu re-run |
| Hasil ekstrem | Skor SUS mentah responden > 100 atau < 0 (mustahil) | Jangan langsung hapus! Cek apakah itu kesalahan ketik responden, filter rentang valid secara eksplisit di code |
| Asumsi uji tidak terpenuhi | P-value uji normalitas Shapiro-Wilk < 0.05 (data tidak berdistribusi normal) | Jangan dipaksakan. Ubah uji parametrik (T-Test) menjadi Non-parametrik (Mann-Whitney U), dan catat alasannya |
| Inkonsistensi antar run | Hasil Bootstrapping seed 123 signfikan, tapi seed 456 tidak signifikan | Naikkan jumlah iterasi bootstrapping (misal dari 1000 ke 10000) agar konvergen/stabil, lalu re-run |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Dulu sering mengambil kesimpulan hanya dari satu kali uji statistik. Jika hasilnya tidak sesuai ekspektasi (misal p > 0.05), data yang dianggap "jelek" kadang dihapus tanpa dokumentasi atau alasan statistik yang kuat (*p-hacking*).
**Yang akan dilakukan berbeda:**
> Sekarang setiap proses (mulai dari pembersihan data kosong, pengujian normalitas, hingga hasil p-value) akan dicatat log-nya. Jika terjadi anomali (misal data tidak normal), anomali tersebut akan diselesaikan sesuai protokol (ganti ke uji non-parametrik) dan didokumentasikan, bukan dibuang secara diam-diam.
