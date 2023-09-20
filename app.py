import streamlit as st
import pandas as pd
import numpy as np
import pickle
import helper


books = pd.read_csv("books.csv")
users = pd.read_csv("users.csv")
ratings = pd.read_csv("ratings.csv")

popular_df = pickle.load(open("popular.pkl","rb"))
pt = pickle.load(open("pt.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl","rb"))
similarity_scores = list(similarity_scores)



def recommend(book_name):
    # index fetch
    index  = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books["Book-Title"] == pt.index[i[0]]] 
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        
        data.append(item)
        
    return data
#     return suggestions


st.header("Book Recommendation System")

tab1, tab2 = st.tabs(["Top Books","Recommend Books"])
with tab1:

    st.header("Top 50 Books")

    book_name = list(popular_df["Book-Title"].values)
    author = list(popular_df["Book-Author"].values)
    image = list(popular_df["Image-URL-M"].values)
    votes = list(popular_df["num_ratings"].values)
    rating = list(popular_df["avg_ratings"].values)
    rounded_list = [round(i,2) for i in rating]



    for i in range(len(book_name)):
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.image(image[i],width=120)
        col2.markdown(book_name[i])
        col3.text(author[i])
        col4.text(votes[i])
        col5.text(rounded_list[i])



with tab2:
    movies_list = books["Book-Title"].unique()

    selected_book_name = st.selectbox(
            "Select a books to get recommendation",
            pt.index)
    # title = st.text_input("Enter Book Name")
    # book_name = st.write(title)
    # book_name = str(selected_book_name)
    
    if st.button('Show Recommendation'):
        m1,m2,m3,m4,m5 = recommend(selected_book_name)
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.image(m1[0])
            st.write(m1[1])
            st.text(m1[2])
        with col2:
            st.image(m2[0])
            st.write(m2[1])
            st.text(m2[2])
        with col3:
            st.image(m3[0])
            st.write(m3[1])
            st.text(m3[2])
        with col4:
            st.image(m4[0])
            st.write(m4[1])
            st.text(m4[2])
        with col5:
            st.image(m5[0])
            st.write(m5[1])
            st.text(m5[2])
    