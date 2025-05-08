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

# Grafik 1: Bar Chart - Total Pemakaian per Hari
st.subheader("Grafik Total Pemakaian per Hari")
fig, ax = plt.subplots()
ax.bar(last_6_months['Tanggal'], last_6_months['Total_Pemakaian'])
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Pemakaian")
ax.set_title("Total Pemakaian per Hari Selama 6 Bulan Terakhir")
plt.xticks(rotation=45)
st.pyplot(fig)

# Grafik 2: Line Chart - Total Pemakaian per Hari
st.subheader("Grafik Line Total Pemakaian per Hari")
fig, ax = plt.subplots()
ax.plot(last_6_months['Tanggal'], last_6_months['Total_Pemakaian'], marker='o', linestyle='-', color='b')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Pemakaian")
ax.set_title("Total Pemakaian per Hari Selama 6 Bulan Terakhir")
plt.xticks(rotation=45)
st.pyplot(fig)
