import os
import sys
# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import unittest
import importlib
import pandas as pd
import sqlite3 
import pipeline

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

class TestPipelineComponents(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.deforestation_file_path = os.path.join(data_dir, 'annual-change-forest-area.csv')
    cls.co2_file_path = os.path.join(data_dir, 'co2_emissions_kt_by_country.csv')
    cls.expected_deforestation_columns = ['Entity', 'Code', 'Year', 'Net forest conversion']
    cls.expected_co2_columns = ['country_code', 'country_name', 'year', 'value']
    cls.dbname = "pipeline"
    cls.dbpath = os.path.join(data_dir, f"{cls.dbname}.db")

  @classmethod
  def tearDownClass(cls):
    if os.path.exists(cls.dbpath):
      os.remove(cls.dbpath)

  def test_data_extraction(self):
    deforestation_data = pd.read_csv(self.deforestation_file_path)
    co2_data = pd.read_csv(self.co2_file_path)

    self.assertFalse(deforestation_data.empty, msg="Deforestation data should not be empty")
    self.assertFalse(co2_data.empty, msg="CO2 emissions data should not be empty")
    self.assertListEqual(list(deforestation_data.columns), self.expected_deforestation_columns,
               msg="Deforestation data columns do not match expected columns")
    self.assertListEqual(list(co2_data.columns), self.expected_co2_columns,
               msg="CO2 emissions data columns do not match expected columns")

  def test_database_integrity(self):
    pipeline.main()

    self.assertTrue(os.path.exists(self.dbpath), msg="Database file should exist after running the pipeline.")
    
    with sqlite3.connect(self.dbpath) as conn:
      deforestation_table = pd.read_sql_query("SELECT * FROM deforestation", conn)
      co2_table = pd.read_sql_query("SELECT * FROM co2", conn)

      self.assertFalse(deforestation_table.empty, msg="The deforestation table should not be empty in the database")
      self.assertFalse(co2_table.empty, msg="The co2 table should not be empty in the database")
      self.assertListEqual(list(deforestation_table.columns), self.expected_deforestation_columns,
                 msg="The columns in the deforestation table do not match the expected columns")
      self.assertListEqual(list(co2_table.columns), self.expected_co2_columns,
                 msg="The columns in the co2 table do not match the expected columns")

if __name__ == "__main__":
  unittest.main()
