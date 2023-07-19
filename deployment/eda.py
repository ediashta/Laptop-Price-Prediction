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
dataset = "https://raw.githubusercontent.com/ediashta/laptop-price-regression/main/laptops.csv"
data = pd.read_csv(dataset)


def distribution():
    # distribution plot
    st.title("Laptop Specs Distribution")

    count_plot_var = st.selectbox("Choose Table", ("Brand", "GPU", "CPU"))
    count_plot(count_plot_var)

    col1, col2 = st.columns([2, 1], gap="large")

    bar_plot_var = col1.selectbox("Choose Table", ("Storage", "RAM"))
    bar_plot(bar_plot_var, col1)

    pie_chart_var = col2.selectbox(
        "Choose Table", ("Screen", "Storage Type", "Touch Type", "Laptop Condition")
    )
    pie_chart(pie_chart_var, col2)

    st.subheader("Price Distribution")
    hist_plot("Final Price")


def corr_matrix():
    # distribution plot
    st.title("Features Correlation")
    col1, col2 = st.columns(2)

    # correlation for numerical
    fig = plt.figure(figsize=(10, 10))
    corr_matrix = data[["RAM", "Storage", "Screen", "Final Price"]].corr(
        method="pearson"
    )
    sns.heatmap(corr_matrix, annot=True, cmap="mako", square=True)
    col1.pyplot(fig)
    col2.write(
        "Heatmap disebelah merupakan korelasi antara data numerikal dengan Final Price sebuah laptop, data dibawah merupakan korelasi data kategorical dengan Final Price sebuah laptop"
    )
    col2.markdown("### Correlation")
    col2.markdown("* **Status** : 0.26450718170008297")
    col2.markdown("* **Brand** : 0.241996453068071")
    col2.markdown("* **Model** : 0.2519900783873629")
    col2.markdown("* **CPU** : 0.2517567086906365")
    col2.markdown("* **GPU** : 0.3422702941182396")
    col2.markdown("* **Touch** : 0.095355125133349")


def count_plot(var):
    # laptop brand distribution
    fig = plt.figure(figsize=(20, 8))
    sns.countplot(
        data=data,
        y=var,
        order=data[var].value_counts().index,
        palette="mako",
    )
    st.pyplot(fig)


def bar_plot(var, col):
    # ram storage dist
    fig = plt.figure(figsize=(10, 5))
    ax1 = sns.countplot(
        data=data,
        x=var,
        palette="mako",
    )
    plt.xlabel(var + " (GB)")
    ax1.bar_label(container=ax1.containers[0], labels=data[var].value_counts().values)
    col.pyplot(fig)


def pie_chart(var, col):
    # pie chart
    palette = sns.color_palette("mako_r", 10)
    fig = plt.figure(figsize=(10, 10))
    screen = pd.DataFrame(
        data["Screen"].value_counts().rename_axis("screen").reset_index(name="counts")
    )
    sum = screen["counts"].sum()

    storage_type = pd.DataFrame(
        data["Storage type"]
        .value_counts()
        .rename_axis("storage_type")
        .reset_index(name="counts")
    )
    touch_type = pd.DataFrame(
        data["Touch"].value_counts().rename_axis("touch").reset_index(name="counts")
    )
    status = pd.DataFrame(
        data["Status"].value_counts().rename_axis("status").reset_index(name="counts")
    )

    for i in screen[(screen["counts"] / sum) < 0.05]["screen"]:
        screen.loc[screen["screen"] == i, "screen"] = "Other"

    screen_new = screen.groupby(screen["screen"]).aggregate(
        {"screen": "first", "counts": "sum"}
    )

    if var == "Screen":
        plt.pie(
            screen_new["counts"],
            labels=screen_new["screen"],
            autopct="%1.1f%%",
            colors=palette,
        )
    elif var == "Storage Type":
        plt.pie(
            storage_type["counts"],
            labels=storage_type["storage_type"],
            autopct="%1.1f%%",
            colors=palette,
        )
    elif var == "Touch Type":
        plt.pie(
            touch_type["counts"],
            labels=touch_type["touch"],
            autopct="%1.1f%%",
            colors=palette,
        )
    elif var == "Laptop Condition":
        plt.pie(
            status["counts"], labels=status["status"], autopct="%1.1f%%", colors=palette
        )
        plt.show()

    col.pyplot(fig)


def hist_plot(var):
    # check price distribution
    fig = plt.figure(figsize=(20, 5))

    palette = sns.color_palette("mako_r", 50)

    plot = sns.histplot(data=data, x=var, kde=True, bins=50, color="teal")

    for bin_, i in zip(plot.patches, palette):
        bin_.set_facecolor(i)

    st.pyplot(fig)


if __name__ == "__main__":
    distribution()
