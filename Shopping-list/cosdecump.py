import os
curent = os.getcwd()

class Cos:
    def __init__(self,nume_client):
        self.nume_client = nume_client
        self.lista = []

    def adauga(self,produs,cantitate,pret):
        self.lista.append([produs,int(cantitate),pret])

    def eliberare_bon(self):
        os.chdir(curent)
        director = "NOTE DE PLATA"
        if not os.path.exists(director):
            os.mkdir(director)
            os.chdir(director)
        else:
            os.chdir(director)
        with open(f'nota.txt {self.nume_client}','w') as nota:
            nota.write(f'Nota de plata\n{"-"*20}\n')
            total = 0
            for achizitie in self.lista:
                nota.write(f'{achizitie[0]},{achizitie[1]},{achizitie[2]} lei\n')
                total += achizitie[2]
            nota.write(f'{"-"*20}\nTotal {total} lei')




if __name__ == '__main__':
    c = Cos(0)
