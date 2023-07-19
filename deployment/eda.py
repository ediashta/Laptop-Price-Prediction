import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="Laptop Price Regression",
    layout="wide",
    initial_sidebar_state="expanded",
)

# dataset
dataset = "https://raw.githubusercontent.com/ediashta/p1-ftds-020-rmt-g3-ediashta/main/h8dsft_P1G3_Ediashta.csv"
data = pd.read_csv(dataset)


def distribution():
    # distribution plot
    st.title("Laptop Price Regression")
    st.subheader("Distribution")

    col1, col2 = st.columns(2)


def corr_matrix():
    # distribution plot
    st.title("Laptop Price Regression")
    st.subheader("Correlation")


if __name__ == "__main__":
    distribution()
