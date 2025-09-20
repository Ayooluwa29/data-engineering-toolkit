import os
from sqlalchemy import create_engine
from google.colab import userdata

DB_USER = userdata.get('DB_USER')
DB_PASS = userdata.get('DB_PASS')
DB_HOST = userdata.get('DB_HOST')
DB_PORT = "5435"
DB_NAME = "postgres"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

try:
    with engine.connect() as connection:
      print("Connection successful!")
      record_no = df.to_sql('sales_data', connection, if_exists='replace', index=False)
      print(f"{record_no} rows of data loaded!")
except Exception as e:
  print(f"Failed to connect: {e}")
