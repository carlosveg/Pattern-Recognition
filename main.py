import cv2
from clasificador import Clasificador
from histograma import Histograma
from imagen import Imagen
from matplotlib import pyplot as plt
from clases import c1, c2, c3

"""
    Verdes: 20 -> 110
    Suelo: 110 -> 170
    Cielo: 170 -> 240
"""


def main():
    imagen = Imagen('./image/3-regiones.png', 1)
    clasificador = Clasificador()
    #hist = Histograma('./image/3-regiones.png', 0)
    print(imagen.clasificar_clic())
    # print(hist.matriz_covarianza())
    canales = imagen.obtener_canales()
    clasificador.umbralizacion(canales)


if __name__ == '__main__':
    main()
