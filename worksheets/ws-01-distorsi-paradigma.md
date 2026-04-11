# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Indah Ruwahna Anugraheni
Tanggal          : 11 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah data yang digunakan cukup besar dan representatif?
   - Data yang dibutuhkan untuk verifikasi: Dataset, metode evaluasi, dan hasil pengujian lengkap

2. Posisi paradigma:
   - Pendekatan: [☑] Positivis  [☑] Interpretivis  [☑] Design Science  [☑] Mixed
   - Alasan: Karena menggunakan data kuantitatif dan juga membangun sistem

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Data dianggap mewakili kondisi nyata
   - Sumber bias potensial: Sampling bias dan overfitting
   - Langkah mitigasi: Menggunakan dataset beragam dan validasi silang

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data hasil eksperimen dan data mentah
   - Batasan yang diakui sejak awal: Dataset terbatas dan kondisi pengujian tidak mencerminkan semua situasi nyata
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul : Analisis Klasifikasi Email Spam Menggunakan Algoritma Naïve Bayes
> Penulis (Tahun): Azan Rahman, Andi Maslan (2024)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan dataset email spam dan non-spam | Dataset mungkin tidak mewakili kondisi nyata (hanya dari sumber tertentu) |
| Data → Processing |Preprocessing data (cleaning, tokenizing, TF-IDF) |Informasi penting bisa hilang saat pembersihan data |
| Processing → Analysis |Melatih model Naïve Bayes dan balancing data (SMOTE) |Overfitting karena data dibuat lebih seimbang secara buatan |
| Analysis → Inference |Menghitung akurasi model (hingga ±98%) |Hanya fokus pada akurasi tanpa metrik lain |
| Inference → Knowledge |Menyimpulkan metode efektif untuk klasifikasi spam |Generalisasi berlebihan ke semua kondisi email |

**Distorsi paling besar di tahap:** Processing → Analysis

**Dua distorsi spesifik yang teridentifikasi:**
1. Overfitting akibat penggunaan teknik balancing data (SMOTE)
2. Sampling bias karena dataset tidak sepenuhnya representatif
---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus melaporkan hasil dengan dan tanpa outlier |
| Transparansi |Peneliti wajib menjelaskan alasan penghapusan outlier secara jelas |
| Peer review |Reviewer akan mengevaluasi apakah penghapusan outlier valid secara metodologis |

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus hanya untuk membuat hasil signifikan; kedua hasil harus dilaporkan

**justifikasi:**
> Menghapus data tanpa alasan ilmiah yang kuat termasuk manipulasi data dan melanggar etika penelitian. Outlier hanya boleh dihapus jika terbukti kesalahan data (error input, noise ekstrem, dll).
---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Analisis klasifikasi email spam menggunakan algoritma Naïve Bayes

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5| 1 | 4|
| Jenis data yang dikumpulkan | Data numerik (akurasi, dataset email)| Persepsi pengguna| Data hasil sistem/model|
| Limitasi paradigma |Tidak melihat aspek subjektif pengguna | Tidak cocok untuk data kuantitatif| Fokus pada artefak, bukan teori|

**Paradigma yang dipilih:** Positivis

**Alasan:** Karena penelitian menggunakan data kuantitatif, eksperimen terukur, dan bertujuan menguji performa algoritma secara objektif.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
>Sebelum membaca materi ini, saya belum terlalu mempertanyakan klaim seperti “95% akurat” dan cenderung langsung mempercayainya.

>Setelah memahami rantai distorsi dalam Research Trust Model, saya menjadi lebih kritis dan akan mengajukan beberapa pertanyaan saat membaca paper, seperti:
- Bagaimana data dikumpulkan dan apakah representatif?
- Apakah ada bias dalam dataset?
- Apakah metode evaluasi yang digunakan sudah tepat?
- Apakah hanya menggunakan akurasi atau juga metrik lain seperti precision dan recall?
Apakah hasil penelitian dapat digeneralisasi ke kondisi nyata?

>Saya juga memahami bahwa setiap tahap dalam penelitian berpotensi mengalami distorsi, sehingga penting untuk mengevaluasi validitas dan etika penelitian sebelum menerima suatu klaim.