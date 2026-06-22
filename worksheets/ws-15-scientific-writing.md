# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

**PAPER STRUCTURE CHECKLIST**

**Title   :** Analisis Komparatif Usability Aplikasi SIGNAL dan New Sakpole Menggunakan System Usability Scale (SUS)
**Target  :** [ ] Jurnal  [x] Konferensi  [ ] Laporan

**Section Check:**
- [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
- [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
- [x] Related Work — concept-centric, gap positioning
- [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
- [x] Results — tabel + grafik + observasi (tanpa interpretasi)
- [x] Discussion — interpretasi, perbandingan, implikasi, limitation
- [x] Conclusion — jawaban RQ, kontribusi, future work

**Consistency Matrix:**
- [x] RQ di Introduction = RQ di Method = RQ di Conclusion
- [x] Variabel di Method = variabel di Results
- [x] Klaim di Discussion didukung data di Results
- [x] Limitasi di Discussion di-address di Conclusion/Future Work

**Writing Quality:**
- [x] Clarity — mudah dipahami tanpa re-read
- [x] Precision — tidak ada istilah ambigu
- [x] Conciseness — tidak ada kalimat redundan

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Aplikasi e-Samsat seringkali memiliki tingkat usability yang beragam sehingga mempengaruhi kepuasan masyarakat. Studi ini membandingkan skor *System Usability Scale* (SUS) antara SIGNAL dan New Sakpole dengan 194 responden. Hasil uji *T-Test* menunjukkan SIGNAL memiliki skor signifikan lebih tinggi (76.90 vs 67.16), memberikan panduan empiris penting untuk desain layanan publik. | 200-250 |
| Introduction | Konteks: Adopsi layanan e-government yang terhambat akibat sulitnya penggunaan antarmuka aplikasi. Gap: Belum banyak evaluasi komparatif empiris antara aplikasi e-Samsat nasional (SIGNAL) dengan provinsi (Sakpole). RQ: Apakah terdapat perbedaan signifikan pada *usability* antara kedua sistem? | 500-700 |
| Related Work | Tinjauan literatur tentang standar evaluasi *usability* menggunakan skor SUS (ambang batas 68). Serta, merangkum tantangan UX pada ranah aplikasi *e-government* di Indonesia. | 700-1000 |
| Method | Menggunakan pendekatan kuantitatif komparatif. Metrik: Skor SUS. Dataset dikumpulkan dari kuesioner pada pengguna aktif. Proses validasi data dan *cleaning* memastikan *outlier* dibuang untuk analisis statistik T-Test. | 800-1200 |
| Results | Laporan objektif data deskriptif: rata-rata SIGNAL 76.90 ± 12.79, Sakpole 67.16 ± 12.03. Disajikan dalam tabel dan diagram *bar chart* dengan *error bar*. Uji hipotesis menghasilkan p < 0.001 dan Cohen's d = 0.78. | 500-800 |
| Discussion | Menjelaskan bahwa perombakan UI pada SIGNAL terbukti sukses melampaui batas standar kelayakan SUS (score > 68), sedangkan Sakpole di bawah standar. Perbedaan memiliki *practical significance* tinggi (d=0.78). Menjelaskan juga limitasi demografi sampel penelitian. | 600-900 |
| Conclusion | SIGNAL secara sah terbukti memiliki tingkat *usability* lebih baik daripada New Sakpole. Saran untuk pemerintah provinsi adalah melakukan audit ulang desain UX Sakpole. Rekomendasi riset mendatang: menambah wawancara kualitatif agar tahu penyebab persisnya. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

| Elemen | Intro | Method | Result | Discussion | Conclusion |
|--------|-------|--------|--------|-----------|-----------|
| RQ Utama (Beda Usability) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik Utama (Skor SUS) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Analisis T-Test | ✗ | ✓ | ✓ | ✓ | ✗ |
| Temuan (SIGNAL lebih baik) | ✗ | ✗ | ✓ | ✓ | ✓ |
| Limitasi Riset | ✗ | ✗ | ✗ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Secara umum alur sudah konsisten. Namun, terkadang alat uji statistik detail (seperti T-Test) sering absen di bab *Conclusion* atau *Intro*, hal ini lumrah karena bab tersebut fokus pada "makna/konsep" alih-alih metode mekanis.

**Tindakan perbaikan:**
> Tetap memastikan bahwa di *Intro* dan *Conclusion*, penekanan ada pada variabel penelitian ("membandingkan skor *usability*"), sementara penjelasan alat statistik spesifik ("*Independent T-test*") hanya difokuskan pada *Method* dan *Results*.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Berdasarkan hasil yang kita peroleh di lapangan setelah menghitung kuesioner dari banyak orang, performa dari aplikasi SIGNAL kelihatan cukup bagus dan grafiknya naik. Kalau dibandingkan sama Sakpole, nilai Sakpole terlihat lebih kecil. Jadi aplikasi SIGNAL terbukti lebih mantap dipakai buat masyarakat.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Gaya bahasanya terlalu informal dan kata-katanya bertele-tele ("hasil yang kita peroleh", "grafiknya naik"). | Gunakan struktur kalimat pasif / objektif akademis. |
| Precision | Sangat tidak presisi. "Performa cukup bagus", "banyak orang", "nilai lebih kecil", "lebih mantap" adalah klaim tak terukur. | Ganti dengan metrik absolut: "n=194", "skor SUS", "signifikan (p<0.001)". |
| Conciseness | Memakai banyak kata *filler* yang tidak menambah informasi penting sama sekali. | Persingkat dan sampaikan langsung *to the point*. |

**Paragraf setelah perbaikan:**
> Evaluasi terhadap 194 responden menunjukkan bahwa rata-rata skor SUS pada aplikasi SIGNAL (M=76.90, SD=12.79) secara signifikan lebih tinggi dibandingkan aplikasi New Sakpole (M=67.16, SD=12.03), dengan nilai *p* < 0.001. Besaran efek (*effect size*) yang dihasilkan adalah Cohen's d = 0.78, mengindikasikan bahwa perbedaan *usability* kedua sistem tidak hanya signifikan secara statistik, tetapi juga memberikan dampak praktis yang substansial bagi pengalaman pengguna akhir.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis *tentang* riset seringkali menyerupai laporan kronologis harian layaknya diari ("pertama saya sebar kuesioner, lalu saya hitung, dan ini nilainya"). Sebaliknya, menulis sebagai *argumen* riset artinya kita menyusun narasi layaknya seorang pengacara: meyakinkan pembaca mengapa masalah ini krusial, menunjukkan metodologi yang kuat sebagai alat bukti, dan menyajikan hasil yang menjawab langsung permasalahan utama.
> 
> Mengubah urutan menulis menjadi mulai dari *Method* dan *Results* terlebih dahulu akan menjangkar (*anchor*) klaim kita pada fakta lapangan yang tak terbantahkan. Saat kemudian kita menulis *Introduction* di tahap akhir, kita dapat menyelaraskan narasi pembuka agar relevan dan langsung menjurus pada temuan aktual yang sudah terbukti, menghindarkan kita dari membuat klaim muluk-muluk di awal *paper* yang ternyata tidak didukung oleh data.
