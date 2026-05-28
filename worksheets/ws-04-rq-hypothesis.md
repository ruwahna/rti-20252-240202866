# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis


RQ-CONTRIBUTION-HYPOTHESIS

**Gap Statement:** 
Belum ada kerangka evaluasi komparatif sistematis untuk membandingkan SIGNAL dan New Sakpole pada tugas-tugas kritis (registrasi, verifikasi identitas, pembayaran) menggunakan instrumen evaluasi yang identik. Studi existing terpisah per platform dengan metodologi berbeda (SUS vs TAM), sehingga tidak bisa dibandingkan langsung.

**Research Question:**
- **Tipe:** [x] Comparison  [ ] Improvement  [ ] Exploratory
- **Formulasi:** Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis (registrasi, verifikasi identitas, pembayaran) ketika dievaluasi dengan instrumen evaluasi yang identik?
- **Variabel IV (Independent):** Platform aplikasi pajak (SIGNAL vs New Sakpole); Fase user journey (registrasi, verifikasi identitas, pembayaran).
- **Variabel DV (Dependent):** SUS Score (Usability), UEQ Score (User Experience), Task Completion Time, Task Success Rate, Error Rate.
- **Metrik:** SUS Score (range 0-100), UEQ Score (6 dimensi), Task completion time (detik), Success rate (%), Error rate (%).
- **Dataset:** Data dari responden yang melakukan ketiga fase tugas pada kedua platform.
- **Baseline:** SUS Score SIGNAL 2024 (~55), UEQ Score SIGNAL 2023.

**Quality Check RQ:**
- [x] Variabel spesifik (platform, phase, metrics)
- [x] Metrik jelas (SUS, UEQ, task metrics)
- [x] Baseline ada (existing SIGNAL studies)
- [x] Konteks disebutkan (three user journeys)
- [x] Memerlukan eksperimen (paired comparison study)

**Contribution Statement:**
- **Apa yang baru diketahui:** Bukti empiris perbedaan sistematis antara aplikasi pajak nasional dan regional dalam hal usability dan user experience pada fase-fase spesifik transaksi, serta identifikasi faktor desain mana yang menjadi driver utama perbedaan tersebut.
- **Jenis kontribusi:** [x] Comparison  [x] Improvement (rekomendasi perbaikan)  [ ] Novel approach
- **Gap yang diisi:** Mengisi Method Gap dan Context Gap dengan menyediakan kerangka evaluasi komparatif terstandar dan mengevaluasi kedua platform secara bersamaan pada domain lokal Indonesia.

**Hypothesis Pair:**
- **H₀:** Tidak ada perbedaan signifikan pada SUS Score dan UEQ Score antara SIGNAL dan New Sakpole pada ketiga fase user journey.
- **H₁:** Ada perbedaan signifikan pada SUS Score dan/atau UEQ Score antara SIGNAL dan New Sakpole, dengan prediksi New Sakpole akan menunjukkan skor lebih tinggi pada minimal dua dari tiga fase berdasarkan studi sebelumnya.
- **Threshold:** Signifikansi statistik α = 0.05 (two-tailed independent t-test untuk per-fase comparison).
- **Justifikasi threshold:** α=0.05 adalah standar riset HCI untuk mendeteksi perbedaan signifikan dalam evaluasi usability antar platform.
---

## Latihan 1 — Dari Gap ke RQ

**Gap dari WS-03:** Belum ada mekanisme penyesuaian serendipity secara dinamis berdasarkan mood/fase belanja user secara real-time.

**RQ versi pertama (tulis bebas):**
> Apakah model yang bisa berubah-ubah parameter kejutannya lebih baik daripada model biasa dalam mengatasi filter bubble?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | DSA vs Hybrid Recommendation |
| Metrik terukur | Ya | F1-Score & Unexpectedness |
| Baseline | Ya | Hybrid Recommendation |
| Dataset/konteks | Ya | Dataset transaksi e-commerce |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah metode `Dynamic Serendipity Adjustment` (DSA) menghasilkan skor *Unexpectedness* lebih tinggi dan tetap mempertahankan *F1-Score* dibandingkan metode *Hybrid Recommendation* standar pada dataset e-commerce?
---

## Latihan 2 — Hypothesis Pair

**Rumuskan pasangan hipotesis dari RQ di Latihan 1.**

| Komponen | Isi |
|----------|-----|
| **H₀** | Tidak ada peningkatan signifikan pada skor *Unexpectedness* dan terjadi penurunan *F1-Score* > 2% pada metode DSA dibandingkan baseline. |
| **H₁** | Metode DSA memberikan peningkatan *Unexpectedness* yang signifikan dan *F1-Score* tetap terjaga pada margin non-inferiority 2%. |
| **Metrik** | *Unexpectedness* (Serendipity) dan *F1-Score* (Akurasi). |
| **Threshold** | α = 0.05; Margin F1 = 0.02. |
| **Justifikasi threshold** | Standar statistik α=0.05; Margin 2% dianggap batas toleransi akurasi yang dapat diterima demi kepuasan eksplorasi. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> **Bagaimana cara membuktikannya salah?** Dengan eksperimen: Jika hasil uji statistik menunjukkan p-value > 0.05 atau skor akurasi (F1) anjlok drastis melebihi 2%, maka H₁ ditolak.
---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| **RQ** | Apakah terdapat perbedaan signifikan pada SUS dan UEQ antara SIGNAL dan New Sakpole pada tiga fase user journey (registrasi, verifikasi, pembayaran)? |
| **Variable (IV)** | Platform aplikasi (SIGNAL vs New Sakpole); Fase task (registrasi, verifikasi identitas, pembayaran). |
| **Variable (DV)** | SUS Score (Usability), UEQ Score (6 dimensi UX), Task completion time, Success rate, Error rate. |
| **Metric** | SUS Score (0-100 skala), UEQ Score (per dimensi), Task time (detik), Success % dan Error %. |
| **Data source** | Responden pengguna aktual yang melakukan tugas pada kedua platform (minimal 30 orang per platform untuk validitas statistik). |
| **Analysis method** | Deskriptif statistik per fase, independent t-test atau Mann-Whitney U test untuk perbandingan per metrik, two-way ANOVA untuk melihat efek platform × phase terhadap SUS/UEQ. |
---

## Refleksi

**Judul:** Analisis Komparatif Usability dan User Experience pada Layanan Pajak Kendaraan Digital: SIGNAL vs New Sakpole.

**RQ yang diekstrak:** Apakah New Sakpole menunjukkan skor usability (SUS) dan user experience (UEQ) yang lebih baik dari SIGNAL, terutama pada fase verifikasi identitas yang saat ini menjadi pain point utama SIGNAL berdasarkan keluhan Play Store?

**Komponen yang hilang:** Breakdown responden berdasarkan demografi (usia, tingkat digital literacy) untuk analisis sub-grup—apakah perbedaan platform signifikan untuk semua demografi atau hanya untuk kelompok tertentu (misal: user senior lebih sulit dengan SIGNAL?).