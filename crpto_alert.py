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

bch_bid_buyucoin,bch_bid_koinex = 0.0
bid_value = 1.0
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

def check_price_ETH():
        i = requests.get(api_buyucoin)
        j = i.json()
        ETH_BuyUcoin=j['BuyUcoin_data'][0]['eth_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        ETH_Koinex=l['prices']['ETH']
        return ETH_BuyUcoin,ETH_Koinex

def check_price_LTC():
        i = requests.get(api_buyucoin)
        j = i.json()
        LTC_BuyUcoin=j['BuyUcoin_data'][0]['ltc_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        LTC_Koinex=l['prices']['LTC']
        return LTC_BuyUcoin,LTC_Koinex

def check_price_BCH():
        while (bch_bid_buyucoin < bid_value):
              i = requests.get(api_buyucoin)
              j = i.json()
              BCH_BuyUcoin=j['BuyUcoin_data'][0]['bcc_buy_price']
              k = requests.get(api_koinex)
              l = k.json()
              BCH_Koinex=l['prices']['BCH']
        return BCH_BuyUcoin,BCH_Koinex

if coin == 'XRP' :
        xrp_bid_buyucoin,xrp_bid_koinex =  check_price_XRP()
        print ("XRP buy Koinex     :-",xrp_bid_koinex,"INR")
        print ("XRP buy Buyucoin   :-",xrp_bid_buyucoin,"INR")

elif coin == 'BTC' :
        btc_bid_buyucoin,btc_bid_koinex =  check_price_BTC()
        print ("BTC buy Koinex     :-",btc_bid_koinex,"INR")
        print ("BTC buy Buyucoin   :-",btc_bid_buyucoin,"INR")

elif coin == 'ETH' :
        eth_bid_buyucoin,eth_bid_koinex =  check_price_ETH()
        print ("ETH buy Koinex     :-",eth_bid_koinex,"INR")
        print ("ETH buy Buyucoin   :-",eth_bid_buyucoin,"INR")

elif coin == 'LTC' :
        ltc_bid_buyucoin,ltc_bid_koinex =  check_price_LTC ()
        print ("LTC buy Koinex     :-",ltc_bid_koinex,"INR")
        print ("LTC buy Buyucoin   :-",ltc_bid_buyucoin,"INR")

elif coin == 'BCH' :
        bch_bid_buyucoin,bch_bid_koinex =  check_price_BCH ()
        print ("BCH buy Koinex     :-",bch_bid_koinex,"INR")
        print ("BCH buy Buyucoin   :-",bch_bid_buyucoin,"INR")
        print ("Enter bid value"),
        bid_value = input()

# send_SMS function is used to send trading alert via SMS using Textlocal's SMS gateway API
def sendSMS(apikey, numbers, sender, message):
    coin_data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    coin_data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, coin_data)
    fr = f.read()
    return(fr)

#while (Bitcoin_Sell < 140000.0):
#	print ("Here in while loop for 10 s")
#	time.sleep (10)

resp =  sendSMS('bAZAwXcHereYourSMSapikeyBmSBy7512njuIAwR1chB676', '919616459876543457',
    'you@email.com', Bitcoin_Sell)
print (resp)

# learn_trade(): function to understand progress curve of trading and notify subscriber accordingly	
# learn_trade():
