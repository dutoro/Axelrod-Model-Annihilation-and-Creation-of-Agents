import numpy as np, copy
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns



def IntProb(lattice,N): #generate a matrix with de interaction probabilities
    Ip={}

    for fAgent in lattice:

        f = fAgent
        for Agent in f:
            vecinos = {}

            position = Agent.position
            CVAgent = Agent.CVector

            i = position[0]
            j = position[1]

            if i != 0 and j != 0 and i != N - 1 and j != N - 1:  # toma todos menos los de los bordes
                for fila in range(i - 1, i + 2):
                    for columna in range(j - 1, j + 2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position
                
                            CVvecino = vecino.CVector
          
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                      
                            vecinos[np.array_str(pvecino)] = p
   

            # Bordes sin esquinas

            elif i == 0 and j != 0 and j != N - 1:  # borde superior sin las esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            CVvecino = vecino.CVector
                         
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                      
                            vecinos[np.array_str(pvecino)] = p

            elif i == N - 1 and j != 0 and j != N - 1:  # borde inferior sin esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                          
                            CVvecino = vecino.CVector
                        
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                       
                            vecinos[np.array_str(pvecino)] = p

            elif j == 0 and i != N - 1 and i != 0:  # borde izquierdo sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                       
                            CVvecino = vecino.CVector
                      
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                    
                            vecinos[np.array_str(pvecino)] = p

            elif j == N - 1 and i != N - 1 and i != 0:  # borde derecho sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                        
                            CVvecino = vecino.CVector
                
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                   
                            vecinos[np.array_str(pvecino)] = p

            # Esquinas

            elif i == 0 and j == 0:
                for fila in range(2):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            
                            CVvecino = vecino.CVector
                        
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                      
                            vecinos[np.array_str(pvecino)] = p

            elif i == 0 and j == N - 1:
                for fila in range(2):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                      
                            CVvecino = vecino.CVector
                      
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                       
                            vecinos[np.array_str(pvecino)] = p


            elif i == N - 1 and j == 0:
                for fila in range(N - 2, N):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                   
                            CVvecino = vecino.CVector
                       
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                         
                            vecinos[np.array_str(pvecino)] = p

            elif i == N - 1 and j == N - 1:
                for fila in range(N - 2, N):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                     
                            CVvecino = vecino.CVector
                  
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                          
                            vecinos[np.array_str(pvecino)] = p

            Ip[np.array_str(position)] = vecinos

    IP={}
    for agente in Ip:
        Agente=Ip[agente]
        sum_p=sum(Agente.values())
        vecinos2={}
        for vecino in Agente:
            if sum_p==0:
                P=0
                vecinos2[vecino]=P
            else:
                P=Agente[vecino]/sum_p
                vecinos2[vecino]=P

        IP[agente]=vecinos2




    return IP




def printLattice_v1(lattice,N): #print the lattice showing the position and the cultural vector.
    for i in range(N):
        for j in range(N):
            print(lattice[i][j].position, lattice[i][j].CVector)


def plotlattice (lattice,f,N,ColorPallet): #Plot the lattice, only the f feature.

    #crea un arreglo 2D con el el q=n para todos los elementos del lattice

    nCV=np.array([]).reshape(0,N)
    for fila in lattice:
        F=np.array([])
        for Agente in fila:
            F=np.append(F,Agente.CVector[f])

        F=np.array([F])
        nCV=np.concatenate((nCV,F))

    return nCV, sns.heatmap(nCV,cmap=ColorPallet[f])


def ChangeLife (lattice,life,q,F): #update the life of eveey agent and change the cultural vector if the agent reach the 
                                   #boundary life.
    for fila in lattice:
        for Agent in fila:
            Agent.life=Agent.life+1
            if Agent.life==20:
                NCV=np.random.randint(q+1,size=F)
                Agent.Death(NCV)

    return None
