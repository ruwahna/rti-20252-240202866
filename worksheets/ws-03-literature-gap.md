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
* **Database**: ACM Digital Library, IEEE Xplore, Google Scholar
* **Query**: `("recommender system") AND ("serendipity" OR "diversity") AND ("filter bubble" OR "exploration-exploitation") AND ("e-commerce")`
* **Tahun**: 2023-2026
* **Hasil awal**: 15 paper → **Screening**: 10 paper final

#### Literature Matrix (Concept-Centric)

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Wang et al. | 2023 | Reinforcement Learning | Amazon | Diversitas ↑ 12% | Penurunan akurasi (CTR) jangka pendek. |
| Zhang & K. | 2024 | Graph Contrastive Learning | Taobao | Penemuan item long-tail | Komputasi graf berat; tidak real-time. |
| Perez et al. | 2024 | Determinantal Point Proc. | Retail Global | Variasi list merata | Fokus visual, bukan kejutan semantik. |
| Li & Suzuki | 2025 | Knowledge Graph Embed. | E-commerce | Relevansi stabil | Parameter serendipity masih statis. |
| Gomez et al. | 2025 | Multi-Armed Bandit | Interaction Log | Eksplorasi seimbang | Cold-start problem pada user baru. |
| Chen et al. | 2024 | Deep Q-Network (DQN) | Alibaba Data | Reward jangka panjang ↑ | Butuh data interaksi masif/historis. |
| Patel et al. | 2026 | Multi-Objective Opt. | Electronics | Trade-off Akurasi-Div | Parameter sangat sensitif/sulit tuning. |

**Pola yang ditemukan:**
* **Metode dominan**: Reinforcement Learning (RL) dan Multi-Armed Bandit untuk menyeimbangkan eksplorasi-eksploitasi.
* **Dataset umum**: Dataset publik skala besar (Amazon, Alibaba, Taobao).
* **Limitasi berulang**: Terjadinya *trade-off* (pertukaran); ketika diversitas/kejutan (serendipity) naik, akurasi prediksi biasanya menurun.

### GAP IDENTIFICATION

#### Gap 1: [Jenis: Method + Context]
* **Deskripsi**: Belum adanya mekanisme adaptasi parameter *serendipity* yang mampu menyesuaikan level kejutan secara dinamis berdasarkan perilaku belanja user secara *real-time*.
* **Bukti**: Berdasarkan matriks literatur (Li & Suzuki, 2025), parameter diversitas masih bersifat statis. Belum ada model yang mampu mendeteksi kapan user merasa jenuh (terjebak *filter bubble*) dan kapan mereka membutuhkan akurasi tinggi (sedang belanja efisien).
* **Signifikansi**: Kegagalan adaptasi ini dapat mengganggu kenyamanan user; terlalu banyak kejutan saat user terburu-buru akan dianggap *noise*, namun tidak ada kejutan saat *browsing* akan memicu kebosanan.

#### Gap 2: [Jenis: Data + Performance]
* **Deskripsi**: Rendahnya efisiensi komputasi pada algoritma penemuan item unik (*long-tail*) yang menghambat implementasi sistem rekomendasi yang *serendipitous* pada trafik tinggi.
* **Bukti**: Metode berbasis graf canggih (Zhang & K., 2024) memang efektif menemukan item tersembunyi, namun beban komputasinya sangat berat sehingga sulit diimplementasikan secara *real-time*.
* **Signifikansi**: Tanpa efisiensi komputasi, elemen kejutan tidak bisa diberikan secara instan, sehingga kehilangan relevansi terhadap minat user yang berubah cepat.

---

### BASELINE SELECTION

| Baseline | Relevansi | Representatif | Source |
| :--- | :--- | :--- | :--- |
| **Neural Collaborative Filtering (NCF)** | Standar utama untuk menangkap interaksi non-linear antara pengguna dan produk. | Patokan akurasi yang digunakan secara universal dalam riset sistem rekomendasi modern. | Wang et al. (2023) |
| **Multi-Armed Bandit (Epsilon-Greedy)** | Metode paling umum untuk menyeimbangkan eksplorasi item baru di industri. | Mewakili *common practice* industri dalam menangani masalah diversitas konten. | Gomez et al. (2025) |

**Justifikasi Pemilihan:**

Pemilihan baseline ini sangat **rigorus** dan adil (*bukan straw man*). NCF dipilih untuk memastikan model baru tetap kompetitif secara akurasi, sementara Bandit dipilih untuk membuktikan bahwa metode optimasi yang diusulkan memang lebih cerdas daripada sekadar memberikan rekomendasi acak.

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Optimasi Serendipity pada Sistem Rekomendasi E-Commerce untuk Mengatasi Filter Bubble.

**Query pencarian:** ("recommender system") AND ("serendipity" OR "diversity") AND ("e-commerce")

**Database:** Google Scholar & ACM DL.

| No | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Wang et al. | 2023 | RL | Amazon | Diversitas ↑ 12% | CTR menurun di awal sesi. |
| 2 | Li & Suzuki | 2025 | Knowledge Graph | E-commerce | Relevansi terjaga | Kejutan item kurang dinamis. |
| 3 | Gomez et al. | 2025 | Bandit Alg. | Log Interaksi | Eksplorasi optimal | Gagal pada user tanpa history. |
| 4 | Patel et al. | 2026 | Multi-Objective | Electronics | Pareto optimal | Kompleksitas komputasi tinggi. |
| 5 | Zhang & K. | 2024 | Graph Learning | Taobao | Long-tail naik | Latensi tinggi pada trafik besar. |

**Pola yang terlihat — Metode dominan:** Reinforcement Learning dan pendekatan berbasis Graph.

**Limitasi yang berulang:** Penurunan kepuasan user jangka pendek saat diberikan rekomendasi yang terlalu "asing".

---

## Latihan 2 — Gap Identification
Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya | Akurasi (Precision/Recall) menurun drastis saat tingkat serendipity ditingkatkan secara paksa. |
| Method Gap | [x] Ya | Mayoritas model menggunakan bobot kejutan statis; belum ada penyesuaian serendipity secara real-time berdasarkan mood user. |
| Data Gap | [x] Ya | Belum ada dataset e-commerce Indonesia untuk menguji toleransi user lokal terhadap filter bubble. |
| Context Gap | [x] Ya | Strategi serendipity belum membedakan fase belanja cepat (buying) vs fase sekadar melihat-lihat (browsing). |

**Gap utama yang dipilih:** **Method Gap (Dynamic Serendipity Adjustment)**
**Mengapa gap ini penting?**

> Karena kebutuhan user akan "kejutan" (serendipity) tidak selalu sama setiap waktu. Memberikan rekomendasi acak saat user sedang terburu-buru akan mengganggu, namun tidak memberikannya saat browsing akan membuat user bosan (*filter bubble*).

---

## Latihan 3 — Baseline Selection

| No | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Neural Collaborative Filtering (NCF) | Standar dasar untuk menangkap interaksi user-item. | Digunakan sebagai perbandingan standar di hampir semua riset. | Ya | Wang et al., 2023 |
| 2 | Epsilon-Greedy Bandit | Metode paling umum untuk menyeimbangkan eksplorasi item baru. | Mewakili praktik paling lazim dalam diversifikasi konten. | Bukan | Gomez et al., 2025 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> **Justifikasi**: Tidak, karena NCF adalah model SOTA yang sangat kuat dalam akurasi. Membandingkan metode baru dengan NCF adalah pengujian yang jujur.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada" hanyalah spekulasi jika tidak ada bukti pencarian. **Research gap yang valid** adalah kesimpulan objektif yang didasarkan pada matriks literatur. Cara membuktikannya adalah dengan menunjukkan bahwa dari sekian banyak paper SOTA (misal 2023-2026), semuanya masih memiliki limitasi yang sama (seperti masalah *accuracy-serendipity trade-off*) yang belum terpecahkan secara tuntas.