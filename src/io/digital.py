def _digital(self):
        if (self.conf['type'] == 5):
            self.cnf_hilbl = self.conf['settings'][0]
            self.cnf_lolbl = self.conf['settings'][1]

        self.valueFromRaw = lambda raw: raw