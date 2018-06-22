import numpy as np , copy
from CellularAutomata import Agent
from Rules_v2 import IntProb, printLattice_v1, plotlattice
import matplotlib
import matplotlib.pyplot as plt






#import CellularAutomata
#crear agentes:

N=10#largo del lattice
q=10#números de opcones por caracterísitcas
F=3 #número de características
NInteractions=3000
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

for f in range(F):
    nCV_f = plotlattice(lattice, f, N, ColorPallet)

n=0

while n<=10:
    i=0
    Lattice = copy.deepcopy(lattice)

    while i <= NInteractions:

        IP = IntProb(Lattice, N)

        I = np.random.randint(N, size=2)
        #    print(I)

        Vecinos = IP[np.array2string(I)]
        #    print(Vecinos)
        J = Vecinos.popitem()

        #    print(J)
        P_ij = J[1]  # Probabilidad que tiene i de interactuar con j
        #    print(P_ij)
        P_ji = IP[J[0]][np.array2string(I)]  # Probabilidad que tiene j de interactuar con i
        #    print(P_ji)

        if P_ij > 0 and P_ji > 0:
            J = J[0]
            J = np.fromstring(J[1:len(J)], dtype=int, sep=' ')
            ChangeV = Lattice[J[0]][J[1]].CVector
            Lattice[I[0]][I[1]].ChangeCVector(ChangeV)

        if i%1000==0 and i!=0:
            #        printLattice_v1(lattice, N)
            print(i)
            for f in range(F):
                plotlattice(Lattice, f, N, ColorPallet)
        #           np.savetxt('/Users/danieltoro/Documents/9no Semestre/IIQ3763 - Análisis de Sistemas Complejos/Proyecto/'
        #                     'Resultados/N5_q10_F2_NI10k_v2/txt/f'+str(f)+'_i'+str(i)+'.txt',nCV_f)

        i = i + 1

    n=n+1

#print(lattice)
#print(IP)

#printLattice_v1(lattice,N)

#primera interacción

#FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar
#SecondV=IVSelection(IP,FirstV)

#print(FirstV,SecondV)

#print('después')


i=0

