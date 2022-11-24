import cv2
import numpy as np
from matplotlib import pyplot as plt


class Clasificador():
    __class = None

    def __init__(self) -> None:
        pass

    def fase_entrenamiento(self):
        pass

    def media(clase):
        media = [0, 0, 0]

        for i in clase:
            for j in range(len(i)):
                media[j] += i[j]

        for i in range(len(media)):
            media[i] /= len(clase)

        return media

    def matriz_covarianza(self) -> np.array:
        """
            aquí debemos tener previamente almacenadas los patrones que pertenecen a cada clase
            para poder tener el valor de n (cuántos elementos tiene la clase) que en un principio
            cada clase va a comenzar con 5 patrones
        """
        c1 = [
            [200, 210, 215, 210, 198],
            [160, 170, 172, 165, 177],
            [120, 130, 133, 134, 138],
        ]

        c1 = np.array(c1)

        # para matriz inversa print(np.linalg.inv(A))

        return np.cov(c1.T)

    def umbralizacion(self, canales: list) -> None:
        [b, g, r] = canales
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

    def mahalanobis(self):
        pass
