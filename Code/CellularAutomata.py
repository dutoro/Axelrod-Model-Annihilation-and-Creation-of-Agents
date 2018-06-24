import numpy as np

class Agent:

    CVector=np.array([])
    position=np.array([])
    life=0

#init characteristics: CVector: Cultural Vector; position: position in the lattice; life: life time

    def __init__(self,i_CVector,i_position,i_life):
        self.CVector=i_CVector
        self.position=i_position
        self.life=i_life

#Change one feature of the CVector

    def ChangeCVector(self,NVector):
        p=np.arange(len(NVector))
        np.random.shuffle(p)
        for i in p:
            if self.CVector[i]!=NVector[i]:
                self.CVector[i]=NVector[i]
                break


#Reset life in 0 and put a new CVector

    def Death(self,CVector):
        self.CVector=CVector
        self.life=0




