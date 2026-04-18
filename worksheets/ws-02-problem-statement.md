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
Domain   : Domain : Human-Computer Interaction (HCI) / UX UI pada platform kesehatan digital

Konteks : Mobile website Halodoc pada proses pencarian dokter dan booking layanan kesehatan
   
System Context
- Input       :
Query   pencarian pengguna (nama dokter/spesialis), lokasi pengguna, serta interaksi pengguna (klik, scroll)

- Process     : 
Sistem menampilkan daftar dokter, filtering, navigasi halaman, serta proses pemilihan jadwal dan booking

- Output      : 
Informasi dokter, jadwal tersedia, dan konfirmasi booking

- Outcome     : 
Pengguna berhasil atau gagal menyelesaikan proses booking

- Constraints : 
Ukuran layar mobile terbatas, koneksi internet, serta beban kognitif

- Stakeholders: Pengguna (pasien), dokter, UX designer, developer, dan platform Halodoc 


Fenomena → Problem
- Fenomena yang diamati             : 
Pengguna mengalami kesulitan dalam mencari dokter dan menyelesaikan proses booking pada mobile website Halodoc
Gejala (symptom) yang terukur : Waktu pencarian lama (>20 detik), task success rate rendah (<60%), dan tingginya navigasi ulang (back navigation)

- Gejala (symptom) yang terukur     : 
Information overload pada tampilan, navigasi tidak intuitif, serta kurangnya feedback visual pada proses booking

- Masalah yang didiagnosis          : 
Information overload pada tampilan, navigasi tidak intuitif, serta kurangnya feedback visual pada proses booking

- Masalah riset (researchable)      : 
Belum ada studi kuantitatif yang mengevaluasi pengaruh kompleksitas informasi dan kejelasan navigasi terhadap efisiensi dan keberhasilan task pengguna pada mobile website Halodoc

- Variabel yang terukur             : 
Task completion time (detik), task success rate (%), jumlah klik, error rate (%), dan skor System Usability Scale (SUS)


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

**Topik awal:** UX/UI mobile website kesehatan (Halodoc) pada proses pencarian dokter dan booking

| Tahap | Hasil |
|-------|-------|
| Reality | Pengguna mobile sering kesulitan mencari dokter dan menyelesaikan booking di website Halodoc |
| Observed Issue (Symptom) | - Waktu pencarian dokter > 20 detik <br> - Task success rate < 60% <br> - Banyak user kembali ke halaman sebelumnya (back navigation tinggi) | Diagnosed Problem (Root Cause) | Information overload pada tampilan mobile, struktur navigasi tidak hierarkis, serta kurangnya feedback visual pada proses booking (tidak ada progress indicator yang jelas)|
| Researchable Problem |Belum ada studi kuantitatif yang mengevaluasi pengaruh information overload dan kejelasan navigasi terhadap efisiensi task dan keberhasilan booking pada mobile website Halodoc | 
| Measurable Variable | - Task completion time (detik) <br> - Task success rate (%) <br> - Number of clicks <br> - Error rate (%) <br> - SUS score (System Usability Scale) |


**Apakah terjebak solution-first thinking?** [ ] Ya / [☑] Tidak
> Jika ya, kembali ke tahap mana?
---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Query pencarian (nama dokter/spesialis), lokasi user, data interaksi (klik, scroll) |
| Process | Rendering UI mobile, filtering dokter, navigasi antar halaman, proses booking|
| Output | Informasi dokter, jadwal tersedia, konfirmasi booking|
| Outcome | Efisiensi pengguna (cepat/lambat) dan keberhasilan booking|
| Constraints |Ukuran layar kecil (mobile), bandwidth terbatas, cognitive load pengguna|
| Stakeholders | Pasien, dokter, UX designer, developer, platform Halodoc|

**Komponen mana yang paling relevan dengan masalah riset?** 

>Process (UI complexity & navigation flow di mobile)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat spesifik: mobile, task, dan variabel jelas|
| Measurability | 5|Semua variabel kuantitatif dan standar UX |
| Relevance |5 |Sangat penting di health-tech |
| Testability | 5| Bisa diuji dengan usability testing & eksperimen|
| Impact | 5|Berdampak pada akses layanan kesehatan digital |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**

>Pada era layanan kesehatan digital, efisiensi interaksi pengguna pada platform mobile menjadi faktor krusial dalam keberhasilan akses layanan. Namun, pada mobile website Halodoc, pengguna masih mengalami kesulitan dalam menemukan dokter dan menyelesaikan proses booking. Hal ini ditunjukkan oleh tingginya waktu penyelesaian tugas, rendahnya tingkat keberhasilan booking, serta meningkatnya navigasi ulang oleh pengguna. Permasalahan ini diduga disebabkan oleh tingginya information overload pada tampilan mobile serta struktur navigasi yang kurang intuitif dan minimnya feedback visual selama proses interaksi. Meskipun demikian, belum terdapat studi kuantitatif yang secara spesifik mengukur pengaruh kompleksitas informasi dan desain navigasi terhadap performa pengguna pada konteks mobile health platform. Oleh karena itu, penelitian ini bertujuan untuk menganalisis hubungan antara kompleksitas UI dan kejelasan navigasi terhadap efisiensi dan keberhasilan task pengguna, dengan menggunakan metrik seperti task completion time, task success rate, error rate, serta System Usability Scale (SUS), melalui pendekatan usability testing dan evaluasi heuristik.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah pada coding seperti bug atau error biasanya bersifat teknis, jelas terlihat, dan memiliki solusi yang relatif langsung, yaitu memperbaiki kode agar sistem dapat berjalan sesuai fungsi yang diharapkan. Pendekatannya cenderung fokus pada “memperbaiki” (problem-solving) dengan cara mencoba, debugging, dan implementasi solusi yang sudah diketahui.

> Sebaliknya, masalah riset tidak selalu terlihat secara langsung dan memerlukan proses identifikasi yang sistematis, mulai dari fenomena, gejala, hingga akar masalah. Masalah riset juga harus dirumuskan secara spesifik, terukur, dan dapat diuji secara ilmiah. Pendekatannya bukan hanya menyelesaikan masalah, tetapi memahami penyebabnya, menguji hipotesis, dan menghasilkan pengetahuan baru yang dapat dibuktikan serta direplikasi.