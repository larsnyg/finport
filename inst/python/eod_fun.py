from eod import EodHistoricalData
import pandas as pd

# Create the instance 
client = EodHistoricalData("5b2b58da20bd52.76199398")

def get_prices_eod(symbol, period='w', order='a'):
  # weekly prices for the Swiss goverment bond
  stock_prices = client.get_prices_eod(symbol, period='w', order='a')
  stock_prices = pd.DataFrame (stock_prices)
  return stock_prices

def get_exchange_symbols(exchange):
  symbols = client.get_exchange_symbols(exchange)
  return symbols
  
def get_exchange_details(exchange):
  exchange_details = client.get_exchange_details(exchange)
  return exchange_details
  
def get_exchanges():
  exchanges = client.get_exchanges()
  return exchanges


