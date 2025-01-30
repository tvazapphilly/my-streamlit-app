import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

df = pd.read_csv("high_popularity_spotify_data[1].csv")
audio_features = ['energy', 'tempo', 'danceability','loudness','liveliness','valence','speechiness','instrumentalness','mode','key','duration_ms','acousticness']

def scatter_plot(x,y, x_label, y_label):
    fig, ax = plt.subplots()
    sn.scatterplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f'{x} vs {y}')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig)

def correlation_heatmap():
    fig, ax = plt.subplots(figsize=(14, 10))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sn.heatmap(corr, annot=True, cmap='coolwarm', fmt='.1f')
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

st.title('Comparing Categories: What makes a song popular?')

x_column = st.selectbox('Select the feature for X axis', audio_features)
y_column = st.selectbox('Select the feature for Y axis', audio_features)

scatter_plot(x_column, y_column, x_column,  y_column)
correlation_heatmap()