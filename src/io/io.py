
class IO:
    def __init__(self,io):
        self = io
        
        initIO(self)

    def initIO(self):
        typeSwitch = {
            "0": _digital(self),
            "1": _digital(self),
            "2": _analog(self),
            "5": _digital(self),
        }

    def _digital(self):
        if (self['type'] == 5):
            self.cnf_hilbl = self['settings'][0]
            self.cnf_lolbl = self['settings'][1]

    def _analog(self):
        self.cnf_anamode = self['settings'][0]
        self.ana_spanlo = self['settings'][1]
        self.ana_spanhi = self['settings'][2]
        self.ana_units = self['settings'][3]

        rawSwitch = {
            "0": _anaRaw0,
            "1": _anaRaw1,
            "2": _unknownIO,
            "3": _unknownIO,
            "4": _anaRaw4
        }

        self.valueFromRaw = rawSwitch[self.settings[0]]

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
            return ((raw / 30000) * (self.settings[2]-self.settings[1]) + self.settings[1]) + self.fvo;

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
            self.fvo + self.settings[1] + (((16/30000*raw) * (self.settings[2] - self.settings[1]))  / 16.0)

    def _unknownIO(self):
        raise 'Unknown io type: ' + self.type