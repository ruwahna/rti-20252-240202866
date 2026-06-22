# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

**RESULT PRESENTATION PLAN**

**Research Question :** Apakah terdapat perbedaan usability (SUS) antara aplikasi SIGNAL dan New Sakpole?
**Metrik Utama      :** Skor SUS (System Usability Scale)

**Tabel Hasil:**

| Skenario    | Metrik 1 (SUS Score mean ± std) | Metrik 2 (-) | n  |
|-------------|---------------------------------|--------------|----|
| SIGNAL      | 76.90 ± 12.79                   | -            | 97 |
| New Sakpole | 67.16 ± 12.03                   | -            | 97 |

**Visualisasi yang Direncanakan:**

| # | Jenis Grafik          | Pesan Utama                                           | Metrik         |
|---|-----------------------|-------------------------------------------------------|----------------|
| 1 | Bar Chart + Error Bar | Perbandingan rata-rata skor SUS SIGNAL vs New Sakpole | Mean SUS ± std |
| 2 | Box Plot              | Distribusi skor SUS responden pada tiap aplikasi      | Semua run SUS  |

**Bias Check:**
- [x] Y-axis mulai dari 0 (atau dijustifikasi)
- [x] Error bar/CI ditampilkan
- [x] Semua data disertakan (tidak cherry-picked)
- [x] Tidak menggunakan 3D tanpa alasan

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario            | Metrik 1 (SUS Score mean ± std) | Metrik 2 (-)     | n  |
|---------------------|---------------------------------|------------------|----|
| *Contoh: BERT-base* | *88.4 ± 1.2%*                   | *45.2 ± 3.1 min* | *10* |
| SIGNAL              | 76.90 ± 12.79                   | -                | 97 |
| New Sakpole         | 67.16 ± 12.03                   | -                | 97 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik                  | Pesan                                                 | Data yang Digunakan       |
|---|-------------------------------|-------------------------------------------------------|---------------------------|
| 1 | *Contoh: Bar chart + error bar* | *Perbandingan accuracy antar 3 model*               | *Mean accuracy ± std*     |
| 2 | Bar Chart + Error Bar         | Perbandingan rata-rata skor SUS SIGNAL vs New Sakpole | Mean SUS ± std            |
| 3 | Box Plot                      | Distribusi skor SUS responden pada tiap aplikasi      | Semua skor SUS yang valid |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | *Contoh: Ya — A terlihat 2× B padahal beda 0.4%* |
| Apakah error bar ditampilkan? | Tidak, visualisasi tersebut menyembunyikan signifikansi statistik |
| Apakah semua kondisi ditampilkan? | Ya, tapi distribusinya tidak terlihat |
| Apa solusinya? | Mulai Y-axis dari 0, atau gunakan range yang masuk akal dengan menyertakan error bar (Standard Deviation/CI) agar terlihat apakah perbedaan 0.4% itu signifikan atau masuk dalam margin of error. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: Tidak ada, saya merencanakan Y-axis dari 0 dan menggunakan error bar.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel diperlukan untuk memberikan nilai persis (presisi) agar data bisa disitasi atau direproduksi oleh orang lain. Sedangkan grafik diperlukan untuk menunjukkan pola visual atau tren yang sulit dilihat sekilas pada angka-angka tabel. Keduanya saling melengkapi.
> 
> Ya, saya pernah membuat grafik bar chart yang rentang Y-axis-nya saya potong (tidak dari 0) agar perbedaannya terlihat besar, padahal bedanya sangat kecil.
