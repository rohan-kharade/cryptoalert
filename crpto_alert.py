import requests
import json
import urllib.request
import urllib.parse
import time

#def select_coin(): 
print ("Select Coin : \n\t ETH \n\t BTC \n\t XRP \n\t LTC \n\t BCH \n"),
coin = input()
print ("Selected coin :-", coin)

# ----- Different Crypto Trading Platforms ---------#
api_btcx = 'https://m.btcxindia.com/api/ticker'
api_koinex = 'https://koinex.in/api/ticker'
api_buyucoin = 'https://www.buyucoin.com/api/v1/crypto/'
api_ethex = 'https://api.ethexindia.com/ticker/'

# check_price function is used to get price from different trading platform APIs
def check_price_XRP():
        i = requests.get(api_buyucoin)
        j = i.json()
        XRP_BuyUcoin=j['BuyUcoin_data'][0]['xrp_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        XRP_Koinex=l['prices']['XRP']
        return XRP_BuyUcoin,XRP_Koinex

def check_price_BTC():
        i = requests.get(api_buyucoin)
        j = i.json()
        BTC_BuyUcoin=j['BuyUcoin_data'][0]['btc_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        BTC_Koinex=l['prices']['BTC']
        return BTC_BuyUcoin,BTC_Koinex

def check_price_ETC():
        print("hello")

if coin == 'XRP' :
        print ('hi')
        xrp_bid_buyucoin,xrp_bid_koinex =  check_price_XRP()
       # print ("ETH bid BTCX   :-",xrp_bid_btcx,"INR")
        print ("XRP buy Koinex     :-",xrp_bid_koinex,"INR")
        print ("XRP buy Buyucoin   :-",xrp_bid_buyucoin,"INR")

elif coin == 'BTC' :
        btc_bid_buyucoin,btc_bid_koinex =  check_price_BTC()
       # print ("ETH bid BTCX   :-",xrp_bid_btcx,"INR")
        print ("BTC buy Koinex     :-",btc_bid_koinex,"INR")
        print ("BTC buy Buyucoin   :-",btc_bid_buyucoin,"INR")

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
	print ("Here in while loop for 10 s")
	time.sleep (10)



resp =  sendSMS('bAZAwXcHereYourSMSapikeyBmSBy7512njuIAwR1chB676', '919689164280',
    'you@email.com', Bitcoin_Sell)
print (resp)

# learn_trade(): function to understand progress curve of trading and notify subscriber accordingly	



