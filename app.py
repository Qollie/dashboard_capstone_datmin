import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Dashboard Pemakaian 6 Bulan Terakhir")

# Load data
df = pd.read_csv("data dashboard.csv")

# Konversi kolom tanggal ke format datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# Urutkan berdasarkan tanggal
df = df.sort_values('Tanggal')

# Ambil data 6 bulan terakhir dari tanggal terakhir yang tersedia
last_6_months = df[df['Tanggal'] >= (df['Tanggal'].max() - pd.DateOffset(months=6))]

# Tampilkan data mentah (opsional)
st.subheader("Data 6 Bulan Terakhir")
st.write(last_6_months)

# Buat line chart
st.subheader("Grafik Total Pemakaian")
fig, ax = plt.subplots()
ax.plot(last_6_months['Tanggal'], last_6_months['Total_Pemakaian'], marker='o', linestyle='-')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Pemakaian")
ax.set_title("Total Pemakaian Selama 6 Bulan Terakhir")
plt.xticks(rotation=45)
st.pyplot(fig)
