import pandas as pd
import streamlit as st
import io

uploaded_csv = st.file_uploader("Introduce aqui tus archivos", [".csv"])

if uploaded_csv:
    df = pd.read_csv(uploaded_csv)

    df["version"] = df["Description"].str.extract(r"(\d{4})")

    last_df = df[df["Description"].str.lower().str.contains("sql server")][["PSComputerName","Description","version"]].drop_duplicates(subset="version").reset_index(drop=True)

    bytes_df = io.BytesIO()
    last_df.to_csv(bytes_df, index=False)
    bytes_df.seek(0)

    st.download_button(label = "Descarga csv filtrado",
                    data  = bytes_df, 
                    file_name="filtered.csv",
                    mime="text/csv")