import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    day_df = pd.read_csv('day_df.csv', parse_dates=['dteday'])
    hour_df = pd.read_csv('hour_df.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

st.title('Bike Rental Analysis Dashboard')

# filtering berdasarkan tahun dan bulan
day_df['month'] = day_df['dteday'].dt.month
day_df['year'] = day_df['dteday'].dt.year

# Unique months and years for 
months = ['All'] + day_df['month'].unique().tolist()
years = ['All'] + day_df['year'].unique().tolist()

# Sidebar filters
st.sidebar.header('Filter')
selected_year = st.sidebar.selectbox('Pilih Tahun', years)
selected_month = st.sidebar.selectbox('Pilih Bulan', months)

# Buat pilihan ALl jika ingin menampilkan semua data juga
if selected_year != 'All':
    filtered_day_df = day_df[day_df['year'] == selected_year]
else:
    filtered_day_df = day_df

if selected_month != 'All':
    filtered_day_df = filtered_day_df[filtered_day_df['month'] == selected_month]

# Pertanyaan 1: Apakah ada pengaruh jumlah permintaan sepeda antara weekday dan holiday?
st.subheader('Jumlah Permintaan Sepeda Pada Weekday dan Holiday')
fig1, ax1 = plt.subplots(figsize=(5, 3))
sns.barplot(x='workingday', y='cnt', data=filtered_day_df, palette='coolwarm', ax=ax1)
ax1.set_xlabel('Hari Kerja')
ax1.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig1)

# Pertanyaan 2: Bagaimana pengaruh cuaca terhadap permintaan sepeda?
st.subheader('Jumlah Permintaan Sepeda Berdasarkan Cuaca')
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(y='weathersit', x='cnt', data=hour_df, palette='coolwarm', ax=ax2)
ax2.set_title('Jumlah Pengguna Sepeda berdasarkan Cuaca')
ax2.set_xlabel('Jumlah Pengguna Sepeda')
ax2.set_ylabel('Kondisi Cuaca')
st.pyplot(fig2)

st.subheader('Korelasi Jumlah Permintaan Sepeda dengan Temperatur, Kelembapan, dan Kecepatan Angin')
column = filtered_day_df[['temp', 'cnt', 'hum', 'windspeed']]
correlation = column.corr()
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation, annot=True, center=0, cmap='coolwarm', ax=ax3)
st.pyplot(fig3)

st.markdown("""
**Keterangan:**
- Korelasi positif antara suhu (temp) dengan jumlah permintaan sepeda menunjukkan bahwa ketika suhu meningkat, jumlah permintaan sepeda juga cenderung meningkat.
- Korelasi negatif antara kelembaban (hum) dan dengan Kecepatan angin (windspeed) jumlah permintaan sepeda menunjukkan bahwa kondisi lembab mengurangi penggunaan sepeda.
""")

# Pertanyaan 3: Bagaimana penggunaan sepeda berbeda antara pengguna terdaftar dan pengguna tidak terdaftar?
st.subheader('Jumlah Permintaan Sepeda Pada Pengguna Terdaftar dan Tidak Terdaftar')
account = filtered_day_df[['casual', 'registered']].sum().reset_index()
account.columns = ['User Type', 'Count']

fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x='User Type', y='Count', data=account, palette='coolwarm', ax=ax4)
ax4.set_xlabel('Tipe Pengguna')
ax4.set_ylabel('Jumlah')
st.pyplot(fig4)

day_pattern = filtered_day_df.groupby('workingday').agg({
    'registered': 'sum',
    'casual': 'sum'
}).reset_index()

st.subheader('Jumlah Permintaan Sepeda Pada Hari Keja dan Libur Pada Pengguna Terdaftar dan Tidak Terdaftar')
fig5, ax5 = plt.subplots(figsize=(8, 5))
ax5.bar(day_pattern['workingday'], day_pattern['registered'], label='Registered', color='#FF9999')
ax5.bar(day_pattern['workingday'], day_pattern['casual'], bottom=day_pattern['registered'], label='Casual', color='#9999FF')
ax5.set_xlabel('Working Day')
ax5.set_ylabel('Jumlah Penyewa Sepeda')
ax5.legend()
st.pyplot(fig5)

# Pertanyaan 4: Apakah ada tren musiman dalam penggunaan sepeda?
st.subheader('Jumlah Pengguna Sepeda Berdasarkan Musim')
fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=filtered_day_df, palette='coolwarm', ax=ax6)
ax6.set_xlabel('Musim')
ax6.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig6)