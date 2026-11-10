import streamlit as st
import base64
import os

def get_base64_img(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nama_dasar = os.path.splitext(file_name)[0].lower()

    # Otomatis cari nama file yang cocok dengan ekstensi .jpg, .jpeg, .png, atau .webp
    target_path = ""
    for f in os.listdir(base_dir):
        nama_file, ext = os.path.splitext(f)
        if f.lower() == file_name.lower() or (
            nama_file.lower() == nama_dasar and ext.lower() in ('.jpg', '.jpeg', '.png', '.webp')
        ):
            target_path = os.path.join(base_dir, f)
            break

    if not target_path:
        daftar_gambar = [
            f for f in os.listdir(base_dir)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))
        ]
        st.warning(f"⚠️ File `{file_name}` nggak ketemu! Gambar yang ada di folder ini: {daftar_gambar}")
        return ""

    ext = os.path.splitext(target_path)[1].lower().lstrip(".")
    mime = "image/png" if ext == "png" else "image/webp" if ext == "webp" else "image/jpeg"
    with open(target_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{encoded}"

# Ekstensinya bakal dicocokkan otomatis selama nama depannya "BANANAS PROMO"
img_url = get_base64_img("BANANAS PROMO.jpg")

# Pastikan tanpa lapisan hitam (rgba) supaya gambar tampil terang maksimal
bg_normal = f'url("{img_url}")' if img_url else 'none'
bg_hover = f'url("{img_url}")' if img_url else 'none'

st.markdown(f"""
<style>
    /* Sembunyikan ruang kosong dari penanda */
    div[data-testid="stElementContainer"]:has(#marker-promosi),
    div.element-container:has(#marker-promosi) {{
        display: none !important;
    }}

    /* Styling tombol Promosi SWISH (lebih tinggi & lebih cerah) */
    .st-key-btn_promosi_swish button,
    div[data-testid="stElementContainer"]:has(#marker-promosi) + div button,
    div.element-container:has(#marker-promosi) + div button {{
        background-image: {bg_normal} !important;
        background-size: cover !important;
        background-position: center !important;
        background-color: #22252a !important;
        height: 206px !important;
        min-height: 206px !important;
        width: 100% !important;
        border-radius: 16px !important;
        border: 2px solid rgba(255, 255, 255, 0.35) !important;
        filter: brightness(1.25) contrast(1.12) saturate(1.15) !important;
        transition: transform 0.2s ease, border-color 0.2s ease, filter 0.2s ease !important;
    }}

    .st-key-btn_promosi_swish button:hover,
    div[data-testid="stElementContainer"]:has(#marker-promosi) + div button:hover,
    div.element-container:has(#marker-promosi) + div button:hover {{
        background-image: {bg_hover} !important;
        transform: scale(1.02) !important;
        border-color: #ffffff !important;
        filter: brightness(1.35) contrast(1.12) saturate(1.15) !important;
    }}
</style>
""", unsafe_allow_html=True)

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

    /* Paksa kotak error Streamlit jadi merah muda terang dengan teks merah tua pekat */
    div[data-testid="stMarkdownContainer"] div.stAlert,
    div[data-testid="stNotification"],
    div.element-container div.stAlert {
        background-color: #f8d7da !important;
        border: 1px solid #f5c6cb !important;
        color: #721c24 !important;
    }
    
    /* Paksa teks dan paragraf di dalam kotak error jadi hitam/merah tua tebal */
    div[data-testid="stMarkdownContainer"] div.stAlert p,
    div[data-testid="stNotification"] p,
    div.stAlert p {
        color: #721c24 !important;
        font-weight: bold !important;
    }

    </style>
    """
    st.markdown(kode_wallpaper, unsafe_allow_html=True)

    # MASTERPIECE MV
    st.video("https://youtu.be/Cu6JU-kNmOU?si=1xExJ6jzl_TLpXyq", autoplay=True, muted=True, loop=True)

    # PASSWORD
    st.title("4SHOGANG Area 🐈‍⬛🌰🐕🐘")
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
        st.image("Logo SWISH.jpeg", width=1000)

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

    # BANANAS MV
    st.video("https://youtu.be/xWNIrOTJ6VA?si=Raw_W-r213yyygfJ", autoplay=True, muted=True, loop=True)
    st.markdown("---")

    # FUN BUTTONS

    # Siapkan memori untuk buka-tutup galeri Promosi SWISH
    if 'buka_promosi_swish' not in st.session_state:
        st.session_state['buka_promosi_swish'] = False

    # Rasio [1, 2, 1] biar kolom tengah 2x lebih lebar
    col_kiri, col_tengah, col_kanan = st.columns([1, 2.6, 1])

    with col_kiri:
        st.markdown(
            "<p style='text-align: center; font-weight: 800; font-size: 18px; letter-spacing: 1px; margin: 0; white-space: nowrap;'>MEMBER PICKS</p>",
            unsafe_allow_html=True
        )
        st.link_button("🐈‍⬛", "https://youtu.be/xWNIrOTJ6VA?si=l-LL116hGEtfsbMf", help="Ozren's Pick", use_container_width=True)
        st.link_button("🌰", "https://youtu.be/URN8b_uSNYU?si=dhJKEE6WtQLRTeAM", help="Miguel's Pick", use_container_width=True)
        st.link_button("🐕", "https://youtu.be/URN8b_uSNYU?si=dhJKEE6WtQLRTeAM", help="Janit's Pick", use_container_width=True)
        st.link_button("🐘", "https://youtu.be/cYMtrxN-BkM?si=P0QlG4Uk37EkpoAE", help="Yeven's Pick", use_container_width=True)

    with col_tengah:
        st.markdown(
            "<p style='text-align: center; font-weight: 800; font-size: 18px; letter-spacing: 1px; margin: 0; white-space: nowrap;'>SWISH PROMOTIONS</p>",
            unsafe_allow_html=True
        )
        st.markdown('<div id="marker-promosi"></div>', unsafe_allow_html=True)
        if st.button(" ", key="btn_promosi_swish", use_container_width=True):
            st.session_state['buka_promosi_swish'] = not st.session_state['buka_promosi_swish']
            st.rerun()

    with col_kanan:
        st.markdown(
            "<p style='text-align: center; font-weight: 800; font-size: 18px; letter-spacing: 1px; margin: 0; white-space: nowrap;'>COMING SOON</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="height: 240px; box-sizing: border-box; border: 2px dashed #cbd5e1; border-radius: 16px; background-color: #f8f9fb; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between;">'
            '<div style="height: 12px; width: 100%; background: repeating-linear-gradient(-45deg, #facc15, #facc15 10px, #1f2937 10px, #1f2937 20px);"></div>'
            '<div style="padding: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; flex: 1;">'
            '<span style="font-size: 36px; line-height: 1; margin-bottom: 10px;">🚧</span>'
            '<span style="font-weight: 800; font-size: 13px; letter-spacing: 1px; color: #1f2937; line-height: 1.3;">UNDER<br>CONSTRUCTION</span>'
            '<span style="font-size: 11px; color: #6b7280; margin-top: 6px;">Lagi disiapin, pantau terus!</span>'
            '</div>'
            '<div style="height: 12px; width: 100%; background: repeating-linear-gradient(-45deg, #facc15, #facc15 10px, #1f2937 10px, #1f2937 20px);"></div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    if st.session_state['buka_promosi_swish']:
        # 1. Cukup tulis nama file fotonya saja (tambah baris baru kalau fotonya lebih dari 3)
        galeri_promosi = [
            "Foto promo 1.jpg",
            "Foto promo 2.jpg",
            "Foto promo 3.jpg",
            "Foto promo 4.jpg",
            "Foto promo 5.jpg",
            "Foto promo 6.jpg",
            "Foto promo 7.jpg",
            "Foto promo 8.jpg",
            "Foto promo 9.jpg",
            "Foto promo 10.jpg",
            "Foto promo 11.jpg",
            "Foto promo 12.jpg",
        ]

        if 'promo_slide_idx' not in st.session_state:
            st.session_state['promo_slide_idx'] = 0

        if st.session_state['promo_slide_idx'] >= len(galeri_promosi):
            st.session_state['promo_slide_idx'] = 0

        idx = st.session_state['promo_slide_idx']
        file_aktif = galeri_promosi[idx]

        # 2. Cari file otomatis (.jpg/.jpeg/.png/.webp)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        nama_dasar = os.path.splitext(file_aktif)[0].lower()
        path_foto = ""
        for f in os.listdir(base_dir):
            nama_f, ext_f = os.path.splitext(f)
            if f.lower() == file_aktif.lower() or (
                nama_f.lower() == nama_dasar and ext_f.lower() in ('.jpg', '.jpeg', '.png', '.webp')
            ):
                path_foto = os.path.join(base_dir, f)
                break

        # 3. Tampilkan foto polos tanpa judul dan tanpa caption
        _, col_foto, _ = st.columns([1, 2.6, 1])
        with col_foto:
            if path_foto:
                st.image(path_foto, use_container_width=True)
            else:
                st.warning(f"⚠️ File `{file_aktif}` belum ketemu di folder kamu.")

        # 4. Navigasi geser kiri-kanan + titik slide
        _, c_prev, c_dots, c_next, _ = st.columns([1, 0.65, 1.3, 0.65, 1])
        with c_prev:
            if st.button("⬅️", key="promo_prev", use_container_width=True):
                st.session_state['promo_slide_idx'] = (idx - 1) % len(galeri_promosi)
                st.rerun()

        with c_dots:
            dots = " ".join(["●" if i == idx else "○" for i in range(len(galeri_promosi))])
            st.markdown(
                f"<p style='text-align: center; margin: 8px 0 0 0; font-size: 13px; letter-spacing: 4px;'>{dots}</p>",
                unsafe_allow_html=True
            )

        with c_next:
            if st.button("➡️", key="promo_next", use_container_width=True):
                st.session_state['promo_slide_idx'] = (idx + 1) % len(galeri_promosi)
                st.rerun()

        # 5. Tombol Tutup Galeri + garis pembatas bawah
        _, col_tutup, _ = st.columns([1, 2.6, 1])
        with col_tutup:
            st.write("")
            if st.button("❌ Tutup Galeri", key="tutup_promosi", use_container_width=True):
                st.session_state['buka_promosi_swish'] = False
                st.rerun()

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
            st.markdown("""
            Bagi manusia bernama Ozren ini, mungkin kafein gaada artinya karena minum gaminum dia akan tetep molor. Ozren paling depan kalau soal makan, karena bagi dia "kalau gak makan gak hidup" jadi jangan heran kalau liat Ozren dengan makanannya. Selain lider yang penuh amarah, Ozren selalu punya cara buat bikin segrup ketakutan klo udah beneran ngamuk. Tapi dibalik itu, Ozren orang nomor 1 yang siap dengerin curhatan member grup serta offer best advices.
                                                                        
             **Role in group:** Leader dengan segala amarah dan kebijakan yang terpancar setiap lihat membernya
            """)
            # Foto aib di bawah teks
            st.image("Foto Ohyul 2.jpg", caption="Ozren setiap kali ada member yang bikin darahnya naik", width=300)
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
                st.markdown("""
                Abang grup yang keliatan gapernah tidur ini akrab disapa sebagai Migel, atau Migwell kalau Lui yang manggil. Hobinya nyari ribut sama Ozren tapi ciut juga kalau udah dimarahin beneran. Motto hidup si manusia KC garis keras dan cinta pikachu serta Ayya ini gak lain dan gak bukan ya *"Hidup tuh  dihiphopin aja, selaw, yang penting jangan jadi KhhCancel"* dan tiap hari harapannya mau menang smtm13 biar jadi King Hiphop kayak Kim Haon, S.Khh, M.Khh, Ph.D
                                                            
                **Role in group:** Ragebaiter nomor 1 yang ga berenti betingkah
                """)
                # Foto aib di bawah teks
                st.image("Foto Ryul 2.jpg", caption="Migel setiap berhasil memancing amarah, terutama amarah Ozren", width=300)
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
                    st.markdown("""
                    Cara nandain pagi sudah menyerang ya pesan good morning dari anak yang dipanggil Janit ini. Beliau bucin nomor #1, paling semangat menyebut nama pacarnya. Janit dengan semangat berkata *"Kasih tau RCTI kalau gua lebih oke"* saking okenya pernah jadi vampire anak ayah agra. Sama kayak Lui, Janit kalau udah *terharu* satu layar bisa penuh tulisan dia, yang gak lupa diiringi emoji nangis banjir air yang sangat dicinta. 
                                            
                    **Role in group:** Adek tengah yang suka skip baca terus nanya lagi "maksudnya apa sih ini?"
                    """)
                    # Foto aib di bawah teks
                    st.image("Foto Woojin 2.jpg", caption="Janit sebelum berucap 'ganteng banget ya gua, pantes naithea suka'", width=300)
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
                        st.markdown("""
                        Walaupun akrab dipanggil Yeven oleh temen-temen diluar, anak ini justru dipanggil Lui oleh 4SHOGANG. Quotes hidupnya *"please hesitate to contact me"* tapi dia justru yang paling seneng gangguin abang-abangnya. Paling sering bilang kangen, paling *affectionate* walaupun juga kena jail terus-terusan. Dia juga proud papa to Hunter, sekali sehari minimal banggain kucing kegendutan itu.
                        
                        **Role in group:** Adek kesayangan, gaada Lui ga rame.
                        """)
                        # Foto aib di bawah teks
                        st.image("Foto Louis 2.jpg", caption="Lui memasak bahan jail baru", width=300)
                        if st.button("Kunci Balik", key="lock_m4"):
                            st.session_state['kunci_m4'] = False
                            st.rerun()