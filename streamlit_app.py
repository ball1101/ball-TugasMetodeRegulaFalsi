import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="wide"
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
# THEME
# =====================================================
if st.session_state.dark_mode:
    BG = "#0e1117"
    TEXT = "#fafafa"
    CARD = "#1c1f26"
else:
    BG = "#f4f6fb"
    TEXT = "#1f2937"
    CARD = "#ffffff"

# =====================================================
# CSS (AMAN & STABIL)
# =====================================================
st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
    background-color: {BG};
    color: {TEXT};
}}

.block-container {{
    padding-top: 2rem;
}}

.card {{
    background-color: {CARD};
    padding: 24px;
    border-radius: 14px;
    margin-bottom: 24px;
}}

header, footer {{
    display: none;
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
# INPUT CARD
# =====================================================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Input Persamaan")

    fungsi_input = st.text_input(
        "Masukkan f(x)",
        value="x**3 - x - 2"
    )

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Nilai a", value=1.0)
    with col2:
        b = st.number_input("Nilai b", value=2.0)

    max_iter = st.slider("Jumlah Iterasi", 1, 50, 10)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# PROSES
# =====================================================
if st.button("Hitung Akar"):
    x = sp.symbols("x")
    f = sp.sympify(fungsi_input)
    f_func = sp.lambdify(x, f, "numpy")

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
        columns=["Iterasi", "a", "b", "c (akar)", "f(c)"]
    )

    # =================================================
    # OUTPUT TABLE
    # =================================================
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Tabel Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =================================================
    # GRAFIK
    # =================================================
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Grafik Fungsi dan Akar")

        x_plot = np.linspace(df["a"].min(), df["b"].max(), 400)
        y_plot = f_func(x_plot)

        fig, ax = plt.subplots()
        ax.axhline(0)
        ax.plot(x_plot, y_plot)
        ax.scatter(df["c (akar)"], df["f(c)"])

        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)
