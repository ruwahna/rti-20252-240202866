# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

**DEFENSE PREPARATION**

**Slide Deck Plan:**
  Total slides   : 9 slide (1 title, 7 konten, 1 closing)
  Time per slide : ~1.5 - 2 menit
  Total time     : 15 menit

**Slide Outline:**
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title (Analisis Usability SIGNAL vs New Sakpole) | Logo SIGNAL & Sakpole | 1 min |
| 2 | Problem: Warga sering ngeluh ribet bayar pajak online | Screenshot keluhan/rating | 2 min |
| 3 | Gap + RQ: Benarkah UI baru SIGNAL lebih baik dari Sakpole? | Tabel gap riset | 1.5 min |
| 4 | Method: Pakai kuesioner SUS dan uji T-Test | Alur riset (diagram) | 2 min |
| 5 | Key Result: Skor SUS SIGNAL 76.90 vs Sakpole 67.16 | Tabel rata-rata skor | 2 min |
| 6 | Visualisasi: Perbedaan ini signifikan banget | Bar chart pakai error bar | 2 min |
| 7 | Interpretasi: SIGNAL udah layak, Sakpole belum | Standar SUS 68 (garis batas) | 2 min |
| 8 | Limitasi: Responden cuma 194 orang | Poin-poin teks singkat | 1.5 min |
| 9 | Conclusion: SIGNAL menang, Sakpole butuh evaluasi UI | Kesimpulan singkat | 1 min |

**Anticipatory Defense Matrix:**
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Kenapa pilih metrik SUS? | SUS itu standar industri yang paling gampang dipahami buat ngukur kepuasan (Claim). Jurnal-jurnal besar juga pakai ini buat riset UX (Evidence). Jadi hasilnya bisa gampang dibandingin (Reasoning). |
| Method   | Yakin sampel 194 orang cukup? | Cukup banget buat T-Test (Claim). Secara teori, sampel di atas 30 aja udah lumayan mendekati normal, apalagi ini 194 (Evidence). Jadi hasil uji statistiknya valid (Reasoning). |
| Results  | Kenapa Sakpole bisa lebih rendah? | Desain UI Sakpole mungkin terlalu kaku atau fiturnya ngebingungin (Claim). Skor yang cuma 67.16 itu di bawah standar layak 68 (Evidence). Berarti emang ada masalah mendasar di aplikasinya (Reasoning). |

**Latihan:**
  Latihan 1: [Belum dilakukan] — [Fokus melancarkan ngomong di 3 slide pertama]
  Latihan 2: [Belum dilakukan] — [Fokus latihan ngejelasin grafik biar nggak berbelit]
  Latihan 3: [Belum dilakukan] — [Simulasi tanya jawab bareng temen kelompok]

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul dan perkenalan topik e-Samsat | Judul paper, nama, dan logo aplikasi | 1 min |
| 2 | Kenapa bayar pajak online kadang masih bikin mumet orang | Screenshot review kurang bagus di PlayStore | 2 min |
| 3 | Rumusan masalah: SIGNAL vs New Sakpole, mana yang lebih enak dipakai? | Highlight pertanyaan utama (RQ) | 1.5 min |
| 4 | Metodologi: Ambil data SUS dari 194 responden, diuji pakai T-Test | Diagram alur pengumpulan data | 2 min |
| 5 | Tabel Hasil: SIGNAL dapat 76.90, Sakpole dapat 67.16 | Tabel angka (Mean & Std) | 2 min |
| 6 | Grafik Hasil: Beda banget loh secara visual | Bar chart pakai garis error (error bar) | 2 min |
| 7 | Interpretasi: SIGNAL masuk kategori "Good", Sakpole "Poor" | Grafik batas kelayakan SUS (angka 68) | 2 min |
| 8 | Limitasi penelitian: Riset kita cuma punya sampel terbatas | List pendek tentang batasan riset kita | 1.5 min |
| 9 | Kesimpulan: Sakpole harus segera merombak UI-nya | Kalimat penutup yang kuat | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | *Method* | Kenapa cuma ngecek usability, kok nggak sekalian ngecek keamanan sistemnya? | Fokus riset ini murni di persepsi user (UX). | Tujuan di awal bab adalah lihat seberapa gampang aplikasi dipakai masyarakat. | Kalau aplikasinya aja ribet dipakai, warganya jadi males bayar pajak online. Jadi ngebahas UX itu penting banget. |
| 2 | *Method* | Kenapa datanya dianalisis pakai T-Test, kenapa nggak ANOVA aja? | Karena kita cuma ngebandingin dua kelompok doang. | Data kelompok uji kita cuma ada 2 aplikasi: SIGNAL dan Sakpole. | Syarat ANOVA itu kan buat 3 kelompok atau lebih. Kalau cuma 2 kelompok, ya pakai Independent T-Test adalah yang paling tepat. |
| 3 | *Results* | Yakin perbedaan skornya nggak cuma kebetulan doang? | Sangat yakin ini bukan kebetulan. | Nilai p-value kita dapet < 0.001, dan Cohen's d nya gede di 0.78. | Angka p-value sekecil itu udah ngebuktiin bedanya sangat signifikan secara statistik. |
| 4 | *Generalization*| Apakah hasil ini berlaku buat semua warga Jawa Tengah? | Nggak sepenuhnya bisa diklaim buat senasional atau se-provinsi. | Responden kita sebarannya mungkin kurang merata ke semua kalangan umur. | Makanya ini ditulis di presentasi sebagai limitasi penelitian. Butuh riset survei besar besaran buat klaim general. |
| 5 | *Problem* | Emangnya standar skor 68 di SUS itu kamu dapet dari mana? | Itu udah kesepakatan baku internasional buat ngukur SUS. | Penemu SUS dan banyak paper literatur bilang kalau 68 itu titik tengah kelayakan rata-rata. | Karena itu, kalau Sakpole cuma dapet 67, ya emang bisa disimpulkan belum cukup layak atau belum seenak itu dipakai. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Saran kongkret kamu buat tim developer Sakpole apa? | Saran saya rombak ulang alur UI-nya, minimal disimplifikasi kayak SIGNAL biar navigasinya ngga bikin user bingung. | [x] Direct [x] Data-based [x] Honest |
| 2 | Pas cleaning data, ada yang kamu buang ngga datanya? Kenapa? | Ada, ada 6 data yang dibuang. Soalnya 5 datanya kosong (user ngga selesai ngisi form), dan 1 data ngasih skor lebih dari 100 padahal ngga logis. | [x] Direct [x] Data-based [x] Honest |
| 3 | Kenapa ngga ngewawancara user aja secara langsung biar tau keluhannya apa? | Riset ini pake pendekatan kuantitatif dulu buat ngebuktiin "beneran beda ngga sih?". Kalau mau cari "kenapa detilnya", itu jatohnya ke riset kualitatif selanjutnya. | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Pas iseng ditanya soal apa sih bedanya fitur Sakpole dan SIGNAL secara spesifik di dalam sistemnya yang bikin nilainya jomplang. Soalnya kan kita cuma nganalisis hasil kuesioner doang, ngga ngebongkar UI/UX aplikasinya secara mendalam satu persatu.

**Apa yang perlu disiapkan lebih baik:**
> Saya harus lebih siap baca-baca konteks atau berita/review user di internet tentang masalah spesifik aplikasinya biar kalau ditanya nyerempet ke teknis sedikit, saya punya gambaran buat argumen *back-up*.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Dulu saya kira ngerjain tugas akhir / riset itu cuma soal nyari data kuesioner yang banyak terus dijadiin laporan tebal berlembar-lembar. Ternyata ngga gitu. Riset itu soal "Bercerita dengan logika dan data". Walaupun hasil hitung-hitungannya jago, kalau kita nggak bisa membingkai masalah dan menceritakan apa dampaknya, ya risetnya bakal kerasa hampa. Saya juga baru sadar kalau hipotesis yang ditolak/hasilnya negatif itu tetep berharga banget, asal kita bisa ngejelasin kondisi "kenapa"-nya.

**Yang akan selalu diterapkan:**
> Saya bakal terus membiasakan diri pakai metode nyusun argumen *CER (Claim, Evidence, Reasoning)*. Terutama pas sesi tanya jawab sama dosen biar ngga muter-muter pas ngomong. Biar kedengeran lugas karena ngomong langsung ngasih bukti konkrit, bukan ngeles doang.
