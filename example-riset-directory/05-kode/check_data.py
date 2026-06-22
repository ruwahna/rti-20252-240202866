import pandas as pd
import numpy as np
import os

def validate_survey_data(filepath):
    print(f"=== Memulai Validasi Data: {filepath} ===")
    
    # 1. Cek apakah file ada
    if not os.path.exists(filepath):
        print(f"[ERROR] File {filepath} tidak ditemukan. Pastikan data dari form sudah diunduh.")
        return
        
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"[ERROR] Gagal membaca CSV. Pastikan format benar. Detail: {e}")
        return

    # 2. Cek Completeness (Missing Value)
    total_rows = len(df)
    print(f"\n[INFO] Total responden tercatat: {total_rows}")
    
    missing_data = df.isnull().sum()
    if missing_data.any():
        print("[WARNING] Ditemukan missing values (data tidak lengkap):")
        print(missing_data[missing_data > 0])
        print("-> Tindakan: Sebaiknya gunakan df.dropna() untuk membersihkan data ini.")
    else:
        print("[OK] Tidak ada data missing. Completeness 100%.")

    # 3. Range & Logic Check (Misal kolom bernama 'SUS_SIGNAL' dan 'SUS_SAKPOLE')
    sus_columns = [col for col in df.columns if 'SUS' in col.upper()]
    
    if not sus_columns:
        print("\n[INFO] Tidak mendeteksi kolom dengan kata 'SUS'. Pastikan header sesuai.")
    else:
        for col in sus_columns:
            # Cek nilai di luar batas 0-100
            out_of_bounds = df[(df[col] < 0) | (df[col] > 100)]
            if not out_of_bounds.empty:
                print(f"\n[WARNING] Anomali pada kolom {col}! Ada nilai di luar 0-100:")
                print(out_of_bounds[[col]])
                print("-> Tindakan: Filter atau drop baris yang nilainya tidak masuk akal ini.")
            else:
                print(f"\n[OK] Range validasi untuk kolom {col} aman (0-100).")

    # 4. Outlier Check menggunakan metode IQR (Optional)
    for col in sus_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        if not outliers.empty:
            print(f"\n[INFO] Terdeteksi outlier statistik (berdasarkan IQR) pada kolom {col}:")
            print(outliers[[col]])
            print("-> Catatan: Outlier statistik tidak wajib dihapus jika masih masuk di range logika 0-100.")

    print("\n=== Validasi Selesai ===")

if __name__ == "__main__":
    # Ini cuma skrip template. Nanti kamu bisa ubah 'survey_data.csv' sesuai nama file aslimu.
    print("Menjalankan skrip validasi data...\n")
    validate_survey_data('survey_data_signal_sakpole.csv')
