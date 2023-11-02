import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.title("Movie Recommendation System (Pero Lite Ra Lods)")

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


select_value = st.selectbox("Search ug Movie Lods",movies_list)

def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations"):
  movie_title, movie_poster = recommend(select_value)
  col1,col2,col3,col4,col5 = st.columns(5)
  with col1 :
    st.text(movie_title[0])
    st.image(movie_poster[0])
  with col2 :
    st.text(movie_title[1])
    st.image(movie_poster[1])
  with col3 :
    st.text(movie_title[2])
    st.image(movie_poster[2])
  with col4 :
    st.text(movie_title[3])
    st.image(movie_poster[3])
  with col5 :
    st.text(movie_title[4])
    st.image(movie_poster[4])




# HOW TO RUN ON BROWSWER
# python -m streamlit run your_script.py
# python -m streamlit run app.py
#==========OR=========#
# streamlit run app.py