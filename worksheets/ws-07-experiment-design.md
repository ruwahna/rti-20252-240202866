# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

### EXPERIMENT DESIGN

**Research Question:** Apakah terdapat perbedaan signifikan pada SUS dan UEQ antara SIGNAL dan New Sakpole pada tiga fase user journey?

**Hypothesis:** 
- H₀: Tidak ada perbedaan signifikan SUS/UEQ antara kedua platform
- H₁: Ada perbedaan signifikan pada SUS dan/atau UEQ

**Tipe Eksperimen:** [✓] Comparison  [ ] Ablation  [ ] Parameter

---

### Kondisi Eksperimen

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Kondisi 1 | Usability testing SIGNAL | Platform = SIGNAL | Device: Samsung A12, Android 11; Task: 3 fase (Registrasi→Verifikasi→Pembayaran); Questionnaire: SUS + UEQ post-task |
| Kondisi 2 | Usability testing New Sakpole | Platform = New Sakpole | Device: Samsung A12, Android 11; Task: 3 fase identik; Questionnaire: SUS + UEQ post-task |

---

### Fairness Checklist

| Item | Status | Keterangan |
|------|--------|-----------|
| Task instruksi identik | [✓] Ya | Protokol task sama: "Daftar akun", "Verifikasi NIK", "Bayar pajak" — hanya app yang berbeda |
| Questionnaire identik | [✓] Ya | SUS (10 item) dan UEQ (26 item) form sama untuk kedua platform |
| Device & Environment | [✓] Ya | Samsung A12, Android 11, quiet room, controlled setting untuk semua responden |
| Task difficulty comparable | [✓] Ya | Registrasi, verifikasi, pembayaran ada di kedua platform dengan flow serupa |
| Maturity apps | [⚠] Partial | SIGNAL mature (nasional), New Sakpole regional — accepted as confounding variable, documented |

---

### Threat Analysis

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| **Internal** | Selection bias: responden prefer SIGNAL (terkenal) tanpa alasan teknis | Counterbalance: 50% SIGNAL-first, 50% Sakpole-first; random assignment |
| **Internal** | Maturation/learning: responden mahir fase 1, fase 3 terasa mudah | Reset antar phase (logout full, 15 min break); instruksi eksplisit: "setiap fase independent" |
| **Internal** | Instrument fatigue: responden kelelahan isi 36 item (2 platform × 3 fase) | Adaptif: SUS per-fase, UEQ only after all 3 phases; skip UEQ if respondent tired |
| **External** | Generalizability geografis: responden urban (kantor pajak), tidak rural | Stratified sampling: include low/medium/high digital literacy; sensitivity analysis per strata |
| **External** | Temporal validity: aplikasi akan update, hasil tidak eternal | Document version & date; recommend repeat study dalam 6 bulan |
| **Construct** | SUS item "sering gunakan sistem" — aplikasi pajak mandatory, bukan optional | Interpret: skor tinggi = minimal friction, bukan user love it |
| **Construct** | UEQ Novelty ceiling effect: kedua app baru bagi responden | Interpret relative (SIGNAL vs Sakpole), bukan absolute; jangan klaim "truly novel" |
| **Conclusion** | Sample N=45 under-powered jika effect size < 0.5 | Power analysis sebelum; target d=0.5, β=0.20 (power 0.80); report actual power |
| **Conclusion** | Multiple comparisons: 9 metrik × 3 fase = 27+ comparisons → false positive | Primary metrics: SUS + task time; sisanya exploratory; apply Bonferroni jika strict |

---

### Statistical Plan

| Elemen | Spesifikasi |
|--------|-----------|
| **Uji statistik** | Independent t-test per metrik per fase (SUS, UEQ per dimensi, task time, success rate) |
| **Justifikasi** | Perbandingan mean dua kelompok independen (SIGNAL vs Sakpole); between-subjects design |
| **Significance level (α)** | 0.05 (two-tailed) |
| **Effect size minimal** | d ≥ 0.5 (medium effect) — praktik signifikan untuk SUS diff ≥10 poin |
| **Sample size** | N ≥ 45 per platform per fase (G*Power: α=0.05, β=0.20, d=0.5) |
| **Confidence Interval** | 95% CI untuk semua effect size estimates |

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis?

**Tipe eksperimen:** [✓] Comparison / [ ] Ablation / [ ] Parameter (Comparison karena membandingkan dua platform existing tanpa modifikasi)

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Kondisi A | Usability testing di SIGNAL | SIGNAL v.X | Device: Samsung A12, OS Android 11, Task: Registrasi→Verifikasi→Pembayaran (instruksi identik), Questionnaire: SUS + UEQ post-task |
| Kondisi B | Usability testing di New Sakpole | New Sakpole v.Y | Device: Samsung A12, OS Android 11, Task: Registrasi→Verifikasi→Pembayaran (instruksi identik), Questionnaire: SUS + UEQ post-task |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Task instruksi identik | ✅ Ya | Protokol task sama: "Daftar akun", "Verifikasi NIK", "Bayar pajak" — hanya app yang berubah |
| Questionnaire identik | ✅ Ya | SUS dan UEQ form sama untuk kedua platform |
| Device dan environment identik | ✅ Ya | Samsung A12, Android 11, quiet room, controlled setting semua responden |
| Maturity/version apps | ⚠️ Partial | SIGNAL mature (nasional), New Sakpole regional — jadi faktor ini diakui sebagai limitation, bukan disiapkan setara |
| Peserta effort comparable | ✅ Ya | Semua responden melakukan 3 fase yang sama complexity untuk kedua platform |

**Ada yang tidak fair?** [✓] Ya / [ ] Tidak
> Jika ya, bagaimana cara memperbaikinya? **Maturity platform berbeda tidak bisa disamakan (by design kedua aplikasi punya development resources berbeda). Namun bisa mitigation dengan acknowledge ini sebagai confounding variable, dan stratifikasi analisis per user segment: apakah user yg terbiasa SIGNAL berat vs lite? Jika hasil berbeda drastis per segment, ada clue bahwa maturity (familiarity) mungkin berperan.**

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Selection bias: responden prefer platform terkenal (SIGNAL) tanpa sebab teknis — pola favorit bukan usability difference | Counterbalance order: half SIGNAL-first, half Sakpole-first; randomize. Menggunakan explicit debriefing question: "which app was easier?" untuk capture bias |
| Internal | Maturation/learning effect: responden master Registrasi phase di platform pertama, jadi Pembayaran phase terasa mudah | Reset antar phase (logout full, 15 min break); protokol instruction explicit: "setiap fase dihitung terpisah, jangan gunakan pengalaman fase sebelum" |
| Internal | Instrument/fatigue bias: responden kelelahan mengisi 36 item SUS+UEQ setelah 6 kondisi (2 platform × 3 fase) | Adaptif: SUS saja per fase (10 item), UEQ hanya setelah semua fase selesai (26 item); jika responden tired, skip UEQ tapi tetap include SUS di analisis |
| External | Generalizability geografis: responden dari Jawa Tengah, berlaku universal? | Dokumentasi: "sample dari kantor pajak Jakarta" → terbatas urban, digital-ready. Acknowledge limitation; jangan klaim generalisasi nasional tanpa data. Saran: repeat studi di region lain (rural, East Indonesia) |
| External | Generalizability waktu: aplikasi akan update, desain berubah, validitas temporal limited | Snapshot version di dokumentasi; catat tanggal eksperimen; recommend future work: "repeat pada versi terbaru 6 bulan lagi" |
| Construct | SUS item "Saya ingin sering menggunakan sistem ini" — apakah relevan untuk aplikasi pajak yang mandatory, bukan optional? | Adjust interpretation: skor SUS tinggi bukan "user love it" tapi "minimal friction untuk mandatory task". Alternatif: tambah item "Akan saya gunakan lagi jika perlu bayar pajak" yang lebih realistic |
| Construct | UEQ "Novelty" dimension ceiling effect | Pre-note: kedua app baru bagi mayoritas responden → expect high novelty score. Interpret novelty score relative, bukan absolute (yang penting compare SIGNAL vs Sakpole novelty score, bukan nilai absolutnya) |
| Conclusion | Sample size N=45 per platform mungkin under-powered jika effect size kecil (d<0.5) | Conduct G*Power sebelum eksperimen dengan target effect size d=0.5 (medium, practically significant untuk SUS score diff ≥10). Power = 1-β = 0.80 minimum. Report actual power achieved di hasil |
| Conclusion | Multiple comparisons: 6 metrik (SUS, UEQ 6 dimensi, task time, success) × 3 fase = 18+ comparisons. Jika tidak correct, false positive rate tinggi | Apply Bonferroni correction (α = 0.05 / jumlah test) atau predefine 1-2 primary metrics (SUS + task time), sisanya exploratory dan report with caution |

**Ancaman mana yang paling sulit dimitigasi?** Selection bias + Maturity platform differences
**Mengapa?**
> Responden sudah tahu SIGNAL nasional (sudah dengar, teman pakai) vs New Sakpole belum luas (baru). Jadi bias favorit/preference sudah tertanam sebelum eksperimen. Sulit eliminate sepenuhnya — hanya bisa minimize dengan counterbalance order dan debriefing. Platform maturity (SIGNAL sudah 10 iterasi, New Sakpole baru 2) adalah inherent difference, bukan bias eksperimen. Ini justru temuan valid jika hasilnya SIGNAL lebih baik (karena maturity) — sesuai kenyataan real-world.

---

## Refleksi

> Dalam studi komparatif SIGNAL vs New Sakpole, jika hasilnya menunjukkan "SIGNAL skor SUS 50, New Sakpole skor 65 — perbedaan 15 poin, signifikan," tapi seseorang bertanya: "Apakah perbedaan ini karena desain app atau karena responden lebih terbiasa Sakpole?" Apa 3 cara untuk mengevaluasi ancaman validity ini?

**Jawaban:**

1. **Cek order effect via counterbalancing:** Jika 50% responden mulai SIGNAL dulu dan 50% Sakpole dulu, bandingkan hasil per group. Jika perbedaan SUS persist across kedua order (SIGNAL-first dan Sakpole-first), maka order bukan confounding. Jika hasil drastis berbeda, ada evidence learning effect — perlu stratifikasi analisis.

2. **Breakdown per user familiarity baseline:** Tanya responden pre-eksperimen: "Apakah anda sudah pernah coba SIGNAL atau Sakpole?" Jika hasil comparison consistent across "familiar" vs "naive" subgroups, maka familiarity bukan bias. Jika hasil berbeda drastis per subgroup, ada clue bahwa familiarity (prior experience) berperan → dokumentasi dengan stratifikasi.

3. **Triangulate subjective vs objective metrics:** Cek consistency antara subjective (SUS score) dan objective (task time, success rate). Jika New Sakpole skor SUS tinggi TAPI task time lebih lama dari SIGNAL (kontradiksi), ada indikasi bias — responden merasa mudah (karena familiar) padahal objectively lebih lambat. Consistency validates result validity; inconsistency adalah red flag.
