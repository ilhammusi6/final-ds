import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Taxi Trip Price Analysis Dashboard",    
    layout="wide",
    initial_sidebar_state="expanded"
)




def chart():
    df = pd.read_csv('Taxi Trip Price.csv')
    st.dataframe(df.head())

    #. kpi metrics
    st.subheader('KPI Metrics')
    total_trips = len(df)
    average_price = df['Trip_Price'].mean()
    average_distance = df['Trip_Distance_km'].mean()
    average_duration = df['Trip_Duration_Minutes'].mean()

    col1, col2, col3, col4 = st.columns(4)
    
    #2 kpi metrics with card rounded corners
    with col1:
        st.markdown(
            f"""
            <div style="background-color: #1E2A47; padding: 3px; border-radius: 3px; text-align: center;">
                <h3 style="color: white;">Total Perjalanan Taxi</h3>
                <h2 style="color: white;">{total_trips}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div style="background-color: #1E2A47; padding: 3px; border-radius: 3px; text-align: center;">
                <h3 style="color: white;">Rata-Rata Harga Taxi</h3>
                <h2 style="color: white;">${average_price:.2f}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )   

    with col3:
        st.markdown(
            f"""
            <div style="background-color: #1E2A47; padding: 3px; border-radius: 3px; text-align: center;">
                <h3 style="color: white;">Rata-Rata Jarak Perjalanan (km)</h3>
                <h2 style="color: white;">{average_distance:.2f} km</h2>
            </div>
            """,
            unsafe_allow_html=True
        )   
    with col4:      
        st.markdown(
            f"""
            <div style="background-color: #1E2A47; padding: 3px; border-radius: 3px; text-align: center;">
                <h3 style="color: white;">Rata-Rata Durasi Perjalanan (menit)</h3>
                <h2 style="color: white;">{average_duration:.2f} menit</h2>
            </div>
            """,
            unsafe_allow_html=True
        )   


 

    #1. Visualisasi Jumlah Penumpang
    st.subheader('Visualisasi Jumlah Penumpang Taxi')   
    fig1 = px.histogram(df, x='Passenger_Count', nbins=30, title='Distribusi Jumlah Penumpang')
    st.plotly_chart(fig1)

    #2. visualisasi Pengaruh Durasi Perjalanan terhadap Harga
    st.subheader('Pengaruh Durasi Perjalanan terhadap Harga Taxi')
    fig2 = px.scatter(df, x='Trip_Duration_Minutes', y='Trip_Price', 
                      title='Durasi Perjalanan vs Harga Taxi',
                      trendline='ols')
    st.plotly_chart(fig2)   

    st.write(
    "Hasil visualisasi menunjukkan bahwa durasi perjalanan memiliki pengaruh signifikan "
    "terhadap kenaikan harga. Perjalanan dengan durasi lebih lama cenderung memiliki "
    "harga yang lebih tinggi akibat akumulasi tarif berbasis waktu."
)
    #3. Visualisasi Distribusi Harga Bedasarkan Kondisi Lalu Lintas
    st.subheader('Distribusi Harga Taxi Berdasarkan Kondisi Lalu Lintas')
    fig3 = px.box(df, x='Traffic_Conditions', y='Trip_Price', 
                  title='Distribusi Harga Taxi berdasarkan Kondisi Lalu Lintas')
    st.plotly_chart(fig3)
    st.write(
    "Dari visualisasi box plot, terlihat bahwa kondisi lalu lintas yang lebih buruk "
    "seperti macet atau sangat macet cenderung menghasilkan harga taxi yang lebih tinggi    . "
    "Hal ini disebabkan oleh waktu perjalanan yang lebih lama akibat kemacetan.")

    #4. Rata-Rata harga Bedasarkan Waktu Perjalanan
    st.subheader('Rata-Rata Harga Taxi Berdasarkan Waktu Perjalanan')
    fig4 = px.bar(df.groupby('Time_of_Day')['Trip_Price'].mean().reset_index(),
                  x='Time_of_Day', y='Trip_Price',
                  title='Rata-Rata Harga Taxi berdasarkan Waktu Perjalanan')    
    st.plotly_chart(fig4)
    st.write(
    "Visualisasi ini menunjukkan bahwa rata-rata harga taxi cenderung lebih tinggi ")
    st.write(
    "pada jam sibuk seperti pagi dan sore hari, yang kemungkinan besar disebabkan oleh "
    "permintaan yang lebih tinggi selama periode tersebut.")    

    #5. Perbandinga Harga Berdasarkan Kondisi Cuaca
    st.subheader('Perbandingan Harga Taxi Berdasarkan Kondisi Cuaca')
    fig5 = px.violin(df, x='Weather', y='Trip_Price', 
                     title='Perbandingan Harga Taxi berdasarkan Kondisi Cuaca',
                     box=True, points='all')
    st.plotly_chart(fig5)
    st.write(
    "Dari visualisasi violin plot, terlihat bahwa kondisi cuaca buruk seperti hujan ")
    st.write(
    "atau badai cenderung menghasilkan harga taxi yang lebih tinggi. Hal ini mungkin "
    "disebabkan oleh faktor risiko dan permintaan yang meningkat selama kondisi cuaca tersebut.")   

    #6.Perbandingan Harga antara Weekday dan Weekend
    st.subheader('Perbandingan Harga Taxi antara Weekday dan Weekend')
    fig6 = px.box(df, x='Time_of_Day', y='Trip_Price', 
                  title='Perbandingan Harga Taxi antara Weekday dan Weekend')   
    st.plotly_chart(fig6)
    st.write(
    "Dari visualisasi box plot, terlihat bahwa harga taxi pada hari kerja cenderung lebih tinggi "
    "dibandingkan akhir pekan. Hal ini bisa disebabkan oleh permintaan yang lebih tinggi selama "
    "hari kerja karena aktivitas bisnis dan transportasi.")     

    #7.Ringkasan Statistik Deskriptif Harga Taxi
    st.subheader('Ringkasan Statistik Deskriptif Harga Taxi')
    st.write(df['Trip_Price'].describe())
    st.write(
    "Ringkasan statistik deskriptif memberikan gambaran umum tentang distribusi harga taxi. "
    "Nilai rata-rata, median, dan standar deviasi menunjukkan variasi harga yang signifikan, "
    "menunjukkan adanya perbedaan harga yang besar antar perjalanan taxi.") 

    #8. Korelasi Antara Fitur Numerik
    st.subheader('Korelasi Antara Fitur Numerik')
    corr = df[['Trip_Price', 'Trip_Distance_km', 'Trip_Duration_Minutes', 'Passenger_Count']].corr()
    fig7 = px.imshow(corr, text_auto=True, title='Matriks Korelasi Antara Fitur Numerik')
    st.plotly_chart(fig7)
    st.write(
    "Matriks korelasi menunjukkan hubungan antara fitur numerik dalam dataset. " )
    st.write(
    "Terlihat bahwa jarak perjalanan dan durasi perjalanan memiliki korelasi positif yang kuat "
    "dengan harga taxi, yang sesuai dengan ekspektasi bahwa perjalanan yang lebih jauh dan "
    "lebih lama cenderung menghasilkan harga yang lebih tinggi.")   

    