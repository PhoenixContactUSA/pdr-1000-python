#!python3
import pprint
import math
import requests

def getLogInfo(self):
    if (self.initialized != True):
        return Exception('Module not initialized.  getConfig must be successfully requested once before calling this method')

    url = 'http://'+self.ip+':'+str(self.port)+'/rtuGetLogInfo'

    headers = {
        'cache-control': "no-cache",
    }
    try:
        res = requests.request("GET",url, headers=headers)
        if (res.status_code == 200):
            return getDateRanges(self,res.json())
        else:
            print('Failed to receive rtuGetLogInfo response')
            print('Status code: ' + str(res.status_code))
            print('Reason: ' + res.reason)
            print(res.text)
    except requests.exceptions.RequestException as e:
        raise e

def getDateRanges(self,data):
    logInfo = data
    logInfo["validDates"] = []
    logInfo["firstDate"] = None
    logInfo["lastDate"] = None
    logInfo["logFileSize"] = None
    dateRanges = []
    mb = 0
    arr = data["indices"]
    sIkey = None #startIndex key
    lIkey = None #lastIndex key
    sUTCkey = None #startUTC key
    sRkey = None    #sampleRate key

    if (len(arr) == 0):
        logInfo["dateRanges"] = []
        return logInfo

    # determine keys based on api version
    if ('startIndex' in arr[0]):
        sIkey = 'startIndex'
        lIkey = 'lastIndex'
        sUTCkey = 'startUTC'
        sRkey = 'sampleRate'
    else:
        sIkey = 'sI'
        lIkey = 'lI'
        sUTCkey = 'sU'
        sRkey = 'sR'
    

    for k in range(0,len(arr)):
        obj = {}
        obj["startDate"] = arr[k][sUTCkey]
        counts = 0

        if (arr[k][lIkey] - arr[k][sIkey] < 0):
            counts = (data["totalMemory"] - arr[k][sIkey]) + arr[k][lIkey] + 1
        else:
            counts = arr[k][lIkey] - arr[k][sIkey] + 1
        
        realFrameSize = data['frameSize']

        ms = math.floor(counts/realFrameSize) * self.config['sampleRate']
        obj["endDate"] = obj["startDate"] + ms
        dateRanges.append(obj)

        mb += counts

    logInfo["validDates"] = dateRanges
    logInfo["firstDate"] = dateRanges[0]["startDate"]
    logInfo["lastDate"] = dateRanges[len(dateRanges)-1]["endDate"]
    logInfo["logFileSize"] = mb

    return logInfo

