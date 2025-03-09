import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
guanyuan = pd.read_csv("Data/PRSA_Data_Guanyuan_20130301-20170228.csv")
shunyi = pd.read_csv("Data/PRSA_Data_Shunyi_20130301-20170228.csv")

# Data preparation
guanyuan['datetime'] = pd.to_datetime(guanyuan[['year', 'month', 'day', 'hour']])
shunyi['datetime'] = pd.to_datetime(shunyi[['year', 'month', 'day', 'hour']])

# Streamlit App
st.set_page_config(page_title="Analisis Kualitas Udara", layout="wide")

st.title("Dashboard Analisis Kualitas Udara PM2.5")
st.write("""
### Proyek Analisis Data - [Air Quality Dataset]
**Nama:** [Mochamad Girvan Azhar]  
**Email:** [girvanazhr@gmail.com]  
**ID Dicoding:** [MC009D5Y0502]
""")

# Sidebar
st.sidebar.header("Pengaturan Parameter")
selected_year = st.sidebar.slider("Pilih Tahun", 2013, 2017, (2013, 2017))

# Fungsi untuk filter data
def filter_data(df, years):
    return df[(df['datetime'].dt.year >= years[0]) & (df['datetime'].dt.year <= years[1])]

# Tab untuk visualisasi
tab1, tab2, tab3 = st.tabs(["Perbandingan Rata-rata", "Tren PM2.5", "Faktor Pengaruh"])

with tab1:
    st.header("Perbandingan Rata-rata PM2.5")
    
    avg_pm25 = pd.DataFrame({
        'Lokasi': ['Guanyuan', 'Shunyi'],
        'PM2.5': [guanyuan['PM2.5'].mean(), shunyi['PM2.5'].mean()]
    })
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=avg_pm25, x='Lokasi', y='PM2.5', palette='Blues')
    plt.title("Perbandingan Rata-rata PM2.5")
    st.pyplot(fig)

with tab2:
    st.header("Tren Polusi PM2.5 Tahun ke Tahun")
    
    guan_filtered = filter_data(guanyuan, selected_year)
    shun_filtered = filter_data(shunyi, selected_year)
    
    guan_monthly = guan_filtered.resample('M', on='datetime')['PM2.5'].mean().reset_index()
    shun_monthly = shun_filtered.resample('M', on='datetime')['PM2.5'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=guan_monthly, x='datetime', y='PM2.5', label='Guanyuan', marker='o')
    sns.lineplot(data=shun_monthly, x='datetime', y='PM2.5', label='Shunyi', marker='o')
    plt.title("Tren Rata-rata PM2.5 Bulanan")
    plt.xlabel("Tahun")
    plt.ylabel("Konsentrasi PM2.5 (µg/m³)")
    plt.grid(True)
    st.pyplot(fig)

with tab3:
    st.header("Faktor yang Mempengaruhi PM2.5")
    
    selected_location = st.radio("Pilih Lokasi", ['Guanyuan', 'Shunyi'])
    variables = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
    selected_var = st.selectbox("Pilih Variabel", variables)
    
    data = guanyuan if selected_location == 'Guanyuan' else shunyi
    filtered_data = filter_data(data, selected_year)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=filtered_data, x=selected_var, y='PM2.5', alpha=0.5)
    plt.title(f'Hubungan {selected_var} dengan PM2.5 di {selected_location}')
    plt.xlabel(selected_var)
    plt.ylabel('Konsentrasi PM2.5 (µg/m³)')
    st.pyplot(fig)
    
    corr = filtered_data[['PM2.5', selected_var]].corr().iloc[0,1]
    st.metric(label="Koefisien Korelasi", value=f"{corr:.2f}")

st.sidebar.header("Statistik Deskriptif")
if st.sidebar.checkbox("Tampilkan Statistik Deskriptif"):
    st.subheader("Statistik Deskriptif PM2.5")
    desc_stats = guanyuan['PM2.5'].describe()
    st.write(desc_stats)

st.markdown("""
**Catatan:**
- Data mencakup periode 2013-2017
- Sumber data: Dataset Kualitas Udara Beijing
- Missing values telah diatasi dengan median imputation
""")