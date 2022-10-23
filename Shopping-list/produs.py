class Produs:

    def __init__(self,nume,stoc,pret):
        self.nume = nume
        self.stoc = int(stoc)
        self.pret = pret

    def salvare(self,d):
        d[self.nume]['cantitate'] -= self.stoc
