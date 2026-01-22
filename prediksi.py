import streamlit as st

# ======================================================
# PREDIKSI KLASTERING (SINKRON DENGAN MODEL .PKL)
# ======================================================
def app_prediksi_klaster_wilayah():

    import numpy as np
    import pandas as pd
    import pickle
    from sklearn.metrics import pairwise_distances

    st.title("🌍 Prediksi Klaster Wilayah")
    st.caption("Model Clustering Tersimpan | Prediksi Data Baru")

    # ======================================================
    # LOAD MODEL
    # ======================================================
    try:
        with open("clustering_model.pkl", "rb") as f:
            bundle = pickle.load(f)
    except FileNotFoundError:
        st.error("❌ File clustering_model.pkl tidak ditemukan.")
        return

    model = bundle["model"]
    scaler = bundle["scaler"]
    features = bundle["features"]
    model_name = bundle["model_name"]

    st.success(f"✅ Model berhasil dimuat ({model_name})")

    # ======================================================
    # INPUT DATA
    # ======================================================
    st.subheader("📥 Input Data Baru")

    input_data = {}
    cols = st.columns(2)

    for i, ftr in enumerate(features):
        input_data[ftr] = cols[i % 2].number_input(
            ftr,
            value=0.0,
            step=0.1
        )

    input_df = pd.DataFrame([input_data])

    # ======================================================
    # PREDIKSI
    # ======================================================
    if st.button("🔮 Prediksi Klaster"):

        X_scaled = scaler.transform(input_df)

        # ===============================
        # CASE 1: MODEL SUPPORT PREDICT
        # ===============================
        if hasattr(model, "predict"):
            cluster = int(model.predict(X_scaled)[0])

        # ===============================
        # CASE 2: MODEL TANPA PREDICT
        # ===============================
        else:
            if hasattr(model, "cluster_centers_"):
                centroids = model.cluster_centers_
            elif hasattr(model, "means_"):
                centroids = model.means_
            else:
                st.error("❌ Model tidak mendukung prediksi data baru.")
                return

            distances = pairwise_distances(X_scaled, centroids)
            cluster = int(np.argmin(distances))

        # ======================================================
        # OUTPUT
        # ======================================================
        st.subheader("📊 Hasil Prediksi")
        st.metric("Klaster Terpilih", f"Klaster {cluster}")

        # ======================================================
        # INTERPRETASI BERBASIS CENTROID
        # ======================================================
        if hasattr(model, "cluster_centers_"):
            centers = model.cluster_centers_
        elif hasattr(model, "means_"):
            centers = model.means_
        else:
            centers = None

        if centers is not None:
            centers_df = pd.DataFrame(centers, columns=features)
            global_mean = centers_df.mean()
            row = centers_df.loc[cluster]

            st.subheader("📌 Karakteristik Klaster")

            interpretasi = []

            for ftr in features:
                if row[ftr] > global_mean[ftr]:
                    interpretasi.append(f"- **{ftr}** cenderung **lebih tinggi**")
                else:
                    interpretasi.append(f"- **{ftr}** cenderung **lebih rendah**")

            st.markdown("\n".join(interpretasi))

            st.subheader("📊 Nilai Centroid Klaster")
            st.dataframe(row.to_frame("Rata-rata"))

        # ======================================================
        # NARASI OTOMATIS (AMAN & UMUM)
        # ======================================================
        st.subheader("🧾 Ringkasan Interpretasi")

        if cluster == 0:
            label = "Klaster Risiko Rendah"
            deskripsi = "Wilayah dengan indikator relatif stabil dan terkendali."
        elif cluster == 1:
            label = "Klaster Risiko Menengah"
            deskripsi = "Wilayah dengan kondisi transisi, perlu perhatian moderat."
        else:
            label = "Klaster Risiko Tinggi"
            deskripsi = "Wilayah dengan indikator dominan tinggi, perlu prioritas penanganan."

        st.markdown(f"### 🏷️ {label}")
        st.write(deskripsi)

        # ======================================================
        # REKOMENDASI UMUM
        # ======================================================
        st.subheader("🧭 Rekomendasi")

        rekomendasi = [
            "Lakukan pemantauan berkala terhadap indikator utama",
            "Gunakan hasil klaster sebagai dasar perencanaan kebijakan",
            "Integrasikan dengan data spasial untuk analisis lanjutan"
        ]

        for i, r in enumerate(rekomendasi, 1):
            st.markdown(f"**{i}.** {r}")
