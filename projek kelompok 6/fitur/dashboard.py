import streamlit as st
from PIL import Image

#Css Streamlit
st.markdown(
    """
    <style>
    .stApp{
        background-color: #151515;
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

st.title("dashboard kelompok")
col1, col2, col3 = st.columns(3)
nama = ["adam.jpg", "auliya.jpg", "syamil.jpg"]
bio = ["Adam Al Muharrom Sholeh", "Aulya Reski", "Muhammad Akhdan Syamil"]
for col, img, cap in zip([col1, col2, col3], nama, bio):
    with col:
        st.image(Image.open(img), caption=cap, use_container_width=True)

# Menampilkan riwayat parkir
st.markdown("---")
st.header("Riwayat Parkir")
if st.session_state.riwayat:
    for i, entry in enumerate((st.session_state.riwayat), 1):
        st.markdown(f"#### Parkir No.{i}")
        st.write(f"**Jenis Kendaraan:** {entry['jenis']}")
        st.write(f"**Waktu Masuk:** {entry['masuk'].strftime('%d-%m-%Y %H:%M:%S')}")
        st.write(f"**Waktu Keluar:** {entry['keluar'].strftime('%d-%m-%Y %H:%M:%S')}")
        st.write(f"**Durasi Parkir:** {entry['durasi']} jam")
        st.write(f"**Total Biaya:** Rp {entry['biaya']:,}")
        st.markdown("---")
else:
    st.info("Belum ada riwayat parkir.")

# Footer aplikasi
st.caption("Dibuat Oleh Kelompok 6")