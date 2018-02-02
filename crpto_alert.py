import requests
import json
import urllib.request
import urllib.parse
import time

# check_price function is used to get price from different trading platform APIs
# def select_coin(): // currency selection to get notified
print ("Select Coin : \n\t ETH \n\t BTC \n\t XRP \n\t LTC \n\t BCH \n"),
coin = input()
print ("Selected coin :-", coin)

def check_price_BTC_ETC_koinex():
	Koinex_api = 'https://koinex.in/api/ticker'
	# Zebpay_api, btcx_api, ethex_api
	r = requests.get(Koinex_api)
	j = r.json()
	return j['prices']['BTC'],j['prices']['ETH'] # j['prices']['selected_coins']

# send_SMS function is used to send trading alert via SMS using textlocal's SMS gateway API

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

Bitcoin_Sell = 0.0
while (Bitcoin_Sell < 140000.0):
	Bitcoin_Sell, ETH_Sell = check_price_BTC_ETC_koinex()
	print ("Bitcoin Sell :-",Bitcoin_Sell,"INR")
	print ("ETH Sell     :-",ETH_Sell,"INR")
	time.sleep (10)

resp =  sendSMS('bAZAwXcHereYourSMSapikeyBmSBy7512njuIAwR1chB676', '919689164280',
    'you@email.com', Bitcoin_Sell)
print (resp)

# learn_trade(): function to understand progress curve of trading and notify subscriber accordingly	



