import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st
import numpy as np

df1 = pd.read_csv("high_popularity_spotify_data[1].csv")
df2 = pd.read_csv("low_popularity_spotify_data[1].csv")
df = df1+df2

audio_features = ['energy', 'tempo', 'danceability','loudness','liveness','valence','speechiness','instrumentalness','mode','key','duration_ms','acousticness']


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

st.title('What makes a song popular?')
multi = "- Pick 2 different audio features to see how they compare in making a song popular. "
st.markdown("Comparing Audio Features:")
st.markdown(multi)

x_column = st.selectbox('Select the audio feature for the X axis', audio_features)
y_column = st.selectbox('Select the audio feature for the Y axis', audio_features)

scatter_plot(x_column, y_column, x_column,  y_column)
st.markdown("Next, I am going to show all of the features to see which ones have the greatest correlation. ")
correlation_heatmap()
st.markdown("From this you can conclude that...")
st.markdown("- energy and loudness(0.8)")
st.markdown("- danceability and valence(0.4)")
st.markdown("- energy and valence(0.4)")
st.markdown("- loudness and valence(0.4)")
st.markdown("have the greatest correlations with each other.")
st.markdown("*Let's take a closer look at each of these features*")

