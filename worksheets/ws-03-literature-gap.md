# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
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

* **Topik**: Optimasi *Serendipity* pada Sistem Rekomendasi E-Commerce untuk Mengatasi *Filter Bubble*
* **Database**: Google Scholar, Garuda, IEEE Xplore
* **Query**: `("sistem rekomendasi") AND ("serendipity" OR "diversitas") AND ("e-commerce")`
* **Tahun**: 2020-2025

#### Literature Matrix (Concept-Centric)

| Study (Penulis & Tahun) | Method | Data | Result | Limitation |
|:---|:---|:---|:---|:---|
| **Mahendra et al. (2020)** | Collaborative Filtering | Dataset Toko Online | Akurasi tinggi dalam prediksi minat. | Terjadi *overspecialization* (*filter bubble*). |
| **Wati et al. (2021)** | Hybrid (CF & Content) | Data Retail Lokal | Relevansi produk sangat personal. | Belum mengukur aspek kejutan (*serendipity*). |
| **Nugraha et al. (2022)** | Re-Ranking Algorithm | E-commerce Fashion | Efektif memunculkan produk unik. | Tidak ada adaptasi *real-time* terhadap user. |
| **Fauzi et al. (2023)** | K-Nearest Neighbor | Marketplace UMKM | Variasi produk meningkat 15%. | Parameter diversitas masih bersifat statis. |
| **Savitri et al. (2024)** | Deep Learning | Dataset E-commerce | *Coverage* produk meningkat luas. | Beban komputasi berat (sulit *real-time*). |

**Pola yang ditemukan:**
* **Metode dominan**: Penggunaan *Hybrid Filtering* dan *Collaborative Filtering* masih mendominasi di Indonesia.
* **Limitasi berulang**: Terjadi *accuracy-serendipity trade-off*; ketika elemen kejutan ditingkatkan, akurasi biasanya menurun drastis karena parameter pembobotan yang masih kaku (statis).

### GAP IDENTIFICATION

#### Gap 1: [Jenis: Method Gap]
* **Deskripsi**: Belum adanya mekanisme adaptasi parameter *serendipity* yang mampu menyesuaikan level kejutan secara dinamis (otomatis) berdasarkan perilaku interaksi pengguna secara *real-time*.
* **Bukti**: Berdasarkan matriks literatur (Fauzi et al., 2023), pembobotan diversitas masih bersifat statis/manual. Belum ada model yang mampu mendeteksi kapan user merasa jenuh (terjebak *filter bubble*) dan kapan mereka sedang membutuhkan akurasi tinggi (sedang belanja cepat).
* **Signifikansi**: Kegagalan adaptasi ini dapat mengganggu kenyamanan user; terlalu banyak kejutan saat user sedang terburu-buru akan dianggap sebagai gangguan (*noise*).

#### Gap 2: [Jenis: Context + Data Gap]
* **Deskripsi**: Minimnya evaluasi aspek *serendipity* pada platform e-commerce khusus produk UMKM lokal Indonesia yang memiliki karakteristik data yang sangat beragam (*long-tail*).
* **Bukti**: Penelitian terbaru (Savitri et al., 2024) masih menggunakan dataset global berskala besar, sehingga belum menyentuh karakteristik unik dari perilaku belanja dan profil produk lokal di Indonesia.
* **Signifikansi**: Tanpa pengujian pada konteks lokal, efektivitas algoritma kejutan mungkin tidak sesuai dengan selera atau toleransi pengguna di Indonesia terhadap barang-barang baru.

---

### BASELINE SELECTION

| Baseline | Relevansi | Representatif | Source |
| :--- | :--- | :--- | :--- |
| **Hybrid Recommendation** | Menyeimbangkan antara akurasi konten (minat) dan perilaku sosial pengguna. | Mewakili standar sistem rekomendasi yang paling banyak diimplementasikan di industri retail saat ini. | Wati et al. (2021) |
| **Collaborative Filtering** | Metode fundamental untuk menangkap pola preferensi pengguna berdasarkan kemiripan komunitas. | Patokan standar (gold standard) untuk mengukur tingkat kejenuhan rekomendasi (*Filter Bubble*). | Mahendra et al. (2020) |

**Justifikasi Pemilihan:**

Pemilihan baseline ini sangat **rigorus** dan adil (*bukan straw man comparison*). **Hybrid Recommendation** dipilih untuk memastikan model optimasi baru tetap kompetitif secara akurasi, sementara **Collaborative Filtering** dipilih sebagai kontrol untuk membuktikan bahwa metode yang diusulkan memang berhasil memberikan variasi (kejutan) yang lebih baik daripada metode standar yang sering terjebak dalam *filter bubble*.

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

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
| 1 | Hybrid Recommendation | Menyeimbangkan akurasi konten dan pola perilaku user. | Standar sistem rekomendasi yang paling banyak digunakan di Indonesia saat ini. | Ya | Wati et al., 2021 |
| 2 | Collaborative Filtering | Dasar utama prediksi berdasarkan kemiripan komunitas. | Patokan standar untuk melihat tingkat kejenuhan (Filter Bubble). | Tidak | Mahendra et al., 2020 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak

**Justifikasi:**
> Tidak, karena Hybrid Recommendation adalah lawan yang sangat kuat dalam hal akurasi. Membandingkan metode baru dengan Hybrid adalah pengujian yang jujur untuk membuktikan peningkatan serendipity tanpa merusak relevansi.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
Klaim **"belum ada yang meneliti ini"** sering kali bersifat spekulatif dan subjektif karena hanya didasarkan pada asumsi pribadi tanpa proses verifikasi yang jelas. Sebaliknya, **research gap yang valid** adalah kesimpulan objektif yang lahir dari sintesis mendalam terhadap literatur yang ada (*positioning*).

**Cara membuktikan bahwa sebuah gap benar-benar ada:**

1. **Sistematika Pencarian:** Menunjukkan bukti penelusuran literatur yang komprehensif melalui matriks literatur (seperti pada Latihan 1).
2. **Identifikasi Pola Limitasi:** Menunjukkan bahwa meskipun terdapat banyak penelitian *State-of-the-Art* (SOTA) terbaru (rentang 2023-2026), mayoritas masih memiliki keterbatasan yang serupa—seperti masalah *accuracy-serendipity trade-off*—yang belum terpecahkan secara tuntas.
3. **Justifikasi Ilmiah:** Gap terbukti nyata ketika kita mampu memetakan secara eksplisit di mana posisi penelitian terdahulu berhenti, dan bagaimana solusi yang kita tawarkan hadir untuk mengisi kekosongan (gap) tersebut.