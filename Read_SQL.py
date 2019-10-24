import pandas as pd
import pandasql as pdsql
import sqlite3
from datetime import date
from datetime import datetime



def read_sql_btc():

  conn = sqlite3.connect('DB/DB_COINS.db')

  sql_datas = f"""
                    SELECT * FROM VARBTC;
  """

  read_db = pd.read_sql_query(sql_datas, conn)
  conn.close()

  return read_db

def read_sql_wallet():

  conn = sqlite3.connect('DB/DB_COINS.db')

  sql_datas = f"""
                    SELECT * FROM WALLET;
  """

  read_db = pd.read_sql_query(sql_datas, conn)
  conn.close()

  return read_db