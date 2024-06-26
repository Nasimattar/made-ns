import os
import sqlite3
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_process_data():
    # Dataset is pulled from Kaggle, the credentials need to be provided.
    api = KaggleApi()
    api.authenticate()

    dataset1 = 'chiticariucristian/deforestation-and-forest-loss'
    dataset2 = 'ulrikthygepedersen/co2-emissions-by-country'

    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print(f"Downloading datasets to {data_dir}")
    api.dataset_download_files(dataset1, path=data_dir, unzip=True)
    api.dataset_download_files(dataset2, path=data_dir, unzip=True)
    print("CSV files downloaded and unzipped successfully. Converting to a database...")
    
    csv_file1 = os.path.join(data_dir, 'annual-change-forest-area.csv')
    csv_file2 = os.path.join(data_dir, 'co2_emissions_kt_by_country.csv')

    try:
        pd_csv1 = pd.read_csv(csv_file1)
        pd_csv2 = pd.read_csv(csv_file2)
        db_path = os.path.join(data_dir, "pipeline.db")
        connection = sqlite3.connect(db_path)
        pd_csv1.to_sql("deforestation", connection, if_exists="replace", index=False)
        pd_csv2.to_sql("co2", connection, if_exists="replace", index=False)
        connection.close()
        print(f"Database saved at {db_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_and_process_data()