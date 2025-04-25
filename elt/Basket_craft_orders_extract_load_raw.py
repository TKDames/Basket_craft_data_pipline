"""
1. Import neceessary libraries.
2. Load source MYSQL and destination PostGres connection details
3. Build connection strings and create database engines
4. Read products table from MYSQL and load into a dataframe
5. Write dataframe to products table in Postgres. (raw schema)
"""
# %%
# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine


# %% 
os.environ['MYSQL_USER']
#%%
# MySQL database connection details
mysql_user = 'analyst'
mysql_password = 'go_lions'
mysql_host = 'db.isba.co'
mysql_db = 'basket_craft'

# Postgres database connection details
pg_user = 'postgres'
pg_password = 'isba_4715'
pg_host = 'isba-dev-02.ccns0o4cgs58.us-east-1.rds.amazonaws.com'
pg_db = 'basket_craft'

# %%
#Build connection strings
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'

# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_str)
pg_engine = create_engine(pg_conn_str)

# %%
# Read orders table from MYSQL
df = pd.read_sql('SELECT * FROM orders', mysql_engine)

# %%
df

# %%
# Write DataFrame to products table in Postgres (raw schema)
df.to_sql('orders', pg_engine, schema='raw', if_exists='replace', index=False)
# %%
print(f'{len(df)} records loaded into Postgres orders table.')
# %% 