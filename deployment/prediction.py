import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json


# load file
# with open("./list_nom_cols.txt", "r") as file_1:
#     model_nom_cols = json.load(file_1)

# with open("./list_num_cols.txt", "r") as file_2:
#     model_num_cols = json.load(file_2)

# with open("./list_num_cols.txt", "r") as file_3:
#     model_ord_cols = json.load(file_3)

# with open("./model_pipeline.pkl", "rb") as file_4:
#     model_pipeline = pickle.load(file_4)


def predict():
    # form
    with st.form("key=form_fifa-2022"):
        st.write("Bio")
        col1, col2, col3 = st.columns(3)
        name = col1.text_input("Full Name", value="")
        age = col2.number_input(
            "Age", min_value=16, max_value=90, value=25, step=1, help="Usia Pasien"
        )
        sex = col3.radio("Gender", (0, 1), help="0=Male, 1=Female")
        st.markdown("---")
        st.write("Medical History")
        col1, col2, col3, col4 = st.columns(4)
        anaemia = col1.radio("Has Anaemia", (0, 1), help="0=No, 1=Yes")
        diabetes = col2.radio("Has Diabetes", (0, 1), help="0=No, 1=Yes")
        hbp = col3.radio("Has Hypertension", (0, 1), help="0=No, 1=Yes")
        smoking = col4.radio("Smoking", (0, 1), help="0=No, 1=Yes")
        st.markdown("---")
        st.write("Medical Status")
        col1, col2 = st.columns(2)
        creatinine = col1.number_input(
            "Creatinine Phosphokinase",
            min_value=0,
            max_value=10000,
            value=1200,
            help="mcg/L",
        )
        ejection = col2.number_input(
            "Ejection Fraction",
            min_value=0,
            max_value=100,
            value=20,
            help="percentage",
        )
        platelets = col1.number_input(
            "Platelets",
            min_value=0,
            max_value=1000000,
            value=200200,
            help="kiloplatelets/mL",
        )
        ss = col2.number_input(
            "Serum Sodium", min_value=0, max_value=200, value=134, help="mEq/L"
        )
        sc = col1.number_input(
            "Serum Creatinine",
            min_value=0.0,
            max_value=100.0,
            value=1.75,
            help="mg/dL",
        )
        time = col2.number_input(
            "Follow-Up Period", min_value=0, max_value=1000, value=20, help="days"
        )
        st.markdown("---")
        submitted = st.form_submit_button("Predict")

    # inferencing
    data_inf = {
        "name": name,
        "age": age,
        "anaemia": anaemia,
        "creatinine_phosphokinase": creatinine,
        "diabetes": diabetes,
        "ejection_fraction": ejection,
        "high_blood_pressure": hbp,
        "platelets": platelets,
        "serum_creatinine": sc,
        "serum_sodium": ss,
        "sex": sex,
        "smoking": smoking,
        "time": time,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        y_pred_inf = model_pipeline.predict(data_inf)
        st.write("# Classification Results:")

        if y_pred_inf[0] == 1:
            st.write(
                "### Pasien diprediksi akan meninggal dunia, <span style='color:red;'> segera hubungi dokter atau tenaga medis </span>",
                unsafe_allow_html=True,
            )
        else:
            st.write(
                "### Pasien tidak diprediksi meninggal dunia,<span style='color:green;'> untuk konsultasi lebih lanjut, hubungi dokter atau tenaga medis </span>",
                unsafe_allow_html=True,
            )


def model():
    st.write("test")


if __name__ == "__main__":
    predict()
