def _uth(self):
    self.cnf_uthsensor = self.conf['settings'][0]
    self.cnf_uthres = self.conf['settings'][1]
    self.cnf_uthcj = self.conf['settings'][2]
    self.cnf_uthtmpunits = self.conf['settings'][3]

    tempConvSwitch = {
        0: _degC,
        1: _degF,
        2: _K
    }

    self.tempConv = tempConvSwitch[int(self.cnf_uthtmpunits)]

    self.valueFromRaw = self._uthConv

def _uthConv(self,raw):
    buff = raw
    resolution = self.cnf_uthres % 2
    highRes = False
    if (resolution == 0):
        highRes = True
    
    if (raw == 0x8001):
        return "Over Range"
    elif (raw == 0x8002):
        return "Open Circuit"
    elif (raw == 0x8004):
        return "Invalid Value"
    elif (raw == 0x8008):
        return "Cold Junction Defective"
    elif (raw == 0x8010):
        return "Invalid Configuration"
    elif (raw == 0x8040):
        return "Module Faulty"
    elif (raw == 	0x8080):
        return "Under Range"

    sensType = self.conf['settings'][0]
    if (sensType < 14):
        sensType = 13

    # high resolution
    if (sensType == 13):
        if (highRes == True):
            buff = buff / 10.0
        else:
            buff = buff
    elif (sensType == 14):
        if (highRes == True):
            buff = buff
        else:
            buff = buff * 10.0

    if (self.cnf_uthres > 1):
        buff = (buff - 32.0) * (5.0 / 9.0)

    return self.tempConv(buff) + self.conf.get('fvo',0)



# deg c to deg c
def _degC(r):
    return r

# deg c to deg f
def _degF(r):
    return (r * (9.0 / 5.0) + 32.0)

# deg c to kelvin
def _K(r):
    return (r + 273.15)

