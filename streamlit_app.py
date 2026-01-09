import streamlit as st
import numpy as np
import pandas as pd
import math

st.set_page_config(page_title="Kalkulator SPNL", layout="wide")

# ============================
# SIDEBAR → TOGGLE
# ============================
with st.sidebar:
    st.markdown("## ⚙️ Pengaturan")
    mode = st.toggle("🌙 Dark Mode", value=True)

# ============================
# WARNA TEMA
# ============================
if mode:  # DARK MODE
    bg = "#020617"
    sidebar = "#020617"
    text = "#f8fafc"
    muted = "#94a3b8"
    accent = "#38bdf8"
    border = "#1e293b"
    input_bg = "#020617"
    button = "#0284c7"
    button_text = "#ffffff"
else:
    bg = "#f8fafc"
    sidebar = "#ffffff"
    text = "#020617"
    muted = "#475569"
    accent = "#0284c7"
    border = "#cbd5e1"
    input_bg = "#ffffff"
    button = "#0284c7"
    button_text = "#ffffff"

# ============================
# CSS GLOBAL
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

h1, h2, h3, h4 {{
    color: {text};
}}

label, p, span, div {{
    color: {text};
}}

.stTextInput input,
.stNumberInput input {{
    background: {input_bg};
    color: {text};
    border: 1px solid {border};
    border-radius: 10px;
}}

.stSlider > div > div > div > div {{
    background-color: {accent};
}}

.stDataFrame {{
    background: {bg};
}}

.stButton button {{
    background: linear-gradient(135deg, {button}, {accent});
    color: {button_text};
    border-radius: 16px;
    padding: 14px 38px;
    font-size: 16px;
    font-weight: 700;
    border: none;
    box-shadow: 0 0 15px rgba(56,189,248,0.6);
}}

.stButton button:hover {{
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(56,189,248,1);
}}

hr {{
    border: 1px solid {border};
}}
</style>
""", unsafe_allow_html=True)

# ============================
# JUDUL
# ============================
st.markdown("<h1 style='text-align:center;'>Kalkulator SPNL – Metode Regula Falsi</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ============================
# INPUT
# ============================
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
# TOMBOL
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

        st.success(f"🎯 Akar hampiran = {c}")

    except:
        st.error("❌ Fungsi tidak valid")
