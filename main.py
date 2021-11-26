class Note:
    PITCHES = ['до', 'ре', 'ми',
               'фа', 'соль', 'ля', 'си']
    LPITCHES = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']

    def str(self):
        if self.d:
            return self.LPITCHES[self.ind]
        else:
            return self.PITCHES[self.ind]
