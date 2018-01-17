import requests
import json
import urllib.request
import urllib.parse
import time


def check_Bitcoin_price_koinex():
	Koinex_URL = 'https://koinex.in/api/ticker'
	r = requests.get(Koinex_URL)
	j = r.json()
	return j['prices']['BTC'],j['prices']['ETH']
	#return j['sell'],j['buy']
		
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


#while (Bitcoin_Sell < 900000.0):
while (1):
	Bitcoin_Sell, ETH_Sell = check_Bitcoin_price_koinex()
	print ("Bitcoin Sell :-",Bitcoin_Sell,"INR")
	print ("ETH Sell     :-",ETH_Sell,"INR")
	time.sleep (2)


#resp =  sendSMS('bAZAwXcCoik-Y2NCBTXBmSBy7512njuIAwR1chB676', '919689164280',
 #   'support@wibronet.com', Bitcoin_Sell)
#print (resp)

	



