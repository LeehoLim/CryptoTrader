from binance.client import Client
from binance.exceptions import BinanceAPIException
import pandas as pd 
import time 
import logging


#Updates: 23.03.18 - defining some functions... do we also want cross exchange arb model?
#Only Binance? 


#Probably want a historical data func
def historical_data(market, timeframe, from_):
	return None

#Current Price
def current_price(market):
	return None

#Market Buy
def market_buy(market, amt):
	return None

#Market Sell
def market_sell(market, amt):
	return None

#Check Current Wallet Balance
def balance():
	return None