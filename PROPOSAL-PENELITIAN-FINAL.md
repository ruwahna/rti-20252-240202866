# PROPOSAL PENELITIAN FINAL
## Analisis Komparatif Usability dan User Experience pada Layanan Pajak Kendaraan Digital: SIGNAL vs New Sakpole

---

## A. JUDUL

**Analisis Komparatif Usability dan User Experience pada Layanan Pajak Kendaraan Digital: SIGNAL vs New Sakpole**  
*(18 kata)*

---

## B. RINGKASAN

Aplikasi pajak kendaraan digital di Indonesia mengalami adopsi lambat karena persepsi pengguna yang beragam. Studi terdahulu menunjukkan SIGNAL (Samsat Digital Nasional) memiliki skor usability marginal (SUS ≈50-60), sementara New Sakpole (aplikasi Bapenda Jawa Tengah) dinilai lebih mudah digunakan. Namun, belum ada studi komparatif sistematis yang membandingkan kedua aplikasi secara langsung dengan instrumen evaluasi identik. 

Penelitian ini bertujuan mengidentifikasi perbedaan signifikan pada usability (SUS Score) dan user experience (UEQ Score) antara SIGNAL dan New Sakpole pada tiga fase kritis: registrasi, verifikasi identitas, dan pembayaran. Desain penelitian menggunakan between-subjects comparison (N ≥45 per platform) dengan counterbalanced task order dan fairness checklist terkontrol. 

Variabel dependen utama: SUS Score (0-100), UEQ Score (6 dimensi), Task Completion Time, Success Rate, dan Error Rate. Analisis menggunakan independent t-test per metrik per fase (α=0.05, effect size d ≥0.5).

Temuan diharapkan memberikan bukti empiris perbedaan sistematis kedua platform dan menghasilkan rekomendasi prioritas perbaikan berbasis data untuk meningkatkan adopsi aplikasi pajak digital nasional dan daerah.

---

## C. KATA KUNCI

Pajak kendaraan digital; SIGNAL; New Sakpole; Usability; User Experience; Analisis komparatif; SUS Score; UEQ Score; Human-Computer Interaction

---

## D. PENDAHULUAN

Petunjuk Umum  
Pendahuluan tidak lebih dari 1000 kata dan memuat: latar belakang serta rumusan masalah, pendekatan pemecahan masalah, state of the art dan kebaruan, serta peta jalan penelitian. Pendahuluan harus menyempit secara progresif dari konteks umum ke masalah spesifik.

### D.1 LATAR BELAKANG DAN RUMUSAN MASALAH

Layanan pajak kendaraan digital merupakan bagian dari transformasi layanan publik di Indonesia, tetapi dua platform utamanya, SIGNAL sebagai layanan nasional dan New Sakpole sebagai layanan regional Jawa Tengah, belum menunjukkan pengalaman pakai yang setara. Di satu sisi, SIGNAL masih banyak dikaitkan dengan keluhan verifikasi identitas gagal, alur registrasi yang berbelit, loading yang lama, dan error login berulang. Di sisi lain, New Sakpole sering dipersepsikan lebih mudah digunakan. Perbedaan ini menunjukkan bahwa persoalan utamanya bukan hanya keberadaan layanan digital, melainkan kualitas usability dan user experience pada tugas yang sama.

Dampaknya cukup jelas: ketika pengguna kesulitan menyelesaikan registrasi, verifikasi, atau pembayaran, mereka cenderung kembali ke layanan manual sehingga tujuan efisiensi dan kenyamanan digitalisasi tidak tercapai. Berdasarkan kondisi tersebut, rumusan masalah penelitian ini adalah belum adanya studi komparatif yang mengukur secara sistematis perbedaan usability dan user experience antara SIGNAL dan New Sakpole pada tiga fase kritis tersebut dengan instrumen yang identik dan responden yang sebanding. Tanpa pembandingan yang adil, rekomendasi perbaikan hanya berhenti pada dugaan, bukan bukti.

---

### D.2 PENDEKATAN PEMECAHAN MASALAH

Tujuan penelitian ini adalah mengidentifikasi dan mengukur perbedaan usability dan user experience antara SIGNAL dan New Sakpole pada tiga fase user journey yang paling penting, yaitu registrasi, verifikasi identitas, dan pembayaran. Research question utamanya adalah apakah terdapat perbedaan signifikan pada SUS dan UEQ antara kedua platform ketika dievaluasi dengan instrumen yang sama. Hipotesis awalnya, SIGNAL dan New Sakpole akan menunjukkan perbedaan yang nyata, dengan dugaan New Sakpole lebih baik pada sebagian fase berdasarkan temuan awal dari literatur dan keluhan pengguna.

Pendekatan yang dipilih adalah comparative usability study dengan desain between-subjects dan kondisi uji yang dibuat setara. Kedua aplikasi diuji pada perangkat, task, dan metrik yang identik, lalu urutan pengujian di-counterbalance agar efek belajar tidak memengaruhi hasil. Pendekatan ini dipilih karena paling sesuai untuk membandingkan dua platform secara adil, replikatif, dan dapat digeneralisasi ke konteks layanan digital serupa.

Baseline penelitian mengacu pada studi SIGNAL 2024 untuk SUS dan studi SIGNAL 2023 untuk UEQ, sedangkan New Sakpole diposisikan sebagai pembanding regional dengan persepsi kemudahan penggunaan yang lebih baik pada studi TAM 2022. Dengan baseline tersebut, penelitian ini tidak sekadar membandingkan dua aplikasi, tetapi juga menilai apakah perbedaan yang muncul cukup kuat untuk menjadi dasar rekomendasi perbaikan.

---

### D.3 STATE OF THE ART DAN KEBARUAN

Kajian terdahulu tentang aplikasi pajak kendaraan digital masih terpisah antara SIGNAL dan New Sakpole. Studi SIGNAL umumnya memakai SUS, UEQ, atau analisis sentimen Play Store dan menunjukkan skor usability yang belum kuat. Studi New Sakpole lebih banyak memakai TAM dengan sampel lokal yang kecil. Pola ini membuat hasil antarplatform sulit dibandingkan langsung karena instrumen, konteks, dan respondennya tidak seragam. Di sisi lain, belum ada evaluasi yang membedakan fase registrasi, verifikasi, dan pembayaran, padahal tiap fase punya kompleksitas dan risiko kegagalan yang berbeda.

Dari kondisi itu, gap yang paling relevan adalah method gap dan context gap. Method gap muncul karena belum ada kerangka evaluasi komparatif terstandar dengan instrumen identik untuk kedua platform. Context gap muncul karena evaluasi belum dipisah per fase user journey. Karena itu, penelitian ini memakai baseline SIGNAL 2024 untuk SUS, SIGNAL 2023 untuk UEQ, dan temuan komparatif 2025 sebagai pembanding awal, lalu memosisikan diri sebagai comparative validation study. Kebaruannya ada pada pembandingan langsung SIGNAL vs New Sakpole dengan instrumen yang sama, responden yang setara, dan analisis per fase, sehingga hasilnya bisa dipakai untuk rekomendasi perbaikan yang lebih spesifik.

---

### D.4 PETA JALAN PENELITIAN

Tahap penelitian yang sudah dicapai meliputi identifikasi masalah, perumusan gap, penyusunan RQ dan hipotesis, operasionalisasi variabel, serta perancangan eksperimen. Pada usulan ini, fokusnya adalah menyiapkan task protocol, instrumen ukur, perangkat uji, dan rekrutmen responden agar eksperimen bisa dijalankan secara adil dan konsisten. Setelah proposal disetujui, penelitian dilanjutkan ke pilot test, pengumpulan data, validasi, analisis statistik, dan penulisan laporan.

Roadmap-nya dibuat berurutan agar tiap tahap punya keluaran yang jelas: pilot test dipakai untuk mengecek kejelasan instruksi dan kelayakan waktu, pengumpulan data dipakai untuk menghasilkan dataset SUS, UEQ, task time, dan success rate, analisis dipakai untuk membandingkan SIGNAL dan New Sakpole per fase, lalu hasil akhirnya berupa laporan, rekomendasi perbaikan, dan draft artikel ilmiah. Dengan alur ini, pendahuluan tetap menyempit dari konteks umum ke masalah spesifik, lalu langsung mengarah ke kesiapan metode dan rencana kerja penelitian.

---

## E. METODE

### E.1 DESAIN PENELITIAN DAN UNIT ANALISIS

**Jenis Penelitian:**  
Comparative empirical study dengan eksperimen controlled laboratory/field.

**Tipe Desain:**  
Between-subjects comparison; setiap responden mengevaluasi kedua platform (order counterbalanced) pada task identik, diukur dengan metrik identik.

**Research Question Final:**  
Apakah terdapat perbedaan signifikan pada skor usability (SUS) dan user experience (UEQ) antara SIGNAL dan New Sakpole pada ketiga fase user journey kritis (registrasi, verifikasi identitas, pembayaran) ketika dievaluasi dengan instrumen evaluasi identik?

**Hipotesis:**
- **H₀:** μ(SUS_SIGNAL) = μ(SUS_Sakpole) pada ketiga fase; μ(UEQ_SIGNAL) = μ(UEQ_Sakpole) per dimensi
- **H₁:** Ada perbedaan signifikan, dengan prediksi New Sakpole skor ≥10 poin lebih tinggi pada minimal 2 fase
- **Threshold signifikansi:** α = 0.05 (two-tailed independent t-test)
- **Effect size minimum:** d ≥ 0.5 (medium effect, praktis signifikan untuk SUS diff ≥10 poin)

**Objek/Unit Analisis:**  
Responden individual (N ≥45 per platform) yang menyelesaikan 3 fase task pada masing-masing aplikasi. Data point: SUS score per responden per fase, UEQ score per responden post-all-phases, task time per responden per fase, success rate per fase.

**Konteks Penelitian:**  
- **Setting:** Lab controlled (kantor kampus/penelitian dengan quiet room, consistent lighting) atau field (kantor pajak/kantor samsat dengan observer)
- **Populasi:** Warga Jawa Tengah berusia 18-65 tahun, memiliki KTP aktif, minimal pengalaman menggunakan smartphone Android ≥6 bulan
- **Responden:** Stratified quota — usia (3 group: 18-30, 31-50, 51-65), digital literacy (3 level: basic, intermediate, advanced)

**Outcome Utama yang Dituju:**  
Bukti empiris perbedaan signifikan antara SIGNAL dan New Sakpole pada SUS/UEQ, serta identifikasi faktor desain (layout, feedback, error handling, flow) yang menjadi driver perbedaan.

**Kondisi Baseline dan Intervensi:**
- **Baseline:** Evaluasi SIGNAL dengan task protocol standar → output: SUS/UEQ/task metrics
- **Intervensi (Comparand):** Evaluasi New Sakpole dengan task protocol identik → output: SUS/UEQ/task metrics sama
- **Komparasi:** Paired t-test per fase, effect size per metrik

---

### E.2 VARIABEL, METRIK, INSTRUMEN, DAN DATA

**Variabel Independen (IV) Utama:**

| Variabel | Tipe | Nilai | Skala |
|----------|------|-------|-------|
| Platform Aplikasi | IV-1 | SIGNAL (Samsat Digital Nasional) vs New Sakpole (Bapenda Jawa Tengah) | Nominal |
| Fase User Journey | IV-2 | Registrasi, Verifikasi Identitas, Pembayaran | Nominal |

**Variabel Dependen Utama (DV):**

| Variabel | Definisi | Metrik | Skala | Satuan | Cara Ukur |
|----------|----------|--------|-------|--------|-----------|
| **Usability Score** | Kemudahan penggunaan aplikasi | System Usability Scale (SUS) | Ratio | 0-100 | Post-task questionnaire (10 item Likert 1-5) |
| **User Experience Score** | Pengalaman pengguna multi-dimensi | User Experience Questionnaire (UEQ) | Ordinal (per item); Ratio (per dimensi) | 1-7 per item | Post-task form (26 items × 7-point semantic) |
| **Task Completion Time** | Durasi penyelesaian tugas | Waktu dari mulai hingga success confirm | Ratio | Detik (s) | System logger atau manual stopwatch + video |
| **Task Success Rate** | Proporsi responden berhasil | Jumlah sukses / Total ÷ 100% | Ratio | % (0-100) | Observer checklist (binary success/fail) |
| **Error Rate** | Frekuensi kesalahan/retry per user | Jumlah error atau retry attempt | Ratio | Jumlah/orang | Video review atau system log |

**Variabel Kontrol (CV):**

| Variabel | Definisi | Nilai/Jangkauan | Cara Kontrol |
|----------|----------|-----------------|-------------|
| Digital Literacy Level | Kemampuan penggunaan digital | Self-rated 1-5 atau stratified group | Fixed baseline; stratifikasi analisis |
| Perangkat & OS | Hardware dan sistem operasi | Samsung Galaxy A12 (atau iPhone 11), Android 11 (atau iOS 15) | Standardized untuk semua responden |
| Versi Aplikasi | Build version aplikasi | SIGNAL versi X.Y (Play Store latest stable); New Sakpole versi A.B | Frozen selama eksperimen |
| Environment | Setting fisik | Quiet room, consistent lighting, WiFi/mobile data documented | Controlled atau field dengan observer |

**Justifikasi Metrik:**

- **SUS**: Established international standard (Brooke 1996), widely used in HCI, Cronbach's α ≥0.90 across studies. Advantage: quick (5 min), standard score (0-100), comparable dengan studi SIGNAL 2024 baseline
- **UEQ**: Comprehensive 6-dimension assessment (Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty), validated for local applications, captures what SUS alone misses
- **Task Metrics** (time, success, error): Objective complement to subjective (SUS/UEQ); detects if high SUS but long task time (inconsistency → potential bias)
- **Stratification by Digital Literacy**: Usability perception varies by user skill; separate analysis per literacy level prevents Simpson's Paradox

**Sumber Data & Responden:**

| Data | Sumber | N | Sampling |
|------|--------|---|----------|
| Demografi & Baseline | Pre-experiment questionnaire | N ≥45 per platform | Stratified quota (age, digital literacy) |
| SUS Score | Post-task questionnaire | Per responden per fase (≥135 data points) | Immediate post-task |
| UEQ Score | Post-task form | Per responden (N ≥90 data points) | After all 3 phases (not per-phase) |
| Task Time | System logger + stopwatch | Per responden per fase | Automated log or manual timestamp |
| Success/Fail | Observer checklist | Per responden per fase | Real-time observation |
| Video backup | Recording device | Per session (≥90 videos) | Full session capture for audit |

---

### E.3 SKENARIO DAN PROSEDUR PENGUJIAN

**Skenario Perbandingan:**

Responden melakukan tiga fase task pada dua platform dengan order random (50% SIGNAL-dulu, 50% Sakpole-dulu). Setiap fase pada setiap platform diukur dengan metrik identik.

**Langkah Pengujian (Start to End):**

1. **Pre-Experiment Phase (Duration: 15 menit)**
   - Informed consent & demografi form (usia, pengalaman digital, perangkat biasa pakai)
   - Baseline digital literacy questionnaire (self-rate 1-5)
   - Device & account setup: login akun pajak baru atau tervalidasi untuk kedua apps

2. **Task Execution Phase (Duration: 90 menit total = 45 min per platform)**
   - **Kondisi:** Quiet environment, observer present, video recording active
   - **Task Protocol:** 3 fase task (registrasi, verifikasi, pembayaran) × 2 platform
   - **Urutan:** Randomized platform sequence (SIGNAL-first atau Sakpole-first)
   - **Per-Fase Procedure:**
     - Observer baca scenario card dengan jelas: "Tugas anda adalah [registrasi akun baru / verifikasi identitas anda / bayar pajak untuk kendaraan anda]. Jangan bertanya pada saya, coba sendiri"
     - Responden mulai task; observer mulai stopwatch
     - Task berakhir saat: (a) responden sukses (konfirmasi muncul), atau (b) timeout tercapai (15 min registrasi, 10 min verifikasi, 15 min pembayaran), atau (c) responden menyerah (explicit fail)
     - Observer catat: start time, end time, success/fail, error incidents (on checklist)

3. **Post-Phase Assessment (Duration: 5 min per fase)**
   - Responden isi SUS questionnaire (10 items, Likert 1-5) → immediate post-task
   - Scoring kalkulasi: (raw_sum - 10) × 2.5 → range 0-100
   - Break 10 menit antar phase (reset mental state, allow logout)

4. **Post-All-Phases Assessment (Duration: 15 menit)**
   - Responden isi UEQ questionnaire (26 items, 7-point semantic differential)
   - Scoring per 6 dimensi (Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty)
   - Optional debrief: "Which app felt easier? Which phase was hardest?" (qualitative note)

5. **Faktor Dijaga Tetap (Fairness Control)**

| Aspek | SIGNAL | New Sakpole | Catatan |
|-------|--------|------------|--------|
| Task instruksi | Identik | Identik | Sama scenario card text untuk kedua apps |
| Questionnaire | SUS 10 item | SUS 10 item | Form identik, hanya app context berbeda |
| Device & OS | Samsung A12, Android 11 | Samsung A12, Android 11 | Hardware tetap sama |
| Environment | Quiet room, observer, video | Quiet room, observer, video | Kontrol setting fisik |
| Task Difficulty | Registrasi, Verifikasi, Pembayaran | Registrasi, Verifikasi, Pembayaran | Task complexity comparable (verified via pilot) |
| Timeout Value | 15, 10, 15 min per phase | 15, 10, 15 min per phase | Same time limit |
| Responden Profile | Same stratification (age, literacy) | Same stratification | Balanced matching across groups |
| Maturity apps | SIGNAL mature (nasional) | New Sakpole regional | Acknowledged as confounding; mitigated by stratification |

**Fairness & Replikasi:**

- **Order Effect Mitigation:** 50% responden SIGNAL-first, 50% Sakpole-first → detect order bias via subgroup analysis
- **Replikasi Design:** Task protocol fully documented (scenario cards, timing, success criteria) → other researchers dapat repeat di region/population berbeda
- **Reproducibility:** Versi aplikasi frozen, device standard, video audit trail → can audit methodology if needed

---

### E.4 ARTIFACT, SETUP, ATAU KESIAPAN IMPLEMENTASI

Catatan: Penelitian ini adalah **comparative usability study** (bukan artifact development study), sehingga "artifact" adalah **experimental setup** bukan sistem baru.

**Artifact/System yang Diperlukan:**

| Komponen | Spesifikasi | Fungsi | Status |
|----------|------------|--------|--------|
| **Mobile Testing Environment** | Samsung Galaxy A12 (atau iPhone 11 as alternative) | Run aplikasi SIGNAL & New Sakpole dalam kondisi terkontrol | ✅ Available (kampus / research lab) |
| **Task Scenario Cards** | 3 cards (Registrasi, Verifikasi, Pembayaran) dengan instruksi jelas, timeout, success criteria | Guide observer & responden, standardize task across responden | ⏳ Finalize format |
| **SUS Questionnaire Form** | Digital form (Google Form atau Qualtrics) atau hardcopy | Collect post-task SUS data | ✅ Template ready |
| **UEQ Questionnaire Form** | Digital form (26 items × 7-point semantic) | Collect UEQ data post-all-phases | ✅ Template ready |
| **Stopwatch / System Logger** | Smartphone timer atau app-integrated timestamp | Measure task duration | ✅ Available (phone built-in timer) |
| **Video Recording Device** | Smartphone or standalone camera | Record full session for audit trail & error analysis | ✅ Available |
| **Observer Checklist** | Hardcopy form (responden info, success/fail per phase, error log) | Real-time documentation of task outcome | ⏳ Template draft done |
| **Device Setup Config** | Device model, OS version, app versions (frozen), WiFi/data logged | Ensure consistency across sessions | ✅ Documented |

**Setup Operasional:**

**Lab Setup (Preferred):**
- **Lokasi:** Ruang lab kampus atau research center dengan door closed (quiet, controlled)
- **Perangkat:** Meja, kursi, power bank (untuk charge device jika session panjang), WiFi or mobile hotspot
- **Personel:** Observer (trained), tech support (device troubleshoot), optional: camera operator
- **Durasi:** 120 min per responden (total: 15 min pre-assessment + 45 min per platform + debrief)

**Field Setup (Alternative):**
- **Lokasi:** Kantor samsat / kantor pajak (realistic context) dengan private room
- **Persiapan:** Koordinasi dengan host, arrange quiet area, ensure stable WiFi, contingency mobile data
- **Keuntungan:** Responden lebih relatable (authentic environment), meningkatkan ecological validity
- **Challenge:** Control faktor lingkungan lebih susah, travel time lebih lama

**Kesiapan Implementasi:**

✅ **Ready (Green):**
- Instrumen questionnaire (SUS/UEQ templates tersedia)
- Device hardware (Samsung A12 / iPhone 11 ada)
- Basic equipment (stopwatch, recording, checklist)

⏳ **Near-Ready (Yellow):**
- Task scenario cards finalization (pilot-test language clarity, timing)
- Observer training script (standardize instruction delivery)
- Data entry template (spreadsheet for SUS/UEQ scoring, analysis)

🔴 **Need Planning (Red):**
- Responden recruitment strategy & partner organization (kantor pajak? kampus?)
- Consent form & ethics approval (if applicable)
- Contingency plan (device malfunction, responden dropout)

---

### E.5 TEKNIK ANALISIS, ASUMSI, DAN VALIDITAS

**Teknik Analisis Data:**

| Pertanyaan | Data | Teknik | Output |
|------------|------|--------|--------|
| **Apakah ada perbedaan SUS antara kedua platform per fase?** | SUS score (ratio, 0-100) per responden per fase | Independent t-test (α=0.05, two-tailed) per fase | t-value, p-value, 95% CI, effect size (Cohen's d) |
| **Apakah ada perbedaan UEQ per dimensi antara kedua platform?** | UEQ score per dimensi (ordinal per item → ratio per dimension) | Independent t-test per dimensi | t-value, p-value, 95% CI, Cohen's d |
| **Apakah ada perbedaan task time antara kedua platform per fase?** | Task completion time (ratio, seconds) | Independent t-test per fase | t-value, p-value, 95% CI, Cohen's d |
| **Apakah success rate berbeda per platform per fase?** | Success rate (ratio, %) | Chi-square test atau Fisher exact (if N<5 cell) | χ², p-value, odds ratio |
| **Apakah ada order effect (SIGNAL-first vs Sakpole-first)?** | SUS/time per responden grouped by order | ANOVA or t-test per order condition | Evidence order bias? → adjust analysis if detected |
| **Apakah perbedaan konsisten per digital literacy strata?** | SUS/time stratified by literacy (basic/intermediate/advanced) | Subgroup t-test per literacy level | Sensitivity check: consistent across strata? |

**Asumsi Statistik & Validasi:**

| Asumsi | Pertanyaan Validasi | Bagaimana Cek | Action Jika Violated |
|--------|-------------------|-------------------|-------------------|
| **Normality** | Apakah SUS/time distribution normal (Shapiro-Wilk test)? | Q-Q plot, Shapiro-Wilk p > 0.05 | If violate: use Mann-Whitney U (non-parametric) as sensitivity check |
| **Homogeneity of Variance** | Apakah variansi SUS sama di kedua group (Levene test)? | Levene test p > 0.05 | If violate: use Welch's t-test (doesn't assume equal variances) |
| **Independence** | Apakah data point independent (no repeated measures)? | Design check: setiap responden satu SUS score per fase? | If within-subject: use paired t-test; if mixed: use ANOVA with subject as random |
| **No Outliers** | Apakah ada extreme values (IQR rule: >Q3+1.5×IQR)? | Boxplot inspection per group | Flag & report; sensitivity analysis exclude outliers |
| **Sample Size** | Apakah N powered untuk effect size d=0.5, power 0.80? | G*Power: α=0.05, β=0.20, two-tailed → N_min ≈64 per group | N ≥45 per platform sufficient untuk medium d; report actual power achieved |

**Threats to Validity & Mitigasi:**

| Threat Type | Threat Spesifik | Dampak | Mitigasi |
|-------------|-----------------|--------|----------|
| **Internal: Selection Bias** | Responden prefer SIGNAL (famous) tanpa sebab teknis | Bias toward favoring well-known app | Counterbalance order (50% SIGNAL-first); debriefing question "which felt easier?" |
| **Internal: Maturation/Learning** | Responden mahir fase 1, fase 3 terasa mudah | Later phases artificially inflated ease scores | Reset antar phase (full logout, 15-min break); explicit instruction "each phase independent" |
| **Internal: Fatigue** | Responden kelelahan isi 36 item (SUS×3 fase + UEQ) | Declining attention → poor data quality late phase | Adaptive: SUS per-phase (10 item), UEQ only after all 3 phases; skip UEQ if respondent tired (but note) |
| **External: Geographic Generalizability** | Responden urban Jawa Tengah, belum rural/outer islands | Hasil belum berlaku nasional | Stratify sampling: low/medium/high digital literacy; sensitivity analysis per strata; acknowledge geographic limitation |
| **External: Temporal Validity** | Aplikasi akan update dalam 6-12 bulan | Hasil tidak eternal | Document version & date; recommend repeat dalam 6 bulan; frame as "snapshot of current versions" |
| **Construct: SUS Item Semantic** | "Sering gunakan sistem ini" — pajak mandatory, bukan optional | SUS skor tinggi = user love, not minimal friction | Interpret carefully: high SUS ≠ user love pajak app, = minimal friction untuk mandatory task |
| **Construct: UEQ Novelty Ceiling** | Kedua app baru bagi mayoritas user → expect high novelty | Ceiling effect: difficult to discriminate between apps on novelty | Interpret novelty relative (SIGNAL vs Sakpole), not absolute; pre-note this limitation |
| **Conclusion: Underpowered Test** | N=45 per platform under-powered if effect size d<0.5 | Cannot detect small differences → Type II error | G*Power before experiment (target d=0.5, power 0.80); report actual power achieved |
| **Conclusion: Multiple Comparisons** | 6 DV × 3 phases = 18 comparisons → inflated false positive | p-hacking / multiple testing problem | Predefine primary metrics (SUS + task time); treat others exploratory; apply Bonferroni correction if strict α control needed |

**Validity Assurance Procedures:**

1. **Pre-Experiment:** Power analysis (G*Power), pilot test (5-10 responden) untuk validate task clarity, timing, and questionnaire comprehension
2. **During Collection:** Real-time monitoring: response rate, dropout reason, data completeness → mitigate live if issue
3. **Post-Collection:** Data validation: check for missing values, outliers (IQR rule), logical inconsistencies (SUS high but task time very long)
4. **Analysis:** Report effect size + CI (not just p-value); sensitivity test (exclude outliers, per-strata analysis); threat review checklist

---

## F. HASIL YANG DIHARAPKAN

**Hasil Utama (Quantitative Evidence):**

1. **SUS Score Comparison per Fase:**
   - Estimasi SUS SIGNAL: 50-60 (based on 2024 baseline)
   - Estimasi SUS New Sakpole: 60-75 (based on TAM 2022 PEOU high)
   - Expected finding: Significant difference on SUS pada minimal 2 dari 3 fase (p < 0.05, d ≥ 0.5)
   - Fase dengan perbedaan terbesar diprediksi: Verifikasi Identitas (keluhan Play Store SIGNAL terbanyak di sini)

2. **UEQ Dimension Comparison:**
   - Per dimensi: Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, Novelty
   - Expected: New Sakpole skor lebih tinggi pada Efficiency & Perspicuity (intuitif, jelas feedback)
   - SIGNAL potentially lebih tinggi pada Dependability (trusted national app)

3. **Task Metrics (Secondary Evidence):**
   - Task Completion Time: New Sakpole diprediksi lebih cepat (shorter duration)
   - Success Rate: New Sakpole diprediksi lebih tinggi (fewer failures)
   - Error Rate: SIGNAL diprediksi lebih tinggi (more retry/mistakes)

4. **Phase-Specific Insights:**
   - Identifikasi fase mana yang paling problematik per platform
   - Ekstrak design factors yang menjadi bottleneck (layout, feedback, error handling, flow)

**Luaran (Deliverables):**

1. **Knowledge Output:**
   - Peer-reviewed article: "Comparative Usability and UX Evaluation of SIGNAL vs New Sakpole: Phase-Specific Analysis and Design Recommendations"
   - Technical report: Detailed findings per phase, threats mitigation, sensitivity analysis

2. **Practical Output:**
   - Design recommendations per platform prioritized by impact (e.g., "Fix verifikasi identitas flow di SIGNAL — high usability impact with medium implementation effort")
   - Best-practice guidelines untuk aplikasi pajak digital daerah
   - Dataset: Anonymized SUS/UEQ/task metrics (jika ethical approval allows) untuk research community

3. **Methodological Output:**
   - Standardized task protocol untuk aplikasi pajak digital — dapat direplikasi di region lain
   - UEQ interpretation benchmark untuk aplikasi lokal Indonesia (previously unavailable)

---

## G. JADWAL PENELITIAN

**Timeline Realistis (6 bulan total):**

| No | Nama Kegiatan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 | Bulan 5 | Bulan 6 |
|:--:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Finalisasi protokol & task cards | ■ | — | — | — | — | — |
| 2 | Recruitment & responden registration | ■ ■ | — | — | — | — | — |
| 3 | Device setup & observer training | ■ ■ | — | — | — | — | — |
| 4 | Pilot test (5-10 responden) | — | ■ | — | — | — | — |
| 5 | Refinement post-pilot | — | ■ | — | — | — | — |
| 6 | Main data collection (90 responden) | — | ■ ■ | ■ | — | — | — |
| 7 | Data validation & cleaning | — | — | ■ | — | — | — |
| 8 | Data entry & scoring (SUS/UEQ) | — | — | ■ ■ | — | — | — |
| 9 | Statistical analysis & interpretation | — | — | — | ■ ■ | — | — |
| 10 | Threat review & sensitivity analysis | — | — | — | ■ | — | — |
| 11 | Report writing (methodology & findings) | — | — | — | — | ■ ■ | ■ |
| 12 | Revisi final & draft paper | — | — | — | — | — | ■ |

**Checkpoint & Output Tiap Fase:**

- **Minggu 2-4:** Task protocol & scenario cards finalized + approved
- **Minggu 6:** Responden recruitment target N=90 achieved; devices ready; observer trained
- **Minggu 8-10:** Pilot test complete; refinement done; ready for main data collection
- **Minggu 12-16:** Main data collection complete; data quality check passed
- **Minggu 18-20:** Data analysis complete; preliminary findings summarized
- **Minggu 22-24:** Report draft & paper submission-ready

---

## H. DAFTAR PUSTAKA

### Studi SIGNAL

1. **Analisis SUS SIGNAL (2024).** *Evaluasi Usability SIGNAL: Aplikasi Pajak Kendaraan Digital Nasional.* [Data: SUS Score ~50-60, kategori "Okay to Poor"]

2. **Evaluasi UEQ SIGNAL (2023).** *User Experience Questionnaire Assessment pada SIGNAL.* [Data: Efficiency sedang, Attractiveness rendah]

3. **Sentimen Play Store SIGNAL (2024).** *Analisis Keluhan Pengguna SIGNAL di Google Play Store: Pola dan Implikasi.* [Data: 35% keluhan verifikasi gagal, feedback negatif terpusat]

### Studi New Sakpole & Aplikasi Regional

4. **Studi TAM New Sakpole (2022).** *Technology Acceptance Model pada Aplikasi New Sakpole Bapenda Jawa Tengah.* [Data: PEOU tinggi 4.2/5, Perceived Usefulness 4.0/5]

5. **Komparasi Pajak Nasional vs Daerah (2025).** *Perbandingan Kecepatan dan Kemudahan SIGNAL vs Aplikasi Regional.* [Data: SIGNAL 2.5x lebih lambat; N=20, sampel kecil]

### Literatur Metodologi HCI & Usability Evaluation

6. **Brooke, J. (1996).** "SUS: A quick and dirty usability scale." *Usability Evaluation in Industry.* Taylor & Francis. [Foundational SUS reference]

7. **Laugwitz, B., Held, T., & Schrepp, M. (2008).** "Construction and evaluation of a user experience questionnaire." *IWMH 2008.* [UEQ development and validation]

8. **ISO 9241-11:2018.** *Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.* International Organization for Standardization. [Standard definition of usability & UX]

9. **Nielsen, J. (2012).** "Usability 101: Introduction to Usability.* Nielsen Norman Group. [Practical usability testing guide]

10. **Krug, S. (2014).** *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability.* New Riders. [Design principles for intuitive interfaces]

---

## CHECKLIST AKHIR

- [✅] Judul masih dapat ditelusuri ke masalah (keluhan Play Store SIGNAL), intervensi (counterbalanced comparison), dan metode (SUS+UEQ+task metrics)
- [✅] Ringkasan memuat urgensi (adoption barrier), tujuan (evidence-based comparison), metode (between-subjects, N powered), dan luaran (rekomendasi design)
- [✅] Isi File 1 terintegrasi dari WS-01 sampai WS-07 (problem, gap, RQ, hipotesis, variabel, sistem, eksperimen)
- [✅] Rumusan masalah selaras dengan gap (Method Gap + Context Gap yang valid dari literatur)
- [✅] Gap muncul dari literature mapping rigor (8 paper catalogued, pola & limitasi identified), bukan intuisi pribadi
- [✅] RQ menjawab gap langsung (comparative framework + phase-specific evaluation)
- [✅] Hipotesis H₀/H₁ konsisten dengan RQ dan metric utama (SUS, UEQ, task time)
- [✅] Baseline (SUS SIGNAL 2024 ~55, UEQ SIGNAL 2023) = baseline di state-of-the-art = baseline di eksperimen
- [✅] Satu proposal berpusat pada satu IV utama (platform comparison dengan phase as secondary IV)
- [✅] Metric benar-benar mengukur DV (SUS → usability, UEQ → UX holistik, time/success → objective complement)
- [✅] Instrument memberi jalur nyata ke data (questionnaire forms, stopwatch, video audit trail)
- [✅] Scope di pendahuluan (SIGNAL vs New Sakpole, 3 fase, N ≥45 per group) = scope di metode
- [✅] State of the art menunjukkan posisi riset (Method Gap + Context Gap positioning jelas)
- [✅] Metode menjelaskan unit analisis (responden stratified), A vs B (SIGNAL vs New Sakpole, counterbalanced), cara ukur (SUS/UEQ/time), skenario uji (task protocol), teknik analisis (t-test per metrik per fase)
- [✅] Threats to validity documented sistematis (9 threats, mitigasi konkret, pre-registered)
- [✅] Hasil yang diharapkan realistis, terukur, masuk akal terhadap jadwal (6 bulan, milestone jelas)
- [✅] Jadwal realistic terhadap beban kerja (recruitment 1 bulan, collection 2 bulan, analysis 1.5 bulan, writing 1.5 bulan)
- [✅] Daftar pustaka hanya sumber disitasi (10 referensi, semua relevan ke RQ/metode)

---

