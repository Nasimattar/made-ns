import os
import sqlite3
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset is pulled from Kaggle, the credentials need to be provided.
api = KaggleApi()
api.authenticate()

dataset1 = 'chiticariucristian/deforestation-and-forest-loss'
dataset2 = 'ulrikthygepedersen/co2-emissions-by-country'

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
response_csv = api.dataset_download_files(dataset1, path=data_dir, unzip=True)
response_csv = api.dataset_download_files(dataset2, path=data_dir, unzip=True)
print("CSV files downloaded and unzipped successfully. Converting to a database...")
csv_file1 = os.path.join(data_dir, 'annual-change-forest-area.csv')
csv_file2 = os.path.join(data_dir, 'co2_emissions_kt_by_country.csv')

try:
    pd_csv1 = pd.read_csv(csv_file1)
    pd_csv2 = pd.read_csv(csv_file2)
    os.makedirs(os.path.dirname("../data/pipeline.db"), exist_ok=True)
    connection = sqlite3.connect("../data/pipeline.db")
    pd_csv1.to_sql("deforestation", connection, if_exists="replace", index=False)
    pd_csv2.to_sql("co2", connection, if_exists="replace", index=False)
    connection.close()
    print("Database saved in 'data' directory successfully.")
    os.remove(csv_file1)
    os.remove(csv_file2)
except Exception as e:
    print(f"Error: {e}")

