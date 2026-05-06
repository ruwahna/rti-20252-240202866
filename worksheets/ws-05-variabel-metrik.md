# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

### Research Question

**Apakah metode Dynamic Serendipity Adjustment (DSA) menghasilkan skor Unexpectedness yang lebih tinggi tanpa menurunkan F1-Score lebih dari 2% dibandingkan dengan metode Hybrid Recommendation pada dataset e-commerce?**

---

### Tabel Definisi Variabel & Metrik

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan |
|----------|------|--------|--------|-------|--------|
| Strategi Pembobotan Serendipity | IV | Pendekatan penyesuaian parameter kejutan | Static Weighting (Hybrid) vs Dynamic Weighting (DSA) | Nominal | — |
| Unexpectedness (Serendipity) | DV | Tingkat kejutan/novelti rekomendasi | Proporsi produk baru dalam rekomendasi | Ratio | 0.0–1.0 |
| F1-Score (Akurasi) | DV | Keseimbangan presisi & recall relevansi | F1-weighted per kategori produk | Ratio | 0.0–1.0 |
| Kategori Produk | CV | Jenis/klasifikasi produk katalog | Fashion, Elektronik, Rumah Tangga, dll | Nominal | — |
| Perilaku User | CV | Konteks interaksi user | Buying Phase vs Browsing Phase | Nominal | — |

---

### Detail Operasionalisasi

**IV: Strategi Pembobotan Serendipity**
- **Metode Hybrid**: Parameter serendipity fix (tidak berubah) sepanjang sesi user
- **Metode DSA**: Parameter dinamis disesuaikan real-time berdasarkan click log & phase detection (buying vs browsing)
- **Cara Mengukur**: Implementasi kedua algoritma di backend, log setiap parameter adjustment
- **Justifikasi**: Elemen utama yang membedakan kedua metode; langsung terikat pada hipotesis

**DV: Unexpectedness Score**
- **Definisi Operasional**: (Jumlah produk baru dalam rekomendasi) / (Total produk direkomendasi)
  - "Baru" = belum diklik/dibeli user dalam 90 hari terakhir AND novelty rank > median
- **Cara Mengukur**: Query transaction log → identifikasi produk rekomendasi → cross-check dengan user history 90 hari → hitung proporsi
- **Validasi Construct**: User survey (10 users × 100 rekomendasi random) → apakah produk benar unexpected? (target: agreement ≥70%, Cronbach's α ≥0.70)
- **Justifikasi**: Operasionalisasi serendipity dengan threshold temporal jelas; multi-metric validation (tambah Coverage & Novelty)

**DV: F1-Score (Weighted)**
- **Definisi Operasional**: $F_1 = \frac{2 \times (Precision \times Recall)}{Precision + Recall}$ per kategori, kemudian weighted average
  - Ground truth: user rating ≥3.5 = positive; rating <3.5 = negative
- **Cara Mengukur**: Hitung TP, FP, FN per kategori → hitung precision & recall → F1 per kategori → weighted by category distribution
- **Justifikasi**: Standar metrik akurasi sistem rekomendasi; F1 dipilih (bukan Accuracy) karena dataset mungkin imbalanced

**CV: Kategori Produk**
- **Nilai**: Fashion, Elektronik, Rumah Tangga, Kesehatan, Olahraga, Hiburan, lainnya
- **Cara Mengukur**: Dari product taxonomy database e-commerce
- **Justifikasi**: Kontrol untuk stratifikasi — toleransi serendipity bisa berbeda per kategori

**CV: Perilaku User (Phase)**
- **Nilai**: (1) Buying Phase (ada pending checkout dalam 15 menit), (2) Browsing Phase (exploratory, >5 menit tanpa checkout)
- **Cara Mengukur**: Log behavior — deteksi pending checkout & time window + interaction count
- **Justifikasi**: Toleransi user terhadap serendipity berbeda per fase; DSA seharusnya adaptif

---

### Alignment Check

```
RQ → Concept → Variable → Metric → Data → Result
```

✅ **Setiap langkah terdokumentasi**
- RQ spesifik: metode (DSA vs Hybrid), outcome (Unexpectedness ↑, F1 ≤2% ↓), baseline, dataset
- Konsep "serendipity" → Operasionalisasi "Unexpectedness Score" (temporal + novelty threshold, user-validated)
- Konsep "akurasi" → Operasionalisasi "F1-Score" (precision-recall dengan category weighting)
- Data source: transaction log, user rating, product taxonomy, behavior log
- Analysis: stratifikasi per kategori & phase, construct validation via user survey

✅ **Tidak ada lompatan logis**
- Dari RQ → IV jelas bagaimana DSA bekerja (real-time adaptation mechanism via click log & phase detection)
- Dari DV → Data eksplisit: query transaction log, hitung proporsi produk baru, ground truth dari rating

✅ **Metrik mengukur apa yang dimaksud (construct validity)**
- Unexpectedness = serendipity (user-validated via survey)
- F1 = akurasi relevansi (standar industri)
- Keduanya ratio scale → boleh semua operasi statistik (t-test, ANOVA, correlation)

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah metode Dynamic Serendipity Adjustment (DSA) menghasilkan skor Unexpectedness yang lebih tinggi tanpa menurunkan F1-Score lebih dari 2% dibandingkan dengan metode Hybrid Recommendation pada dataset e-commerce?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Strategi Pembobotan Serendipity | IV | Pendekatan penyesuaian parameter kejutan | Categorical: Static Weighting (Hybrid) vs Dynamic Weighting (DSA) | Nominal | — |
| Unexpectedness (Serendipity) | DV | Tingkat kejutan/novelti rekomendasi produk | Unexpectedness Score (proporsi produk baru terhadap total rekomendasi) | Ratio | 0.0–1.0 (persentase) |
| F1-Score (Akurasi) | DV | Keseimbangan presisi dan recall relevansi produk | F1-weighted (weighted average dari semua kategori produk) | Ratio | 0.0–1.0 (decimal) |
| Kategori Produk | CV | Jenis produk yang merekomendasikan (fashion, elektronik, dll) | Categorical: Product Categories dalam dataset | Nominal | — |
| Perilaku User | CV | Pola interaksi user (browsing vs buying) | Categorical: User Phase (browsing/buying) atau Ordinal: Click Count | Ordinal | Jumlah klik per sesi |

**Apakah ada lompatan logis dalam rantai?** [x] Ya / [ ] Tidak
> Jika ya, di mana? Dari "Strategi Pembobotan" (IV) → harus jelaskan bagaimana "real-time adaptation mechanism" dioperasionalisasi. Perlu ditambah: **Mechanism (How): Real-time perilaku user dideteksi melalui click log dan phase recognition, kemudian parameter serendipity dalam DSA disesuaikan secara dinamis.**

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 4 | **F1-Score** mewakili keseimbangan precision-recall akurasi rekomendasi secara keseluruhan (skor 4, bukan 5, karena focus pada relevansi tetapi tidak menangkap user satisfaction langsung). **Unexpectedness Score** mewakili proporsi produk baru/novel terhadap total rekomendasi, valid untuk operasionalisasi serendipity. Keduanya mengukur aspek yang dimaksud. |
| Sensitive | 4 | Kedua metrik cukup sensitif menangkap perbedaan bermakna antara metode. **DSA diharapkan meningkatkan Unexpectedness** (range 0.0–1.0 scale), sementara **F1 hanya boleh turun max 2%**. Perbedaan 2% F1 masih terdeteksi dengan baik pada dataset besar (>10K transaksi, power test dengan α=0.05 akan significant). Unexpectedness skala ratio juga peka terhadap variasi 5–10%. Tidak ada ceiling effect karena baseline F1≈0.80 (masih ada ruang turun 2%). |
| Feasible | 5 | Kedua metrik **sangat feasible** dikumpulkan otomatis: (1) F1-Score dihitung langsung dari prediksi vs ground truth (user rating >3.5 = positive); (2) Unexpectedness Score dihitung dari log rekomendasi (tracking produk baru vs repeat dalam history 90 hari); (3) Keduanya bisa dikomputasi on-the-fly di backend tanpa setup tambahan. Data sudah ada di e-commerce transaction log. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? **Coverage** (berapa % katalog produk yang pernah direkomendasikan >= 1x selama eksperimen) dan **Novelty** (average recency rank dari rekomendasi terhadap tanggal publikasi produk). Alasan: (1) Unexpectedness saja tidak cukup mengukur diversity — produk bisa unexpected tapi kategorinya tetap monoton. (2) Coverage mengukur apakah DSA benar-benar showcase "hidden gems" dari long-tail catalog, bukan hanya produk baru acak. (3) Novelty membedakan "baru bagi user" vs "baru di platform" — melengkapi perspektif temporal. Ketiga metrik ini bersama-sama memberikan picture lengkap tentang serendipity quality.

**Contoh kasus ceiling effect untuk metrik ini:**
> **Skenario ceiling effect pada F1-Score**: Jika baseline Hybrid Recommendation sudah sangat akurat (F1 > 0.92), ketika DSA menambah serendipity, F1 tidak bisa turun hanya 2% karena sudah mendekati ceiling (akurasi maksimal). Dalam kasus ini, ceiling effect akan memaksa F1 turun minimal 5–8%, menggagalkan hypothesis non-inferiority (H1: turun max 2%). **Mitigation strategy**: (1) Pre-select dataset dengan F1 baseline 0.75–0.85 agar ada margin penurunan 2% yang realistis; (2) Validasi baseline melalui pilot test sebelum eksperimen penuh; (3) Jika ceiling terjadi, revisi metric: gunakan **Relative F1 Drop** (% penurunan terhadap baseline) bukan absolute, atau kombinasikan dengan user satisfaction rating.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | **Risks tinggi** pada log rekomendasi; ada kemungkinan data miss karena timeout API atau user keluar aplikasi tiba-tiba sebelum rating dikumpulkan. Dari 10K user, diperkirakan 5–8% data tidak tercatat (incomplete logs). | **Strategi**: (1) Setup query logs dengan retry mechanism pada API; (2) Implementasi graceful shutdown untuk menyimpan sesi user yang pending; (3) Gunakan data cleaning: hapus session dengan missing >3 interaksi dalam satu task; (4) Pre-register threshold: data dianggap complete jika ≥92% records tercatat. |
| Consistency | *Apakah ada kontradiksi internal?* | **Risks sedang** pada timestamp dan user behavior. Contoh: user_id X melakukan 2 checkout simultan (race condition), atau timestamp interaksi tidak monoton (klik ke belakang). Juga: Unexpectedness Score mungkin melebihi 1.0 karena pembagian salah atau metric formula conflict dengan definisi. | **Strategi**: (1) Validasi timestamp: reject records dengan non-monotonic timestamps dalam satu sesi; (2) Deduplicate: hapus duplikat checkout/rating dalam window 5 detik; (3) Validasi range: Unexpectedness ∈ [0, 1], F1 ∈ [0, 1], bukan negatif; (4) Cross-check: jika user rating = 5 bintang tapi click count = 1, flag sebagai suspicious dan review; (5) Implement data validation schema sebelum import ke analytics. |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | **Construct validity sedang**: F1-Score adalah metrik standar akurasi (valid). Unexpectedness Score (proporsi produk baru) valid untuk serendipity—NAMUN asumsi implisit: "produk baru bagi user = unexpected". Jika user sudah lihat produk X di browse history tapi tidak di rekomendasi sebelumnya, apakah tetap dihitung unexpected? Perlu definisi operasional ketat. | **Strategi**: (1) Pre-define: "Unexpected = produk yang belum pernah diklik/dibeli user dalam 90 hari terakhir AND rank novelty > median"; (2) Validasi construct: sebelum eksperimen, ambil 100 rekomendasi random, tanya 10 user apakah produk itu benar-benar "unexpected"—jika agreement <70%, revisi formula; (3) Triangulation: gunakan secondary metric (Coverage, Novelty) untuk validate bahwa Unexpectedness Score benar mengukur serendipity. |
| Representativeness | *Apakah sampel mewakili populasi target?* | **Risks tinggi** pada bias representasi: Dari populasi 1M user e-commerce Indonesia, jika data hanya dari 10K user aktif/regular, sampling bias terjadi (tidak mewakili casual/seasonal users). Juga: kategori produk mungkin skewed (fashion >50%, elektronik >30%, lainnya <20%), tidak seimbang. | **Strategi**: (1) Stratified random sampling: bagi user per kategori dan activity level (heavy, medium, light), sample proportional dari setiap strata; (2) Dataset balance: jika fashion dominan, oversample kategori lain agar analisis per-kategori valid; (3) Document population characteristics: "Dataset mewakili: 40% heavy users (>20 interaksi/bulan), 40% medium users, 20% light users; kategori fashion 45%, elektronik 35%, lainnya 20%"; (4) Conduct sensitivity analysis: jalankan eksperimen juga pada heavy users saja, medium saja, dll. Jika hasil konsisten, maka representativeness cukup baik. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**

**P-hacking** adalah praktik memilih metrik, analisis statistik, atau subset data *setelah* melihat hasil eksperimen dengan tujuan membuat hasil menjadi signifikan secara artifisial. Contoh: "Jika saya ukur F1 saja, tidak signifikan (p=0.08). Tapi jika saya ukur Precision saja, signifikan (p=0.02). Saya pilih Precision."

**Perbedaan fundamental dengan eksplorasi data yang sah:**

| Aspek | P-hacking | Eksplorasi Data Sah |
|-------|-----------|-------------------|
| **Kapan metrik dipilih?** | *Setelah* melihat data & hasil eksperimen | *Sebelum* eksperimen (pre-registration) |
| **Tujuan pemilihan** | Membuat hasil terlihat signifikan (bias) | Memahami fenomena lebih mendalam (ilmiah) |
| **Transparansi** | Dihiden/tidak dilaporkan | Dilaporkan jelas: "metric ini exploratory, bukan confirmatory" |
| **Berapa metrik diuji?** | Banyak (fishing expedition), hanya report yang signifikan | Terbatas, semua dilaporkan termasuk yang not significant |
| **Threshold statistik** | Flexible (cari hingga p<0.05) | Fixed (α=0.05 ditetapkan sebelumnya) |

**Contoh konkret dalam penelitian DSA:**

❌ **P-hacking:** "Setelah lihat data, ternyata F1 turun 5% (gagal). Tapi Precision naik 3% dan Novelty naik 8%. Saya hanya lapor Precision dan Novelty aja."

✓ **Eksplorasi sah:** "Saya pre-register metric: F1, Unexpectedness, Coverage. Dari hasil: F1 turun 2% (sesuai), Unexpectedness naik 12% (lebih baik dari expected 5%), Coverage turun 3% (unexpected). Saya lapor semua hasil lengkap dan diskusikan mengapa Coverage turun meski Unexpectedness naik."

**Kunci membedakan keduanya:** Apakah metrik sudah **ditentukan sebelum melihat data** dan apakah **semua hasil dilaporkan** (tidak cherry-picked)?
