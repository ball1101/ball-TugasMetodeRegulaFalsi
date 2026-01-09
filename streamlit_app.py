import streamlit as st
import numpy as np
import pandas as pd
import math

st.set_page_config(page_title="Kalkulator SPNL", layout="wide")

# ============================
# TOGGLE MODE
# ============================
mode = st.toggle("🌙 Dark Mode", value=True)

# ============================
# WARNA TEMA
# ============================
if mode:  # DARK MODE
    bg = "#020617"
    sidebar = "#020617"
    card = "#020617"
    text = "#f8fafc"
    muted = "#94a3b8"
    accent = "#38bdf8"
    border = "#1e293b"
    button = "#0284c7"
    button_text = "#ffffff"
else:  # LIGHT MODE
    bg = "#f8fafc"
    sidebar = "#ffffff"
    card = "#ffffff"
    text = "#020617"
    muted = "#475569"
    accent = "#0284c7"
    border = "#cbd5e1"
    button = "#0284c7"
    button_text = "#ffffff"

# ============================
# CSS PROFESIONAL
# ============================
st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
    background: {bg};
    color: {text};
}}

[data-testid="stSidebar"] {{
    background: {sidebar};
    border-right: 1px solid {border};
}}

h1, h2, h3, h4, h5 {{
    color: {text};
}}

label, p, span, div {{
    color: {text};
}}

.stTextInput input,
.stNumberInput input {{
    background-color: {card};
    color: {text};
    border: 1px solid {border};
    border-radius: 10px;
}}

.stSlider > div > div > div > div {{
    background-color: {accent};
}}

.stButton button {{
    background: {button};
    color: {button_text};
    border-radius: 14px;
    padding: 12px 32px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    box-shadow: 0 0 12px rgba(56,189,248,0.4);
}}

.stButton button:hover {{
    background: {accent};
    box-shadow: 0 0 18px rgba(56,189,248,0.8);
    transform: scale(1.03);
}}

.card {{
    background: {card};
    padding: 30px;
    border-radius: 20px;
    border: 1px solid {border};
}}

.toggle-box {{
    display: flex;
    align-items: center;
    gap: 10px;
    color: {text};
    font-weight: 600;
    font-size: 16px;
}}

.toggle-label {{
    color: {text};
}}
</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR
# ============================
with st.sidebar:
    st.markdown("<h3>⚙️ Pengaturan</h3>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='toggle-box'><span class='toggle-label'>🌙 Dark Mode</span></div>",
        unsafe_allow_html=True
    )

# ============================
# JUDUL
# ============================
st.markdown("<h1 style='text-align:center;'>Kalkulator SPNL – Metode Regula Falsi</h1>", unsafe_allow_html=True)

# ============================
# FORM INPUT
# ============================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("### Input Persamaan")
fx = st.text_input("Masukkan fungsi f(x)", "x**3 - x - 2")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Nilai a", value=1.0)
with col2:
    b = st.number_input("Nilai b", value=2.0)

iterasi = st.slider("Jumlah Iterasi", 1, 50, 10)

st.markdown("<br>", unsafe_allow_html=True)

# ============================
# TOMBOL HITUNG (YANG DILINGKARI)
# ============================
if st.button("🔍 Hitung Akar"):
    try:
        def f(x):
            return eval(fx)

        data = []
        for i in range(iterasi):
            fa, fb = f(a), f(b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c)

            data.append([i+1, a, b, c, fc])

            if fa * fc < 0:
                b = c
            else:
                a = c

        df = pd.DataFrame(data, columns=["Iterasi","a","b","c","f(c)"])
        st.dataframe(df, use_container_width=True)

        st.success(f"Akar hampiran = {c}")

    except:
        st.error("Fungsi tidak valid")

st.markdown("</div>", unsafe_allow_html=True)
