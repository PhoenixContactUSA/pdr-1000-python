#!python3
import requests

def getConfig(self):
    url = 'http://'+self.ip+'/rtuGetConfig'
    querystring = {"cb":"1574803349"}

    headers = {
        'cache-control': "no-cache",
    }

    res = requests.request("GET",url, headers=headers,params=querystring)
    if (res.status_code == 200):
        print(res.json())
    else:
        print('Failed to receive rtuGetConfig response')
        print(res.text)
