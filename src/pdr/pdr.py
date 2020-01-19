#!python3
class PDR:
    apiPorts = [1523,1524,1525,1526]

    from ..getLogData.getLogData import getLogData
    from ..getConfig.getConfig import getConfig

    def __init__(self,ip,timeout):
        self.config = {}
        self.ip = ip
        self.timeout = timeout
        self.portIndex = 0
        self.port = self.__class__.apiPorts[1]
        self.connected = False

        
        self.getConfig()

        
