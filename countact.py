import streamlit as st

def contact_tab():

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown(
        "<h1 style='text-align:center;'>📬 Hubungi Saya</h1>",
        unsafe_allow_html=True
    )
    st.caption("Informasi kontak, media sosial, dan form feedback terkait dashboard")
    st.markdown("---")

    # =====================================================
    # IDENTITAS PENGEMBANG
    # =====================================================
    st.subheader("👨‍💻 Identitas Pengembang")

    col1, col2 = st.columns([1.2, 4])

    with col1:
        st.image(
            "https://i.pinimg.com/originals/05/5a/91/055a91979264664a1ee12b9453610d82.png",
            width=110
        )

    with col2:
        st.markdown("""
        **Muhammad Ilham Nurul Azka**

        Universitas : Universitas Muhammadiyah Semarang  
        Program Studi : S1 Sains Data  
        NIM : B2D023007  
        Dosen Pembimbing : Saeful Amri, S.Kom., M.Kom
        """)

    st.markdown("---")

    # =====================================================
    # MEDIA SOSIAL & KONTAK (FIX EMAIL)
    # =====================================================
    st.subheader("🌐 Media Sosial & Kontak")
    st.caption("Klik ikon di bawah untuk terhubung langsung")

    social_links = {
        "Email": (
            "https://img.icons8.com/fluency/48/gmail-new.png",
            "mailto:milhamnurulazka@gmail.com"
        ),
        "GitHub": (
            "https://img.icons8.com/ios-glyphs/48/github.png",
            "https://github.com/milhamnurulazka-ctrl"
        ),
        "WhatsApp": (
            "https://img.icons8.com/fluency/48/whatsapp.png",
            "https://wa.me/6285878599921"
        ),
        "Instagram": (
            "https://img.icons8.com/fluency/48/instagram-new.png",
            "https://www.instagram.com/ilhnrlazk"
        ),
    }

    cols = st.columns(len(social_links))

    for col, (name, (icon, link)) in zip(cols, social_links.items()):
        with col:
            st.markdown(
                f"""
                <div style="text-align:center;">
                    <a href="{link}">
                        <img src="{icon}" width="42">
                    </a>
                    <div style="margin-top:6px;">{name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    # =====================================================
    # FORM FEEDBACK
    # =====================================================
    st.subheader("✉️ Kirim Pesan / Feedback")
    st.info("Gunakan form ini untuk mengirim pertanyaan atau saran terkait dashboard")

    with st.form("contact_form", clear_on_submit=True):
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        pesan = st.text_area("Pesan / Feedback")
        kirim = st.form_submit_button("Kirim")

        if kirim:
            if nama and email and pesan:
                st.success("Terima kasih, pesan Anda berhasil dikirim.")
            else:
                st.warning("Mohon lengkapi seluruh kolom.")

    st.markdown("---")

    # =====================================================
    # FOOTNOTE
    # =====================================================
    st.caption(
        "Dashboard ini dibuat untuk keperluan akademik (UAS Machine Learning) "
        "dan digunakan untuk tujuan edukatif."
    )
