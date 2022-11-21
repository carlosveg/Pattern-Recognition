import cv2
from histograma import Histograma
from imagen import Imagen
from matplotlib import pyplot as plt

"""
    Cielo: 170 -> 240
    Verdes: 20 -> 110
    Suelo: 110 -> 170
"""


def main():
    imagen = Imagen('./image/3-regiones.png', 1)
    #hist = Histograma('./image/3-regiones.png', 0)
    # print(imagen.clasificar_move())
    # print(hist.matriz_covarianza())
    [b, g, r] = imagen.obtener_canales()
    #cv2.imshow("Canal azul", b)
    #cv2.imshow("Canal verde", g)
    #cv2.imshow("Canal rojo", r)

    _, ax = plt.subplots(2, 2)

    # Verdes
    #_, newB = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)
    _, newB = cv2.threshold(r, 130, 255, cv2.THRESH_BINARY)
    ax[0, 0].set_title("Verdes")
    ax[0, 0].imshow(newB, cmap="gray")
    # Cielo
    _, newG = cv2.threshold(b, 190, 255, cv2.THRESH_BINARY_INV)
    ax[0, 1].set_title("Cielo")
    ax[0, 1].imshow(newG, cmap="gray")
    # Suelo
    _, newR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
    ax[1, 0].set_title("Suelo")
    ax[1, 0].imshow(newR, cmap="gray")
    plt.show()


if __name__ == '__main__':
    main()
