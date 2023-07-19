import streamlit as st
import eda
import prediction
from streamlit_option_menu import option_menu


with open("./style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.header("Laptop Price Database")


with st.sidebar:
    st.write("Ediashta Revindra - FTDS-020")
    selected = option_menu(
        "Menu",
        [
            "Distribution",
            "Correlation Matrix",
            "Model",
            "Regression",
        ],
        icons=["bar-chart", "link-45deg", "box", "code-square"],
        menu_icon="cast",
        default_index=1,
    )

if selected == "Distribution":
    eda.distribution()
elif selected == "Correlation Matrix":
    eda.corr_matrix()
elif selected == "Model":
    prediction.model()
elif selected == "Regression":
    prediction.predict()
