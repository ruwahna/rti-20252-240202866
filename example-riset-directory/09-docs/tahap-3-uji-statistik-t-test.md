# Tahap 3 — Uji Statistik Inferensial (T-Test)

**Status:** Selesai  
**Tujuan:** Menguji signifikansi statistik dari perbedaan tingkat usability (Skor SUS) antara SIGNAL dan New Sakpole secara kuantitatif.

---

## 1. Rumusan Hipotesis
- **Hipotesis Nol ($H_0$):** $\mu_1 = \mu_2$ (Tidak ada perbedaan rata-rata skor SUS yang signifikan antara SIGNAL dan New Sakpole).
- **Hipotesis Alternatif ($H_1$):** $\mu_1 \neq \mu_2$ (Ada perbedaan rata-rata skor SUS yang signifikan antara SIGNAL dan New Sakpole).
- **Tingkat Signifikansi ($\alpha$):** 0.05 (Uji dua arah/*two-tailed*).

## 2. Pelaksanaan Independent T-Test
Karena keterbatasan dependensi pustaka statistika eksternal, pengujian T-Test dihitung secara langsung menggunakan formula matematis di Python pada script `generate_output.py`:

- **Derajat Kebebasan (*dof*):** $n_1 + n_2 - 2 = 97 + 97 - 2 = 192$
- **t-statistic:** 5.46
- **p-value:** < 0.001 (Sangat signifikan, karena jauh di bawah batas $\alpha = 0.05$).
- **Keputusan:** Menolak $H_0$ dan menerima $H_1$.

## 3. Perhitungan Effect Size (Cohen's d)
Untuk mengukur seberapa kuat perbedaan kegunaan secara praktis di dunia nyata, dihitung nilai *Cohen's d*:
- **Cohen's d:** 0.78
- **Kategori:** *Medium-to-large effect* (efek perbedaan tergolong kuat). Hal ini membuktikan perbedaan sekitar 9.7 poin antara kedua platform tersebut tidak terjadi karena kebetulan melainkan akibat perbedaan nyata dalam kualitas rancangan antarmuka aplikasi.

Hasil akhir uji statistik disimpan di berkas [t_test_results.md](../06-output/tables/t_test_results.md).
