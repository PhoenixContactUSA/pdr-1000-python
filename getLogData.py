#!python3
import requests

def getLogData(self,startUTC,endUTC):
res = requests.get(self.ip+'/rtuGetData?startUTC=' + startUTC + '&endUTC=' + endUTC)
    if (res.status_code == 200):
        return parseRawLogData(self,rawData)
    else:
        print('Failed to receive rtuGetData response')
        print(res.text)



def parseRawLogData(self,rawData):
    parsedData = []
    rec = self.config.record    #pull in configuration
    #for rec[i].name


