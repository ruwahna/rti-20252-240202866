# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
  RAM     : 8 GB
  GPU     : CPU-only
  Storage : SSD Standar

Software:
  OS        : Microsoft Windows 11 Home 64-bit
  Runtime   : Python 3.13.6
  Framework : Jupyter Notebook

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| pandas  | 2.3.3   | PyPI   | N/A           |
| numpy   | 2.3.5   | PyPI   | N/A           |
| matplotlib | 3.10.7 | PyPI | N/A           |

Konfigurasi:
  Config file     : Variabel di dalam Notebook
  Random seed     : 42
  Hyperparameters : Alpha (Signifikansi) = 0.05

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz |
| RAM | 8 GB |
| GPU | CPU-only |
| OS | Microsoft Windows 11 Home 64-bit |
| Runtime | Python 3.13.6 |
| Framework | Jupyter Notebook |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| pandas | 2.3.3 | Manipulasi dan agregasi data kuesioner (SUS/UEQ) |
| numpy | 2.3.5 | Operasi numerik untuk perhitungan skor |
| matplotlib | 3.10.7 | Visualisasi grafik bar chart dan boxplot |
| scipy | *Perlu diinstal* | Uji statistik komparatif (T-Test / Mann-Whitney U) |
| seaborn | *Perlu diinstal* | Visualisasi distribusi skor UX yang lebih estetik |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | P-Value (Uji Beda SUS) | — |
| 2 | 42 | P-Value (Uji Beda SUS) | [x] Ya / [ ] Tidak |
| 3 | 42 | P-Value (Uji Beda SUS) | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

Karena eksperimen ini berfokus pada analisis data kuesioner (bukan training model berat), hasil perbedaan eksekusi biasanya disebabkan oleh versi library `scipy` yang berbeda atau file data mentah yang belum disanitasi.

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level
- [x] Tidak ada background process yang mengganggu (tidak relevan untuk analisis data kuesioner)
- [x] Cache notebook dibersihkan (Restart Kernel) antar-run
- [x] Config file/Script analisis yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
Judul Eksperimen: Analisis Statistik Komparatif SUS & UEQ (SIGNAL vs New Sakpole)

1. Environment
   - OS: Microsoft Windows 11 Home 64-bit
   - CPU: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
   - RAM: 8 GB
   - Runtime: Python 3.13.6

2. Installation
   - Instal library yang dibutuhkan:
     pip install pandas numpy matplotlib scipy seaborn

3. Data
   - File: survey_data_signal_sakpole.csv
   - Isi: Data mentah respons kuesioner dari pengguna SIGNAL dan New Sakpole

4. Execution
   - Buka command prompt / terminal, jalankan: jupyter notebook
   - Buka file analysis_notebook.ipynb
   - Pilih menu "Run All" untuk mengeksekusi semua blok kode

5. Configuration
   - Random seed = 42
   - Alpha (tingkat signifikansi) = 0.05

6. Expected Output
   - Teks: Nilai p-value dari uji statistik (Mann-Whitney U)
   - Visual: Grafik komparasi SUS/UEQ tersimpan dalam format .png
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> File `requirements.txt` belum dibuat secara fisik di direktori proyek, dan dataset `.csv` masih dalam tahap pengumpulan data dari responden.
