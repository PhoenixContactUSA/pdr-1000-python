#!python3
import pprint
import requests

def getLogData(self,startUTC,endUTC):
    pp = pprint.PrettyPrinter(indent=4)
    
    print('Record? : ' + str(self.config['record']))
    res = requests.get('http://' + self.ip+':'+str(self.port)+'/rtuGetData?startUTC=' + str(startUTC) + '&endUTC=' + str(endUTC))
    if (res.status_code == 200):
        pp.pprint(res.text)
        #return parseRawLogData(self,rawData)
    else:
        print('Failed to receive rtuGetData response')
        print(res.text)



def parseRawLogData(self,rawData):

    parsedData = {
        "timestamps": []
    }

    # ios = []
    # pos = 0
    # lastDt = 0
    # numRecorded = self.config['record'].len()

    # while (pos < rawData.len()):
    #     dt = 0
        
    #     for j in range(0,3):
    #         dt += (rawData[pos++]<<(8*(3-j)))

    #      dt =(dt*1000)+(rawData[pos++]*10);
        
    #     if dt < lastDt:
    #         break
        
    #     lastDt = dt
    
    # #loop through recorded io and parse rawData
    # for index in self.config['record']:
    #     if 


