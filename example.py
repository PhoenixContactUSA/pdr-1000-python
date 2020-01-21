#!python3
import time
from src.pdr.pdr import PDR

def connected(pdr):
        print('Connected to PDR: ' + pdr.config['name'])
        now = int(time.time())
        lastMin = now - 60
        data = pdr.getLogData(lastMin,now)
        print(data)
    
    
def connect(pdr):
    try:
        pdr.getConfig()
        connected(pdr)

    except Exception as e:
        print('Failed to connect to pdr on port: ' + str(pdr.port))
        pdr.switchPort()
        time.sleep(1)
        connect(pdr)

def main():

    pdr = PDR("192.168.0.5",5)

    connect(pdr)

if __name__ == "__main__":
    main()

