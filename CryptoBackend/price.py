import requests
import json
import time

# GLOBAL VARIABLES
payload={}
# symbol = "ETHBUSD"
# data_list = []

# BASE_URL = "https://api.binance.com"
# API_KEY = "eba2hrjHECrvuHsG6UTpcEYcPKjE6wi1HtOwixM4lb9REq3iaT4mIjepW90nnyCB"

# binance_qry - Query the binance API
# @binance_base_url: Binance's Base URL parameter.
# @symbol: Symbol used to query the Binance API, e.g BTCBNB.
# @api_key: API KEY required to query the binance API.
# Return: The response API data in JSON
def binance_qry(binance_base_url: str, symbol: str, api_key: str):
  
  # API call happens here
  headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': api_key
  }
  
  url = f"{binance_base_url}/sapi/v1/margin/priceIndex?symbol={symbol}"

  # response = None

  try:
    response = requests.request("GET", url, headers=headers, data=payload).json()
    return response
  except requests.exceptions.ConnectionError as e:
    print("Something went wrong. Check your internet connection")
    exit()
  except response is None as e:
    print("No data gotten from the binance API")
  else:
    print("Something else happened")

# i = 0
# while i < 10:
#   newdata = binance_qry(BASE_URL, symbol, API_KEY)
#   data_list.append(newdata)
#   time.sleep(1)
#   i += 1
# print(data_list)
