def _analog(self):
    self.cnf_anamode = self.conf['settings'][0]
    self.ana_spanlo = self.conf['settings'][1]
    self.ana_spanhi = self.conf['settings'][2]
    self.ana_units = self.conf['settings'][3]

    rawSwitch = {
        0: self._anaRaw0,
        1: self._anaRaw1,
        2: self._unknownIO,
        3: self._unknownIO,
        4: self._anaRaw4
    }

    self.valueFromRaw = rawSwitch[int(self.conf['settings'][0])]

def _anaRaw0(self,raw):
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
    else:
        return ((raw / 30000) * (self.conf['settings'][2]-self.conf['settings'][1]) + self.conf['settings'][1]) + self.conf['fvo'];

def _anaRaw1(self,raw):
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
    else:
        self._unknownIO()

def _anaRaw4(self,raw):
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
    else:
        return self.conf['fvo'] + self.conf['settings'][1] + (((16/30000*raw) * (self.conf['settings'][2] - self.conf['settings'][1]))  / 16.0)
