import pandas as pd
import pandasql as pdsql
import sqlite3
from datetime import date
from datetime import datetime
import CreateTable_SQL

#--------------------------------------------
#Adicionar dados no banco - VarBitcoin

def add_var_bitcoin(btc_last,btc_buy,btc_sell,date_btc):

  CreateTable_SQL.create_VarBTC()
  CreateTable_SQL.create_Wallet()

  conn = sqlite3.connect('DB/DB_COINS.db')
  c = conn.cursor()

  qsl_datas = f"""INSERT INTO VARBTC(VAR_BTC_LAST,VAR_BTC_BUY,VAR_BTC_SELL,VAR_BTC_DATE)
                VALUES ({btc_last},{btc_buy},{btc_sell},'{date_btc}');
  """

  c.execute(qsl_datas)

  conn.commit()
  conn.close()

def add_var_wallet(my_wallet_control,profit,date_today):

  CreateTable_SQL.create_VarBTC()
  CreateTable_SQL.create_Wallet()

  conn = sqlite3.connect('DB/DB_COINS.db')
  c = conn.cursor()

  qsl_datas = f"""INSERT INTO WALLET(VAR_WALLET,WIN_LOSE,DATE_NEGOCIATION)
                VALUES ({my_wallet_control}, {profit},'{date_today}');
  """

  c.execute(qsl_datas)

  conn.commit()
  conn.close()



