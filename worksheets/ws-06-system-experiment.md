# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

### Research Question
**Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis (registrasi, verifikasi identitas, pembayaran)?**

---

### Variable → Component Mapping

Catatan: Karena riset ini adalah **comparative usability study** (bukan artifact development), "sistem" yang dimaksud adalah **experimental setup** (testing environment + task protocol) bukan implementasi algoritma baru.

| Variabel | Tipe | Komponen Experimental | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|------------------------------|
| **Platform Aplikasi** | IV | **Mobile Testing Environment** — Install SIGNAL dan New Sakpole di device terkontrol (Android emulator atau actual phone). Isolasi kedua apps supaya tidak mutual interference. | Switch platform per sesi responden via random assignment. Dokumentasi: app version, OS version, device type tetap sama untuk semua responden (control). |
| **Fase User Journey** | IV | **Task Protocol Module** — 3 task terstruktur (Registrasi → Verifikasi → Pembayaran) dengan instruksi eksplisit dan scenario kartu. | Standardisasi task: "Daftar akun baru dengan NIK Anda", "Verifikasi dengan foto KTP", "Bayar pajak untuk kendaraan anda". Setiap fase dimulai dari state clean (logout/app restart antar fase). |
| **Usability Score (SUS)** | DV | **Post-Task Questionnaire Module** — Digital form atau paper-based SUS questionnaire (10 items × Likert 1-5). | Administer SUS setelah setiap fase selesai (atau failed). Scoring formula: (raw_sum - 10) × 2.5 → range 0-100. Auto-compute via spreadsheet atau script. |
| **User Experience Score (UEQ)** | DV | **Post-Task Questionnaire Module** — Digital form UEQ (26 items × 7-point semantic differential). | Administer setelah semua 3 fase selesai (tidak per-fase, karena UEQ panjang). Scoring per dimensi (Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty). |
| **Task Completion Time** | DV | **System Logger + Stopwatch** — Auto-log timestamp start/end dari task di app (jika API available), fallback: observer manual stopwatch dengan video backup. | Measure duration dari user mulai interact hingga konfirmasi success (atau timeout/fail). Format: detik. Validasi manual via video review jika ada discrepancy. |
| **Task Success Rate** | DV | **Observer Checklist** — Binary per-phase: sukses (konfirmasi muncul) vs gagal (error/timeout). | Dokumentasi per responden per platform per phase. Hitung: (count success) / (total attempts) × 100%. |
| **Digital Literacy Level** | CV | **Pre-Experiment Questionnaire** — Self-rated digital literacy (1-5 Likert) atau objective test (e.g., "berapa jam per hari pakai smartphone?"). | Fixed at baseline, tidak dimanipulasi. Gunakan untuk stratification dan sensitivity analysis. |
| **Perangkat & OS Version** | CV | **Device Specification Config** — Standar device untuk semua responden (e.g., "Samsung Galaxy A12, Android 11" atau "iPhone 11, iOS 15"). | Locked/tidak bervariasi. Jika variation perlu, dokumentasi jelas dan stratifikasi analisis. |

---

### 4 Prinsip Desain

✅ **Traceability** — Setiap komponen percobaan bisa ditelusuri ke variabel
- Mobile Testing Environment & Task Protocol ↔ IV (platform, phase)
- Questionnaire Module & System Logger ↔ DV (SUS, UEQ, task metrics)
- Device Spec & Pre-Exp Questionnaire ↔ CV (digital literacy, device)

✅ **Variable Isolation** — IV bisa diubah (platform/phase) tanpa mengubah setup lain
- Instruksi task identik untuk kedua platform
- SUS dan task metrics diukur identik untuk SIGNAL dan New Sakpole
- Random assignment responden ke sequence (SIGNAL dulu atau New Sakpole dulu) untuk eliminate order effect

✅ **Measurement Integration** — Pengukuran DV standardisasi
- SUS questionnaire identical template
- UEQ questionnaire identical template  
- Task timing metodologi sama (video + stopwatch)
- Success criteria dokumentasi jelas sebelum eksperimen

✅ **Reproducibility** — Setup bisa direkonstruksi
- Task protocol dokumentasi detail di task cards (bukan verbal instruction random)
- Questionnaire versi digital saved untuk audit trail
- Video recordings disimpan untuk verification
- Responden demographics dokumentasi lengkap

---

### Experimental Setup

**Setting:**
- Lokasi: Controlled lab environment (quiet room, consistent lighting) atau field (kantor pajak, rumah responden dengan observer) — dokumentasi mana pilihan dan justifikasi

**Responden:**
- Target sample: N≥30 per platform × 3 fase (minimum 90 data points)
- Stratification: usia <30, 30-55, >55; digital literacy rendah/sedang/tinggi
- Random assignment: half eksperimen SIGNAL dulu, half New Sakpole dulu (counterbalance order effect)

**Hardware:**
- Device: Standard phone (e.g., Samsung A series or iPhone 11) — sama untuk semua responden
- OS: Latest stable version (Android 12+ atau iOS 15+)
- Internet: Stable WiFi (fixed ISP) atau mobile data (dokumentasi)
- Screen recording: OBS Studio atau phone built-in recorder untuk capture task behavior

**Task Scenario Cards:**
```
PHASE 1: REGISTRASI
Instruksi: "Buka aplikasi ini. Daftar akun baru menggunakan NIK Anda yang sebenarnya. Catat waktu mulai sekarang. Klik tombol Selesai ketika akun berhasil dibuat."
Success Criteria: Konfirmasi "Akun Berhasil Dibuat" muncul; responden bisa lihat dashboard home.
Timeout: 15 menit.

PHASE 2: VERIFIKASI IDENTITAS
Instruksi: "Lanjutkan dari akun yang sudah dibuat. Ikuti proses verifikasi identitas dengan foto KTP Anda (atau KTP dummy untuk testing). Catat waktu mulai sekarang. Selesai ketika sistem menerima verifikasi."
Success Criteria: Status menunjukkan "Terverifikasi" atau "Sedang Diproses"; user dapat lanjut ke pembayaran.
Timeout: 10 menit.

PHASE 3: PEMBAYARAN
Instruksi: "Lanjutkan pembayaran pajak untuk kendaraan Anda. Pilih metode pembayaran (boleh pilihan dummy/cancel di akhir jika ingin). Catat waktu mulai sekarang. Selesai ketika konfirmasi pembayaran muncul atau transaksi tercatat."
Success Criteria: Konfirmasi pembayaran atau struk muncul di aplikasi.
Timeout: 15 menit.
```

**Output Format:**
- Per-session JSON: {session_id, recommender_type, unexpectedness_score, f1_weighted, category, user_phase}
- Aggregated CSV: satu baris per session

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah metode Dynamic Serendipity Adjustment (DSA) menghasilkan skor Unexpectedness yang lebih tinggi tanpa menurunkan F1-Score lebih dari 2% dibandingkan dengan metode Hybrid Recommendation pada dataset e-commerce?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Strategi Pembobotan Serendipity | IV | Recommendation Engine Module (dual-algorithm: Hybrid vs DSA) | Config recommender_type swap antara hybrid dan dsa; init weight param dari config file. |
| Unexpectedness Score | DV | Metrics Collector Module — calculate_unexpectedness() | Query transaction log per session, cross-check user history 90 hari, hitung proporsi produk baru, output nilai 0.0-1.0. |
| F1-Score (Weighted) | DV | Metrics Collector Module — calculate_f1_weighted() | Ground truth: rating >= 3.5 = positive. Compute TP/FP/FN per kategori, precision/recall per kategori, F1-weighted average. |
| Kategori Produk | CV | Configuration (product_categories.yaml) | Fixed list: Fashion, Elektronik, Rumah Tangga, dll. Load saat startup, gunakan untuk stratifikasi. |
| Perilaku User (Phase) | CV | Phase Detector Module | Classify dari behavior log: Buying Phase (pending checkout <15 min) vs Browsing Phase (exploratory >5 min no checkout). |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Semua 5 variabel (2 IV, 2 DV, 2 CV) sudah ter-map ke komponen spesifik. Tidak ada lompatan logis; setiap variabel punya role jelas di sistem.

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| **Traceability** | OK | Recommendation Engine module langsung map ke IV (strategi pembobotan). Metrics Collector map ke DV (unexpectedness, F1). Config & Phase Detector map ke CV. RQ -> Variables -> Components membentuk rantai jelas. |
| **Modularity** | OK | Recommendation Engine, Metrics Collector, Phase Detector, Config adalah modul terpisah. IV (algoritma) bisa di-swap via config tanpa modifikasi code lain. Metrics Collector bisa dijalankan independent. |
| **Controllability** | OK | Semua CV (kategori, phase threshold, lookback_days) dieksternalisasi ke YAML config files. Tidak hardcoded. Tim dapat mereproduksi eksperimen dengan swap config file saja. |
| **Measurability** | OK | DV (Unexpectedness, F1) dihitung otomatis oleh Metrics Collector per session. Output format JSON terstruktur. Tidak ada manual calculation atau ambiguitas. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (menutup hardcoding parameter)

**Strategi untuk mengatasinya:**
> (1) Identifikasi semua parameter yang CV: product_categories, phase_threshold_min, novelty_lookback_days, weight_serendipity_hybrid, weight_serendipity_dsa. (2) Buat YAML config template dengan section terpisah untuk setiap parameter. (3) Modifikasi startup code untuk load semua param dari YAML, bukan hardcode. (4) Tambah validation function: jika param di-code dan config berbeda, raise error & log warning. (5) Document per config item: apa artinya, range valid, alasan tetap? (fixed untuk fairness, controlled untuk sensitivity analysis). (6) Version control config files bersama code → reproducibility terjamin.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama pada DSA, rencanakan ablation study.

<<<<<<< HEAD
| Kondisi | Real-time Behavior Detection | Dynamic Weight Adjustment | Phase-Aware Adaptation | Hasil yang Diharapkan |
=======
> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
>>>>>>> upstream/main
|---------|-----------|-----------|-----------|----------------------|
| Full DSA | Aktif (Click log + time) | Aktif (Adjust serendipity weight) | Aktif (Buying vs Browsing) | Unexpectedness maksimal, F1 <= baseline - 2% |
| - A | Nonaktif (Fixed user profile) | Aktif | Aktif | Unexpectedness menurun ~15% |
| - B | Aktif | Nonaktif (Static weight 0.3) | Aktif | Unexpectedness menurun ~20% |
| - C | Aktif | Aktif | Nonaktif (Uniform weight) | Unexpectedness naik tapi F1 turun >5% |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen B (Dynamic Weight Adjustment)

**Mengapa?**
> Komponen B adalah "inti" DSA — real-time adjustment sesuai behavior signal. Tanpa ini, sistem hanya reactive (tahu user lagi browsing) tapi tidak bisa adaptively ubah output. Komponen A (detection) & C (phase-aware) penting tapi lebih sebagai input/context; tanpa B, konteks itu tidak dimanfaatkan untuk keputusan rekomendasi. Prediksi: menghilangkan B akan menurunkan Unexpectedness 20-25%, sementara menghilangkan A hanya 10-15%, dan C hanya 5-8%.
>
> Expected Unexpectedness Contribution:
> - Full DSA: 0.45 (target)
> - Without A: 0.30 (↓33%)
> - Without B: 0.25 (↓44%)
> - Without C: 0.40 (↓11%)
> Ranking: B (44%) > A (33%) > C (11%)

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**

**Risiko Sistem Monolitik:**

1. **Confounding Variables** — Fitur lengkap berarti banyak komponen saling-interaksi. Ketika eksperimen mengubah satu variabel, banyak hal lain ikut berubah. Tidak bisa isolate IV dari noise.
   - Contoh: Jika Hybrid Recommendation sudah hardcoded dengan ranking, filtering, caching kompleks, lalu DSA diganti algoritma inti, perubahan F1 bisa karena DSA algorithm OR karena cache behavior berubah. Tidak bisa dibedakan.

2. **Variable Isolation Impossible** — Untuk ablation study atau sensitivity analysis, harus bisa toggle komponen satu per satu. Pada sistem monolitik, setiap toggle requires code change di banyak tempat, risiko bug tinggi.
   - Contoh: Mau test apakah phase-aware adaptation diperlukan? Pada sistem monolitik, harus find-replace phase detection di 5+ file, test, kemudian revert. Rawan error.

3. **Reproducibility Problem** — Sistem product-focused sering optimize untuk performa/UX, bukan untuk eksperimen. Hardcoded parameter, implicit dependencies, magic numbers tersebar. Sulit direkonstruksi.
   - Contoh: Serendipity weight_hybrid mungkin di-tune manual oleh engineer ke 0.35 untuk "looks good", tidak terdokumentasi. Ketika kolaborator ingin replikasi, tidak tahu dari mana nilai itu.

4. **Measurement Overhead** — Metrik pengukuran mungkin tidak built-in. Harus extract log, post-process, hitung manual. Rentan human error, tidak reproducible.
   - Contoh: F1-Score calculation mungkin harus query 3 database berbeda, join manual, then hitung. Jika ada typo di SQL, F1 salah.

5. **Time & Cost** — Refactor monolitik ke modular memakan waktu + risiko breaking production. Telat eksperimen, telat publikasi.

---

**Mengapa Arsitektur Modular Penting untuk Riset:**

1. **Variable Isolation by Design** — Setiap IV punya komponen dedikasi. Swap komponen = ubah IV saja. CV & DV unaffected.

2. **Ablation Study Straightforward** — Toggle fitur via config flag bukan code change. Menjalankan Full, –A, –B, –C hanya perlu ubah config YAML, bukan rebuild.

3. **Measurement Built-in** — DV (metrics) computed otomatis setiap session. Tidak perlu manual processing post-eksperimen.

4. **Reproducibility Maksimal** — Config files ter-version-control, code stable, no hardcoding. Kolaborator bisa replikasi dengan: (1) git clone, (2) swap config, (3) run.

5. **Agile Experimentation** — Kalau hypothesis di-revise, hanya update config, tidak rebuild. Cepat iterate, fast learning.

**Kesimpulan:** Arsitektur modular adalah investasi di depan yang menghemat waktu + meningkatkan confidence dalam hasil riset. Sistem riset ≠ sistem produksi — harus optimize untuk evidence, bukan untuk user experience.
