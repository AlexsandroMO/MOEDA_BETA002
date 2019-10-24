import pandas as pd
import pandasql as pdsql
import sqlite3
from datetime import date
from datetime import datetime
import os

directory = 'DB'
dir = directory 

if not os.path.exists(directory):      
  os.makedirs(dir)



#-------------------------------------------------------
#Criar Tabela VARBITCOIN
def create_VarBTC():
  conn = sqlite3.connect('DB/DB_COINS.db')
  c = conn.cursor()

  table_createdb = f"""
    
  CREATE TABLE IF NOT EXISTS VARBTC (
    ID INTEGER PRIMARY KEY,
    VAR_BTC_LAST DOUBLE NOT NULL,
    VAR_BTC_BUY DOUBLE NOT NULL,
    VAR_BTC_SELL DOUBLE NOT NULL,
    VAR_BTC_DATE DATE NOT NULL
    )
    
    """

  c.execute(table_createdb)

  conn.commit()
  conn.close()

#-------------------------------------------------------
#Criar Tabela Wallet
def create_Wallet():
  conn = sqlite3.connect('DB/DB_COINS.db')
  c = conn.cursor()

  table_createdb = f"""
    
  CREATE TABLE IF NOT EXISTS WALLET (
    ID INTEGER PRIMARY KEY,
    VAR_WALLET DOUBLE NOT NULL,
    WIN_LOSE DOUBLE NOT NULL,
    DATE_NEGOCIATION DATE NOT NULL
    
    )
    
    """

  c.execute(table_createdb)

  conn.commit()
  conn.close()
#-------------------------



#db = TinyDB('db.json')
#Ft = Query()