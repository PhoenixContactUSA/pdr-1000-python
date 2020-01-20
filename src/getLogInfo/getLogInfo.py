#!python3
import pprint
import requests

def getLogInfo(self):
    url = 'http://'+self.ip+':'+str(self.port)+'/rtuGetLogInfo'

    headers = {
        'cache-control': "no-cache",
    }

    res = requests.request("GET",url, headers=headers)
    if (res.status_code == 200):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(res.json())
    else:
        print('Failed to receive rtuGetLogInfo response')
        print('Status code: ' + str(res.status_code))
        print('Reason: ' + res.reason)
        print(res.text)