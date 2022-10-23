import os
import sys
from os import listdir
from os.path import isfile, join
from produs import Produs
from client import Client
from cosdecump import Cos
l_produse,l_cump = sys.argv[1],sys.argv[2]
onlyfiles = [f for f in listdir(l_cump) if isfile(join(l_cump, f))]
d = {}
with open(l_produse) as lista_produse:
    for line in lista_produse.readlines():
        nume, cantitate, pret = line.split(',')
        d[nume] = {'pret':int(pret),'cantitate':int(cantitate)}
for fila in onlyfiles:
    os.chdir(l_cump)
    with open(fila) as f:
        cos = Cos(f.name)
        client = Client(int(f.readline()))
        for line in f.readlines():
            produs, cantitate = line.strip(',').strip('\n').split(',')
            p = Produs(produs,cantitate,d[produs]['pret'])
            if d[produs]['cantitate'] > int(cantitate):
                pret = int(p.stoc) * int(p.pret)
                if client.plateste(p):
                    cos.adauga(p.nume, p.stoc, pret)
                    p.salvare(d)
                else:
                    print(f'{cos.nume_client} Insuficient {p.stoc},{p.nume}')
        cos.eliberare_bon()








