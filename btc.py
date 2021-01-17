import requests
import json
import time

befCurrent = float(0)

while True:
	response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=IDR')
	data = json.loads(response.text)
	price = '{:,.2f}'.format(float(data["data"]["amount"]))
	if befCurrent != float(data["data"]["amount"]):	
		if befCurrent < float(data["data"]["amount"]):
			keterangan = "NAIK"
		else:
			keterangan = "TURUN"

		befCurrent = float(data["data"]["amount"])
		print('Rp. ' + price + ' (' + keterangan + ')')
	time.sleep(15)

