#!python3
import time
class PDR:
    apiPorts = [1523,1524,1525,1526]

    from ..getLogData.getLogData import getLogData
    from ..getConfig.getConfig import getConfig
    from ..getLogInfo.getLogInfo import getLogInfo

    def __init__(self,ip,timeout):
        self.config = {}
        self.ip = ip
        self.timeout = timeout
        self.portIndex = 1
        self.port = self.__class__.apiPorts[1]
        self.initialized = False
        self.connected = False
        # self.connectedCallback = hooks.get('connected')
        # self.disconnectedCallback = hooks.get('disconnected')
        
    def switchPort(self):
        self.portIndex = (self.portIndex + 1) % 4
        self.port = self.__class__.apiPorts[self.portIndex]    

    def getIO(self,index):
        return self.config['io'][index]
    
    @staticmethod
    def _isDigital(io):
        if ((io['type'] < 2) or (io['type'] == 5)):
            return True
        else:
            return False