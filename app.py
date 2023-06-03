import streamlit as st
import pickle
from PIL import Image
import pandas as pd
import requests


def movie_details(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    poster = "https://image.tmdb.org/t/p/w500" + data['poster_path']
    budget = data['budget']
    overview = data['overview']
    revenue = data['revenue']
    popularity = data['popularity']
    return poster, budget, overview, revenue, popularity



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_budget = []
    recommended_movies_overview =[]
    recommended_movies_revenue = []
    recommended_movies_popularity = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch movie_details from API

        mov_poster, mov_budget, mov_overview, mov_revenue, mov_popularity = movie_details(movie_id)
        recommended_movies_posters.append(mov_poster)
        recommended_movies_budget.append(mov_budget)
        recommended_movies_overview.append(mov_overview)
        recommended_movies_revenue.append(mov_revenue)
        recommended_movies_popularity.append(mov_popularity)




    return recommended_movies, recommended_movies_posters, recommended_movies_budget, recommended_movies_overview, recommended_movies_revenue, recommended_movies_popularity


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pickle', 'rb'))

# ---- Page title --- #

image = Image.open("recommender.png")
st.image(image, use_column_width=True)

st.title(' Movie Recommender System')



selected_movie_name = st.selectbox(
    'Select Any Movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, budget, overview, revenue, popularity = recommend(selected_movie_name)

    col1, col2, col3, col4  = st.columns([1,1.5,1,1.5])
    with col1:
        st.image(posters[0])

    with col2:
        st.write('Title : ', names[0])
        st.write('Budget : ', budget[0])
        st.write('Revenue : ', revenue[0])
        st.write('Popularity : ', popularity[0])
        st.write('Overview : ', overview[0])

    with col3:
        st.image(posters[1])

    with col4:
        st.write('Title : ', names[1])
        st.write('Budget : ', budget[1])
        st.write('Revenue : ', revenue[1])
        st.write('Popularity : ', popularity[1])
        st.write('Overview : ', overview[1])

    col5, col6, col7, col8 = st.columns([1,1.5,1,1.5])
    with col5:
        st.image(posters[2])

    with col6:
        st.write('Title : ', names[2])
        st.write('Budget : ', budget[2])
        st.write('Revenue : ', revenue[2])
        st.write('Popularity : ', popularity[2])
        st.write('Overview : ', overview[2])
    with col7:
        st.image(posters[3])

    with col8:
        st.write('Title : ', names[3])
        st.write('Budget : ', budget[3])
        st.write('Revenue : ', revenue[3])
        st.write('Popularity : ', popularity[3])
        st.write('Overview : ', overview[3])


    col9, col10, col11, col12 = st.columns([1,1.5,1,1.5])

    with col9:
        st.image(posters[4])

    with col10:
        st.write('Title : ', names[4])
        st.write('Budget : ', budget[4])
        st.write('Revenue : ', revenue[4])
        st.write('Popularity : ', popularity[4])
        st.write('Overview : ', overview[4])

    with col11:
        st.image(posters[5])

    with col12:
        st.write('Title : ', names[5])
        st.write('Budget : ', budget[5])
        st.write('Revenue : ', revenue[5])
        st.write('Popularity : ', popularity[5])
        st.write('Overview : ', overview[5])





    col13, col14, col15, col16 = st.columns([1,1.5,1,1.5])
    with col13:
        st.image(posters[6], use_column_width = True)

    with col14:
        st.write('Title : ', names[6])
        st.write('Budget : ', budget[6])
        st.write('Revenue : ', revenue[6])
        st.write('Popularity : ', popularity[6])
        st.write('Overview : ', overview[6])

    with col15:
        st.image(posters[7], use_column_width = True)

    with col16:
        st.write('Title : ', names[7])
        st.write('Budget : ', budget[7])
        st.write('Revenue : ', revenue[7])
        st.write('Popularity : ', popularity[7])
        st.write('Overview : ', overview[7])






