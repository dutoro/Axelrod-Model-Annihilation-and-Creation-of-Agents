import numpy as np
import matplotlib
import matplotlib.pyplot as plt




def IntProb(lattice,N,F):
    IP={}

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
                        if fila != i or columna != j:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P
            #            print(vecinos)

            # Bordes sin esquinas

            elif i == 0 and j != 0 and j != N - 1:  # borde superior sin las esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(2):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            elif i == N - 1 and j != 0 and j != N - 1:  # borde inferior sin esquinas
                for columna in range(j - 1, j + 2):
                    for fila in range(N - 2, N):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            elif j == 0 and i != N - 1 and i != 0:  # borde izquierdo sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(2):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            elif j == N - 1 and i != N - 1 and i != 0:  # borde derecho sin esquinas
                for fila in range(i - 1, i + 2):
                    for columna in range(N - 2, N):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            # Esquinas

            elif i == 0 and j == 0:
                for fila in range(2):
                    for columna in range(2):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            elif i == 0 and j == N - 1:
                for fila in range(2):
                    for columna in range(N - 2, N):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P


            elif i == N - 1 and j == 0:
                for fila in range(N - 2, N):
                    for columna in range(2):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            elif i == N - 1 and j == N - 1:
                for fila in range(N - 2, N):
                    for columna in range(N - 2, N):
                        if columna != j or fila != i:
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
                            P = contador / F
                            #                        print(fila,columna,P)
                            vecinos[np.array_str(pvecino)] = P

            IP[np.array_str(position)] = vecinos

    return IP


def IVSelection (IP,FirstV):
#    FirstV = np.random.randint(N, size=2)  # selecciona el primer vector a interactuar

    # Seleccionar el segundo vector, el cual debe ser el de mayor probabilidad de interactuar

    FVProbs = IP[np.array_str(FirstV)]

    # print(IP)
    # print(FirstV)

    # print(FVProbs)

    Pmax = max(FVProbs.values())  # maxima probabilidad entre los vecinos

    # print(Pmax)

    # Elegir el primer vecino que tenga una prob igual a la maxima. Esta función le asigna la posición en un np.array

    for vecino in FVProbs:
        if FVProbs[vecino] == Pmax:
            SecondV = vecino
            SecondV = np.fromstring(SecondV[1:len(SecondV)], dtype=int, sep=' ')
            break

    return SecondV

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
        print(F)
        nCV=np.concatenate((nCV,F))


    #generar el heatmap

    plt.imshow(nCV,cmap=ColorPallet[f])
    plt.show()



    return nCV



