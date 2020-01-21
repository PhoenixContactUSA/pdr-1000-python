#!python3
import requests
import json
import time

def getConfig(self):
    url = 'http://'+self.ip+':'+str(self.port)+'/rtuGetConfig'
    t = str(int(time.time()))
    querystring = {"cb":t}

    headers = {
        'cache-control': "no-cache",
    }

    try:
        res = requests.request("GET",url, headers=headers,params=querystring)
        if (res.status_code == 200):
            self.config = res.json()
            self.initialized = True
            return self.config
        else:
            print('Failed to receive rtuGetConfig response')
            print('Status code: ' + str(res.status_code))
            print('Reason: ' + res.reason)
            print(res.text)
    except requests.exceptions.RequestException as e:
        raise e
    
