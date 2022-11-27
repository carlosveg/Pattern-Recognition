import cv2
import numpy as np
from matplotlib import pyplot as plt
from typing import List


class Clasificador():
    __files = []
    __clases = []

    def __init__(self, clases: List[List[int]]) -> None:
        for clase in clases:
            filename = f"dataClass{clases.index(clase) + 1}.txt"
            self.__files.append(filename)
            np.savetxt(filename, np.array(clases[0]))

    def fase_entrenamiento(self) -> None:
        for file in self.__files:
            data = np.loadtxt(file)
            self.__clases.append(data)

    def media(self, clase: List[int]) -> List[int]:
        media = [0, 0, 0]

        for i in clase:
            for j in range(len(i)):
                media[j] += i[j]

        for i in range(len(media)):
            media[i] /= len(clase)

        return media

    def matriz_covarianza(self, calse: List[List[int]]) -> np.array:
        clase = np.array(clase)
        # para matriz inversa print(np.linalg.inv(A))
        return np.cov(clase.T)

    """
        Verdes: 20 -> 110
        Suelo: 110 -> 170
        Cielo: 170 -> 240
    """

    def umbralizacion(self, canales: List[int]) -> None:
        [b, g, r] = canales

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

    def mahalanobis(self, patron: List[int], clases: List[List[int]]) -> int:
        distancias = []

        for clase in clases:
            clase = np.array(clase)
            media = self.media(clase)
            covarianza = np.cov(clase.T)
            diferencia = np.subtract(patron, media)
            distancia = diferencia @ np.linalg.inv(covarianza) @ diferencia.T
            distancias.append(distancia)

        print(distancias)
        distancia_minima = distancias.index(min(distancias))
        print(
            f"El patron { patron } pertenece a la clase { distancia_minima + 1 }")
