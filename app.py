import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Dashboard Pemakaian 6 Bulan Terakhir")

# Load data
df = pd.read_csv("data dashboard.csv")
df['Tanggal'] = pd.to_datetime(df['Tanggal'])
df = df.sort_values('Tanggal')
last_6_months = df[df['Tanggal'] >= (df['Tanggal'].max() - pd.DateOffset(months=6))]

# Konfigurasi layout dengan teks dan grid jelas
layout_style = dict(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='black'),
    title_font=dict(color='black'),
    xaxis=dict(
        title_font=dict(color='black'),
        tickfont=dict(color='black'),
        showgrid=True,
        gridcolor='lightgray'
    ),
    yaxis=dict(
        title_font=dict(color='black'),
        tickfont=dict(color='black'),
        showgrid=True,
        gridcolor='lightgray'
    )
)

# Bar Chart
fig_bar = px.bar(
    last_6_months,
    x='Tanggal',
    y='Total_Pemakaian',
    labels={'Total_Pemakaian': 'Total Pemakaian'},
    title='Total Pemakaian Harian Selama 6 Bulan Terakhir'
)
fig_bar.update_xaxes(tickangle=45)
fig_bar.update_layout(**layout_style)
st.plotly_chart(fig_bar, use_container_width=True)

# Line Chart
fig_line = px.line(
    last_6_months,
    x='Tanggal',
    y='Total_Pemakaian',
    markers=True,
    labels={'Total_Pemakaian': 'Total Pemakaian'},
    title='Total Pemakaian Harian Selama 6 Bulan Terakhir'
)
fig_line.update_xaxes(tickangle=45)
fig_line.update_layout(**layout_style)
st.plotly_chart(fig_line, use_container_width=True)
