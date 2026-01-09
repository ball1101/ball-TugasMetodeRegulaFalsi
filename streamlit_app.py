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
# THEME COLOR (HIGH CONTRAST)
# =====================================================
if st.session_state.dark_mode:
    # DARK MODE – NAVY (HIGH CONTRAST)
    BG = "#0b1c2d"
    TEXT = "#f1f5f9"        # hampir putih
    TEXT_MUTED = "#cbd5e1"
    ACCENT = "#60a5fa"
    BORDER = "#1e3a5f"
    GRID = "#334155"
else:
    # LIGHT MODE – CLEAN
    BG = "#f3f5f9"
    TEXT = "#111827"        # hitam lembut
    TEXT_MUTED = "#374151"
    ACCENT = "#2563eb"
    BORDER = "#d1d5db"
    GRID = "#9ca3af"

# =====================================================
# CSS (TEKS TERBACA DI SEMUA MODE)
# =====================================================
st.markdown(f"""
<style>

/* GLOBAL */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: {BG};
    color: {TEXT};
}}

/* HEADER */
[data-testid="stHeader"] {{
    background: transparent;
}}

/* MAIN CONTAINER */
.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

/* SIDEBAR */
[data-testid="stSidebar"] {{
    background-color: {BG};
    border-right: 1px solid {BORDER};
}}

/* HEADINGS */
h1, h2, h3, h4 {{
    color: {TEXT};
}}

/* PARAGRAPH & LABEL */
p, label, span {{
    color: {TEXT_MUTED};
}}

/* INPUT & SELECT */
input, textarea, select {{
    color: {TEXT} !important;
    background-color: transparent !important;
}}

/* BUTTON */
button[kind="primary"] {{
    background-color: {ACCENT};
    color: white;
    border-radius: 8px;
}}

/* DATAFRAME */
[data-testid="stDataFrame"] {{
    color: {TEXT};
}}

/* DIVIDER */
hr {{
    border-color: {BORDER};
}}

/* FOOTER */
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
    "Masukkan fungsi f(x)",
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
# PROCESS
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
    ax.axhline(0, color=GRID)
    ax.plot(x_plot, y_plot, color=ACCENT)
    ax.scatter(df["c (akar)"], df["f(c)"], color="red")

    ax.set_facecolor(BG)
    fig.patch.set_facecolor(BG)

    ax.tick_params(colors=TEXT)
    ax.spines["bottom"].set_color(TEXT)
    ax.spines["left"].set_color(TEXT)

    ax.grid(True, color=GRID, alpha=0.4)

    st.pyplot(fig)
