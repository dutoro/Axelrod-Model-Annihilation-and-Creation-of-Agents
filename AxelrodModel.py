import numpy as np
from CellularAutomata import Agent
from Rules_v3 import IntProb, IVSelection, printLattice_v1, plotlattice
import matplotlib
import matplotlib.pyplot as plt

#import CellularAutomata
#crear agentes:

N=5#largo del lattice
q=50#números de opcones por caracterísitcas
F=4 #número de características
NInteractions=2000
life=20
ColorPallet=['viridis','inferno','PuBu','PuRd']


lattice=[]


for i in range(N):
    l=[]
    for j in range(N):
        CVector=np.random.randint(q+1,size=F)
        position=np.array([i,j])
        life=np.random.randint(20)
        A=Agent(CVector,position,life)
        l.append(A)

    lattice.append(l)


IP=IntProb(lattice,N,F)

#print(lattice)
#print(IP)

#printLattice_v1(lattice,N)

#primera interacción

#FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar
#SecondV=IVSelection(IP,FirstV)

#print(FirstV,SecondV)

#print('después')

for f in range(F):
    print(plotlattice(lattice, f, N,ColorPallet))

i=0

while i<=NInteractions:
    IP = IntProb(lattice, N,F)
    FirstV = np.random.randint(N, size=2)
    SecondV = IVSelection(IP, FirstV)
#    print(SecondV)
    ChangeV = lattice[SecondV[0]][SecondV[1]].CVector
    lattice[FirstV[0]][FirstV[1]].ChangeCVector(ChangeV)
#    print(FirstV, SecondV)
    if i == NInteractions/2:
        #        printLattice_v1(lattice, N)
        #  print(i)
        for f in range(F):
            print(plotlattice(lattice, f, N, ColorPallet))
    if i==NInteractions:
#        printLattice_v1(lattice, N)
  #  print(i)
        for f in range(F):
            print(plotlattice(lattice, f, N,ColorPallet))
    print(i)
    i=i+1

