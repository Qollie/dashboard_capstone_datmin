import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data dashboard.csv")

# Tampilkan tabel data mentah (opsional)
st.subheader("Data Mentah")
st.write(df)

# Pastikan kolom tanggal dalam format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Filter 6 bulan terakhir
df_sorted = df.sort_values(by='tanggal')
last_6_months = df_sorted[df_sorted['tanggal'] >= (df_sorted['tanggal'].max() - pd.DateOffset(months=6))]

# Tampilkan chart
st.subheader("Line Chart - 6 Bulan Terakhir")
fig, ax = plt.subplots()
ax.plot(last_6_months['tanggal'], last_6_months['jumlah'], marker='o')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah")
ax.set_title("Tren Jumlah Selama 6 Bulan Terakhir")
st.pyplot(fig)
