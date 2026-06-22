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

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

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
Tanggal          : 17 Mei 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Angka itu diukur pakai metrik apa, untuk siapa, dan dibandingkan dengan apa?
   - Data yang dibutuhkan untuk verifikasi: Instrumen evaluasi (SUS/UEQ), jumlah responden, profil responden, serta konteks tugas yang diuji

2. Posisi paradigma:
   - Pendekatan: [☑] Positivis  [ ] Interpretivis  [☑] Design Science  [ ] Mixed
   - Alasan: Topik berfokus pada pengukuran usability secara objektif dan pemetaan perbaikan antarmuka berbasis bukti

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Semua pengguna punya literasi digital yang sama
   - Sumber bias potensial: Bias ulasan negatif di Play Store, responden didominasi pengguna muda, dan efek wilayah (nasional vs daerah)
   - Langkah mitigasi: Gunakan lebih dari satu sumber bukti (SUS, UEQ, sentimen), tulis batasan sampel secara eksplisit, dan gunakan indikator yang sama saat membandingkan

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Nilai metrik asli dari paper, hasil coding literatur, dan kutipan temuan
   - Batasan yang diakui sejak awal: Tidak semua paper memakai instrumen dan populasi yang identik
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul : Analisis Usability Pada Aplikasi Samsat Digital Nasional (SIGNAL) Menggunakan Metode System Usability Scale (SUS)
> Penulis (Tahun): (2024)
> Judul: _______________________________________________
> Penulis (Tahun): ______________________________________
> Sumber/Link DOI: _____________________________________

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengambil data persepsi pengguna aplikasi SIGNAL melalui kuesioner SUS | Responden bisa tidak mewakili semua segmen (misalnya lebih banyak pengguna muda/mahir digital) |
| Data → Processing | Membersihkan respons yang tidak lengkap atau tidak valid | Data ekstrem bisa terhapus tanpa alasan metodologis yang kuat |
| Processing → Analysis | Menghitung skor SUS rata-rata dan memetakan ke kategori | Jika hanya pakai rata-rata, variasi pengalaman tiap kelompok pengguna bisa tertutup |
| Analysis → Inference | Menyimpulkan tingkat kemudahan penggunaan aplikasi | Ada risiko menganggap skor SUS sebagai gambaran semua aspek UX, padahal SUS fokus usability |
| Inference → Knowledge | Menarik simpulan bahwa alur aplikasi perlu perbaikan | Generalisasi berlebihan jika konteks pengujian tidak dijelaskan (fitur apa, perangkat apa, jaringan seperti apa) |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Sampling bias pada profil responden (usia, kemampuan digital, wilayah)
2. Over-generalization dari satu instrumen (SUS) untuk menyimpulkan pengalaman pengguna secara keseluruhan
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

**Topik riset:** Analisis komparatif usability dan user experience aplikasi pajak kendaraan digital SIGNAL vs New Sakpole
**Topik riset:** ________________________________________

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 3 | 4 |
| Jenis data yang dikumpulkan | Skor SUS/UEQ, tingkat keberhasilan tugas, waktu tugas, error rate | Narasi keluhan pengguna dari ulasan | Rekomendasi desain perbaikan alur/fungsi |
| Limitasi paradigma | Bisa kurang menangkap konteks emosional pengguna | Sulit membandingkan hasil secara numerik lintas platform | Fokus implementasi bisa melebar jika scope tidak dikunci |
| Kesesuaian dengan topik (1–5) | *Contoh: 4 — topik kuantitatif, cocok uji hipotesis* | *Contoh: 2 — topik tidak studi makna/konteks* | *Contoh: 5 — membangun artefak untuk uji klaim* |
| Jenis data yang dikumpulkan | *Metrik numerik, log eksperimen* | *Wawancara, observasi kualitatif* | *Hasil uji artefak, komparasi kinerja* |
| Limitasi paradigma | | | |

**Paradigma yang dipilih:** Positivis

**Alasan:** Karena riset menekankan perbandingan terukur antar platform dengan indikator yang jelas, lalu hasilnya dipakai sebagai dasar rekomendasi perbaikan.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
>Sebelum memahami materi ini, saya cenderung cepat percaya kalau ada paper yang menulis aplikasi "sudah baik" hanya dari satu skor.

>Sekarang saya akan lebih hati-hati dan biasanya langsung cek hal ini:
- Respondennya siapa saja, cukup beragam atau tidak?
- Metrik yang dipakai cuma satu atau ada triangulasi (misalnya SUS + UEQ + keluhan nyata)?
- Konteks uji jelas atau tidak (fitur yang diuji, perangkat, jaringan)?
- Hasilnya berlaku umum atau hanya pada kondisi studi tertentu?

>Intinya, saya tidak hanya melihat angka akhir, tapi juga melihat proses bagaimana angka itu dihasilkan.