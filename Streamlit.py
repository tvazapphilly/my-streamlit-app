import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st
import numpy as np

df1 = pd.read_csv("high_popularity_spotify_data[1].csv")
df2 = pd.read_csv("low_popularity_spotify_data[1].csv")
df = pd.concat([df1, df2])

audio_features = ['energy', 'tempo', 'danceability','loudness','liveness','valence','speechiness','instrumentalness','mode','key','duration_ms','acousticness']

# Removing duplicate labels from the DataFrame index
df = df[~df.index.duplicated()]
df = df.reset_index(drop=True)

def scatter_plot(x,y, x_label, y_label):
    fig, ax = plt.subplots()
    sn.scatterplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(f'{x_label} vs {y_label}')
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
st.markdown("**Main Idea:**")
st.markdown(
    """
    I want to analyze the factors that contribute to the popularity of different songs on Spotify by examining their audio features such as energy, tempo, danceability, and more. By using this data and visualizations, this project aims to identify the correlations among these features,and ultimately uncover insights into what makes a song popular. Understanding these patterns can provide valuable information for artists, producers, and the music industry in general, helping people craft songs that resonate with audiences and achieve popularity on streaming platforms like Spotify.
    """
)

st.markdown("**Table of Definitions:**")
st.markdown(
    """
    | **Audio Feature**    | **Definition**                                                                                   |
    |----------------------|--------------------------------------------------------------------------------------------------|
    | **Energy**           | A measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.        |
    | **Tempo**            | The speed of a track, measured in beats per minute (BPM).                                |
    | **Danceability**     | A score describing how suitable a track is for dancing based on tempo, rhythm stability, beat strength and overall regularity.|
    | **Loudness**         | The overall loudness of a track in decibels (dB). Higher values indicate louder tracks overall.                                 |
    | **Liveness**         | The likelihood of a track being performed live. Higher values suggest more audience presence.|
    | **Valence**          | The overall musical positiveness(emotion) of a track. High valence sounds happy; low valence sounds sad or angry.|
    | **Speechiness**      | Measures the presence of spoken words.     |
    | **Instrumentalness** | TThe likelihood a track contains no vocals. Values closer to 1.0 suggest solely instrumental tracks. |
    | **Mode**             | Indicates the modality of the track.                    |
    | **Key**              | The musical key, represented as an integer from 0 to 11, mapping to standard Pitch class notation.                  |
    | **Duration**         | The length of the track, measured in milliseconds.                                              |
    | **Acousticness**     | A confidence measure of whether a track is acoustic(1) or not(0).    |
    """
)

multi = "- Pick 2 different audio features to see how they compare in making a song popular. "
st.markdown("Comparing Audio Features:")
st.markdown(multi)

x_column = st.selectbox('Select the audio feature for the X axis', audio_features)
y_column = st.selectbox('Select the audio feature for the Y axis', audio_features)

scatter_plot(x_column, y_column, x_column,  y_column)
st.markdown("Next, I am going to show all of the features to see which ones have the greatest correlation. ")
correlation_heatmap()

st.markdown(
    """
    This heatmap provides a clear visual comparison of how each audio feature compares with one another. Red boxes indicate a stronger correlation, while blue boxes signify a weaker correlation.
    """
)

st.markdown("So, by looking at the top 5 correlations...")
st.markdown("- energy and loudness(0.8)")
st.markdown("- danceability and loudness(0.6)")
st.markdown("- danceability and valence(0.6)")
st.markdown("- energy and valence(0.5)")
st.markdown("- energy and danceability(0.5)")
st.markdown("have the strongest relationships with each other.")
st.markdown("*Let's take a closer look at each of these features*")

def scatter_plot():
    fig, ax = plt.subplots()
    sn.scatterplot(x='energy', y='loudness', data=df, ax=ax)
    ax.set_title('Energy vs Loudness')
    ax.set_xlabel('Energy')
    ax.set_ylabel('Loudness')
    st.pyplot(fig)
scatter_plot()

st.markdown(
    """
    __Energy and Loudness__: Songs that have high energy and loudness tend to be more popular. The strong correlation of 0.8 between these two audio features shows that lively, dynamic, and intense tracks are popular with listeners. Songs with high energy and loudness are often used in social settings like parties, workouts, and other events that require an upbeat atmosphere.
    """
)

def scatter_plot():
    fig, ax = plt.subplots()
    sn.scatterplot(x='danceability', y='loudness', data=df, ax=ax)
    ax.set_title('Danceability vs Loudness')
    ax.set_xlabel('Danceability')
    ax.set_ylabel('Loudness')
    st.pyplot(fig)
scatter_plot()


st.markdown(
    """
    __Danceablity and Loudness__: The correlation between these two features is evident as both contribute to a song's overall appeal and energy. High danceability usually means the song has a strong rhythmic groove that makes people want to move, while loudness enhances the intensity and impact of the music.
    """
)

def scatter_plot():
    fig, ax = plt.subplots()
    sn.scatterplot(x='danceability', y='valence', data=df, ax=ax)
    ax.set_title('Danceability vs Valence')
    ax.set_xlabel('Danceability')
    ax.set_ylabel('Valence')
    st.pyplot(fig)
scatter_plot()

st.markdown(
    """
    __Danceability and Valence__: Danceability measures how suitable a track is for dancing based on tempo, rhythm stability, beat strength, and overall regularity. Valence, on the other hand, indicates the musical positiveness conveyed by a track. High valence tracks sound more happy, cheerful, and euphoric. When a song combines high danceability with high valence, it becomes a feel-good anthem that's perfect for parties, celebrations, or just lifting your mood.
    """
)

def scatter_plot():
    fig, ax = plt.subplots()
    sn.scatterplot(x='energy', y='valence', data=df, ax=ax)
    ax.set_title('Energy vs Valence')
    ax.set_xlabel('Energy')
    ax.set_ylabel('Valence')
    st.pyplot(fig)
scatter_plot()

st.markdown(
    """
    __Energy and Valence__: Energy reflects the intensity and activity present in the music, while valence measures the emotional positivity conveyed. When a track is high in both, it means it's not only dynamic and intense but also cheerful and uplifting.
    """
)

def scatter_plot():
    fig, ax = plt.subplots()
    sn.scatterplot(x='energy', y='danceability', data=df, ax=ax)
    ax.set_title('Energy vs Danceability')
    ax.set_xlabel('Energy')
    ax.set_ylabel('Danceability')
    st.pyplot(fig)
scatter_plot()

st.markdown(
    """
    __Energy and Danceability__: Energy reflects the intensity and activity in the music, while danceability measures how suitable a track is for dancing based on tempo, rhythm stability, beat strength, and overall regularity. Songs that score high in both these features are dynamic, vibrant, and make you want to move.
    """
)
st.header("*So, what  really makes a song popular?*")
st.markdown(
    """
    From our data we can conclude that the most popular songs on Spotify often combine features such as high energy, loudness, danceability, and valence. These features work together to create engaging, enjoyable, and memorable listening experiences that appeal to a broad audience. By understanding and using these correlations, artists can create music that their listeners will enjoy and increases their chances of having a popular song.
    """
)
