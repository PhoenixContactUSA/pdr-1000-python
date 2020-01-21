
#class to handle common IO functionality
class IO:

    from .digital import _digital
    from .analog import _analog,_anaRaw0,_anaRaw1,_anaRaw4

    def __init__(self,io):
        self.conf = io
        
        self.initIO()

    def initIO(self):
        typeSwitch = {
            0: self._digital,
            1: self._digital,
            2: self._analog,
            5: self._digital
        }
        initFunc = typeSwitch.get(self.conf['type'])
        initFunc()

    def _unknownIO(self):
        print('Unknown io type: ' + self.conf['type'])