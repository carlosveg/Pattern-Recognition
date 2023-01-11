"""
    Clasificador con media y matriz de covarianza desconocidas

    Equipo 2
        Documentación e Investigación:
            Escobedo Dominguez Nadia Gabriela
            Medina Posadas Enrique
            Sevillano Mendoza Victor Manuel
        Programación:
            Lemus Ruiz Mariana Elizabeth
            Vega Gloria Carlos Raymundo
"""

__author__ = ["Vega Gloria Carlos Raymundo", "Lemus Ruiz Mariana Elizabeth"]
__copyright__ = "Copyright 2023, Carlos Vega"
__credits__ = ["Carlos Vega"]
__version__ = "1.0.1"
__maintainer__ = "Carlos Vega"

from typing import List
import numpy as np


class Clasificador():
    __files = []
    __clases = []

    def __init__(self, clases: List[List[int]]) -> None:
        """
            Inicializa un clasificador de regiones.

            Args:
                clases (list[list]): Clases para crear los archivos
        """
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
        """
            Calcula la media de una clase.

            @param clase (list[int]): Lista en formato [B,G,R] con los patrones respectivos a una clase.
            @return: Lista unidimensional con los valores de la media del parámetro clase.
        """
        media = [0, 0, 0]

        for i in clase:
            for j in range(len(i)):
                media[j] += i[j]

        for i in range(len(media)):
            media[i] /= len(clase)

        return media

    def classify(self, patron: List[int]) -> None:
        """
            Clasifica el patrón recibido a la clase que le corresponde.

            @param patron (list[int]): Lista en formato [B,G,R] con los valores del patrón que se quiere clasificar.
        """
        # variable para almacenar las distancias del patrón hacia cada clase
        distancias = []

        for clase in self.__clases:
            # clase = np.array(clase)
            media = self.media(clase)
            covarianza = np.cov(clase.T)
            diferencia = np.subtract(patron, media)
            distancia = diferencia @ np.linalg.inv(covarianza) @ diferencia.T
            distancias.append(distancia)

        # Obtengo el minimo de las distancias, dicho valor es al que pertenece el patrón
        distancia_minima = distancias.index(min(distancias))
        print(
            f"El patron { patron[0][::-1] } pertenece a la clase { distancia_minima + 1 }")
