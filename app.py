import streamlit as st

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Climate Change Analytics Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ======================================================
# HEADER (SIMPLE & RINGKAS)
# ======================================================
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0;'>🌍 Climate Change Analytics Dashboard</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:gray; margin-top:4px;'>"
    "Klastering Kerentanan Wilayah Berdasarkan Indikator Perubahan Iklim"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ======================================================
# IDENTITAS AKADEMIK (COMPACT, TANPA BACKGROUND)
# ======================================================
col1, col2, col3 = st.columns([1.2, 1.6, 1.2])

with col2:
    st.markdown(
        "<p style='text-align:center; font-size:14px; line-height:1.5;'>"
        "<b>Dosen Pengampu:</b> Bapak Saeful Amri., S.Kom., M.Kom<br>"
        "<b>Mahasiswa:</b> Muhammad Ilham Nurul Azka | <b>NIM:</b> B2D023007<br>"
        "<b>Prodi:</b> S1 Sains Data – Universitas Muhammadiyah Semarang<br>"
        "<span style='color:gray;'>Semarang, 21 Desember 2026</span>"
        "</p>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ======================================================
# TAB NAVIGATION (LANGSUNG TERLIHAT)
# ======================================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📘 Dataset",
    "📊 Visualisasi",
    "🤖 Machine Learning",
    "🧠 Alur Model",
    "🔮 Prediksi",
    "📬 Kontak"
])

# ======================================================
# TAB 1
# ======================================================
with tab1:
    st.subheader("📘 Dataset Perubahan Iklim")
    st.caption("Deskripsi sumber data dan variabel iklim")
    import about_dataset
    about_dataset.about_dataset()

# ======================================================
# TAB 2
# ======================================================
with tab2:
    st.subheader("📊 Visualisasi Data Iklim")
    st.caption("Eksplorasi pola dan tren indikator iklim")
    import visualisasi
    visualisasi.visualisasi()

# ======================================================
# TAB 3
# ======================================================
with tab3:
    import machine_learning
    machine_learning.machine_learning2()

# ======================================================
# TAB 4
# ======================================================
with tab4:
    import tahapan_model
    tahapan_model.Tahapan_model()

# ======================================================
# TAB 5
# ======================================================
with tab5:
    import prediksi
    prediksi.app_prediksi_klaster_wilayah()

# ======================================================
# TAB 6
# ======================================================
with tab6:
    import countact
    countact.contact_tab()

# ======================================================
# FOOTER (KECIL & RAPI)
# ======================================================
st.markdown("---")
st.caption("© 2025 Climate Change Analytics Dashboard | Python & Streamlit")
