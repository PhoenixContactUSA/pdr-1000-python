
#class to handle common IO functionality
class IO:

    from .digital import _digital
    from .analog import _analog,_anaRaw0,_anaRaw1,_anaRaw4
    from .uth import _uth,_uthConv
    from .rtd import _rtd,_rtdConv

    def __init__(self,io):
        self.conf = io
        
        self.initIO()

    def initIO(self):
        typeSwitch = {
            0: self._digital,
            1: self._digital,
            2: self._analog,
            3: self._uth,
            4: self._rtd,
            5: self._digital
        }
        initFunc = typeSwitch.get(self.conf['type'])
        initFunc()

    def isDigital(self):
        if ((self.conf['type'] < 2) or (self.conf['type'] == 5)):
            return True
        else:
            return False

    def _unknownIO(self):
        print('Unknown io type: ' + self.conf['type'])