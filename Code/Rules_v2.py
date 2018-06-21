import numpy as np
import matplotlib
import matplotlib.pyplot as plt




def IntProb(lattice,N):
    Ip={}

    for fAgent in lattice:
        #    print(fAgent)
        f = fAgent
        for Agent in f:
            vecinos = {}
            #        print(Agent)
            position = Agent.position
            CVAgent = Agent.CVector
            #        print(position)
            i = position[0]
            j = position[1]

            #        print(i,j)
            if i != 0 and j != 0 and i != N - 1 and j != N - 1:  # toma todos menos los de los bordes
                for fila in range(i - 1, i + 2):
                    for columna in range(j - 1, j + 2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position
                            #                        print("vecino", pvecino)
                            #                        print(CVAgent)
                            CVvecino = vecino.CVector
                            #                        print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = p
            #            print(vecinos)

            # Bordes sin esquinas

            elif i == 0 and j != 0 and j != N - 1:  # borde superior sin las esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            elif i == N - 1 and j != 0 and j != N - 1:  # borde inferior sin esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            elif j == 0 and i != N - 1 and i != 0:  # borde izquierdo sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            elif j == N - 1 and i != N - 1 and i != 0:  # borde derecho sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            # Esquinas

            elif i == 0 and j == 0:
                for fila in range(2):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                       print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            elif i == 0 and j == N - 1:
                for fila in range(2):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p


            elif i == N - 1 and j == 0:
                for fila in range(N - 2, N):
                    for columna in range(2):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
                            vecinos[np.array_str(pvecino)] = p

            elif i == N - 1 and j == N - 1:
                for fila in range(N - 2, N):
                    for columna in range(N - 2, N):
                        if (fila==i-1 and columna==j) or (fila==i and columna==j+1) or (fila==i+1 and j==columna)\
                            or (fila==i and columna==j-1):
                            vecino = lattice[fila][columna]
                            pvecino = vecino.position

                            #                        print("vecino", pvecino)
                            # print(CVAgent)
                            CVvecino = vecino.CVector
                            # print(CVvecino)
                            contador = 0
                            for k in range(len(CVAgent)):
                                if CVAgent[k] == CVvecino[k]:
                                    contador = contador + 1
                            p = contador
                            #                        print(fila,columna,p)
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







#    print (IP)
    return IP


#def IVSelection (IP,FirstV):

#    FVP=IP[np.array_str(FirstV)] #Extrae la probabilidad de interactuar los vecinos (Diccionario)
#    i=0
#    while i<=4:
#        SVP=FVP.popitem()
#        SV=SVP[0]
#        if IP[np.array_str(FirstV)][SVP[1]]<=IP[SVP[1]][np.array_str(FirstV)]:
#            return np.fromstring(SVP[1:len(SecondV)], dtype=int, sep=' ')
#        i=i+1



#def IVSelection (IP,FirstV):
#    FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar

    # Seleccionar el segundo vector, el cual debe ser el de mayor probabilidad de interactuar

#    FVProbs = IP[np.array_str(FirstV)]
#    for vecino in FVProbs:
 #       if


def printLattice_v1(lattice,N):
    for i in range(N):
        for j in range(N):
            print(lattice[i][j].position, lattice[i][j].CVector)


def plotlattice (lattice,f,N,ColorPallet):

    #crea un arreglo 2D con el el q=n para todos los elementos del lattice

    nCV=np.array([]).reshape(0,N)
    for fila in lattice:
        F=np.array([])
        for Agente in fila:
            F=np.append(F,Agente.CVector[f])

        F=np.array([F])
#        print(F)
        nCV=np.concatenate((nCV,F))


    #generar el heatmap

    plot=plt.imshow(nCV,cmap=ColorPallet[f])
    plt.show()



    return nCV



