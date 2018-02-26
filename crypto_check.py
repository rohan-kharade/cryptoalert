from flask import Flask,render_template, redirect, url_for, request 
import requests
import json

# ----- Different Crypto Trading Platforms ---------#
api_btcx = 'https://m.btcxindia.com/api/ticker'
api_koinex = 'https://koinex.in/api/ticker'
api_buyucoin = 'https://www.buyucoin.com/api/v1/crypto/'
api_ethex = 'https://api.ethexindia.com/ticker/'


app = Flask(__name__)
@app.route("/",methods = ['POST', 'GET'])
def select_currency():
   if request.method == 'POST':
      coin = request.form['nm']
      if coin == 'ETH':
          bid_koinex, bid_BuyUcoin =  check_price_ETH()
          templateData = {'coin': coin,'price_koinex': bid_koinex,'price_buyucoin': bid_BuyUcoin}		
          return  render_template('crypto_alert.html',**templateData)
      elif coin == 'LTC':
          bid_koinex, bid_BuyUcoin =  check_price_LTC()
          templateData = {'coin': coin,'price_koinex': bid_koinex,'price_buyucoin': bid_BuyUcoin}		
          return  render_template('crypto_alert.html',**templateData)
      elif coin == 'XRP':
          bid_koinex, bid_BuyUcoin =  check_price_XRP()
          templateData = {'coin': coin,'price_koinex': bid_koinex,'price_buyucoin': bid_BuyUcoin}		
          return  render_template('crypto_alert.html',**templateData) 
      elif coin == 'BTC':
          bid_koinex, bid_BuyUcoin =  check_price_BTC()
          templateData = {'coin': coin,'price_koinex': bid_koinex,'price_buyucoin': bid_BuyUcoin}		
          return  render_template('crypto_alert.html',**templateData)  
      elif coin == 'BCH':
          bid_koinex, bid_BuyUcoin =  check_price_BCH()
          templateData = {'coin': coin,'price_koinex': bid_koinex,'price_buyucoin': bid_BuyUcoin}		
          return  render_template('crypto_alert.html',**templateData) 
   else:
      user = request.args.get('nm')
      return 'You have selected %s having bid value %s' % user % bid_koinex


def check_price_ETH():
        i = requests.get(api_buyucoin)
        j = i.json()
        ETH_BuyUcoin=j['BuyUcoin_data'][0]['eth_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        ETH_Koinex=l['prices']['ETH']
        return ETH_Koinex, ETH_BuyUcoin

def check_price_XRP():
        i = requests.get(api_buyucoin)
        j = i.json()
        XRP_BuyUcoin=j['BuyUcoin_data'][0]['xrp_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        XRP_Koinex=l['prices']['XRP']
        return XRP_Koinex,XRP_BuyUcoin

def check_price_BTC():
        i = requests.get(api_buyucoin)
        j = i.json()
        BTC_BuyUcoin=j['BuyUcoin_data'][0]['btc_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        BTC_Koinex=l['prices']['BTC']
        return BTC_Koinex,BTC_BuyUcoin

def check_price_LTC():
        i = requests.get(api_buyucoin)
        j = i.json()
        LTC_BuyUcoin=j['BuyUcoin_data'][0]['ltc_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        LTC_Koinex=l['prices']['LTC']
        return LTC_Koinex,LTC_BuyUcoin

def check_price_BCH():
        i = requests.get(api_buyucoin)
        j = i.json()
        BCH_BuyUcoin=j['BuyUcoin_data'][0]['bcc_buy_price']
        k = requests.get(api_koinex)
        l = k.json()
        BCH_Koinex=l['prices']['BCH']
        return BCH_Koinex,BCH_BuyUcoin
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9211)


 


