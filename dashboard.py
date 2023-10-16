import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

day_df = pd.read_csv('day.csv')

st.title('Dashboard Analisis Data Sepeda Sewaan')

st.write('Ini adalah dashboard analisis data sepeda sewaan berdasarkan pertanyaan')

selected_question = st.selectbox('Pilih Pertanyaan:', ['Pertanyaan 1: Hubungan Musim dan Jumlah Sewa Sepeda', 'Pertanyaan 2: Pola Penggunaan Sepeda Sewaan'])

if selected_question == 'Pertanyaan 1: Hubungan Musim dan Jumlah Sewa Sepeda':
    season_rentals = day_df.groupby('season')['cnt'].sum().reset_index()

    # Plot hubungan antara musim dan jumlah total sewa sepeda
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', data=season_rentals, ax=ax)

    ax.set_title('Hubungan Musim dan Jumlah Sewa Sepeda', pad=20)

    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Total Sewa Sepeda')

    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])

    st.pyplot(fig)
    # st.write('Berikut adalah hubungan antara musim dan jumlah total sewa sepeda.')
    
    # multi = ''' Kesimpulan:
    # - <div style="text-align: justify;">Musim Gugur Paling Populer: Musim gugur (Musim 3) adalah musim dengan jumlah total sewa sepeda yang paling tinggi. Ini mungkin disebabkan oleh cuaca yang nyaman dan kemungkinan liburan musim panas yang berakhir dapat menjelaskan popularitas musim ini.</div>

    # - <div style="text-align: justify;">Musim Panas Mengikuti: Musim panas (Musim 2) memiliki jumlah sewa sepeda yang tinggi, meskipun sedikit lebih rendah daripada musim panas. Kondisi cuaca yang lebih hangat dan kondisi yang lebih bersahabat untuk bersepeda.</div>

    # - <div style="text-align: justify;">Musim Dingin Menengah: Musim dingin (Musim 4) memiliki jumlah sewa sepeda yang cukup baik, meskipun lebih rendah dibandingkan dengan musim gugur dan panas. Penggunaan sepeda sewaan selama musim dingin mungkin dipengaruhi oleh cuaca yang lebih dingin, kondisi jalan yang lebih sulit, atau kurangnya kegiatan bersepeda di musim ini.</div>

    # - <div style="text-align: justify;">Musim Semi Tidak Populer: Musim semi (Musim 1) adalah musim dengan jumlah total sewa sepeda yang paling rendah. Penggunaan sepeda sewaan selama musim semi mungkin dipengaruhi oleh cuaca yang belum sepenuhnya hangat dan kondisi jalan yang mungkin tidak sesuai untuk bersepeda.</div>
    
    # '''
    # st.markdown(multi, unsafe_allow_html=True)

elif selected_question == 'Pertanyaan 2: Pola Penggunaan Sepeda Sewaan':
    average_rentals_by_day = day_df.groupby(['yr', 'workingday', 'holiday'])['cnt'].mean().reset_index()

    # Plot pola penggunaan sepeda berdasarkan hari kerja dan hari libur
    fig, ax = plt.subplots()
    sns.barplot(x='yr', y='cnt', hue='workingday', data=average_rentals_by_day, ax=ax)

    ax.set_title('Pola Penggunaan Sepeda Sewaan berdasarkan hari kerja dan hari libur dari tahun ke tahun', pad=20)

    ax.set_xlabel('Tahun')
    ax.set_ylabel('Jumlah Total Sewa Sepeda')

    ax.set_xticks([0, 1])
    ax.set_xticklabels([2011, 2012])

    st.pyplot(fig)
    # st.write('Berikut adalah pola penggunaan sepeda sewaan berdasarkan hari kerja dan hari libur dari tahun ke tahun.')

    # multi = ''' Kesimpulan:
    # - <div style="text-align: justify;">Penggunaan Lebih Tinggi pada Hari Kerja: Penggunaan sepeda sewaan lebih tinggi pada hari kerja dibandingkan dengan hari libur. Ini dapat disebabkan oleh banyak orang yang menggunakan sepeda sewaan untuk pergi bekerja.</div>

    # - <div style="text-align: justify;">Konsistensi dari Tahun ke Tahun: Pola penggunaan sepeda sewaan berdasarkan hari kerja dan hari libur nampaknya konsisten dari tahun 2011 (yr = 0) hingga tahun 2012 (yr = 1). Artinya, tren ini tidak mengalami perubahan yang signifikan dari tahun ke tahun.</div>

    # '''
    # st.markdown(multi, unsafe_allow_html=True)

if st.checkbox('Tampilkan Data'):
    st.write('Data Hari:')
    st.write(day_df.head())
