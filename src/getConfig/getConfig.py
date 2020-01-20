#!python3
import requests
import json

def getConfig(self):
    url = 'http://'+self.ip+':'+str(self.port)+'/rtuGetConfig'
    querystring = {"cb":"1574803349"}

    headers = {
        'cache-control': "no-cache",
    }

    res = requests.request("GET",url, headers=headers,params=querystring)
    if (res.status_code == 200):
        self.config = res.json()
        return self.config
    else:
        print('Failed to receive rtuGetConfig response')
        print('Status code: ' + str(res.status_code))
        print('Reason: ' + res.reason)
        print(res.text)
