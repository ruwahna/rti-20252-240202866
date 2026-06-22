# Landasan Teori dan Kerangka Metodologi

## 1. System Usability Scale (SUS)

*System Usability Scale* (SUS) adalah instrumen kuesioner *"quick and dirty"* yang sangat andal dan umum digunakan untuk mengevaluasi *usability* berbagai macam produk teknologi, termasuk perangkat lunak dan aplikasi seluler. Dalam riset ini, saya menggunakan SUS karena instrumen ini ringkas (hanya terdiri dari 10 pertanyaan), tidak terlalu membebani responden, namun terbukti memberikan hasil ukur kuantitatif yang telah tervalidasi secara luas selama puluhan tahun.

**Sistem Penilaian Perhitungan SUS:**
- Pertanyaan bernada ganjil (1, 3, 5, 7, 9) bernada positif. Rumus skornya adalah `Nilai Skala - 1`.
- Pertanyaan bernada genap (2, 4, 6, 8, 10) bernada negatif. Rumus skornya adalah `5 - Nilai Skala`.
- Seluruh total penjumlahan skor responden kemudian dikalikan dengan bobot **2.5** untuk mendapatkan skor akhir dalam rentang skala baku 0-100.

**Standar Interpretasi Skor:**
- Kurang dari 68 : *Poor* / Belum layak pakai
- 68 : *Average* / Batas rata-rata kelayakan minimum
- Di atas 68 hingga 80 : *Good* / Nyaman dan layak digunakan
- Di atas 80 : *Excellent* / Sangat superior

## 2. Independent T-Test

*Independent T-Test* adalah metode analisis statistika inferensial parametrik yang saya gunakan untuk membandingkan rata-rata dari dua kelompok sampel yang saling bebas (tidak memiliki hubungan berpasangan). Dalam konteks komparasi UX pada riset ini, kedua kelompok tersebut merepresentasikan populasi pengguna aplikasi SIGNAL dan pengguna aplikasi New Sakpole.

**Syarat Penggunaan Metode yang Telah Saya Penuhi:**
1. Variabel terikat (*dependent variable*) berupa data berskala rasio/kontinu (yaitu metrik Skor SUS).
2. Terdapat tepat dua variabel bebas yang kategorik dan saling eksklusif (Grup Aplikasi SIGNAL dan Grup Aplikasi Sakpole).
3. Data terdistribusi secara normal atau memiliki sampel memadai. Pada kasus saya, jumlah n=194 telah secara sah memenuhi asumsi *Central Limit Theorem*.
4. Tidak ada pencilan (*outlier*) ekstrem (telah saya atasi pada tahap pembersihan data dengan membuang hasil skor yang tidak logis/ > 100).

Melalui uji T-Test ini, saya dapat menarik kesimpulan *p-value* untuk menentukan secara sah apakah hipotesis nol (tidak terdapat perbedaan *usability*) dapat ditolak pada tingkat signifikansi 5% (α = 0.05).
