import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalkulator SPNL", layout="wide")

# ============================
# SIDEBAR
# ============================
with st.sidebar:
    st.markdown("## ⚙️ Pengaturan")
    mode = st.toggle("🌙 Dark Mode", value=True)

# ============================
# WARNA TEMA
# ============================
if mode:
    bg = "#0b1e3a"
    sidebar = "#102a4c"
    topbar = "#0b1e3a"
    text = "#e0f2ff"
    accent = "#38bdf8"
    border = "#1e3a5f"
    input_bg = "#102a4c"
    button = "#2563eb"
    switch_on = "#38bdf8"
    switch_off = "#1e3a5f"
    collapse_color = "#ffffff"
else:
    bg = "#f8fafc"
    sidebar = "#ffffff"
    topbar = "#ffffff"
    text = "#020617"
    accent = "#2563eb"
    border = "#cbd5e1"
    input_bg = "#ffffff"
    button = "#2563eb"
    switch_on = "#2563eb"
    switch_off = "#94a3b8"
    collapse_color = "#020617"

# ============================
# CSS
# ============================
st.markdown(f"""
<style>

html, body, [data-testid="stAppViewContainer"] {{
    background: {bg};
    color: {text};
}}

header[data-testid="stHeader"] {{
    background: {topbar};
    border-bottom: 1px solid {border};
}}

[data-testid="stSidebar"] {{
    background: {sidebar};
    border-right: 1px solid {border};
}}

h1,h2,h3,h4,label {{
    color: {text} !important;
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

.stButton button {{
    background: linear-gradient(135deg, {button}, {accent});
    color: white;
    border-radius: 16px;
    padding: 14px 38px;
    font-weight: 700;
    border: none;
    box-shadow: 0 0 15px rgba(56,189,248,0.5);
}}

div[data-baseweb="switch"] > div {{
    background-color: {switch_off};
}}

div[data-baseweb="switch"]:has(input:checked) > div {{
    background-color: {switch_on};
    box-shadow: 0 0 10px {switch_on};
}}

button[data-testid="collapsedControl"] svg {{
    stroke: {collapse_color} !important;
}}

button[data-testid="collapsedControl"] {{
    border: 1px solid {border};
    border-radius: 8px;
    padding: 4px;
}}

</style>
""", unsafe_allow_html=True)

# ============================
# UI
# ============================
st.markdown("<h1 style='text-align:center;'>Kalkulator SPNL – Metode Regula Falsi</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("### Input Persamaan")
fx = st.text_input("Masukkan fungsi f(x)", "x**3 - x - 2")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Nilai a", value=1.0)
with col2:
    b = st.number_input("Nilai b", value=2.0)

iterasi = st.slider("Jumlah Iterasi", 1, 50, 10)

# ============================
# HITUNG
# ============================
if st.button("🔍 Hitung Akar"):
    try:
        def f(x): return eval(fx)

        data = []
        a0, b0 = a, b

        for i in range(iterasi):
            fa, fb = f(a), f(b)
            c = (a*fb - b*fa) / (fb - fa)
            fc = f(c)
            data.append([i+1, a, b, c, fc])
            if fa * fc < 0:
                b = c
            else:
                a = c

        df = pd.DataFrame(data, columns=["Iterasi","a","b","c","f(c)"])
        st.dataframe(df, use_container_width=True)

        st.success(f"🎯 Akar hampiran = {c}")

        x = np.linspace(a0-2, b0+2, 500)
        y = [f(i) for i in x]

        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(x, y)
        ax.axhline(0)
        ax.scatter(c, f(c))
        ax.set_title("Grafik f(x)")

        st.pyplot(fig, use_container_width=True)

    except:
        st.error("❌ Fungsi tidak valid")
