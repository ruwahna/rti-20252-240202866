# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

**ANALYSIS & INTERPRETATION**

**1. Statistik Deskriptif:**

| Skenario    | Mean  | Std   | n  |
|-------------|-------|-------|----|
| SIGNAL      | 76.90 | 12.79 | 97 |
| New Sakpole | 67.16 | 12.03 | 97 |

**2. Uji Hipotesis:**
- **Uji yang digunakan  :** Independent T-Test
- **Justifikasi         :** Membandingkan nilai rata-rata (mean) dari 2 grup/kelompok data numerik yang saling bebas (independent) dan n > 30.
- **Hasil               :** p-value < 0.001, effect size (Cohen's d) = 0.78
- **CI 95%              :** Perbedaan ~9.74 poin (Interval tidak memotong nol)

**3. Keputusan:**
- [x] H₀ ditolak → H₁ diterima (Terdapat perbedaan signifikan)
- [ ] H₀ tidak ditolak

**4. Interpretasi:**
- **Hubungan ke RQ       :** Menjawab Research Question bahwa aplikasi SIGNAL terbukti memiliki tingkat usability (skor SUS) yang secara signifikan lebih tinggi dibandingkan New Sakpole.
- **Practical significance:** Perbedaan rata-rata skor sebesar nyaris 10 poin dengan effect size kategori *Large* (0.78) menunjukkan bahwa secara praktis di dunia nyata, perbedaannya benar-benar dapat dirasakan langsung oleh end-user.
- **Perbandingan literatur:** Berdasarkan literatur, batas kelayakan skor SUS adalah 68. New Sakpole (67.16) berada di bawah standar kelayakan minimum industri, sedangkan SIGNAL (76.90) berhasil masuk ke dalam kategori "Good / Acceptable".

**5. Limitation:**

| Jenis                | Ancaman                             | Dampak                               | Mitigasi                              |
|----------------------|-------------------------------------|--------------------------------------|---------------------------------------|
| Statistical validity | Asumsi normalitas mungkin meleset   | Mengurangi ketepatan estimasi p-value| Menggunakan uji non-parametrik (Wilcoxon/Mann-Whitney) jika data terbukti sangat skew. |
| External validity    | Responden mungkin terpusat di 1 demografi | Kesimpulan sulit digeneralisasi | Menyajikan batasan demografi secara transparan pada kesimpulan riset. |

**6. Failure Analysis (jika H₀ tidak ditolak):**
- **Penyebab potensial  :** N/A (H₀ berhasil ditolak)
- **Boundary condition  :** N/A
- **Insight             :** N/A

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 Grup (SIGNAL dan New Sakpole) |
| Apakah data berpasangan (paired)? | Tidak (Independent) |
| Apakah distribusi normal? (uji normalitas) | Ya (Berdasarkan Central Limit Theorem, n=97 > 30) |
| **Uji yang dipilih:** | Independent T-Test |
| **Justifikasi:** | T-test independen adalah standar emas di literatur untuk membandingkan rata-rata skor dari dua kelompok yang saling bebas dengan sampel yang cukup besar. |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data Riil:**
| Model       | SUS Score (mean ± std) | n  |
|-------------|------------------------|----|
| SIGNAL      | 76.90 ± 12.79          | 97 |
| New Sakpole | 67.16 ± 12.03          | 97 |

p < 0.001, Cohen's d = 0.78

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p-value < 0.001 (jauh di bawah ambang batas α=0.05), artinya perbedaan skor antara kedua kelompok sangat signifikan secara statistik (bukan karena kebetulan). |
| Effect size | Cohen's d = 0.78 menunjukkan *Medium-to-Large Effect*. Perbedaannya tidak hanya "ada", tapi juga berskala besar. |
| Practical significance | Secara praktis, peningkatan 9.7 poin pada skala SUS akan langsung mengubah pengalaman dan impresi responden dari yang tadinya "Marginal/Kurang" menjadi "Baik/Nyaman". |
| Hubungan ke RQ | Menjawab hipotesis utama penelitian bahwa perombakan desain sistem pada SIGNAL benar-benar membuahkan hasil positif yang signifikan dibanding sistem lama. |
| Perbandingan literatur | Skor standar minimal SUS di dunia industri UX adalah 68. Sakpole (67) tergolong "Poor", sementara SIGNAL (76) tergolong "Good". |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan gagal. Mendapati bahwa hipotesis alternatif tidak terdukung (H0 tidak ditolak) adalah temuan empiris yang valid dan berguna bagi komunitas sains. |
| Kemungkinan penyebab? | Pendekatan baru mungkin *over-engineered* sehingga menambah kompleksitas proses tanpa membawa manfaat berarti dibandingkan *baseline* yang sudah sederhana. |
| Boundary condition? | Metode eksperimental ini mungkin hanya bekerja dan relevan pada ukuran dataset raksasa, sementara pada data kecil ia justru kurang stabil. |
| Insight yang bisa diambil? | Terdapat *trade-off* di mana metode lama (*baseline*) terbukti jauh lebih efisien dan *robust* untuk menyelesaikan skenario standar sehari-hari. |
| Apakah layak dilaporkan? Mengapa? | Ya. Mempublikasikan *negative result* beserta analisis batasannya sangat krusial untuk mencegah peneliti masa depan membuang waktu di jalan buntu yang sama. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical limitation | Kurangnya ukuran sampel (*Sample size* kecil) | *Statistical power* menjadi terlalu rendah, sehingga gagal mendeteksi *effect size* yang kecil meskipun perbedaannya sebenarnya ada. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> "Failure" (yakni kegagalan menolak hipotesis nol) bukanlah sebuah kegagalan ilmiah, melainkan kontribusi dalam bentuk penetapan *boundary condition* (kondisi batas operasional sebuah sistem/teori). Dengan mengadopsi pola pikir *failure analysis*, hasil riset yang "negatif" tidak lagi dianggap sebagai aib yang harus dimanipulasi (*p-hacking*), melainkan sebagai kesempatan berharga untuk menjelaskan "kapan", "bagaimana", dan "kenapa" sesuatu tidak bekerja sesuai ekspektasi. Ini mendorong transparansi dan kemajuan ilmu pengetahuan itu sendiri.
