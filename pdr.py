#!python3
class PDR:
    apiPorts = [1523,1524,1525,1526]

    def __init__(self,ip,timeout):
        self.config = {}
        self.ip = ip
        self.timeout = timeout
        self.portIndex = 0
        self.port = apiPorts[self.portIndex]
        self.connected = false

        self.getConfig()

        from .getLogData import getLogData
        from .getConfig import getConfig
