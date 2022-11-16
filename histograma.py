import cv2
import numpy as np
from imagen import Imagen
from matplotlib import pyplot as plt
"""
    La clase histograma hereda de la clase imagen, esta clase permite
    generar y manipular el histograma de la imagen padre
    Recibe como parametros de su metodo incializador la direccion relativa
    o absoluta de la imagen padre y un valor entero 0 o 1 el cual indica
    si se usara en esacala de grises o a color
"""


class Histograma(Imagen):

    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self._hist = cv2.calcHist([self._imagen], [0], None, [256], [0, 256])
        fig, ax = plt.subplots(2)

        ax[0].imshow(self._imagen, cmap="gray")
        ax[0].set_title("Imagen")
        ax[0].axis("off")

        ax[1].plot(self._hist, color="gray")
        ax[1].set_title("Histograma b/n")

        plt.show()

    def media(self):
        return self._hist.mean()

    def mediana(self):
        valores = [i for i, valor in enumerate(self._hist) if valor > 0]
        return valores[int(len(valores)/2)]

    def moda(self):
        moda = 0
        repeticion = 0

        for i, rep in enumerate(self._hist):
            if rep > repeticion:
                moda = i
                repeticion = rep
        return moda

    def equializar(self):
        pass
