import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

def visualisasi():
    # =======================
    # STYLE
    # =======================
    st.markdown("""
        <style>
        .info-box {
            background:#f6f9fc;
            padding:1.3rem 1.6rem;
            border-radius:14px;
            border-left:5px solid #1e5f74;
            font-size:0.95rem;
            margin-bottom:1.8rem;
        }
        .interp-box {
            background:#ffffff;
            padding:1.4rem;
            border-radius:16px;
            box-shadow:0 8px 22px rgba(0,0,0,0.08);
            font-size:0.95rem;
            margin-top:0.8rem;
            margin-bottom:1.8rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # =======================
    # DESKRIPSI HALAMAN
    # =======================
    st.markdown("""
    <div class="info-box">
        Halaman ini menyajikan visualisasi interaktif untuk mengeksplorasi
        pola, tren, dan hubungan antar indikator perubahan iklim global.
        Analisis dilakukan secara lintas negara dan waktu untuk mendukung
        interpretasi berbasis data.
    </div>
    """, unsafe_allow_html=True)

    # ================= LOAD DATA =================
    df = pd.read_csv("climate_change_dataset.csv")

    # ================= METRIC =================
    avg_temp = df['Avg Temperature (°C)'].mean()
    avg_co2 = df['CO2 Emissions (Tons/Capita)'].mean()
    avg_sea = df['Sea Level Rise (mm)'].mean()
    avg_extreme = df['Extreme Weather Events'].mean()

    st.markdown("### 🌐 Ringkasan Indikator Global")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌡️ Suhu Rata-rata (°C)", f"{avg_temp:.2f}")
    col2.metric("🏭 CO₂ per Kapita", f"{avg_co2:.2f}")
    col3.metric("🌊 Kenaikan Laut (mm)", f"{avg_sea:.2f}")
    col4.metric("⛈️ Cuaca Ekstrem", f"{avg_extreme:.1f}")

    st.markdown("""
    <div class="interp-box">
        Indikator ini merepresentasikan kondisi rata-rata global.
        Nilai digunakan sebagai baseline untuk membandingkan dinamika
        perubahan iklim antar negara.
    </div>
    """, unsafe_allow_html=True)

    # ================= FILTER =================
    st.markdown("### 🌍 Filter Negara")

    country_list = sorted(df['Country'].unique())
    country_list.insert(0, "ALL")

    selected_country = st.multiselect(
        "Pilih negara untuk dianalisis",
        country_list,
        default=["ALL"]
    )

    if "ALL" in selected_country or not selected_country:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Country'].isin(selected_country)]

    # ================= LINE CHART =================
    st.markdown("### 📈 Tren Suhu Rata-rata")

    line_temp = alt.Chart(filtered_df).mark_line(point=True).encode(
        x=alt.X('Year:O', title='Tahun'),
        y=alt.Y('Avg Temperature (°C):Q', title='Suhu Rata-rata (°C)'),
        color='Country:N',
        tooltip=['Country', 'Year', 'Avg Temperature (°C)']
    ).properties(height=360)

    st.altair_chart(line_temp, use_container_width=True)

    st.markdown("""
    <div class="interp-box">
        Tren kenaikan suhu yang konsisten mengindikasikan pemanasan global.
        Variasi antar negara dipengaruhi oleh faktor geografis dan aktivitas manusia.
    </div>
    """, unsafe_allow_html=True)

    # ================= BAR CHART =================
    st.markdown("### 🏭 Emisi CO₂ Rata-rata per Negara")

    co2_bar = alt.Chart(
        filtered_df.groupby('Country', as_index=False)['CO2 Emissions (Tons/Capita)'].mean()
    ).mark_bar().encode(
        x=alt.X('CO2 Emissions (Tons/Capita):Q', title='CO₂ (Ton/Kapita)'),
        y=alt.Y('Country:N', sort='-x'),
        color=alt.Color('CO2 Emissions (Tons/Capita):Q', scale=alt.Scale(scheme='reds')),
        tooltip=['Country', 'CO2 Emissions (Tons/Capita)']
    ).properties(height=420)

    st.altair_chart(co2_bar, use_container_width=True)

    st.markdown("""
    <div class="interp-box">
        Negara dengan emisi CO₂ tinggi umumnya memiliki ketergantungan
        besar terhadap energi fosil dan aktivitas industri intensif.
    </div>
    """, unsafe_allow_html=True)

    # ================= SCATTER =================
    st.markdown("### 🌡️ Hubungan Suhu dan Emisi CO₂")

    scatter = alt.Chart(filtered_df).mark_circle(size=90).encode(
        x='CO2 Emissions (Tons/Capita):Q',
        y='Avg Temperature (°C):Q',
        color=alt.Color('Extreme Weather Events:Q', scale=alt.Scale(scheme='orangered')),
        tooltip=[
            'Country',
            'Avg Temperature (°C)',
            'CO2 Emissions (Tons/Capita)',
            'Extreme Weather Events'
        ]
    ).interactive().properties(height=360)

    st.altair_chart(scatter, use_container_width=True)

    st.markdown("""
    <div class="interp-box">
        Hubungan positif antara emisi karbon dan suhu menunjukkan
        kontribusi aktivitas manusia terhadap peningkatan suhu global.
    </div>
    """, unsafe_allow_html=True)

    # ================= BUBBLE =================
    st.markdown("### 🌱 Energi Terbarukan dan Emisi CO₂")

    bubble = alt.Chart(filtered_df).mark_circle().encode(
        x='Renewable Energy (%):Q',
        y='CO2 Emissions (Tons/Capita):Q',
        size=alt.Size('Population:Q', scale=alt.Scale(range=[300, 3200])),
        color='Country:N',
        tooltip=[
            'Country',
            'Renewable Energy (%)',
            'CO2 Emissions (Tons/Capita)',
            'Population'
        ]
    ).interactive().properties(height=420)

    st.altair_chart(bubble, use_container_width=True)

    st.markdown("""
    <div class="interp-box">
        Pemanfaatan energi terbarukan yang lebih tinggi
        cenderung berkorelasi dengan emisi CO₂ yang lebih rendah,
        dengan pengaruh tambahan dari ukuran populasi.
    </div>
    """, unsafe_allow_html=True)

    # ================= HEATMAP =================
    st.markdown("### 🔥 Korelasi Variabel Iklim")

    corr_cols = [
        'Avg Temperature (°C)',
        'CO2 Emissions (Tons/Capita)',
        'Sea Level Rise (mm)',
        'Rainfall (mm)',
        'Renewable Energy (%)',
        'Extreme Weather Events',
        'Forest Area (%)'
    ]

    corr = filtered_df[corr_cols].corr()

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Korelasi Antar Variabel Perubahan Iklim")

    st.pyplot(fig)

    st.markdown("""
    <div class="interp-box">
        Heatmap ini menunjukkan kekuatan dan arah hubungan antar variabel iklim.
        Korelasi digunakan sebagai dasar eksplorasi lebih lanjut,
        bukan sebagai hubungan sebab akibat langsung.
    </div>
    """, unsafe_allow_html=True)
