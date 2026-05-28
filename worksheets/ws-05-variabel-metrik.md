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

**Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis (registrasi, verifikasi identitas, pembayaran) ketika dievaluasi dengan instrumen evaluasi yang identik?**

---

### Tabel Definisi Variabel & Metrik

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan |
|----------|------|--------|--------|-------|--------|
| Platform Aplikasi Pajak | IV | Jenis aplikasi yang diuji | SIGNAL vs New Sakpole | Nominal | — |
| Fase User Journey | IV | Tahap transaksi dalam alur pembayaran pajak | Registrasi, Verifikasi Identitas, Pembayaran | Nominal | — |
| Usability Score | DV | Kemudahan penggunaan aplikasi | System Usability Scale (SUS) | Ratio | 0-100 (skor mentah) |
| User Experience Score | DV | Pengalaman pengguna multi-dimensi | User Experience Questionnaire (UEQ) | Ordinal | 1-7 per item (6 dimensi) |
| Task Completion Time | DV | Kecepatan penyelesaian tugas | Waktu dari mulai hingga sukses selesai | Ratio | Detik (s) |
| Task Success Rate | DV | Proporsi pengguna berhasil menyelesaikan | Jumlah responden sukses / Total responden | Ratio | % (0-100) |
| Error Rate | DV | Frekuensi kesalahan/retry | Jumlah kesalahan per fase per user | Ratio | Jumlah/orang |
| Demografi Pengguna | CV | Karakteristik responden | Usia, tingkat digital literacy, pengalaman pajak | Nominal/Ordinal | — |
| Jenis Perangkat | CV | Hardware yang digunakan | Smartphone (Android/iOS), Tablet | Nominal | — |

---

### Detail Operasionalisasi

**IV-1: Platform Aplikasi**
- **SIGNAL**: Aplikasi Samsat Digital Nasional (versi terbaru di Play Store)
- **New Sakpole**: Aplikasi Bapenda Jawa Tengah New Sakpole (versi terbaru di Play Store)
- **Cara Mengukur**: Pengguna melakukan task di aplikasi masing-masing sesuai random assignment
- **Justifikasi**: Variabel utama yang ingin dibandingkan; eksekusi harus konsisten (versi sama untuk semua responden per platform)

**IV-2: Fase User Journey**
- **Registrasi**: Dari akses aplikasi hingga akun terbentuk
- **Verifikasi Identitas**: Dari input NIK/STNK hingga sistem memverifikasi data identitas
- **Pembayaran**: Dari pemilihan metode pembayaran hingga konfirmasi pembayaran berhasil
- **Cara Mengukur**: Protokol task yang sama untuk kedua platform; video recording + think-aloud protocol untuk capture friction points
- **Justifikasi**: Tiga fase dipilih berdasarkan studi gap; keluhan Play Store SIGNAL fokus di verifikasi; setiap fase punya kompleksitas berbeda

**DV-1: SUS Score**
- **Definisi Operasional**: 10 item Likert 1-5 → skor raw (jumlah respons) → formula SUS = (raw_score - 10) × 2.5, range 0-100
- **Cara Mengukur**: Post-task questionnaire setelah setiap fase; responden rate persetujuan dengan 10 statements tentang usability
- **Validasi Construct**: SUS adalah instrumen standar internasional (Brooke, 1996) dengan Cronbach's α ≥0.90 di banyak studi; tidak perlu re-validasi
- **Justifikasi**: SUS dipilih karena (1) standar industri, (2) sudah dipakai SIGNAL 2024, memungkinkan baseline comparison, (3) mudah diadministrasikan

**DV-2: UEQ Score (User Experience Questionnaire)**
- **Definisi Operasional**: 26 items × 7-point semantic differential scale → skor per dimensi (Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty)
- **Cara Mengukur**: Post-task questionnaire dengan format pasangan kata (misal: "buruk/baik", "kusut/teratur")
- **Validasi Construct**: UEQ adalah instrumen standar dengan Cronbach's α 0.76-0.84 per dimensi; referensi benchmark untuk aplikasi lokal Indonesia belum ada, jadi gunakan benchmark umum
- **Justifikasi**: UEQ dipilih sebagai complement SUS untuk capture UX holistik (bukan hanya usability); sudah dipakai studi SIGNAL 2023, memungkinkan trend analysis
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

**RQ:** Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis (registrasi, verifikasi identitas, pembayaran)?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Platform Aplikasi Pajak | IV | Jenis sistem yang diuji | Categorical: SIGNAL vs New Sakpole | Nominal | — |
| Fase User Journey | IV | Tahap spesifik dalam workflow pembayaran pajak | Categorical: Registrasi, Verifikasi Identitas, Pembayaran | Nominal | — |
| Usability Score | DV | Kemudahan penggunaan aplikasi | System Usability Scale (SUS) Score = (jumlah item × scoring) / 10 × 2.5 | Ratio | 0–100 |
| User Experience Score | DV | Pengalaman multidimensi pengguna | UEQ Score (6 dimensi: Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty) | Ordinal | 1–7 per item; rata-rata per dimensi 1–7 |
| Task Completion Time | DV | Waktu penyelesaian task | Durasi dari start hingga sukses konfirmasi | Ratio | Detik (s) |
| Task Success Rate | DV | Proporsi pengguna berhasil | Jumlah responden sukses / Total responden per fase | Ratio | % (0–100) |
| Digital Literacy | CV | Kemampuan pengguna dengan teknologi | Categorical: Rendah (≤2 jam/hari), Sedang (2-6 jam), Tinggi (>6 jam) | Ordinal | — |
| Usia Pengguna | CV | Demografi responden | Ordinal atau Categorical: <30 th, 30-50 th, >50 th | Ordinal | Tahun |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Tidak ada. Setiap langkah terdokumentasi: RQ → IV (platform × phase) → DV (SUS, UEQ, task metrics) → data source (questionnaire post-task, log sistem, timer) → analysis (statistical comparison per phase).

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | **SUS Score** adalah instrumen standar untuk usability aplikasi (standar industri sejak 1996). **UEQ Score** mengukur 6 dimensi UX secara holistik (lebih comprehensive dari SUS). Kedua instrumen diakui internasional dan sudah dipakai studi SIGNAL sebelumnya (memungkinkan trend comparison). **Task metrics** (time, success, error) adalah hard metrics yang objektif. Semua metrik secara langsung mengukur apa yang ingin dibandingkan: usability dan UX antara kedua platform. |
| Sensitive | 4 | Kedua instrumen cukup sensitif menangkap perbedaan bermakna. **SUS score range 0-100** → perbedaan 5-10 poin signifikan (dari paper 2024 SIGNAL skor ~55). **UEQ per dimensi 1-7 scale** → perbedaan 0.5-1.0 poin terdeteksi dengan baik dengan N≥30 responden per kondisi (power test α=0.05). **Task time dan success rate** adalah hard metrics yang sangat sensitif (jika New Sakpole 2x lebih cepat, akan terlihat jelas). Satu-satunya tidak max (skor 4 bukan 5): UEQ dimensi "Novelty" mungkin ceiling effect karena kedua apps sama-sama baru bagi many users. |
| Feasible | 5 | Kedua instrumen **sangat feasible** dikumpulkan: (1) SUS & UEQ adalah questionnaire standard yang bisa diadministrasikan post-task via paper atau digital form (~5-10 menit per responden); (2) Task metrics (time, success/fail) bisa ditrack otomatis via sistem atau manual observation; (3) Instrumen sudah validated — tidak perlu pilot ekstensif; (4) Setup minimal: hanya perlu responden willing, 30 menit per orang × 2 platform × 3 fase ≈ total 3 jam per responden. Feasible untuk eksperimen lokal. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? 
> - **System Usability Confidence Score**: Rating "apakah saya percaya data yang dimasukkan sudah terproses?" (1-5 Likert). Alasan: verifikasi identitas adalah pain point utama SIGNAL; confidence score menangkap aspek trust/reassurance yang tidak tercakup SUS/UEQ.
> - **Error Type Breakdown**: Kategorisasi jenis error (salah input vs sistem timeout vs UI confusing) untuk diagnosa root cause. Alasan: tidak cukup hanya "error rate naik 5%" — perlu tahu error apa untuk rekomendasi perbaikan spesifik.
> - **Perceived Workload (NASA TLX single item)**: Rating mental/physical demand (1-5 Likert). Alasan: melengkapi UEQ "Efficiency" dengan perspektif subjektif usability cognitive load.

**Contoh kasus ceiling effect untuk metrik ini:**
> **Skenario ceiling effect pada SUS Score**: Jika New Sakpole baseline SUS sudah sangat tinggi (≥75), dan SIGNAL skor~55, perbedaan 20 poin signifikan. NAMUN jika New Sakpole skor 85, tidak bisa meningkat lebih dari 15 poin (ceiling 100). Dalam kasus ini, efek perbedaan akan terlihat tapi magnitude diminished. **Mitigation**: (1) Pre-test dengan small sample (5 orang per app × 3 fase) untuk cek baseline skor; (2) Jika ceiling terdeteksi, gunakan **Relative Improvement** (% gain terhadap baseline) bukan absolute poin; (3) Fokus pada phase-spesifik: jika fase registrasi New Sakpole ceiling, gunakan focus group untuk explore dimensi UX lain (trust, satisfaction dengan visual design, etc.).

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua responden menyelesaikan semua fase pada kedua aplikasi?* | **Risks sedang-tinggi**. Ada kemungkinan dropout: responden selesai registrasi SIGNAL, tapi jenuh tidak melanjutkan ke fase pembayaran; atau sebaliknya, merasa Sakpole lebih mudah dan skip tahap verifikasi. Juga: beberapa responden mungkin tidak mengisi questionnaire lengkap (SUS 10 item, UEQ 26 item = 36 item panjang, butuh 15-20 menit). Estimasi: 10-15% dropout rate. | **Strategi**: (1) Incentive: bayar responden per fase completed, bukan lump sum, untuk encourage completion semua fase; (2) Questionnaire adaptive: jika responden tired, gunakan SUS saja first, UEQ sebagai optional; (3) Protocol clarity: sebelum mulai, jelaskan estimasi waktu dan pentingnya lengkap semua fase; (4) Pre-register: data hanya dianggap valid jika ≥90% complete (6 dari 6 sub-tasks selesai); (5) Intention-to-treat analysis: jika dropout, coba kontak untuk late completion atau exclude secara dokumentasi jelas. |
| Consistency | *Apakah ada kontradiksi logis dalam data?* | **Risks sedang**. Contoh: responden rate SUS item "Sistem ini mudah digunakan" dengan score 5 (sangat setuju), tapi Task Success Rate 0% (gagal semua tugas) → kontradiktif. Atau: UEQ "Efisiensi" rating tinggi, tapi task completion time >10 menit untuk registrasi sederhana. Juga mungkin: ada data duplikat (responden didata dua kali), timestamp tidak masuk akal (verifikasi selesai sebelum registrasi mulai). | **Strategi**: (1) Validasi range: SUS item 1-5, UEQ 1-7, task time >0 detik, success rate 0-100%; reject outliers seperti task time 0.001 detik (tidak masuk akal); (2) Cross-check logic: jika success rate=0% tapi SUS score >75, flag untuk review manual (mungkin responden tidak paham instruction atau data entry error); (3) Deduplicate: merge records dengan responden_id + platform + phase sama, ambil record paling lengkap; (4) Timestamp validation: pastikan registrasi_end ≤ verifikasi_start ≤ pembayaran_start per responden. (5) Video review: kalau ada kontradiksi, tonton video task untuk verify apakah benar-benar sukses atau data entry error. |
| Validity | *Apakah instrumen benar-benar mengukur yang dimaksud?* | **Construct validity sedang-tinggi** untuk SUS (instrumen established sejak 1996, validity terbukti). **UEQ juga established** (validity reported Cronbach's α 0.76-0.84). **Namun construct validity perlu validasi di konteks lokal**: SUS item "I think I would like to use this system frequently" — apakah responden Indonesia paham "frequently" berarti apa? Task time adalah metrik objektif (valid). **UEQ Novelty dimensi mungkin problematic**: kedua apps sama-sama "aplikasi pajak baru" bagi responden → semua rate novelty tinggi (ceiling effect). | **Strategi**: (1) Cognitive walkthrough: sebelum eksperimen penuh, 5 responden pilot → tanya mereka paham item satu per satu (think-aloud protocol); (2) Translate validation: SUS sudah ada versi Bahasa Indonesia (dari studi lain), gunakan itu instead of translating sendiri; (3) UEQ: pre-note bahwa Novelty dimension mungkin ceiling effect, tidak akan interpret sebagai platform yang truly novel tapi responden expectation mismatch; (4) Triangulation: gunakan task metrics (objective) untuk cross-validate subjective SUS/UEQ scores (jika task time tinggi tapi SUS score tinggi, ada issue); (5) Konten validity: involve HCI expert untuk review instrumen sebelum deploy. |
| Representativeness | *Apakah sampel responden mewakili pengguna actual SIGNAL/Sakpole?* | **Risks tinggi pada seleksi bias**. Real users SIGNAL/Sakpole adalah mostly orang yang perlu bayar pajak kendaraan — skewed ke usia 30-60 tahun, pendapatan menengah ke atas (punya kendaraan), variable digital literacy. Jika recruitment di kampus universitas, bakal skewed ke muda/tech-savvy. Jika recruitment di kantor pajak, skewed ke yang sudah digital-literate (karena datang ke kantor pajak untuk self-service). Ideal perlu quota sampling dari berbagai segment. | **Strategi**: (1) Stratified quota sampling: target demographics → 20% umur <30, 50% umur 30-55, 30% umur >55; 40% Android phone, 40% iPhone, 20% browser desktop; 30% self-rate digital literacy "rendah", 50% "sedang", 20% "tinggi"; (2) Recruitment diverse: recruit tidak hanya dari online, tapi juga offline (kantor pajak, kelurahan) untuk catch non-digital-native users; (3) Document characteristics: laporkan di write-up "sampel mewakili: X% female, Y% rural, Z% pensiunan, dll" agar readers dapat judge generalizability; (4) Sensitivity analysis: jalankan analisis terpisah per demographic group (usia <30 vs 30-55 vs >55) → jika pola konsisten across groups, representativeness baik; jika hasil beda drastis per group, berarti ada moderating effect; (5) Compare to population: jika ada statistics resmi "berapa % SIGNAL users usia <30", bandingkan dengan sampel — jika deviasi >10%, dokumentasikan dan acknowledge limitation. |

---

## Refleksi

> Dalam desain studi komparatif SIGNAL vs New Sakpole, mengapa penting untuk pre-register metrik DV sebelum eksperimen bukan sesudah melihat data?

**Jawaban:**

Pre-registrasi metrik penting karena tanpa itu, kita bisa tergoda untuk **cherry-pick hasil yang sudah dilihat**. Contoh: "SUS score SIGNAL 50, New Sakpole 60 — perbedaan 10 poin significant. Tapi kalau lihat per fase, hanya verifikasi phase beda signifikan (fase registrasi hampir sama skor-nya). Saya lapor hanya hasil verifikasi phase saja." Ini adalah **selective reporting**, bentuk p-hacking.

**Perbedaan fundamental:**

| Aspek | Selective Reporting (P-hacking) | Transparent Reporting (Riset Sah) |
|-------|-----------|-------------------|
| **Metrik dipilih kapan?** | *Setelah* melihat data eksperimen | *Sebelum* eksperimen dimulai (dokumentasi RQ + DV) |
| **Yang dilaporkan** | Hanya metrik yang "significant" atau "menarik" | Semua metrik yang pre-register, signifikan atau tidak |
| **Contoh selektif** | "SUS saja signifikan, UEQ tidak — jadi saya lapor SUS saja" | "SUS signifikan (p=0.03), UEQ tidak (p=0.12) — lapor keduanya, explain perbedaan" |
| **Analisis tambahan** | Dilakukan *after seeing results* (bias) | Dilakukan *planned in advance* sebagai secondary analysis |

**Contoh konkret untuk SIGNAL vs New Sakpole:**

❌ **Selective reporting:** 
- Lihat data: SUS significant (p=0.02), Task Time significant (p=0.01), tapi UEQ tidak (p=0.18)
- Lapor: "SIGNAL dan New Sakpole berbeda signifikan pada usability dan kecepatan task"
- Ignore: Tidak mention bahwa UEQ (yang dijanjikan sebagai DV utama di WS-04) not significant

✓ **Transparent reporting:**
- Pre-register: DV1=SUS, DV2=UEQ, DV3=Task Time (semua sama penting)
- Lihat data: SUS sig (p=0.02), Task Time sig (p=0.01), UEQ not sig (p=0.18)
- Lapor: "SUS dan task time menunjukkan SIGNAL vs New Sakpole signifikan berbeda (p<0.05). Namun UEQ score tidak signifikan (p=0.18), suggesting keduanya similar pada dimensi UX 6-faktor. Ini unexpected — mungkin karena ceiling effect pada dimensi 'Novelty' atau metrik ini less sensitive untuk digital payment app. Butuh investigasi lebih lanjut."

**Praktik best practice:** Simpan **pre-registration document** (bisa di OSF.io atau git) yang berisi RQ + IV + DV semua detail sebelum data collection, jadi tidak bisa berubah-ubah sesuai hasil.
