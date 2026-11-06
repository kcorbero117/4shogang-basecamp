import streamlit as st

# ==========================================
# Halaman awal (LOGIN)

# KEPALA PROYEK
st.set_page_config(page_title="4SHOGANG")

# MEMORI WEB
if 'izin_masuk' not in st.session_state:
    st.session_state['izin_masuk'] = False
if 'kunci_m1' not in st.session_state: st.session_state['kunci_m1'] = False
if 'kunci_m2' not in st.session_state: st.session_state['kunci_m2'] = False
if 'kunci_m3' not in st.session_state: st.session_state['kunci_m3'] = False
if 'kunci_m4' not in st.session_state: st.session_state['kunci_m4'] = False

# WALLPAPER
if st.session_state['izin_masuk'] == False:
    kode_wallpaper = """ 
    <style>
    [data-testid="stAppViewContainer"] {
    background: #000000 !important; /* Mengubah layar jadi hitam pekat */
    }
    [data-testid="stHeader"] {
    background: rgba(0,0,0,0);
    }
    /* Memaksa judul dan teks biasa jadi warna putih */
    h1, p, label, .stMarkdown {
    color: #FFFFFF !important;
    }
    
    /* MENGUBAH WARNA TOMBOL */
    /* Warna kotak tombolnya jadi putih */
    div[data-testid="stButton"] button {
    background-color: #FFFFFF !important; /* Tombol jadi putih */
    border: none !important;
    }
    
    /* Warna teks di dalam tombol dipaksa jadi hitam */
    div[data-testid="stButton"] button p {
    color: #000000 !important;
    font-weight: bold !important;
    }
    
    /* Efek saat tombolnya ditunjuk mose (Hover) */
    div[data-testid="stButton] button:hover {
    background-color: #CCCCCC !important; /* Tombol agak meredup */
    color: #000000 !important;
    }

    /* 8. Agar teks di dalam kotak peringatan/error password salah jadi jelas dibaca */
    div[data-testid="stNotification"], div.stAlert {
        background-color: #f8d7da !important;
        border: 1px solid #f5c6cb !important;
    }
    div[data-testid="stNotification"] p, div.stAlert p {
        color: #721c24 !important;
        font-weight: bold !important;
    }

    </style>
    """
    st.markdown(kode_wallpaper, unsafe_allow_html=True)

    # S.W.I.S.H teaser
    st.video("https://youtu.be/7eWA-YKZoL8?si=dqY7eXXpeG2r-uCl", autoplay=True, muted=True, loop=True)

    # PASSWORD
    st.title("4SHOGANG Area 🐈‍⬛🌰🐘🐕")
    st.write("Access restricted, prove you're one of the broskis")

    # PASSWORD (Disensor jadi titik-titik)
    tebakan_pw = st.text_input("Sebutkan Password Rahasia (angka only):", type="password")
    if st.button("Go"):
        if tebakan_pw == "101126":
            st.session_state['izin_masuk'] = True
            st.rerun() # refresh web otomatis ke halaman utama
        elif tebakan_pw != "":
            st.error("Password salah, coba lagi (hint: tanggal cb)")

# ==========================================
# Halaman UTAMA

if st.session_state['izin_masuk'] == True:
    kode_utama_animasi = """
    <style>
    /* 1. Rumus Animasi untuk Barang-barangnya */
    @keyframes munculPelan {
        0% { opacity: 0; transform: scale(0.90); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    /* 2. Tembok/Background web LANGSUNG berubah jadi putih */
    [data-testid="stAppViewContainer"] {
        background: #FFFFFF !important;
    }
    
    /* 3. Terapkan animasi ke Logo, Teks, dan Tombol */
    [data-testid="stImage"],
    [data-testid="stMarkdownContainer"],
    [data-testid="stVerticalBlock"] div[data-testid="stButton"] {
        animation: munculPelan 4s ease-out forwards !important;
    }
    
    /* 4. Teks wajib hitam */
    h1, p, .stMarkdown {
        color: #000000 !important;
    }

    /* 5. Teks 'Password:' dan kotak brankas */
    .stTextInput label {
        color: #000000 !important;
        font-weight: bold !important;
    }
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #000000 !important;
    }

   /* 6. TOMBOL BUKA BRANKAS JADI TERANG & KONTRAS */
    div[data-testid="stButton"] button {
        background-color: #f0f2f6 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 1px solid #d0d0d0 !important;
        border-radius: 8px !important;
    }
    
    /* Efek pas tombolnya di-hover (disorot mouse) */
    div[data-testid="stButton"] button:hover {
        background-color: #e0e2e6 !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
    }

    /* 7. GARIS PEMISAH (---) JADI HITAM PEKAT */
    hr {
        border-color: #000000 !important;
        opacity: 1 !important;
    }

    </style>
    """
    st.markdown(kode_utama_animasi, unsafe_allow_html=True)

    st.set_page_config(page_title="4SHOGANG", layout="wide")

    # LOGO SWISH 
    kolom_kiri, kolom_tengah, kolom_kanan = st.columns([2.5, 1, 2.5])
    with kolom_tengah:
        st.image("Logo SWISH.jpeg", width=200)

    st.markdown("---") 

    # MEDSOS (LNGSHOT + us)
    col_ig, col_tt, col_wv, col_sp, col_yt, col_tg = st.columns(6)

    tombol_style = "display: block; text-align: center; background-color: #262730; color: white; padding: 10px; border-radius: 8px; text-decoration: none; font-weight: bold; border: 1px solid rgba(250, 250, 250, 0.2);"

    # --- 6 KOLOM MEDSOS (POSISI TENGAH & KONTRAS JELAS) ---
    col_ig, col_tt, col_wv, col_sp, col_yt, col_tg = st.columns(6)

    # CSS tambahan khusus tombol biar teksnya kontras dan posisinya di tengah
    tombol_style = "display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background-color: #262730; color: white; padding: 12px 10px; min-height: 65px; border-radius: 8px; text-decoration: none; font-weight: bold; border: 1px solid rgba(250, 250, 250, 0.2);"

    with col_ig:
        st.markdown(f'<a href="https://www.instagram.com/lngshot4sho/" target="_blank" style="{tombol_style}">📸 IG</a>', unsafe_allow_html=True)

    with col_tt:
        st.markdown(f'<a href="https://www.tiktok.com/@lngshot4sho" target="_blank" style="{tombol_style}">🎵 TikTok</a>', unsafe_allow_html=True)

    with col_wv:
        st.markdown(f'<a href="https://weverse.io/lngshot/highlight" target="_blank" style="{tombol_style}">🌟 Weverse</a>', unsafe_allow_html=True)

    with col_sp:
        st.markdown(f'<a href="https://open.spotify.com/prerelease/7EAdbJSW3zhQ6aUFre1mao?si=7510GXaBTWWkm3PabLZdqg&utm_source=copy-link&nd=1&dlsi=c7992718db9340d7" target="_blank" style="{tombol_style}">🎧 Spotify</a>', unsafe_allow_html=True)

    with col_yt:
        st.markdown(f'<a href="https://www.youtube.com/@LNGSHOT4SHO" target="_blank" style="{tombol_style}">📺 YouTube</a>', unsafe_allow_html=True)

    with col_tg:
        st.markdown(f'<a href="https://t.me/lngsoht" target="_blank" style="{tombol_style}">✈️ Telegram<span style="font-size: 9px; color: #ff4b4b; font-weight: normal; margin-top: 2px;">(RP Not Official)</span></a>', unsafe_allow_html=True)

    st.markdown("---")

    # Membagi layar sama rata 
    kolom1, kolom2, kolom3, kolom4 = st.columns(4)

    # Member 1 (Ozren)
    with kolom1:
        st.markdown("Ozren Kheir")
        st.image("Foto Ohyul.jpg", width="stretch")
        if st.session_state['kunci_m1'] == False:
            tebakan_m1 = st.text_input("Password:", type="password", key="pw_m1")
            if st.button("Buka Brankas", key="btn_m1"):
                if tebakan_m1 == "562": # SANDI
                    st.session_state['kunci_m1'] = True
                    st.rerun()
                elif tebakan_m1 != "":
                    st.error("Ozren's code name: 562")
        else:
            st.success("Open!")
            st.write("Coming soon...")
            if st.button("Kunci Balik", key="lock_m1"):
                st.session_state['kunci_m1'] = False
                st.rerun()

    # Member 2 (Miguel)
    with kolom2:
            st.markdown("Miguel Corberò")
            st.image("Foto Ryul.jpg", width="stretch")
            if st.session_state['kunci_m2'] == False:
                tebakan_m2 = st.text_input("Password:", type="password", key="pw_m2")
                if st.button("Buka Brankas", key="btn_m2"):
                    if tebakan_m2 == "118": # SANDI
                        st.session_state['kunci_m2'] = True
                        st.rerun()
                    elif tebakan_m2 != "":
                        st.error("Miguel's code name: 118")
            else:
                st.success("Open!")
                st.write("Coming soon...")
                if st.button("Kunci Balik", key="lock_m2"):
                    st.session_state['kunci_m2'] = False
                    st.rerun()

    # Member 3 (Janit)
    with kolom3:
                st.markdown("Ja Nitra")
                st.image("Foto Woojin.jpg", width="stretch")
                if st.session_state['kunci_m3'] == False:
                    tebakan_m3 = st.text_input("Password:", type="password", key="pw_m3")
                    if st.button("Buka Brankas", key="btn_m3"):
                        if tebakan_m3 == "3814": # SANDI
                            st.session_state['kunci_m3'] = True
                            st.rerun()
                        elif tebakan_m3 != "":
                            st.error("Janit's code name: 3814")
                else:
                    st.success("Open!")
                    st.write("Coming soon...")
                    if st.button("Kunci Balik", key="lock_m3"):
                        st.session_state['kunci_m3'] = False
                        st.rerun()

    # Member 4 (Yeven)
    with kolom4:
                    st.markdown("Yeven Kheirò")
                    st.image("Foto Louis.jpg", width="stretch")
                    if st.session_state['kunci_m4'] == False:
                        tebakan_m4 = st.text_input("Password:", type="password", key="pw_m4")
                        if st.button("Buka Brankas", key="btn_m4"):
                            if tebakan_m4 == "724": # SANDI
                                st.session_state['kunci_m4'] = True
                                st.rerun()
                            elif tebakan_m4 != "":
                                st.error("Yeven's code name: 724")
                    else:
                        st.success("Open!")
                        st.write("Coming soon...")
                        if st.button("Kunci Balik", key="lock_m4"):
                            st.session_state['kunci_m4'] = False
                            st.rerun()
    # SOUNDTRACK (MASTERPIECE)
    st.markdown("---")
    st.audio("Masterpiece - LNGSHOT.mp3", format="audio/mp3", autoplay=True, loop=True)