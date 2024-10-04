import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go 
from sklearn.preprocessing import StandardScaler

# Load dataset
@st.cache
def load_data():
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSlySm-EwCHnAjF3165w3dwWw_UalzGS-gDJSrBfP2XqlfoikexojkZKyTykMIMCg/pub?gid=1808118811&single=true&output=csv') 
    return df 

df = load_data()

# Menambahkan Sidebar untuk Navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih halaman:", ["Beranda", "Visualisasi"])

# Halaman Beranda
if page == "Beranda":
    st.title("Hotel Data Explorer: Temukan Insight dari Data Hotel")
    st.write("""
        Selamat datang di aplikasi web interaktif yang dirancang khusus untuk mengeksplorasi data hotel dengan cara yang menarik dan mudah dipahami. Nikmati berbagai visualisasi interaktif yang tidak hanya memperlihatkan gambaran besar, tetapi juga menyelami detail tersembunyi. Dengan setiap klik, Anda dapat menggali insight berharga dari dataset dan mengungkap pola serta tren yang mungkin tidak terlihat sebelumnya!
    """)

# Halaman Visualisasi
elif page == "Visualisasi":
    st.title("Visualisasi Data")

    # Menambahkan dropdown untuk memilih fitur yang akan divisualisasikan
    feature = st.selectbox("Pilih fitur untuk visualisasi", df.columns)

    # Visualisasi 1: Histogram Distribusi
    st.subheader(f"Distribusi {feature}")
    fig_hist = px.histogram(df, x=feature, nbins=20, title=f"Distribusi {feature}")
    st.plotly_chart(fig_hist)

    # Insight untuk Histogram
    st.write(f"Dari visualisasi distribusi {feature}, kita bisa melihat pola distribusi dari data. Jika distribusi mendekati normal, ini dapat menunjukkan bahwa nilai {feature} memiliki variasi yang tidak terlalu ekstrem di dalam dataset.")

    # Visualisasi 2: Scatter Plot untuk hubungan antar fitur
    st.subheader("Scatter Plot Fitur Terpengaruh")
    scatter_feature = st.selectbox("Pilih fitur untuk Scatter Plot", df.columns, index=1)
    fig_scatter = px.scatter(df, x=feature, y=scatter_feature, title=f"Scatter Plot {feature} vs {scatter_feature}")
    st.plotly_chart(fig_scatter)

    # Insight untuk Scatter Plot
    st.write(f"Scatter plot antara {feature} dan {scatter_feature} dapat membantu kita melihat hubungan linier atau pola keterkaitan antara dua variabel. Jika terlihat pola linier, mungkin ada hubungan sebab-akibat antara kedua variabel tersebut.")

    