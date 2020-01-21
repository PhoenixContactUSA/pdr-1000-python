def _rtd(self):
    self.cnf_rtdcon = self.conf['settings'][0]
    self.cnf_rtdr0 = self.conf['settings'][1]
    self.cnf_rtdtmpunits = self.conf['settings'][2]
    self.cnf_rtdsensor = self.conf['settings'][3]
    self.cnf_rtdres = self.conf['settings'][4]

    tempConvSwitch = {
        0: _degC,
        1: _degF,
        2: _K
    }

    self.tempConv = tempConvSwitch[int(self.cnf_rtdtmpunits)]

    self.valueFromRaw = self._rtdConv

def _rtdConv(self,raw):
    buff = raw
    if (raw == 0x8001):
        return "Over Range"
    elif (raw == 0x8002):
        return "Open Circuit"
    elif (raw == 0x8004):
        return "Invalid Value"
    elif (raw == 0x8010):
        return "Invalid Configuration"
    elif (raw == 0x8040):
        return "Module Faulty"
    elif (raw == 0x8080):
        return "Under Range"

    r0 = RTD_R0[int(self.cnf_rtdr0)]
    res  = int(self.cnf_rtdres)
    highRes = (res == 1) or (res == 3)

    if (self.cnf_rtdsensor == 13):
        buff = (buff / 100.0 * r0)
    elif (self.cnf_rtdsensor == 14):
        if (highRes == True):
            buff = (buff / 100.0)
        else:
            buff = (buff / 10.0)
    elif (self.cnf_rtdsensor == 15):
        if (highRes == True):
            buff = (buff / 10.0)
    else:
        if (highRes == True):
            buff = (buff / 100.0)
        else:
            buff = (buff / 10.0)


    #if in units of fahrenheit, convert to centigrade before final output unit conversion
    if (int(self.cnf_rtdres) > 1):
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

RTD_R0 = {
	0: 100.0,
	1: 10.0,
	2: 20.0,
	3: 30.0,
	4: 50.0,
	5: 120.0,
	6: 150.0,
	7: 200.0,
	8: 240.0,
	9: 300.0,
	10: 400.0,
	11: 500.0,
	12: 1000.0,
	13: 1500.0,
	14: 2000.0,
	15: 3000.0
}