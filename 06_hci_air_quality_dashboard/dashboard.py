"""Dashboard Streamlit untuk data kualitas udara historis UCI ID 360."""
import pandas as pd
import streamlit as st
from ucimlrepo import fetch_ucirepo

st.set_page_config(page_title="UCI Air Quality Explorer", layout="wide")
st.title("UCI Air Quality Explorer")
st.caption("Data pengukuran historis dari dataset UCI; bukan pembacaan kualitas udara real-time.")

@st.cache_data(show_spinner="Mengunduh dataset publik UCI...")
def load_data():
    ds = fetch_ucirepo(id=360)
    df = pd.concat([ds.data.features, ds.data.targets], axis=1)
    # Dalam dataset ini, nilai -200 digunakan sebagai penanda missing pada beberapa variabel.
    df = df.replace(-200, float("nan"))
    numeric = df.select_dtypes(include="number").columns.tolist()
    for c in df.columns:
        if c not in numeric:
            df[c] = pd.to_numeric(df[c], errors="ignore")
    return df

try:
    df = load_data()
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        st.error("Tidak ditemukan kolom numerik setelah pemuatan data.")
    else:
        chosen = st.sidebar.selectbox("Pilih variabel sensor", numeric_cols)
        series = pd.to_numeric(df[chosen], errors="coerce").dropna()
        a, b, c = st.columns(3)
        a.metric("Jumlah pengukuran valid", f"{len(series):,}")
        b.metric("Rata-rata", f"{series.mean():.3f}")
        c.metric("Median", f"{series.median():.3f}")
        st.subheader(f"Distribusi dan urutan data: {chosen}")
        st.line_chart(series.reset_index(drop=True).rename("measurement"))
        st.subheader("Sampel data")
        st.dataframe(df[[chosen]].head(100), use_container_width=True)
        st.write("Interpretasikan variabel berdasarkan metadata dataset; jangan menganggap semua kolom memiliki satuan atau arti yang sama.")
except Exception as e:
    st.error(f"Dataset belum dapat dimuat. Periksa koneksi internet dan dokumentasi UCI. Detail: {e}")
