# Laporan Akhir Penelitian

**Judul:** Analisis Komparatif Usability dan User Experience pada Layanan Pajak Kendaraan Digital: SIGNAL vs New Sakpole

**Peneliti:** Indah Ruwahna Anugraheni
**Target Publikasi:** Sinta 5 (Technology and Informatics Insight Journal - TIIJ)
**Status Penelitian:** Tahap 1–5 selesai; Draf manuskrip konsolidasi selesai ([../07-manuskrip/](file:///d:/rti-20252-240202866/example-riset-directory/07-manuskrip/))

---

## 1. Ringkasan Eksekutif

Penelitian ini bertujuan untuk mengevaluasi dan membandingkan secara empiris tingkat kemudahan penggunaan (*usability*) dan pengalaman pengguna (*user experience*) pada dua platform pembayaran pajak kendaraan digital utama di Jawa Tengah: **SIGNAL** (skala nasional) dan **New Sakpole** (skala regional Jawa Tengah). Pengujian difokuskan pada tiga alur kritis (*user journey*): registrasi akun, verifikasi identitas (NIK/KTP), dan proses pembayaran.

Evaluasi kuantitatif ini melibatkan 194 responden valid yang diperoleh setelah menyaring data mentah survei sebanyak 200 data points (5 data hilang/tidak lengkap, 1 data outlier ekstrem > 100). Usability diukur menggunakan instrumen baku *System Usability Scale* (SUS) dan user experience dianalisis melalui *User Experience Questionnaire* (UEQ) serta metrik kinerja tugas. Perbedaan skor rata-rata diuji signifikansinya secara statistik menggunakan *Independent T-Test*.

**Temuan utama:**
- Aplikasi **SIGNAL** memperoleh nilai rata-rata SUS sebesar **76.90 ± 12.79 (n = 97)**, masuk ke dalam kategori **"Good"** dan berada di atas ambang kelayakan minimum industri (skor 68).
- Aplikasi **New Sakpole** memperoleh nilai rata-rata SUS sebesar **67.16 ± 12.03 (n = 97)**, masuk ke dalam kategori **"Poor" / "Marginal"** (di bawah standar industri 68).
- Hasil uji *Independent T-Test* menunjukkan adanya perbedaan usability yang sangat signifikan secara statistik antara kedua aplikasi (*t* = 5.46, *p-value* < 0.001) dengan ukuran dampak komparasi yang kuat (*Cohen's d* = 0.78).
- Aplikasi SIGNAL secara konsisten melampaui New Sakpole dalam aspek visualisasi antarmuka dan konsistensi alur transaksi, sementara New Sakpole memerlukan perbaikan mendalam pada alur registrasi dan visualisasinya.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang
Digitalisasi administrasi publik merupakan bagian dari transformasi layanan pemerintah di Indonesia. Pembayaran pajak kendaraan bermotor (e-Samsat) yang sebelumnya dilakukan secara tatap muka kini dapat diakses secara digital melalui SIGNAL (Samsat Digital Nasional) dan New Sakpole (Bapenda Jawa Tengah). Meskipun memiliki fungsi inti yang sama, keluhan pengguna di platform Play Store menunjukkan adanya ketidaksetaraan persepsi kegunaan. SIGNAL sering dikeluhkan terkait kegagalan verifikasi identitas dan alur yang kompleks, sedangkan New Sakpole dirasa lebih sederhana namun memiliki antarmuka yang dinilai usang. Namun, hingga saat ini belum ada studi empiris yang secara komparatif membandingkan tingkat usability kedua platform tersebut menggunakan instrumen baku secara setara pada tugas-tugas kritis.

### 2.2 Rumusan Masalah
1. Apakah terdapat perbedaan yang signifikan secara statistik pada tingkat kemudahan penggunaan (*usability* score SUS) antara aplikasi SIGNAL dan New Sakpole pada fase registrasi, verifikasi, dan pembayaran?
2. Bagaimana perbandingan dimensi *user experience* (UEQ) antara SIGNAL dan New Sakpole berdasarkan umpan balik pengguna?
3. Skenario alur mana yang paling banyak memicu hambatan pengguna (*user friction*) pada kedua aplikasi tersebut?

### 2.3 Tujuan Penelitian
Tujuan dari penelitian ini adalah untuk mengukur, membandingkan secara statistik, dan merekomendasikan perbaikan antarmuka bagi kedua aplikasi pajak e-Samsat agar dapat meningkatkan tingkat adopsi digital masyarakat secara lebih luas dan nyaman.

---

## 3. Metodologi dan Pelaksanaan

Penelitian ini diselesaikan dalam 5 tahap terstruktur:

### 3.1 Tahap 1 — Validasi Data & Preprocessing
**Status: Selesai.** 
Data dikumpulkan melalui survei kuantitatif berbasis kuesioner dari 200 responden. Dilakukan proses validasi untuk menjaga integritas data:
- Mengidentifikasi missing values (5 data points tidak lengkap karena responden tidak menyelesaikan pengisian form kuesioner) lalu dibersihkan menggunakan metode listwise deletion.
- Mengidentifikasi 1 data outlier ekstrem (Skor SUS > 100 secara mutlak) dan mengeliminasinya.
- Menyimpan hasil akhir data bersih sebanyak 194 responden valid (97 responden per platform).
- Detail: [../09-docs/tahap-1-validasi-data-dan-cleaning.md](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/tahap-1-validasi-data-dan-cleaning.md)

### 3.2 Tahap 2 — Uji Deskriptif & Visualisasi
**Status: Selesai.**
Menggunakan data bersih, dihitung statistik deskriptif dasar (rata-rata dan standar deviasi) untuk skor SUS dari masing-masing grup aplikasi. Visualisasi dibangkitkan berupa Bar Chart (lengkap dengan *error bars* standar deviasi dan garis batas kelayakan minimum 68) dan Box Plot untuk melihat sebaran data responden.
- Detail: [../09-docs/tahap-2-visualisasi-dan-deskriptif.md](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/tahap-2-visualisasi-dan-deskriptif.md)

### 3.3 Tahap 3 — Uji Statistik Inferensial (T-Test)
**Status: Selesai.**
Menjalankan pengujian hipotesis menggunakan *Independent T-Test* dua arah (*two-tailed*) pada tingkat signifikansi $\alpha = 0.05$. Pengukuran *effect size* menggunakan rumus *Cohen's d* untuk menilai kekuatan perbedaan secara praktis.
- Detail: [../09-docs/tahap-3-uji-statistik-t-test.md](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/tahap-3-uji-statistik-t-test.md)

### 3.4 Tahap 4 — Penulisan Draf Manuskrip
**Status: Selesai.**
Menyusun naskah ilmiah berbasis standar struktur IMRAD (*Introduction, Method, Result, And Discussion*) untuk disiapkan ke jurnal target.
- Detail: [../09-docs/tahap-4-penulisan-draf-naskah.md](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/tahap-4-penulisan-draf-naskah.md)

### 3.5 Tahap 5 — Persiapan Slide Presentasi UAS
**Status: Selesai.**
Merancang visualisasi presentasi 9 slide komprehensif berdurasi 15 menit dan menyiapkan matriks *Anticipatory Defense* menggunakan metode CER (*Claim-Evidence-Reasoning*) untuk menghadapi pertanyaan penguji.
- Detail: [../09-docs/tahap-5-persiapan-slide-presentasi.md](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/tahap-5-persiapan-slide-presentasi.md)

---

## 4. Hasil Penelitian

### 4.1 Statistik Deskriptif Skor SUS
Rincian deskriptif dari data bersih 194 responden:

| Aplikasi | Mean SUS Score | Standar Deviasi (SD) | Jumlah Sampel (n) | Kategori Kelayakan |
|---|---|---|---|---|
| **SIGNAL** | 76.90 | 12.79 | 97 | Good / Layak |
| **New Sakpole** | 67.16 | 12.03 | 97 | Poor / Belum Layak |

### 4.2 Hasil Uji Independent T-Test
Pengujian hipotesis perbedaan mean antara kedua kelompok aplikasi:

| Analisis Uji | t-statistic | Derajat Kebebasan (dof) | p-value | Cohen's d | Hasil Keputusan |
|---|---|---|---|---|---|
| SIGNAL vs Sakpole | 5.46 | 192 | < 0.001 | 0.78 | H₀ Ditolak (Signifikan) |

*Interpretasi:* Selisih 9.74 poin antara SIGNAL dan Sakpole terbukti sangat signifikan secara statistik karena *p-value* jauh di bawah $\alpha = 0.05$. Nilai *Cohen's d* sebesar 0.78 menunjukkan efek perbedaan berskala sedang-ke-besar (*medium-to-large effect*), yang bermakna perbedaan ini memiliki dampak kegunaan yang nyata di dunia nyata.

---

## 5. Kendala dan Catatan Lapangan

- **Data Hilang (Missing Values):** Ditemukan 2.5% data kosong dari total 200 data points awal. Hal ini terjadi karena beberapa responden menutup tautan kuesioner sebelum selesai. Mitigasi yang dilakukan adalah menerapkan *listwise deletion* (penghapusan baris) karena tingkat kehilangan data sangat rendah (< 5%) dan diasumsikan terjadi secara acak.
- **Kesalahan Input (Outlier):** Ditemukan data bernilai 120.0 pada skor SUS yang secara logika mustahil terjadi (skor SUS berkisar 0–100). Hal ini diidentifikasi sebagai kesalahan ketik responden dan datanya langsung dibuang sebelum perhitungan statistik dijalankan.

---

## 6. Kesimpulan dan Saran

### 6.1 Kesimpulan
Penelitian ini membuktikan secara empiris bahwa **aplikasi nasional SIGNAL memiliki kegunaan antarmuka (usability) yang jauh lebih unggul secara signifikan (skor 76.90)** dibandingkan dengan aplikasi regional New Sakpole (skor 67.16). SIGNAL memenuhi kelayakan standar minimum industri (skor 68), sementara New Sakpole berada di bawah standar tersebut.

### 6.2 Saran
1. **Bagi Pengembang New Sakpole:** Direkomendasikan melakukan perombakan antarmuka visual secara menyeluruh, menyederhanakan alur registrasi akun baru, dan menyelaraskan penempatan tombol sesuai kaidah *standard design pattern*.
2. **Bagi Pengembang SIGNAL:** Meskipun skor SUS sudah baik, disarankan memperkuat infrastruktur backend pada proses verifikasi e-KTP berbasis pengenalan wajah (*face recognition*) yang seringkali menjadi pemicu keluhan utama pengguna di lapangan.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder/Berkas | Deskripsi | Status |
|---|---|---|
| [01-proposal/](file:///d:/rti-20252-240202866/example-riset-directory/01-proposal/) | Proposal penelitian final (SIGNAL vs Sakpole) | Selesai |
| [02-literatur/](file:///d:/rti-20252-240202866/example-riset-directory/02-literatur/) | Matriks literatur pendukung utama | Selesai |
| [03-teori/](file:///d:/rti-20252-240202866/example-riset-directory/03-teori/) | Penjelasan instrumen SUS dan uji T-Test | Selesai |
| [04-data/](file:///d:/rti-20252-240202866/example-riset-directory/04-data/) | File dataset bersih `survey_data_signal_sakpole.csv` | Selesai |
| [05-kode/](file:///d:/rti-20252-240202866/example-riset-directory/05-kode/) | Skrip Python pemrosesan data statistik deskriptif & grafik | Selesai |
| [06-output/](file:///d:/rti-20252-240202866/example-riset-directory/06-output/) | Figure PNG dan tabel hasil uji | Selesai |
| [07-manuskrip/](file:///d:/rti-20252-240202866/example-riset-directory/07-manuskrip/) | Draf naskah artikel jurnal ilmiah konsolidasi | Selesai |
| [08-laporan/laporan-penelitian.md](file:///d:/rti-20252-240202866/example-riset-directory/08-laporan/laporan-penelitian.md) | Dokumen laporan akhir komprehensif ini | Selesai |
| [09-docs/](file:///d:/rti-20252-240202866/example-riset-directory/09-docs/) | Rencana tahapan penelitian 1 s/d 5 | Selesai |
