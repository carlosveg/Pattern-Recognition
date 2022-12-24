import numpy as np
from typing import List


class Clasificador():
    __files = []
    __clases = []

    def __init__(self, clases: List[List[int]]) -> None:
        for clase in clases:
            filename = f"assets/dataClass{clases.index(clase) + 1}.txt"
            self.__files.append(filename)
            np.savetxt(filename, np.array(clase))

        self.fase_entrenamiento()

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

    def classify(self, patron: List[int]) -> None:
        distancias = []

        for clase in self.__clases:
            #clase = np.array(clase)
            media = self.media(clase)
            covarianza = np.cov(clase.T)
            diferencia = np.subtract(patron, media)
            distancia = diferencia @ np.linalg.inv(covarianza) @ diferencia.T
            distancias.append(distancia)

        distancia_minima = distancias.index(min(distancias))
        print(
            f"El patron { patron[0][::-1] } pertenece a la clase { distancia_minima + 1 }")
