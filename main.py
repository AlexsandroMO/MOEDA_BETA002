#https://imasters.com.br/desenvolvimento/conhecendo-o-jinja2-um-mecanismo-para-templates-no-flask


##########################################
#PROJETO PYTHON TRAIDE
#CREATE BY: Alexsandro M. Oliveira
#DATE: 16/08/2019
##########################################

from tinydb import TinyDB, where, Query
import pandas as pd
import lxml
import json
import requests
import re
from datetime import date
from datetime import datetime
from datetime import date, datetime
import time
import Read_SQL
import Write_SQL
import os



class VarBitcoin():
  def __init__(self, btc_last, btc_buy, btc_sell, btc_date, date_btc, btc_buy_save, btc_sell_save):
    self.btc_last = btc_last
    self.btc_buy = btc_buy
    self.btc_sell = btc_sell
    self.btc_date = btc_date
    self.date_btc = date_btc
    self.btc_buy_save = btc_buy_save
    self.btc_sell_save = btc_sell_save

class DollarEuro():
  def __init__(self, dollar, euro, dollar_date, euro_date):
    self.dollar = dollar
    self.euro = euro
    self.dollar_date = dollar_date
    self.euro_date = euro_date
    
class VarWallet():
  def __init__(self, inicial_wallet, wallet_current, win_lose, wallet_floating_value, wallet_btc, wallet_buy,  wallet_sell, wallet_set_buy, wallet_set_sell, last_var_buy, last_var_sell, cont):
    
    self.inicial_wallet = inicial_wallet
    self.wallet_current = wallet_current
    self.win_lose = win_lose
    self.wallet_floating_value = wallet_floating_value
    self.wallet_btc = wallet_btc
    self.wallet_pay = wallet_buy
    self.wallet_sell = wallet_sell
    self.wallet_set_pay = wallet_set_buy
    self.wallet_set_sell = wallet_set_sell
    self.last_var_buy =  last_var_buy
    self.last_var_sell = last_var_sell
    self.cont = cont

#=====================================================================


def run():
  dados = [['BITICOIN', BTC.btc_last, BTC.btc_buy, BTC.btc_sell, BTC.date_btc, '-'],
         ['DOLAR', USD_EUR.dollar, '-', '-', USD_EUR.dollar_date, '-'],
         ['EURO', USD_EUR.euro, '-', '-', USD_EUR.euro_date, '-']
        ]

  df = pd.DataFrame(data=dados,columns=['MOEDA', 'ULTIMA_TRANS', 'COMPRA', 'VENDA', 'DATA','STATUS'])
  print('--------------------------------------------------------------------')

  print(df)

  Write_SQL.add_var_bitcoin(BTC.btc_last,BTC.btc_buy,BTC.btc_sell,BTC.date_btc)



#===================================================================================
#Aplication Base
def loop_prog():
  current_date = datetime.now()
  now_date = current_date.strftime('%d/%m/%Y %H:%M:%S')

  list_btc = requests.get('https://api.bitcointrade.com.br/v2/public/BRLBTC/ticker')
  btc_cotation = json.loads(list_btc.text)
  btc_last = btc_cotation['data']['last']
  btc_buy = btc_cotation['data']['buy']
  btc_sell = btc_cotation['data']['sell']

  btc_buy_save = btc_buy #Ultimo Biticoin compra salvo
  btc_sell_save = btc_sell #Ultimo Biticoin compra salvo

  cont = 0

  my_wallet = VarWallet(inicial_wallet, wallet_current, win_lose, wallet_floating_value, wallet_btc, wallet_pay,  wallet_sell, wallet_set_pay, wallet_set_sell, last_var_buy, last_var_sell, cont)

  lista_vars = [btc_last, btc_buy_save, btc_sell_save,my_wallet.wallet_current, my_wallet.win_lose, my_wallet.wallet_btc, my_wallet.win_lose]

  return lista_vars

#======================================================================
#Start Aplication

list_btc = requests.get('https://api.bitcointrade.com.br/v2/public/BRLBTC/ticker')
btc_cotation = json.loads(list_btc.text)
btc_buy = btc_cotation['data']['buy']
btc_sell = btc_cotation['data']['sell']

inicial_wallet = 5000.00 #Quantidade de Bitcoins comprados inicialemente na transação
wallet_current = inicial_wallet #Valor atual da carteira que inicialmente é o valor da carteira
win_lose = 0.00 #Ganhos e perdas da transação
wallet_floating_value = wallet_current + win_lose #valor atual + os ganhos ou - as perdas
wallet_btc = wallet_floating_value / btc_buy #Valor em Biticoins
wallet_pay = 500.00 #Valor a comprar
wallet_sell = 800.00 #Valor a vender
wallet_set_pay = 43500.00 #Valor quando comprar
wallet_set_sell = 43800.00 #Valor quando vender
last_var_buy = btc_buy #Ultimo valor de compra
last_var_sell = btc_sell #Ultimo valor de venda


loop_coin = 0
xxx = 0

while loop_coin == 0:
  
  lista_vars = loop_prog()

  print("\n" * 500)
  print('\n\n=================================')
  print('LAST_BTC: ', lista_vars[0])
  print('=================================\n')

  xxx += 1
  print('\n>>>>>>>>>>>>>> Ciclo de Transação: ', xxx)
  
  current_date = datetime.now()
  now_date = current_date.strftime('%d/%m/%Y %H:%M:%S')

  #hj = TimeNow(now_date)

  list_btc = requests.get('https://api.bitcointrade.com.br/v2/public/BRLBTC/ticker')
  list_usd_eur = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL')
  btc_cotation = json.loads(list_btc.text)
  usd_eur_cotation = json.loads(list_usd_eur.text)
  #-------------------------------------------------------
  btc_last = btc_cotation['data']['last'] # Ultimo Biticoin negociado
  btc_buy = btc_cotation['data']['buy']
  btc_sell = btc_cotation['data']['sell']
  btc_date = btc_cotation['data']['date']
  date_btc = btc_date[:len(btc_date)-14:] + ' ' + btc_date[11:len(btc_date)-5:]
  last_var = btc_last #<<<<<<<<<<<
  #-------------------------------------------------------
  dollarR = usd_eur_cotation['USD']['high']
  dollarL = usd_eur_cotation['USD']['low']
  dollar_date = usd_eur_cotation['USD']['create_date']
  test_x = dollarR.split(',')
  x = float(test_x[0] + '.' + test_x[1])
  test_y = dollarL.split(',')
  y = float(test_y[0] + '.' + test_y[1])
  dollar = round((x + y) / 2,2)
  #-------------------------------------------------------
  euroR = usd_eur_cotation['EUR']['high']
  euroL = usd_eur_cotation['EUR']['low']
  euro_date = usd_eur_cotation['EUR']['create_date']
  test_x = euroR.split(',')
  x = float(test_x[0] + '.' + test_x[1])
  test_y = euroL.split(',')
  y = float(test_y[0] + '.' + test_y[1])
  euro = round((x + y) / 2,2)
  #-------------------------------------------------------
  #btc_buy_save,   btc_sell_save                                            
  BTC = VarBitcoin(btc_last, btc_buy, btc_sell, btc_date, date_btc, lista_vars[0], lista_vars[2])

  USD_EUR = DollarEuro(dollar, euro, dollar_date, euro_date)

  run()

  print('--------------------------------------------------------------------------------------------')
  #my_wallet_control = round((my_wallet.wallet_current + my_wallet.win_lose),2)
  #fraction_btc = round(my_wallet.wallet_btc,2)
  #profit = round(my_wallet.win_lose,2)

  my_wallet_control = round((lista_vars[3] + lista_vars[4]),2)
  btc_var = round(BTC.btc_last,2)
  fraction_btc = round(lista_vars[5],2)
  profit = round(lista_vars[6],2)

  print('VALOR NA CARTEIRA: {} | BTC: {} | FRAÇÃO CARTEIRA EM BTC: {} | VALOR LUCRO: {}'.format(my_wallet_control, btc_var, fraction_btc, profit))
  print('--------------------------------------------------------------------------------------------\n')

  BTC.btc_buy_save = BTC.btc_buy
  BTC.btc_sell_save = BTC.btc_sell

  Write_SQL.add_var_wallet(my_wallet_control,profit,now_date)

  #print(Read_SQL.read_sql_btc())

  print('\n\n--------------------------------')
  #print(Read_SQL.read_sql_wallet())
  print('\n\n')

  
  time.sleep(20)

  
  
#os.system('cls' if os.name == 'nt' else 'clear')

