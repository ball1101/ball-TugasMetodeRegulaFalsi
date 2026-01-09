import streamlit as st
import pandas as pd
import sympy as sp

# =====================================================
# PAGE CONFIG (WAJIB)
# =====================================================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SESSION STATE
# =====================================================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("## Pengaturan")
    st.session_state.dark_mode = st.checkbox("🌙 Dark Mode")

# =====================================================
# THEME COLOR
# =====================================================
if st.session_state.dark_mode:
    BG = "#0e1117"
    TEXT = "#fafafa"
    CARD = "#1c1f26"
    BORDER = "#2a2f3a"
else:
    BG = "#f4f6fb"
    TEXT = "#1f2937"
    CARD = "#ffffff"
    BORDER = "#e5e7eb"

# =====================================================
# GLOBAL CSS (INI KUNCI UTAMA)
# =====================================================
st.markdown(f"""
<style>

/* ====== FORCE REMOVE SEMUA BACKGROUND PUTIH ====== */
html, body {{
    background-color: {BG} !important;
    color: {TEXT} !important;
}}

[data-testid="stAppViewContainer"] {{
    background-color: {BG} !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

[data-testid="stToolbar"] {{
    display: none !important;
}}

[data-testid="stSidebar"] {{
    background-color: {CARD} !important;
}}

/* MAIN AREA */
[data-testid="stMain"] {{
    background-color: {BG} !important;
}}

/* BLOCK UTAMA */
.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    background-color: {BG} !important;
}}

/* ====== CARD ====== */
.card {{
    background-color: {CARD};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

/* INPUT */
input, textarea {{
    border-radius: 10px !important;
}}

/* HAPUS SEMUA BLOCK KOSONG */
div[data-testid="stVerticalBlock"]:has(> div:empty) {{
    display: none !important;
}}

footer {{
    display: none !important;
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================
st.markdown(
    "<h1 style='text-align:center;'>Kalkulator SPNL – Metode Regula Falsi</h1>",
    unsafe_allow_html=True
)

# =====================================================
# STEP 1
# =====================================================
st.markdown("""
<div class="card">
    <h3>Step 1: Masukkan Persamaan f(x)</h3>
    <p>Contoh: <code>x**3 - x - 2</code></p>
</div>
""", unsafe_allow_html=True)

fungsi_input = st.text_input(
    "Persamaan",
    value="x**3 - x - 2",
    label_visibility="collapsed"
)

# =====================================================
# STEP 2
# =====================================================
st.markdown("""
<div class="card">
    <h3>Step 2: Interval Awal</h3>
</div>
""", unsafe_allow_html=True)

a = st.number_input("Nilai a", value=1.0)
b = st.number_input("Nilai b", value=2.0)

# =====================================================
# STEP 3
# =====================================================
st.markdown("""
<div class="card">
    <h3>Step 3: Iterasi</h3>
</div>
""", unsafe_allow_html=True)

max_iter = st.slider("Jumlah Iterasi", 1, 50, 10)

# =====================================================
# PROSES
# =====================================================
if st.button("Hitung Akar"):
    x = sp.symbols("x")
    f = sp.sympify(fungsi_input)
    f_func = sp.lambdify(x, f)

    hasil = []
    for i in range(max_iter):
        fa = f_func(a)
        fb = f_func(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f_func(c)

        hasil.append([i + 1, a, b, c, fc])

        if fa * fc < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(
        hasil,
        columns=["Iterasi", "a", "b", "c", "f(c)"]
    )

    st.markdown("""
    <div class="card">
        <h3>Hasil Iterasi</h3>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)
