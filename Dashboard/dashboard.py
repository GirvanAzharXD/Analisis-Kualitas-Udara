import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Harus di baris pertama setelah import
st.set_page_config(page_title="Analisis Kualitas Udara", layout="wide")

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    guanyuan = pd.read_csv("Dashboard/data/PRSA_Data_Guanyuan_20130301-20170228.csv")
    shunyi = pd.read_csv("Dashboard/data/PRSA_Data_Shunyi_20130301-20170228.csv")
    return guanyuan, shunyi

# Memuat data
guanyuan, shunyi = load_data()

st.title("Analisis Data Kualitas Udara Beijing")

# Sidebar untuk kontrol
st.sidebar.header("Pengaturan Parameter")
selected_location = st.sidebar.radio(
    "Pilih Lokasi:",
    ('Guanyuan', 'Shunyi')
)

selected_year = st.sidebar.slider(
    "Pilih Rentang Tahun:",
    min_value=2013,
    max_value=2017,
    value=(2013, 2017)
)

# Pilih dataset berdasarkan lokasi
data = guanyuan if selected_location == 'Guanyuan' else shunyi

# Preprocessing data
data['date'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data_filtered = data[(data['year'] >= selected_year[0]) & (data['year'] <= selected_year[1])]

# Tampilkan data mentah
if st.sidebar.checkbox('Tampilkan Data Mentah'):
    st.subheader('Data Mentah')
    st.write(data_filtered)

# Visualisasi 1: Tren PM2.5 Tahunan
st.subheader(f'Tren PM2.5 Tahunan di {selected_location}')
yearly_avg = data_filtered.groupby('year')['PM2.5'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='PM2.5', data=yearly_avg, marker='o')
plt.title('Rata-rata PM2.5 Tahunan')
plt.xlabel('Tahun')
plt.ylabel('PM2.5 (μg/m³)')
plt.grid(True)
st.pyplot(plt)

# Visualisasi 2: Hubungan dengan Faktor Lain
st.subheader('Hubungan PM2.5 dengan Faktor Lingkungan')
selected_feature = st.selectbox(
    'Pilih Faktor:',
    ('TEMP', 'PRES', 'WSPM', 'DEWP')
)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=selected_feature, y='PM2.5', data=data_filtered, alpha=0.5)
plt.title(f'PM2.5 vs {selected_feature}')
plt.xlabel(selected_feature)
plt.ylabel('PM2.5 (μg/m³)')
st.pyplot(plt)

# Tampilkan statistik deskriptif
st.subheader('Statistik Deskriptif')
st.write(data_filtered[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']].describe())

# Analisis Korelasi
st.subheader('Matriks Korelasi')
corr_matrix = data_filtered[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot(plt)
