#!python3
import time
from src.pdr.pdr import PDR

def main():
    
    p = PDR("192.168.0.5",5)
    #p.getLogInfo()
    now = int(time.time())
    lastTen = now - 60*10
    p.getLogData(lastTen,now)

if __name__ == "__main__":
    main()

