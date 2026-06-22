# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification


LITERATURE MAPPING

* **Topik**: Analisis komparatif usability dan user experience pada layanan pajak kendaraan digital
* **Database**: Google Scholar, Garuda, ResearchGate, IEEE Xplore
* **Query**: `("SIGNAL" OR "Samsat" OR "pajak kendaraan") AND ("usability" OR "user experience" OR "UX") AND ("aplikasi" OR "mobile")`
* **Tahun**: 2022-2025

#### Literature Matrix (Concept-Centric)

| Study (Penulis & Tahun) | Platform | Method | Metric | Result | Limitation |
|:---|:---|:---|:---|:---|:---|
| **Analisis SUS SIGNAL (2024)** | SIGNAL | SUS | SUS Score | Skor marginal (50-60), kategori "Okay" | Hanya SUS, tidak ada breakdown per fase tugas |
| **Evaluasi SIGNAL UEQ (2023)** | SIGNAL | UEQ | 6 dimensi | Efisiensi sedang, daya tarik rendah | Hanya platform nasional, tidak ada komparasi |
| **Sentimen Play Store SIGNAL (2024)** | SIGNAL | Sentiment Analysis | Rating + text | 35% keluhan tentang verifikasi gagal | Hanya feedback negatif yang dominan |
| **Studi TAM New Sakpole (2022)** | New Sakpole | TAM | PEOU, PU | Perceived Ease of Use tinggi (4.2/5) | Dataset lokal, sulit digeneralisasi |
| **Komparasi Pajak Nasional vs Daerah (2025)** | SIGNAL & Daerah | Comparison | SUS, task time | SIGNAL lebih lambat 2.5x | Sampel kecil (20 responden) |

**Pola yang ditemukan:**
* **Metode dominan**: Studi SIGNAL cenderung pakai instrumen kuantitatif (SUS, UEQ, TAM). Studi New Sakpole lebih lokal dan terbatas.
* **Limitasi berulang**: Tidak ada studi komparatif sistematis dengan instrumen identik untuk kedua platform; keluhan di Play Store banyak tapi belum ditinjau dengan kerangka teoritis.

### GAP IDENTIFICATION

#### Gap 1: [Jenis: Method Gap]
* **Deskripsi**: Belum ada kerangka komparatif terstandar yang membandingkan SIGNAL dan New Sakpole pada tugas yang sama (registrasi, verifikasi, pembayaran) menggunakan instrumen evaluasi yang identik (SUS + UEQ + task metrics).
* **Bukti**: Paper 2024 pakai SUS untuk SIGNAL, paper 2022 pakai TAM untuk New Sakpole. Akibatnya sulit menyimpulkan perbedaan secara langsung karena instrumen berbeda.
* **Signifikansi**: Tanpa kerangka komparatif yang sama, rekomendasi perbaikan akan spekulatif, bukan berbasis bukti sistematis.

#### Gap 2: [Jenis: Context + Data Gap]
* **Deskripsi**: Studi yang ada mayoritas fokus di satu platform (SIGNAL atau New Sakpole saja), belum ada yang mengevaluasi kedua aplikasi dalam konteks task workflow yang sama dan dengan responden profil yang setara.
* **Bukti**: Paper komparatif 2025 hanya dengan 20 responden. Paper SUS SIGNAL tidak membedakan fase tugas (fase registrasi vs verifikasi vs pembayaran punya kompleksitas berbeda).
* **Signifikansi**: Tanpa evaluasi fase-spesifik, sulit mengidentifikasi tahap mana yang paling problematik dan butuh prioritas perbaikan.

---

### BASELINE SELECTION

| Baseline | Relevansi | Representatif | Source |
| :--- | :--- | :--- | :--- |
| **SUS Score dari paper SIGNAL 2024** | Metrik standar usability yang paling sering dipakai untuk aplikasi lokal | Mewakili studi SUS terakhir dan paling relevan untuk SIGNAL | (2024) |
| **UEQ dari evaluasi SIGNAL 2023** | Mengukur 6 dimensi UX, lebih comprehensive dari hanya SUS | Standar internasional untuk evaluasi user experience | (2023) |

**Justifikasi Pemilihan:**

Baseline dipilih dari studi terbaru (2024, 2023) yang secara langsung mengevaluasi SIGNAL dengan instrumen standar industri. UEQ dipilih sebagai baseline tambahan untuk menangkap aspek UX yang lebih holistik dari hanya usability (SUS). Pemilihan ini tidak termasuk straw man comparison karena both baselines adalah hasil evaluasi serius platform SIGNAL itu sendiri.

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Optimasi Serendipity pada Sistem Rekomendasi E-Commerce untuk Mengatasi Filter Bubble.

**Query pencarian:** `("sistem rekomendasi") AND ("serendipity" OR "diversitas") AND ("e-commerce")`

**Database:** Google Scholar & Garuda.

| No | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Mahendra et al. | 2020 | Collaborative Filtering | Toko Online | Akurasi prediksi tinggi. | Terjebak Filter Bubble (monoton). |
| 2 | Wati et al. | 2021 | Hybrid (CF & Content) | Retail Lokal | Relevansi produk meningkat. | Mengabaikan aspek kejutan (serendipity). |
| 3 | Nugraha et al. | 2022 | Re-Ranking Algorithm | Fashion | Produk unik lebih terlihat. | Parameter masih bersifat statis. |
| 4 | Fauzi et al. | 2023 | K-Nearest Neighbor | UMKM Indo | Variasi produk ↑ 15%. | Penyesuaian bobot manual/kaku. |
| 5 | Savitri et al. | 2024 | Deep Learning | E-commerce | Coverage produk meluas. | Beban komputasi tinggi (lambat). |

**Pola yang terlihat — Metode dominan:** Hybrid Filtering dan pendekatan berbasis Re-ranking.

**Limitasi yang berulang:** Terjadinya trade-off akurasi; ketika kejutan ditambah, sistem sering kehilangan relevansi karena parameter yang digunakan tidak fleksibel (statis).
---

## Latihan 2 — Gap Identification
Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya | Akurasi (CTR) menurun drastis saat tingkat serendipity ditingkatkan secara manual tanpa kontrol. |
| Method Gap | [x] Ya | Belum ada mekanisme pembobotan dinamis (Dynamic Weighting) yang menyesuaikan level kejutan secara real-time. |
| Data Gap | [x] Ya | Minimnya penggunaan dataset e-commerce khusus produk lokal (UMKM) untuk menguji toleransi kejutan user. |
| Context Gap | [x] Ya | Strategi serendipity belum membedakan fase belanja cepat (buying) vs fase sekadar melihat-lihat (browsing). |

**Gap utama yang dipilih:** **Method Gap (Dynamic Serendipity Adjustment)**

**Mengapa gap ini penting?**
> Karena kebutuhan user akan "kejutan" tidak selalu sama. Jika sistem memberikan barang asing saat user sedang terburu-buru (misal: beli sabun yang biasa dipakai), itu dianggap gangguan. Namun, jika tidak ada kejutan saat browsing (cuci mata), user akan merasa bosan karena barang yang muncul itu-itu saja (filter bubble).

---

## Latihan 3 — Baseline Selection

| No | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | SUS Score SIGNAL 2024 | Metrik standar untuk mengevaluasi usability aplikasi lokal | Representatif dari evaluasi SIGNAL terkini dan paling relevan | Ya | Paper 2024 |
| 2 | UEQ Score SIGNAL 2023 | Mengukur enam dimensi UX secara comprehensive, bukan hanya usability | Mewakili evaluasi UX yang lebih mendalam dari paper SIGNAL sebelumnya | Ya | Paper 2023 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak

**Justifikasi:**
> Tidak, karena baseline adalah hasil evaluasi riil platform SIGNAL itu sendiri, bukan perbandingan dengan sistem yang jauh lebih sederhana. Dengan baseline ini, kita bisa membandingkan hasil komparatif kita dengan studi sebelumnya dan melihat apakah temuan konsisten atau berbeda. Ini pendekatan yang adil dan ilmiah.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**

> Dalam riset, sering ada peneliti bilang "belum ada yang teliti ini" tapi sebenarnya maksudnya just belum teliti dengan cara yang mereka rasa lebih baik. Itu beda dengan gap yang valid.

> Gap yang valid itu terbukti dengan:
1. **Bukti pencarian**: "Saya cari pakai keywords X, Y, Z di database A, B, C. Ini hasilnya." (lihat tabel literatur kami di atas)
2. **Pola limitasi yang konsisten**: "Lihat nih lima paper terbaru, semuanya punya keterbatasan yang sama—tidak ada satu pun yang compare kedua platform dengan instrumen identik"
3. **Posisi jelas**: "Paper 2024 evaluate SIGNAL dengan SUS, paper 2022 evaluate New Sakpole dengan TAM. Karena instrumen beda, hasil tidak bisa dibandingkan langsung. Itu gap kami isi."