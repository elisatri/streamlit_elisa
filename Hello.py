import streamlit as st
import pandas as pd

# Memuat data CSV
data = pd.read_csv("tips.csv")

# Pemilihan kolom oleh pengguna (asumsikan "total_bill" dan "tip")
kolom_pilihan = st.selectbox("Pilih Kolom untuk Distribusi", data.columns)

# Bagan distribusi (asumsikan kolom "tip" mewakili rating)
st.subheader("Distribusi Rating dalam 5 Tahun Terakhir (Mengasumsikan Kolom 'tip')")

# Menangani data yang tidak memiliki kolom 'datetime'
if 'datetime' in data.columns:
  data['tahun'] = pd.to_datetime(data['datetime']).dt.year  # Ekstraksi tahun
  data_difilter = data[data['tahun'] >= 2018]  # Filter untuk 5 tahun terakhir (asumsi 2023)
  st.bar_chart(data_difilter[kolom_pilihan])  # Bagan distribusi untuk kolom yang dipilih
else:
  st.write("Data tidak mengandung kolom 'datetime' untuk ekstraksi tahun.")

# Penanganan peringatan deprekasi Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Hapus fungsi run jika tidak diperlukan (sesuaikan dengan kode Anda)
# if __name__ == "__main__":
#     run()
