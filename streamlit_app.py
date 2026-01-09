import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    st.markdown("## ⚙️ Pengaturan")
    dark = st.toggle("🌙 Dark Mode", value=True)

# =====================
# THEME COLORS
# =====================
if dark:
    bg = "#0b1e3a"
    sidebar = "#102a4c"
    topbar = "#0b1e3a"
    text = "#e0f2ff"
    accent = "#38bdf8"
    border = "#1e3a5f"
    input_bg = "#102a4c"
    collapse = "#ffffff"   # PUTIH
else:
    bg = "#f8fafc"
    sidebar = "#ffffff"
    topbar = "#ffffff"
    text = "#020617"
    accent = "#2563eb"
    border = "#cbd5e1"
    input_bg = "#ffffff"
    collapse = "#020617"   # HITAM

# =====================
# CSS
# =====================
st.markdown(f"""
<style>
:root {{
    --collapse-color: {collapse};
    --border-color: {border};
}}

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

button[data-testid="collapsedControl"] svg {{
    stroke: var(--collapse-color) !important;
}}

button[data-testid="collapsedControl"] {{
    border: 1px solid var(--border-color) !important;
    border-radius: 8px;
    padding: 4px;
    background: transparent !important;
}}

h1,h2,h3,label {{
    color: {text} !important;
}}
</style>
""", unsafe_allow_html=True)

# =====================
# UI
# =====================
st.markdown("<h1 style='text-align:center;'>Kalkulator SPNL</h1>", unsafe_allow_html=True)

st.write("Masukkan fungsi dan interval:")
fx = st.text_input("f(x)", "x**3 - x - 2")

col1,col2 = st.columns(2)
a = col1.number_input("a",1.0)
b = col2.number_input("b",2.0)

if st.button("Hitung"):
    st.success("Mode dan ikon « bekerja dengan benar!")
