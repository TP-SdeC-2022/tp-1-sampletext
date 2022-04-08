from ctypes import *
import subprocess
import json
import requests
import subprocess

url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
url2 = 'http://api.exchangeratesapi.io/v1/latest?access_key=ffc3f5155ae0404d34a5be9da3a68d86'
r = requests.get(url)
r2 = requests.get(url2)
data = r.json()
data2 = r2.json()

BitcoinADolar =  data['price']
DolarAPesos =  ( float(data2['rates']['ARS'])/ float(data2['rates']['USD']))
DolarAEuros   =  data2['rates']['USD']

#data2['rates']['ARS']

print("EL precio del Bitcoin en pesos: ")
BitcoinAPesos = subprocess.run(["./ejecutable", str(BitcoinADolar) , str(DolarAPesos)], capture_output = True)

print(float(BitcoinAPesos.stdout))


print("EL precio del Bitcoin en dolares:")
print(BitcoinADolar)

print("EL precio del Bitcoin en euros: ")
BitcoinAEuros = subprocess.run(["./ejecutable", str(BitcoinADolar) , str(DolarAEuros)], capture_output = True)

print(float(BitcoinAEuros.stdout))




