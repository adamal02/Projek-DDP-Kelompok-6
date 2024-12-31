import streamlit as st
from datetime import datetime, timedelta

#Css Streamlit
st.markdown(
    """
    <style>
    .stApp{
        background-color: #171717;
    }
    
    [data-testid="stSidebar"]{
        background-color: #A91D3A;
        color: #EEEEEE;
    }
    
    [data-testid="stSidebar"] * {
        color: #EEEEEE !important;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html = True 
)

# fungsi untuk menghitung biaya parkir
def hitung_biaya(jenis, jam):
    if jenis == "Mobil":
        biaya = jam * 3000
    elif jenis == "Motor":
        biaya = jam * 2000
    elif jenis == "Mini Bus":
        biaya = jam * 5000
    else:
        st.error("Jenis kendaraan tidak valid.")
        return None, None, None
    
    waktu_masuk = datetime.now()
    waktu_keluar = waktu_masuk + timedelta(hours=jam)

    return biaya, waktu_masuk, waktu_keluar

# judul aplikasi
title=("Aplikasi Parkir")

# sidebar untuk input pengguna
st.sidebar.header("Apa Kendaraan kamu")
jenis_kendaraan = st.sidebar.selectbox(
    "Pilih Jenis Kendaraan:", ["Mobil", "Motor", "Mini Bus"]
)
durasi = st.sidebar.text_input("Masukkan Durasi Parkir (jam):")

# tampilan halaman berdasarkan jenis kendaraan
if jenis_kendaraan == "Mobil":
    st.title("🚗 Halaman Parkir Mobil")
    
elif jenis_kendaraan == "Motor":
    st.title("🏍️ Halaman Parkir Motor")
    
elif jenis_kendaraan == "Mini Bus":
    st.title("🚌 Halaman Parkir Mini Bus")

# tombol hitung di sidebar
if st.sidebar.button("Hitung Biaya"):
    try:
        jam = int(durasi)
        biaya, waktu_masuk, waktu_keluar = hitung_biaya(jenis_kendaraan, jam)

        if biaya is not None:
            # menambahkan hasil ke riwayat parkir
            st.session_state.riwayat.append({
                "jenis": jenis_kendaraan,
                "masuk": waktu_masuk,
                "keluar": waktu_keluar,
                "durasi": jam,
                "biaya": biaya
            })

            # menampilkan hasil
            st.success("Hasil Perhitungan Biaya Parkir")
            st.write(f"**Kendaraan :** {jenis_kendaraan}")
            st.write(f"**Waktu Masuk :** {waktu_masuk.strftime('%d-%m-%Y %H:%M:%S')}")
            st.write(f"**Waktu Keluar :** {waktu_keluar.strftime('%d-%m-%Y %H:%M:%S')}")
            st.write(f"**Durasi Parkir :** {jam} jam")
            st.markdown(f"### Total Biaya : **Rp {biaya:,}**", unsafe_allow_html=True)

    except ValueError:
        st.sidebar.error("Durasi yang dimasukkan harus berupa angka")