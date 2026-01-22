import streamlit as st

# =====================================================
# MENU UTAMA
# =====================================================
def Tahapan_model():

    # =======================
    # HEADER UTAMA
    # =======================
    st.markdown("## 🧠 Tahapan Model Machine Learning")
    st.caption(
        "Penjelasan sistematis tahapan pembentukan model klastering "
        "untuk analisis risiko perubahan iklim berbasis data."
    )

    st.markdown("""
    <div style="
        background:#f6f9fc;
        padding:1.3rem 1.6rem;
        border-radius:14px;
        border-left:5px solid #1e5f74;
        font-size:0.95rem;
        margin-top:0.8rem;
        margin-bottom:1.8rem;
    ">
        Tahapan ini menjelaskan proses pembangunan model machine learning
        menggunakan pendekatan unsupervised learning. Fokus utama berada pada
        metode klastering K-Means yang digunakan untuk mengelompokkan wilayah
        berdasarkan kemiripan indikator iklim dan risiko lingkungan.
        Penjelasan disusun secara konseptual dan matematis agar mudah dipahami
        serta relevan untuk analisis akademik dan pengambilan keputusan berbasis data.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    Langkah_model_Klastering()


# =====================================================
# TAHAPAN MODEL KLASTERING
# =====================================================
def Langkah_model_Klastering():

    st.markdown("### 📊 Tahapan Model Klastering K-Means")

    st.markdown("""
    Pemilihan model klastering didasarkan pada evaluasi beberapa algoritma
    unsupervised learning yang umum digunakan dalam analisis data numerik.
    Evaluasi dilakukan untuk memastikan bahwa model yang dipilih mampu
    menghasilkan klaster yang stabil, terpisah dengan baik, dan mudah diinterpretasikan.
    """)

    st.markdown("""
    Berdasarkan hasil pengujian terhadap beberapa metode klastering,
    yaitu K-Means, Hierarchical Clustering, dan DBSCAN, diperoleh bahwa
    **K-Means Clustering** menunjukkan performa paling konsisten berdasarkan
    metrik evaluasi internal berikut:
    - Silhouette Score
    - Davies–Bouldin Index
    - Calinski–Harabasz Index

    Oleh karena itu, K-Means digunakan sebagai model utama dalam proses
    pengelompokan wilayah berdasarkan indikator risiko perubahan iklim.
    """)

    st.markdown("---")

    # =====================================================
    # 1️⃣ PENENTUAN JUMLAH KLASTER
    # =====================================================
    st.subheader("1️⃣ Penentuan Jumlah Klaster")

    st.markdown(r"""
    Penentuan jumlah klaster merupakan tahap awal yang sangat penting
    dalam algoritma K-Means. Nilai jumlah klaster menentukan bagaimana
    data akan dikelompokkan dan seberapa baik struktur alami data dapat direpresentasikan.

    Dalam penelitian ini, penentuan jumlah klaster dilakukan dengan
    mempertimbangkan keseimbangan antara kompleksitas model dan kualitas klaster.
    Beberapa pendekatan yang digunakan meliputi:
    - Elbow Method
    - Silhouette Score
    - Davies–Bouldin Index
    - Calinski–Harabasz Index
    """)

    st.markdown(r"""
    Salah satu ukuran yang digunakan adalah **Within-Cluster Sum of Squares (WCSS)**,
    yang didefinisikan sebagai:

    $$
    WCSS = \sum_{k=1}^{K} \sum_{\mathbf{x}_i \in C_k}
    \lVert \mathbf{x}_i - \boldsymbol{\mu}_k \rVert^2
    $$

    Nilai klaster optimal dipilih pada titik di mana penurunan WCSS
    mulai melambat dan diperkuat oleh hasil metrik evaluasi lainnya.
    """)

    # =====================================================
    # 2️⃣ INISIALISASI PUSAT KLASTER
    # =====================================================
    st.subheader("2️⃣ Inisialisasi Pusat Klaster")

    st.markdown(r"""
    Setelah jumlah klaster ditentukan, algoritma K-Means melakukan
    inisialisasi pusat klaster awal. Setiap pusat klaster direpresentasikan
    sebagai vektor dengan dimensi yang sama dengan data input.

    Inisialisasi yang baik berperan penting dalam mempercepat konvergensi
    dan menghindari solusi lokal yang kurang optimal.
    """)

    # =====================================================
    # 3️⃣ PERHITUNGAN JARAK
    # =====================================================
    st.subheader("3️⃣ Perhitungan Jarak Data ke Pusat Klaster")

    st.markdown(r"""
    Pada tahap ini, setiap observasi dihitung jaraknya terhadap seluruh
    pusat klaster menggunakan jarak Euclidean. Jarak ini mencerminkan
    tingkat kemiripan antara suatu wilayah dan karakteristik klaster.

    Rumus jarak Euclidean dinyatakan sebagai:

    $$
    d_{ik} = \lVert \mathbf{x}_i - \boldsymbol{\mu}_k \rVert
    $$
    """)

    # =====================================================
    # 4️⃣ PENENTUAN KEANGGOTAAN KLASTER
    # =====================================================
    st.subheader("4️⃣ Penentuan Keanggotaan Klaster")

    st.markdown(r"""
    Setiap data kemudian ditempatkan ke dalam klaster dengan jarak terdekat
    terhadap pusat klaster. Proses ini memastikan bahwa setiap observasi
    hanya menjadi anggota satu klaster.

    Secara matematis, keanggotaan klaster ditentukan dengan:

    $$
    \text{Cluster}(\mathbf{x}_i) =
    \arg \min_{k} \, d_{ik}
    $$
    """)

    # =====================================================
    # 5️⃣ PEMBARUAN PUSAT KLASTER
    # =====================================================
    st.subheader("5️⃣ Pembaruan Pusat Klaster")

    st.markdown(r"""
    Setelah seluruh data dialokasikan ke klaster masing-masing,
    pusat klaster diperbarui dengan menghitung rata-rata seluruh
    anggota klaster.

    Proses ini bertujuan agar pusat klaster merepresentasikan
    karakteristik rata-rata dari data dalam klaster tersebut.
    """)

    st.markdown(r"""
    Pembaruan pusat klaster dinyatakan sebagai:

    $$
    \boldsymbol{\mu}_k =
    \frac{1}{|C_k|}
    \sum_{\mathbf{x}_i \in C_k} \mathbf{x}_i
    $$
    """)

    # =====================================================
    # 6️⃣ ITERASI HINGGA KONVERGEN
    # =====================================================
    st.subheader("6️⃣ Iterasi Hingga Konvergen")

    st.markdown(r"""
    Langkah penugasan klaster dan pembaruan pusat klaster dilakukan
    secara berulang hingga algoritma mencapai kondisi stabil.
    Proses iterasi dihentikan ketika tidak terjadi perubahan signifikan
    pada keanggotaan klaster atau pusat klaster.

    Pada tahap ini, model dianggap telah mencapai kondisi konvergen.
    """)

    # =====================================================
    # 7️⃣ HASIL AKHIR KLASTERING
    # =====================================================
    st.subheader("7️⃣ Hasil Akhir Klastering")

    st.markdown("""
    Hasil akhir dari model klastering K-Means berupa:
    - Label klaster untuk setiap wilayah atau observasi
    - Nilai centroid sebagai representasi karakteristik klaster
    - Pola umum indikator iklim dan risiko lingkungan pada setiap klaster

    Informasi ini digunakan sebagai dasar analisis lanjutan,
    seperti identifikasi tingkat kerentanan wilayah, perbandingan antar klaster,
    serta dukungan pengambilan keputusan berbasis data dalam konteks
    mitigasi dan adaptasi perubahan iklim.
    """)

    st.success("Tahapan model klastering K-Means telah dijelaskan secara sistematis dan lengkap.")
