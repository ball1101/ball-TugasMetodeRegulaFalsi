import streamlit as st
import pandas as pd
import sympy as sp

# =========================
# PAGE CONFIG (WAJIB WIDE)
# =========================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.session_state.dark_mode = st.toggle("🌙 Dark Mode")

# =========================
# THEME
# =========================
if st.session_state.dark_mode:
    bg = "#0E1117"
    text = "#FAFAFA"
    card = "#1E1E1E"
else:
    bg = "#F6F7FB"
    text = "#2E2E2E"
    card = "#FFFFFF"

# =========================
# CSS (BERSIH & AMAN)
# =========================
st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
    background-color: {bg};
    color: {text};
}}

.block-container {{
    padding-top: 2rem;
}}

.card {{
    background: {card};
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 24px;
}}

input {{
    border-radius: 12px !important;
}}

header, footer {{
    visibility: hidden;
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
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Step 1: Masukkan Persamaan f(x)")
    st.caption("Contoh: x**3 - x - 2")

    fungsi_input = st.text_input(
        "Persamaan",
        value="x**3 - x - 2",
        label_visibility="collapsed"
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# STEP 2
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Step 2: Interval Awal")

    a = st.number_input("Nilai a", value=1.0)
    b = st.number_input("Nilai b", value=2.0)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# STEP 3
# =========================
with st.container():
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

    data = []
    for i in range(max_iter):
        fa = f_func(a)
        fb = f_func(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f_func(c)

        data.append([i + 1, a, b, c, fc])

        if fa * fc < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "c", "f(c)"])

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Hasil Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
