class Note:
    PITCHES = ['до', 'ре', 'ми',
               'фа', 'соль', 'ля', 'си']
    LPITCHES = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']

    def init(self, note, d=False):
        self.d = d
        self.ind = self.PITCHES.index(note)

    def str(self):
        if self.d:
            return self.LPITCHES[self.ind]
        else:
            return self.PITCHES[self.ind]
