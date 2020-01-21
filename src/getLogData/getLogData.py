#!python3
import pprint
import time
import requests
from ..io.io import IO

def getLogData(self,startUTC,endUTC):
    if (self.initialized != True):
        return Exception('You must wait until connection initialization is complete')

    #pp = pprint.PrettyPrinter(indent=4)
    time.sleep(0.05)
    #print('Record? : ' + str(self.config['record']))
    try:
        url = 'http://' + self.ip+':'+str(self.port)+'/rtuGetData?startUTC=' + str(startUTC) + '&endUTC=' + str(endUTC)
        res = requests.get(url)
        if (res.status_code == 200):
            #pp.pprint(res.text)
            return _parseRawLogData(self,res.content)
        else:
            print('Failed to receive rtuGetData response')
            print(res.text)

    except requests.exceptions.RequestException as e:
            raise e


def _parseRawLogData(self,rawData):

    bArr = bytearray(rawData)
    ret = []
    numRec = len(self.config['record'])
    pos = 0
    lastDt = 0

    #format the recorded io in the expected list order
    ios = []
    for i in range(0,numRec,1):
        id = self.config['record'][i]
        io = IO(self.getIO(id))
        if (io.isDigital() == False):
            ios.append(io)

    for i in range(0,numRec,1):
        id = self.config['record'][i]
        io = IO(self.getIO(id))
        if (io.isDigital() == True):
            ios.append(io)


    #loop through the byte array and parse the data
    while pos < (len(bArr) - 1):
        dt = 0
        values = [None] * numRec
        sample = {"values":values}
        errState = [None] * numRec
        for i in range(0,4,1):
            dt += (bArr[pos]<<(8*(3-i)))
            pos+=1
        
        dt = (dt*1000)+(bArr[pos]*10)
        pos+=1

        if (dt < lastDt):
            break

        sample['time'] = dt
        lastDt = dt

        for i in range(0,numRec):
            errState[i]=(bArr[pos] >> (i%8)) & 1
            if (i%8==7 or i==numRec-1):
                pos+=1

        bcnt = 0
        for i in range(0,numRec):
            io = ios[i]
            rIndex = i
            if (io.isDigital()==True):
                if (errState[rIndex] != 0):
                    sample['values'][rIndex] = "ERR"
                else:
                    sample['values'][rIndex] = ((bArr[pos]>>bcnt)&1)

                bcnt = (bcnt+1)&8
                if (bcnt==0):
                    pos+=1
            else:
                if (io.conf['type'] == 7):
                    if (errState[rIndex] != 0):
                        pos+=3
                        samples['values'][rIndex] = "ERR"+str(bArr[pos])
                        pos+=1
                    else:
                        samples['values'][rIndex] = io.valueFromRaw((bArr[pos]<<24)+(bArr[pos+1]<<16)+(bArr[pos+2]<<8)+(bArr[pos+3]));									
                        pos+=4
                else:
                    if (errState[rIndex] != 0):
                        pos+=1
                        sample['values'][rIndex] = "ERR"+str(bArr[pos])
                        pos+=1
                    else:
                        sample['values'][rIndex] = io.valueFromRaw((bArr[pos]<<8)+bArr[pos+1]);
                        pos+=2

        if (bcnt != 0):
            pos+=1
        
        ret.append(sample)

    #format the collected data
    parsedData = {
        "timestamps": []
    }

    #create the keys
    for i in range(0,len(ios)):
        parsedData[ios[i].conf['name']] = []

    #append the data
    for i in range(0,len(ret)):
        parsedData['timestamps'].append(ret[i]['time'])

        for j in range(0,len(ret[i]['values'])):
            if (ios[j].isDigital() == True):
                parsedData[ios[j].conf['name']].append((ret[i]['values'][j]+1)%2)
            else:
                parsedData[ios[j].conf['name']].append(ret[i]['values'][j])

    return parsedData
