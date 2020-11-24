import random


class Enigma:
    def __init__(self, rotor1 = [], rotor2 = [], rotor3 = []):
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.rotor1 = []
        self.rotor2 = []
        self.rotor3 = []
    
    def setRotor1(self, arrayRotor):
        if (len(arrayRotor)>0):
            self.rotor1 = arrayRotor
        else:
            self.rotor1 = self.geraRotor()
    def setRotor2(self, arrayRotor):
        if (len(arrayRotor)>0):
            self.rotor2 = arrayRotor
        else:
            self.rotor2 = self.geraRotor()
    def setRotor3(self, arrayRotor):
        if (len(arrayRotor)>0):
            self.rotor3 = arrayRotor
        else:
            self.rotor3 = self.geraRotor()
    def getrotor1(self):
        return self.rotor1
    def getrotor2(self):
        return self.rotor2
    def getrotor3(self):
        return self.rotor3
    def retornaLetra(self):
        return (self.abc[random.randint(0, 25)])
    def geraArray(self):
        array = []
        i = 1
        while(i <=25):
            indiceNovo = self.retornaLetra()
            if(indiceNovo in array):
                indiceNovo = self.retornaLetra()
            else:
                array.append(indiceNovo)
                i+=1
        return array
    def geraRotor(self):
        return self.geraArray()

    def retornaIndiceLetra(self, letra, rotor):
        return

    def retornamath(self, indiceEntrada, inicioRotor1, inicioRotor2, arrayRotorDois):
        if(indiceEntrada > inicioRotor1):
            calculo1 = indiceEntrada - inicioRotor1
            match = inicioRotor2+calculo1
            if(match >len(arrayRotorDois)-1):
                match = match-(len(arrayRotorDois)-1)
                match = match-1

        elif(indiceEntrada < inicioRotor1):
            calculo1 = inicioRotor1-indiceEntrada
            match = inicioRotor2-calculo1
            if(match<0):
               match = (match*(-1 ))-1
               arrayRotorDois= arrayRotorDois[::-1]
               
        elif(indiceEntrada == inicioRotor1):
            match = inicioRotor2
        return match



enig = Enigma()