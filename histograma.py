import cv2
from imagen import Imagen
import numpy as np
# La clase histograma hereda de la clase imagen, esta clase permite
# generar y manipular el histograma de la imagen padre
# Recibe como parametros de su metodo incializador la direccion relativa
# o absoluta de la imagen padre y un valor entero 0 o 1 el cual indica
# si se usara en esacala de grises o a color
class Histograma(Imagen):
    
    def __init__(self,nombre,tipo):
        super().__init__(nombre,tipo)
        self._hist=cv2.calcHist([self._imagen],[0],None,[256],[0,256])

    def media(self):
        return self._hist.mean()

    def mediana(self):
        valores = [i for i,valor in enumerate(self._hist) if valor>0]
        return valores[int(len(valores)/2)]

    def moda(self):
        moda=0
        repeticion=0

        for i,rep in enumerate(self._hist):
            if rep>repeticion:
                moda=i
                repeticion=rep
        return moda
    def equializar(self):
        pass
        