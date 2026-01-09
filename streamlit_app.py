import streamlit as st
import numpy as np
import pandas as pd
import sympy as sp

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# =========================
# SIDEBAR - DARK MODE
# =========================
with st.sidebar:
    st.session_state.dark_mode = st.toggle("🌙 Dark Mode")

# =========================
# CUSTOM CSS (FIX KOTAK PUTIH)
# =========================
if st.session_state.dark_mode:
    bg = "#0E1117"
    text = "#FAFAFA"
    card = "#1E1E1E"
else:
    bg = "#F6F7FB"
    text = "#2E2E2E"
    card = "#FFFFFF"

st.markdown(f"""
<style>

/* RESET BODY */
html, body, [class*="css"] {{
    background-color: {bg} !important;
    color: {text} !important;
}}

/* HILANGKAN PADDING UTAMA */
.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 0rem !important;
}}

/* HILANGKAN CONTAINER KOSONG */
.stContainer:empty {{
    display: none !important;
}}

/* HILANGKAN MARKDOWN KOSONG */
.stMarkdown:empty {{
    display: none !important;
}}

/* CARD STYLE */
.card {{
    background: {card};
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}}

/* INPUT */
input {{
    border-radius: 12px !important;
}}

/* HILANGKAN WHITE STRIP PALING SERING MUNCUL */
div[data-testid="stVerticalBlock"] > div:empty {{
    display: none !important;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
    "<h1 style='text-align:center;'>Kalkulator SPNL – Metode Regula Falsi</h1>",
    unsafe_allow_html=True
)

# =========================
# STEP 1
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Step 1: Masukkan Persamaan f(x)")
st.caption("Contoh: x**3 - x - 2")

fungsi_input = st.text_input(
    "Persamaan f(x)",
    value="x**3 - x - 2",
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# STEP 2
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Step 2: Interval Awal")
a = st.number_input("Nilai a", value=1.0)
b = st.number_input("Nilai b", value=2.0)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# STEP 3
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Step 3: Iterasi")
max_iter = st.slider("Jumlah Iterasi", 1, 50, 10)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PROSES
# =========================
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

        hasil.append([i+1, a, b, c, fc])

        if fa * fc < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(
        hasil,
        columns=["Iterasi", "a", "b", "c", "f(c)"]
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Hasil Iterasi")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
