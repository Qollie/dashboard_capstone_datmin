import streamlit as st
import pandas as pd
import plotly.express as px

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

# Tampilkan data mentah
st.subheader("Data 6 Bulan Terakhir")
st.write(last_6_months)

# Bar Chart Interaktif
st.subheader("Bar Chart Interaktif per Hari")
fig_bar = px.bar(
    last_6_months,
    x='Tanggal',
    y='Total_Pemakaian',
    labels={'Total_Pemakaian': 'Total Pemakaian'},
    title='Total Pemakaian Harian Selama 6 Bulan Terakhir'
)
fig_bar.update_xaxes(tickangle=45)
st.plotly_chart(fig_bar, use_container_width=True)

# Line Chart Interaktif
st.subheader("Line Chart Interaktif per Hari")
fig_line = px.line(
    last_6_months,
    x='Tanggal',
    y='Total_Pemakaian',
    markers=True,
    labels={'Total_Pemakaian': 'Total Pemakaian'},
    title='Total Pemakaian Harian Selama 6 Bulan Terakhir'
)
fig_line.update_xaxes(tickangle=45)
st.plotly_chart(fig_line, use_container_width=True)
