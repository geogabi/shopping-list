class Client:

    def __init__(self,buget):
        self.buget = buget

    def plateste(self,p):
        de_platit = int(p.stoc) * int(p.pret)
        if self.buget > de_platit:
            self.buget -= de_platit
            return de_platit





if __name__ == "__main":
    c = Client(0)
    c.plateste(0)





