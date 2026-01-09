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
    st.session_state.dark_mode = st.toggle("🌙 Dark Mode")

# =====================================================
# THEME COLOR
# =====================================================
if st.session_state.dark_mode:
    # DARK MODE – NAVY
    BG = "#0b1c2d"
    TEXT = "#e6f0ff"
    ACCENT = "#4da3ff"
    BORDER = "#1e3a5f"
else:
    # LIGHT MODE
    BG = "#f3f5f9"
    TEXT = "#1f2937"
    ACCENT = "#2563eb"
    BORDER = "#e5e7eb"

# =====================================================
# CSS (TANPA CARD)
# =====================================================
st.markdown(f"""
<style>

/* GLOBAL */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: {BG};
    color: {TEXT};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

/* SIDEBAR */
[data-testid="stSidebar"] {{
    border-right: 1px solid {BORDER};
}}

/* TEXT */
h1, h2, h3 {{
    color: {TEXT};
}}

a {{
    color: {ACCENT};
}}

/* INPUT */
input, textarea {{
    border-radius: 8px !important;
}}

/* BUTTON */
button[kind="primary"] {{
    background-color: {ACCENT};
    color: white;
    border-radius: 8px;
}}

/* REMOVE FOOTER */
footer {{
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

st.divider()

# =====================================================
# INPUT SECTION
# =====================================================
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

st.divider()

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
    # TABLE
    # =================================================
    st.subheader("Tabel Iterasi")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # =================================================
    # GRAPH
    # =================================================
    st.subheader("Grafik Fungsi dan Akar")

    x_plot = np.linspace(df["a"].min(), df["b"].max(), 400)
    y_plot = f_func(x_plot)

    fig, ax = plt.subplots()
    ax.axhline(0)
    ax.plot(x_plot, y_plot)
    ax.scatter(df["c (akar)"], df["f(c)"])

    ax.set_facecolor(BG)
    fig.patch.set_facecolor(BG)
    ax.tick_params(colors=TEXT)
    ax.spines["bottom"].set_color(TEXT)
    ax.spines["left"].set_color(TEXT)

    st.pyplot(fig)
