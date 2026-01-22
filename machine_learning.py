import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.cluster import (
    KMeans, AgglomerativeClustering, DBSCAN, SpectralClustering
)
from sklearn.mixture import GaussianMixture

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

# ======================================================
# MAIN FUNCTION
# ======================================================
def machine_learning2():

    # =======================
    # HEADER UTAMA
    # =======================
    st.markdown("## 🤖 Analisis Machine Learning")
    st.caption(
        "Eksplorasi pola tersembunyi data iklim menggunakan pendekatan "
        "unsupervised learning dan evaluasi klaster berbasis metrik statistik."
    )

    st.markdown("""
    <div style="
        background:#f6f9fc;
        padding:1.2rem 1.6rem;
        border-radius:14px;
        border-left:5px solid #1e5f74;
        font-size:0.95rem;
        margin-top:0.8rem;
        margin-bottom:1.8rem;
    ">
        Halaman ini menyajikan analisis machine learning tanpa label (unsupervised)
        untuk mengidentifikasi struktur alami dalam data iklim global.
        Pendekatan klastering digunakan untuk mengelompokkan observasi berdasarkan
        kemiripan karakteristik numerik, sehingga mendukung eksplorasi risiko
        lingkungan dan segmentasi wilayah berbasis data.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ======================================================
    # UPLOAD DATA
    # ======================================================
    uploaded_file = st.file_uploader("📤 Upload Dataset (CSV)", type=["csv"])

    if uploaded_file is None:
        st.info("Silakan unggah file CSV untuk memulai analisis machine learning.")
        return

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Pratinjau Dataset")
    st.dataframe(df.head(), use_container_width=True)

    numeric_df = df.select_dtypes(include=np.number).dropna()

    if numeric_df.shape[1] < 2:
        st.error("Dataset harus memiliki minimal dua variabel numerik.")
        return

    # ======================================================
    # SIDEBAR SETTINGS
    # ======================================================
    st.sidebar.header("⚙️ Pengaturan Model")

    model_name = st.sidebar.selectbox(
        "Pilih Algoritma Klastering",
        ["KMeans", "Agglomerative", "Gaussian Mixture", "Spectral Clustering", "DBSCAN"]
    )

    max_k = st.sidebar.slider(
        "Maksimum Jumlah Klaster (Auto-search)",
        2, 10, 6
    )

    # ======================================================
    # SCALING
    # ======================================================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_df)

    # ======================================================
    # AUTO SEARCH k TERBAIK
    # ======================================================
    def auto_search_k(X, max_k):
        records = []
        for k in range(2, max_k + 1):
            labels = KMeans(n_clusters=k, random_state=42).fit_predict(X)
            score = silhouette_score(X, labels)
            records.append((k, score))
        return pd.DataFrame(records, columns=["k", "Silhouette Score"])

    auto_k_df = auto_search_k(X_scaled, max_k)
    best_k = auto_k_df.loc[auto_k_df["Silhouette Score"].idxmax(), "k"]

    st.sidebar.success(f"Jumlah klaster optimal: {best_k}")

    st.subheader("📊 Pencarian Jumlah Klaster Optimal")
    st.dataframe(auto_k_df, use_container_width=True)

    # ======================================================
    # TRAIN MODEL
    # ======================================================
    if model_name == "KMeans":
        model = KMeans(n_clusters=best_k, random_state=42)
        labels = model.fit_predict(X_scaled)
        centroids = model.cluster_centers_

    elif model_name == "Agglomerative":
        model = AgglomerativeClustering(n_clusters=best_k)
        labels = model.fit_predict(X_scaled)
        centroids = None

    elif model_name == "Gaussian Mixture":
        model = GaussianMixture(n_components=best_k, random_state=42)
        labels = model.fit_predict(X_scaled)
        centroids = model.means_

    elif model_name == "Spectral Clustering":
        model = SpectralClustering(n_clusters=best_k, random_state=42)
        labels = model.fit_predict(X_scaled)
        centroids = None

    elif model_name == "DBSCAN":
        model = DBSCAN(eps=0.7, min_samples=5)
        labels = model.fit_predict(X_scaled)
        centroids = None

    # ======================================================
    # EVALUASI MODEL
    # ======================================================
    if len(set(labels)) > 1:
        sil = silhouette_score(X_scaled, labels)
        dbi = davies_bouldin_score(X_scaled, labels)
        chi = calinski_harabasz_score(X_scaled, labels)
    else:
        sil, dbi, chi = np.nan, np.nan, np.nan

    metric_df = pd.DataFrame({
        "Model": [model_name],
        "Silhouette Score": [sil],
        "Davies-Bouldin Index": [dbi],
        "Calinski-Harabasz Index": [chi]
    })

    st.subheader("📈 Evaluasi Kualitas Klaster")
    st.dataframe(metric_df, use_container_width=True)

    # ======================================================
    # PCA VISUALISASI
    # ======================================================
    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame({
        "PC1": pca_data[:, 0],
        "PC2": pca_data[:, 1],
        "Cluster": labels.astype(str)
    })

    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color="Cluster",
        template="plotly_white",
        title=f"Visualisasi PCA – {model_name}"
    )

    st.subheader("📉 Proyeksi Data Menggunakan PCA")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    Visualisasi PCA digunakan untuk mereduksi dimensi data dan menampilkan
    distribusi klaster dalam ruang dua dimensi. Pemisahan klaster yang jelas
    menunjukkan tingkat homogenitas internal dan perbedaan antar kelompok data.
    """)

    # ======================================================
    # NARASI KLASTER
    # ======================================================
    st.subheader("🧾 Interpretasi Hasil Klaster")

    df_clustered = numeric_df.copy()
    df_clustered["Cluster"] = labels

    for c in sorted(df_clustered["Cluster"].unique()):
        data_c = df_clustered[df_clustered["Cluster"] == c]
        st.markdown(f"""
        **Klaster {c}**  
        Jumlah observasi: **{len(data_c)}**  
        Klaster ini merepresentasikan kelompok data dengan karakteristik numerik
        yang relatif serupa dan dapat digunakan sebagai dasar analisis lanjutan
        terkait pola iklim dan risiko lingkungan.
        """)

    # ======================================================
    # CENTROID
    # ======================================================
    if centroids is not None:
        st.subheader("🎯 Nilai Centroid Klaster")
        centroid_df = pd.DataFrame(centroids, columns=numeric_df.columns)
        centroid_df["Cluster"] = centroid_df.index
        st.dataframe(centroid_df, use_container_width=True)

    # ======================================================
    # SIMPAN MODEL
    # ======================================================
    st.subheader("💾 Penyimpanan Model")

    model_package = {
        "model_name": model_name,
        "model": model,
        "scaler": scaler,
        "pca": pca,
        "best_k": best_k,
        "features": list(numeric_df.columns)
    }

    model_filename = "clustering_model.pkl"

    with open(model_filename, "wb") as f:
        pickle.dump(model_package, f)

    st.success("Model berhasil disimpan dalam format .pkl")

    # ======================================================
    # EXPORT CSV
    # ======================================================
    st.subheader("📥 Ekspor Hasil")

    export_df = df.copy()
    export_df["Cluster"] = labels

    st.download_button(
        "⬇️ Unduh Data Hasil Klaster",
        export_df.to_csv(index=False),
        file_name="hasil_clustering.csv"
    )

    if centroids is not None:
        st.download_button(
            "⬇️ Unduh Data Centroid",
            centroid_df.to_csv(index=False),
            file_name="centroid_clustering.csv"
        )
