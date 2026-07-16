import streamlit as st 
import joblib
import pickle
import nltk
import sklearn
import pandas

st.title("Movie Recommendation System")


with open("data.pickle", 'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load('similarity.joblib')
movies_name = movies['title'].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    recommendation = similarity[movie_index]
    movie_list = sorted(enumerate(recommendation), reverse =True, key = lambda x:x[1])[1:10]
    the_list = []
    for i in movie_list:
        the_list.append(movies.iloc[i[0]].title)
    return the_list

name = st.selectbox("Enter the Movie Name", movies_name)

if st.button("Recommend"):
    r = recommend(name)
    st.success("Recommended Movies")

for idx, movie in enumerate(r, start=1):
    st.write(f"{idx}. {movie}")        


