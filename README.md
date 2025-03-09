# Analisis Kualitas Udara Beijing
Proyek ini terdiri dari :
1. Analisis Data (Jupyter Notebook)
2. Dashboard (Streamlit)
## Gambaran Umum Proyek
Analisis data kualitas udara di Beijing dengan fokus pada parameter PM2.5 di lokasi Guanyuan dan Shunyi periode 2013-2017. Proyek ini mencakup:

- Analisis tren polusi PM2.5 tahunan
- Identifikasi faktor yang mempengaruhi konsentrasi PM2.5
- Visualisasi interaktif menggunakan Streamlit
- Pemrosesan data dan EDA dalam Jupyter Notebook

## Fitur Dashboard
### Tampilan Interaktif
1. **Perbandingan Rata-rata**  
   - Grafik batang perbandingan PM2.5 antar lokasi
   - Statistik deskriptif PM2.5

2. **Tren Temporal**  
   - Grafik garis perkembangan PM2.5 bulanan
   - Filter rentang tahun (2013-2017)
   - Overlay data dua lokasi

3. **Analisis Faktor**  
   - Scatter plot hubungan parameter cuaca dengan PM2.5
   - Perhitungan koefisien korelasi
   - Pilihan variabel: suhu, tekanan udara, titik embun, curah hujan, dan kecepatan angin

### Fungsi Interaktif
- Filter tahun dengan slider
- Pemilihan lokasi dengan radio button
- Tampilan responsif untuk berbagai device

## Struktur Dataset
File data dalam format CSV:
- `PRSA_Data_Guanyuan_20130301-20170228.csv`
- `PRSA_Data_Shunyi_20130301-20170228.csv`

Variabel yang tersedia:
- Parameter polusi: PM2.5, PM10, SO2, NO2, CO, O3
- Parameter cuaca: Temperatur, Tekanan Udara, Titik Embun, Curah Hujan, Kecepatan Angin
- Data temporal: Tahun, Bulan, Hari, Jam

## Instalasi
1. Clone repositori
```
git clone https://github.com/username/air-quality-analysis.git
cd air-quality-analysis
Install dependencies


pip install -r requirements.txt
Jalankan dashboard


streamlit run dashboard.py
```
**Teknis Implementasi**
Requirements:

Python 3.7+

Streamlit

Pandas

Matplotlib

Seaborn

Struktur File:


Submission

├───Dashboard

| ├───PRSA_Data_Guanyuan_20130301-20170228.csv

| └───PRSA_Data_Shunyi_20130301-20170228.csv 

| └───dashboard.py

├───Data

| ├───PRSA_Data_Guanyuan_20130301-20170228.csv

| └───PRSA_Data_Shunyi_20130301-20170228.csv 

├───Proyek_Analisis_Data.ipynb

├───README.md

└───requirements.txt

└───url.txt

Lisensi
Proyek ini dilisensikan di bawah MIT License

Penulis
Mochamad Girvan Azhar

Email: girvanazhr@gmail.com

Dicoding: MC009D5Y0502

Catatan:
Dataset harus ditempatkan dalam folder Data sesuai struktur direktori. Untuk analisis detail proses pembersihan data dan EDA, lihat file Proyek_Analisis_Data.ipynb

File ini mencakup:
1. Informasi esensial tentang proyek
2. Petunjuk instalasi lengkap
3. Dokumentasi fitur dashboard
4. Penjelasan struktur dataset
5. Panduan teknis untuk menjalankan aplikasi
6. Informasi lisensi dan kontak penulis

Sesuaikan path dataset dan informasi repositori sesuai kebutuhan aktual sebelum digunakan.
