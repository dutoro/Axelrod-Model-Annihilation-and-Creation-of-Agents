import numpy as np
from CellularAutomata import Agent
from Rules import IntProb
from Rules import IVSelection

#import CellularAutomata
#crear agentes:

N=3 #largo del lattice
q=3 #números de opcones por caracterísitcas
F=6 #número de características
life=20

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

print(lattice)
print(IP)

for i in range(N):
    for j in range(N):
        print(lattice[i][j].position,lattice[i][j].CVector)

#primera interacción

FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar
SecondV=IVSelection(IP,FirstV)

print(FirstV,SecondV)

#Cambio

ChangeV=lattice[SecondV[0]][SecondV[1]].CVector
lattice[FirstV[0]][FirstV[1]].ChangeCVector(ChangeV)

print(lattice[FirstV[0]][FirstV[1]].CVector)

#Segunda interacción

FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar
SecondV=IVSelection(IP,FirstV)

print(FirstV,SecondV)

#Cambio

ChangeV=lattice[SecondV[0]][SecondV[1]].CVector
lattice[FirstV[0]][FirstV[1]].ChangeCVector(ChangeV)

print(lattice[FirstV[0]][FirstV[1]].CVector)

