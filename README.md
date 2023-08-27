# What is it about ?
This project is made to create a machine learning model that can predict books ratings.

# What you will find in the repository
- The "books_rating.ipynb" notebook traces back the process of how the model was created.
- The "book_rating_predictor.py" file is a script that uses the model to predict a book's rating.

# How to install (with anaconda)
```bash
conda create -n "books-rating" python=3.11

conda activate books-rating

pip install -r requirements.txt
```

# How to run
- The notebook is made to run in google colab.
- For the "book_rating_predictor.py" file : modify the publisher and authors in the "book_to_predict" DataFrame and then run :
    ```bash
    python book_rating_predictor.py
    ```
    You should see the average rating predicted in terminal.