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
Belum adanya mekanisme adaptasi parameter *serendipity* yang dinamis untuk mengatasi *filter bubble* pada sistem rekomendasi e-commerce (masalah parameter statis).

**Research Question:**
- **Tipe:** [x] Comparison  [ ] Improvement  [ ] Exploratory
- **Formulasi:** Apakah metode `Dynamic Serendipity Adjustment` (DSA) menghasilkan skor *Unexpectedness* yang lebih tinggi tanpa menurunkan *F1-Score* lebih dari 2% dibandingkan dengan metode `Hybrid Recommendation` pada dataset e-commerce?
- **Variabel IV:** Jenis strategi pembobotan (*Static weighting* vs *Dynamic weighting*).
- **Variabel DV:** Skor *Unexpectedness* (Serendipity) dan *F1-Score* (Akurasi).
- **Metrik:** *F1-Score*, *Unexpectedness Score*, dan *Novelty*.
- **Dataset:** Dataset transaksi e-commerce (Log interaksi user-item).
- **Baseline:** *Hybrid Recommendation* (Wati et al., 2021).

**Quality Check RQ:**
- [x] Variabel spesifik
- [x] Metrik jelas
- [x] Baseline ada
- [x] Konteks disebutkan
- [x] Memerlukan eksperimen

**Contribution Statement:**
- **Apa yang baru diketahui:** Bukti empiris mengenai efektivitas penyesuaian parameter kejutan secara otomatis dalam meningkatkan eksplorasi pengguna tanpa merusak relevansi rekomendasi.
- **Jenis kontribusi:** [x] Improvement  [x] Comparison  [ ] Novel approach
- **Gap yang diisi:** Mengisi *Method Gap* dengan mengganti parameter statis menjadi mekanisme dinamis berbasis perilaku *real-time* user.

**Hypothesis Pair:**
- **H₀:** Tidak ada perbedaan signifikan pada skor *Unexpectedness* antara metode DSA dan Hybrid standar.
- **H₁:** Metode DSA menghasilkan skor *Unexpectedness* yang signifikan lebih tinggi dengan penurunan *F1-Score* yang tidak lebih dari 2% (non-inferior).
- **Threshold:** Signifikansi statistik α = 0.05.
- **Justifikasi threshold:** α=0.05 adalah standar riset statistik untuk menolak hipotesis nol.
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
| **RQ** | Apakah DSA menghasilkan skor Unexpectedness lebih tinggi tanpa menurunkan F1-Score secara signifikan? |
| **Variable (IV)** | Strategi pembobotan kejutan (*Static* vs *Dynamic*). |
| **Variable (DV)** | Tingkat Serendipity (*Unexpectedness*) dan Akurasi (*F1-Score*). |
| **Metric** | *Unexpectedness Score*, *F1-weighted*, *p-value*. |
| **Data source** | Dataset publik e-commerce (seperti Amazon Metadata) atau log transaksi UMKM. |
| **Analysis method** | *Preprocessing*, implementasi algoritma, *K-fold cross-validation*, dan *paired t-test* untuk uji signifikansi. |
---

## Refleksi

**Judul:** Optimasi Serendipity pada Sistem Rekomendasi E-Commerce untuk Mengatasi Filter Bubble.

**RQ yang diekstrak:** Apakah implementasi pembobotan dinamis mampu meningkatkan variasi item yang mengejutkan pengguna tanpa mengurangi ketepatan prediksi produk yang dibutuhkan?

**Komponen yang hilang:** Dataset yang memiliki label konteks sesi (sedang *browsing* atau *buying*) untuk pengujian yang lebih akurat secara *real-time*.