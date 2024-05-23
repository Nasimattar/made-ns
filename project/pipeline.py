import os
import sqlite3
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset is pulled from Kaggle, the credentials need to be provided.
api = KaggleApi()
api.authenticate()

dataset = 'shubhammaindola/tmdb-top-rated-movies-dataset'

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
response_csv = api.dataset_download_files(dataset, path=data_dir, unzip=True)
print("CSV file downloaded and unzipped successfully. Converting to a database...")
csv_file = os.path.join(data_dir, 'movie_dataset.csv')

try:
    pd_csv = pd.read_csv(csv_file)
    os.makedirs(os.path.dirname("../data/movies.db"), exist_ok=True)
    connection = sqlite3.connect("../data/movies.db")
    pd_csv.to_sql("movies", connection, if_exists="replace", index=False)
    connection.close()
    print("Database saved in 'data' directory successfully.")
    os.remove(csv_file)
except Exception as e:
    print(f"Error occured: {e}")
