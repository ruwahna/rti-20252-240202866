# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
Domain   : Human-Computer Interaction (HCI) / Usability & User Experience pada layanan publik digital

Konteks : Aplikasi dan website layanan pajak kendaraan digital nasional (SIGNAL) vs aplikasi daerah (New Sakpole Jawa Tengah)
   
System Context
- Input       : 
Identitas pengguna (NIK/nomor kendaraan), lokasi pembayaran, metode pembayaran, dan pilihan menu di antarmuka

- Process     : 
Sistem menampilkan pilihan pajak yang berlaku, proses verifikasi identitas, input data kendaraan, perhitungan pajak, proses pembayaran

- Output      : 
Konfirmasi pembayaran pajak, dokumen bukti pembayaran (digital)

- Outcome     : 
Pengguna berhasil atau gagal menyelesaikan pembayaran pajak dalam waktu yang wajar

- Constraints : 
Keterbatasan literasi digital pengguna, kecepatan koneksi internet, keamanan transaksi

- Stakeholders: Warga pembayar pajak, petugas samsat, developer aplikasi, Korlantas Polri, dan Bapenda Jawa Tengah 


Fenomena → Problem
- Fenomena yang diamati             : 
Warga sering mengalami kesulitan saat menggunakan aplikasi SIGNAL untuk bayar pajak, sedangkan aplikasi New Sakpole dianggap lebih mudah
Gejala (symptom) yang terukur : Banyak keluhan di Play Store tentang alur verifikasi rumit, waktu loading lama, error login berulang

- Gejala (symptom) yang terukur     : 
Alur registrasi SIGNAL berbelit-belit, feedback sistem tidak jelas, proses verifikasi wajah sering gagal

- Masalah yang didiagnosis          : 
Desain antarmuka SIGNAL terlalu kompleks untuk pengguna awam, sedangkan New Sakpole relatif lebih sederhana dalam hal alur dan visual

- Masalah riset (researchable)      : 
Belum ada studi komparatif yang sistematis mengukur tingkat usability dan user experience antara aplikasi pajak nasional (SIGNAL) dan aplikasi daerah (New Sakpole) pada konteks tugas-tugas kritis (registrasi, verifikasi, pembayaran)

- Variabel yang terukur             : 
SUS score, task completion time (detik), task success rate (%), jumlah error, dan UEQ score (User Experience Questionnaire)


Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham?
  [x] Measurability — Apakah ada metrik kuantitatif?
  [x] Relevance — Apakah penting untuk domain?
  [x] Testability — Apakah bisa gagal?
  [x] Impact — Apakah ada kontribusi jika terjawab?


Problem Statement (1 paragraf):

Penggunaan mobile website Halodoc dalam layanan kesehatan digital masih menghadapi kendala dalam pengalaman pengguna, khususnya pada proses pencarian dokter dan booking layanan. Hal ini ditunjukkan oleh lamanya waktu penyelesaian tugas, rendahnya tingkat keberhasilan pengguna, serta tingginya navigasi ulang selama interaksi. Permasalahan ini diduga disebabkan oleh tingginya information overload pada tampilan antarmuka, struktur navigasi yang kurang intuitif, serta minimnya feedback visual dalam proses booking. Namun, belum terdapat studi kuantitatif yang secara spesifik mengukur pengaruh kompleksitas informasi dan kejelasan navigasi terhadap efisiensi serta keberhasilan task pengguna pada platform tersebut. Oleh karena itu, penelitian ini bertujuan untuk menganalisis hubungan antara kompleksitas UI dan desain navigasi terhadap performa pengguna, menggunakan metrik seperti task completion time, task success rate, error rate, dan System Usability Scale (SUS). 

```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Komparasi usability aplikasi pajak kendaraan digital SIGNAL (nasional) vs New Sakpole (Jawa Tengah)

| Tahap | Hasil |
|-------|-------|
| Reality | Warga Jawa Tengah bisa pakai dua aplikasi untuk bayar pajak motor/mobil, tapi respons berbeda |
| Observed Issue (Symptom) | - Skor SUS aplikasi SIGNAL lebih rendah daripada New Sakpole (data dari paper 2024) <br> - Banyak keluhan di Play Store tentang SIGNAL sulit digunakan <br> - Task completion time SIGNAL lebih lama |
| Diagnosed Problem (Root Cause) | Desain UI/UX SIGNAL lebih kompleks, alur registrasi berbelit, feedback sistem kurang jelas, sedangkan New Sakpole lebih ringkas |
| Researchable Problem | Belum ada studi komparatif yang sistematis dan terstruktur membandingkan usability dan UX kedua aplikasi pada tugas-tugas yang sama dengan instrumen evaluasi yang identik |
| Measurable Variable | - SUS score <br> - UEQ score (User Experience Questionnaire) <br> - Task completion time <br> - Task success rate <br> - Error rate <br> - Serendipity/novelty dalam rekomendasi fitur |


**Apakah terjebak solution-first thinking?** [ ] Ya / [☑] Tidak
> Riset dimulai dari identifikasi perbedaan pengalaman pengguna, bukan langsung proposal perbaikan.
---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | NIK/STNK pengguna, pilihan metode pembayaran, data perangkat (OS, screen size) |
| Process | Render antarmuka, validasi identitas, input data kendaraan, hitung pajak, proses pembayaran, verifikasi wajah |
| Output | Konfirmasi pembayaran, bukti digital pajak |
| Outcome | Pengguna berhasil/gagal bayar pajak, waktu tempuh, jumlah error yang terjadi |
| Constraints | Literasi digital beragam, koneksi internet variabel, keamanan transaksi |
| Stakeholders | Warga, petugas samsat, developer, Korlantas, Bapenda, regulator |

**Komponen mana yang paling relevan dengan masalah riset?** 

>Process (kompleksitas alur, kejelasan feedback, konsistensi design pattern antara SIGNAL dan New Sakpole)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas: dua platform spesifik, tugas spesifik (registrasi, verifikasi, bayar), metrik terukur |
| Measurability | 5 | Semua variabel terukur dengan instrumen standar (SUS, UEQ, waktu, success rate) |
| Relevance | 5 | Sangat penting untuk peningkatan layanan pajak digital di Indonesia |
| Testability | 5 | Bisa diuji dengan usability testing, bisa replikasi dengan mahasiswa/responden berbeda |
| Impact | 5 | Hasilnya bisa jadi rekomendasi perbaikan ke Korlantas dan Bapenda |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**

>Layanan pajak kendaraan digital di Indonesia tersedia dalam dua bentuk: aplikasi nasional (SIGNAL) dan aplikasi daerah (New Sakpole di Jawa Tengah). Meskipun tujuannya sama, pengguna sering melaporkan pengalaman berbeda—SIGNAL dianggap lebih rumit dan membingungkan, sementara New Sakpole dirasa lebih mudah dipahami. Hal ini ditunjukkan oleh perbedaan skor SUS dan banyaknya keluhan di Play Store terkait alur registrasi, verifikasi, dan pembayaran pada SIGNAL. Belum ada studi komparatif yang sistematis mengukur perbedaan usability dan user experience kedua platform pada tugas-tugas kritis menggunakan instrumen evaluasi yang sama. Oleh karena itu, penelitian ini bertujuan untuk melakukan analisis komparatif mendalam terhadap platform SIGNAL dan New Sakpole pada tiga user journey utama (registrasi, verifikasi identitas, pembayaran) dengan menggunakan metrik SUS score, UEQ score, task completion time, task success rate, dan error rate, untuk mengidentifikasi faktor-faktor desain yang berkontribusi pada perbedaan pengalaman pengguna dan memberikan rekomendasi perbaikan berbasis bukti.

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
>Bug atau error pas coding biasanya langsung terlihat jelas (aplikasi error, fitur tidak jalan). Cara mengatasinya relatif straightforward: cari error log, debug, fix kode, test.

>Masalah riset itu beda. Misalnya, warga bilang SIGNAL "susah", tapi "susah" itu artinya apa? Alur rumit? Feedback tidak jelas? Button yang kecil? Perlu digali dulu dengan sistematis—dari gejala, ke akar masalah, terus riset yang terukur. Bukan hanya ngerasa, tapi harus buktikan dengan data dan bisa diulang orang lain dengan hasil mirip.