from flask import Flask, redirect, url_for, request, 
import requests
import json

api_koinex = 'https://koinex.in/api/ticker'
api_buyucoin = 'https://www.buyucoin.com/api/v1/crypto/'

app = Flask(__name__)

#user = "" 
@app.route("/",methods = ['POST', 'GET'])
def select_currency():
   if request.method == 'POST':
      user = request.form['nm']
      if user == 'ETH':
         bid_koinex =  check_price_ETH()		
      #return 'You have selected %s having bid value INR %s' % (user, bid_koinex)
	  return  render_templatete(crypto_alert.html)
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
        return ETH_Koinex
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9211)


 


