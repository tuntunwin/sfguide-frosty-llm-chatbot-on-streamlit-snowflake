import pandas as pd
from sqlalchemy import create_engine

# Create a SQLAlchemy engine to connect to the SQL Server
server = 'localhost'
database = 'LTA'
username = 'sa'
password = 'Secr3t999'
driver = 'ODBC Driver 17 for SQL Server'
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')

def query(sql):
    return pd.read_sql(sql, engine) 