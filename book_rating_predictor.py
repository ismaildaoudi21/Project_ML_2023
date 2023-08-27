import pickle

import pandas as pd
from joblib import load

# Specify the file paths where the encoding maps are saved
publisher_encoding_map_file_path = "publisher_encoding_map.pkl"
authors_encoding_map_file_path = "authors_encoding_map.pkl"

# Load the encoding_map from the file
with open(publisher_encoding_map_file_path, "rb") as file:
    publisher_encoding_map = pickle.load(file)

# Load the encoding_map from the file
with open(authors_encoding_map_file_path, "rb") as file:
    authors_encoding_map = pickle.load(file)

model = load("book_rating_predictor.joblib")

# Change the publisher and authors to those of any book to predict the average rating
book_to_predict = pd.DataFrame(
    {
        "publisher": "Scholastic",
        "authors": "J.K. Rowling",
    },
    index=[0],
)

book_to_predict["publisher_encoded"] = book_to_predict["publisher"].map(publisher_encoding_map)
book_to_predict["authors_encoded"] = book_to_predict["authors"].map(authors_encoding_map)

print(book_to_predict)

book_to_predict = book_to_predict[["publisher_encoded", "authors_encoded"]]

print(book_to_predict)

prediction = model.predict(book_to_predict)

print(prediction)
