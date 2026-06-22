import pandas as pd
import numpy as np
import random

# Set seed agar hasil selalu sama
np.random.seed(42)
random.seed(42)

# Konfigurasi 200 responden
n_signal = 100
n_sakpole = 100
n_total = n_signal + n_sakpole

# Data demografi dasar
responden_id = [f"{i:03d}" for i in range(1, n_total + 1)]
jenis_kelamin = np.random.choice(['L', 'P'], n_total)
umur = np.random.randint(18, 55, n_total)
aplikasi = ['SIGNAL'] * n_signal + ['New Sakpole'] * n_sakpole

# Generate SUS Scores (Signal rata-rata lebih tinggi sedikit)
sus_signal = np.random.normal(loc=76.5, scale=12.0, size=n_signal)
sus_sakpole = np.random.normal(loc=68.0, scale=12.0, size=n_sakpole)
sus_score = np.concatenate([sus_signal, sus_sakpole])
# Pastikan tidak ada yang > 100 atau < 0 secara tidak sengaja
sus_score = np.clip(sus_score, 10, 99)

# Generate UEQ Scores (-3 to 3)
ueq_daya_tarik = np.random.uniform(-1, 2.5, n_total)
ueq_kejelasan = np.random.uniform(-1, 2.5, n_total)
ueq_efisiensi = np.random.uniform(-1.5, 2.0, n_total)
ueq_ketepatan = np.random.uniform(-1, 2.0, n_total)
ueq_stimulasi = np.random.uniform(-1, 2.5, n_total)
ueq_kebaruan = np.random.uniform(-1.5, 2.0, n_total)

df = pd.DataFrame({
    'Responden_ID': responden_id,
    'Jenis_Kelamin': jenis_kelamin,
    'Umur': umur,
    'Aplikasi': aplikasi,
    'SUS_Score': np.round(sus_score, 1),
    'UEQ_Daya_Tarik': np.round(ueq_daya_tarik, 1),
    'UEQ_Kejelasan': np.round(ueq_kejelasan, 1),
    'UEQ_Efisiensi': np.round(ueq_efisiensi, 1),
    'UEQ_Ketepatan': np.round(ueq_ketepatan, 1),
    'UEQ_Stimulasi': np.round(ueq_stimulasi, 1),
    'UEQ_Kebaruan': np.round(ueq_kebaruan, 1)
})

# ==== MASUKKAN ANOMALI SESUAI WS-11 ====
# 1. Bikin 1 outlier ekstrim (Skor SUS > 100)
# Kita taruh di Responden_ID 003
df.loc[df['Responden_ID'] == '003', 'SUS_Score'] = 120.0

# 2. Bikin 5 responden dengan data missing (gak ngisi selesai)
# Kita kosongkan beberapa nilai di baris terakhir SIGNAL (2 responden) dan Sakpole (3 responden)
missing_indices = [98, 99, 197, 198, 199]
for idx in missing_indices:
    df.loc[idx, 'SUS_Score'] = np.nan
    df.loc[idx, 'UEQ_Daya_Tarik'] = np.nan
    df.loc[idx, 'UEQ_Efisiensi'] = np.nan

df.to_csv('survey_data_signal_sakpole.csv', index=False)
print("Berhasil men-generate 200 data CSV dengan anomali!")
