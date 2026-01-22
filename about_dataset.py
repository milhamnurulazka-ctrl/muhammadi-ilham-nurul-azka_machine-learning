import streamlit as st

def about_dataset():
    # =======================
    # CUSTOM CSS (SAFE)
    # =======================
    st.markdown("""
        <style>
        .hero-card {
            background: linear-gradient(135deg, #0b1f33, #133b5c, #1e5f74);
            padding: 2.2rem;
            border-radius: 20px;
            color: white;
            box-shadow: 0 12px 28px rgba(0,0,0,0.25);
        }
        .hero-card h3 {
            margin-top: 0;
            color: #ffffff;
        }
        .dataset-link {
            background: #f5f7fa;
            padding: 1rem 1.5rem;
            border-radius: 14px;
            border-left: 6px solid #1e5f74;
            font-size: 0.95rem;
        }
        .section-box {
            background: #ffffff;
            padding: 1.7rem;
            border-radius: 18px;
            box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        }
        .section-box h4 {
            margin-top: 0;
        }
        .ref-box {
            background: #f9fafb;
            padding: 1.4rem;
            border-radius: 14px;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # =======================
    # HEADER
    # =======================
    st.markdown("## 🌍 About Dataset")

    st.markdown("""
    <div class="dataset-link">
        🔗 <b>Data Source</b><br>
        Climate Change Dataset (Kaggle)  
        <a href="https://www.kaggle.com/datasets/bhadramohit/climate-change-dataset" target="_blank">
        https://www.kaggle.com/datasets/bhadramohit/climate-change-dataset
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📘 Dataset Perubahan Iklim")
    st.markdown("---")

    # =======================
    # HERO SECTION
    # =======================
    col1, col2 = st.columns([6, 8], gap="large")

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="hero-card">
            <h3>Climate Change and Environmental Risk Dataset</h3>
            <p>
            Dataset ini menyajikan data lingkungan global yang digunakan untuk
            menganalisis dinamika perubahan iklim serta risiko lingkungan
            yang dihadapi berbagai negara.
            </p>
            <p>
            Data disusun secara longitudinal dan lintas negara sehingga
            memungkinkan analisis tren jangka panjang, perbandingan regional,
            serta pengelompokan tingkat kerentanan iklim.
            </p>
            <p>
            Dataset ini menjadi dasar pengembangan Climate Change Analytics Dashboard
            yang berfokus pada analisis berbasis data dan visualisasi interaktif.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # =======================
    # DATASET DESCRIPTION
    # =======================
    st.markdown("## 📌 Deskripsi Dataset")

    st.markdown("""
    <div class="section-box">
        <p>
        Dataset perubahan iklim ini mengintegrasikan berbagai indikator lingkungan
        yang merepresentasikan kondisi fisik iklim, tekanan aktivitas manusia,
        serta respons keberlanjutan lingkungan.
        </p>
        <p>
        Setiap observasi menggambarkan kondisi suatu negara pada tahun tertentu.
        Pendekatan ini memungkinkan analisis temporal, identifikasi pola global,
        dan evaluasi perbedaan risiko antar wilayah.
        </p>
        <p>
        Dataset dirancang agar kompatibel dengan analisis statistik,
        exploratory data analysis, serta metode machine learning tanpa supervisi.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # =======================
    # VARIABLES
    # =======================
    st.markdown("## 📂 Variabel Dataset")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="section-box">
            <h4>Indikator Waktu dan Iklim</h4>
            <p><b>Year</b> menunjukkan tahun pengamatan.</p>
            <p><b>Country</b> merepresentasikan unit analisis negara.</p>
            <p><b>Avg Temperature (°C)</b> menggambarkan tren pemanasan global.</p>
            <p><b>Rainfall (mm)</b> merefleksikan perubahan pola curah hujan.</p>
            <p><b>Sea Level Rise (mm)</b> menunjukkan dampak pemanasan global
            terhadap kenaikan muka laut.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-box">
            <h4>Tekanan Lingkungan dan Keberlanjutan</h4>
            <p><b>CO₂ Emissions (Tons/Capita)</b> mencerminkan aktivitas industri
            dan konsumsi energi.</p>
            <p><b>Extreme Weather Events</b> merepresentasikan intensitas
            kejadian cuaca ekstrem.</p>
            <p><b>Population</b> menunjukkan tekanan demografis.</p>
            <p><b>Renewable Energy (%)</b> mengukur transisi energi berkelanjutan.</p>
            <p><b>Forest Area (%)</b> merepresentasikan kondisi ekosistem darat.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # =======================
    # ANALYTICAL PURPOSE
    # =======================
    st.markdown("## 🎯 Tujuan Analisis")

    st.markdown("""
    <div class="section-box">
        <p>
        Analisis dataset ini bertujuan untuk mengidentifikasi pola perubahan iklim
        global serta mengukur tingkat risiko lingkungan di berbagai negara.
        </p>
        <p>
        Dataset ini mendukung analisis hubungan antara emisi karbon,
        peningkatan suhu, dan frekuensi kejadian cuaca ekstrem.
        </p>
        <p>
        Metode analisis yang digunakan meliputi exploratory data analysis,
        clustering risiko iklim, dan visual analytics berbasis dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =======================
    # REFERENCES
    # =======================
    st.markdown("## 📚 Referensi")

    st.markdown("""
    <div class="ref-box">
        <p>
        1. IPCC. (2023). <i>Climate Change 2023: Synthesis Report</i>.
        Intergovernmental Panel on Climate Change.
        </p>
        <p>
        2. World Bank. (2022). <i>Climate Risk Country Profiles</i>.
        </p>
        <p>
        3. Kaggle. (2024). <i>Climate Change Dataset</i>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Dataset ini digunakan sebagai dasar analisis akademik dan eksploratif "
        "dalam pengembangan dashboard perubahan iklim berbasis data."
    )
