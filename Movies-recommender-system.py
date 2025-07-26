import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=cb074d7380106f7d68c25e5991b98c1d&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
   

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:8]
  recommended_movies = []
  recommended_movies_posters = []   
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_posters

movies_list = pickle.load(open(r'C:\Users\PC\Desktop\Movies-recommender\Movie-Recommendation-System\movies.pkl', 'rb'))
similarity = pickle.load(open(r'C:\Users\PC\Desktop\Movies-recommender\Movie-Recommendation-System\similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

st.title('Movies Recommender System')
selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):    
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
