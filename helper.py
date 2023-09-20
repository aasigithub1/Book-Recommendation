import pandas as pd
import numpy as np
import pickle

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

recommend("The Notebook")