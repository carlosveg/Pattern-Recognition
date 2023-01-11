"""
    Clasificador KNN con distancia mímina

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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, precision_score


class KNNClassifier():
    def __init__(self, k=1) -> None:
        """
            Inicializa un clasificador de regiones KNN.

            Args:
                k (int) default 1: Valor de k para crear el clasificador
        """
        self.__classifier = KNeighborsClassifier(n_neighbors=k)

    def training(self, patterns: List[List[int]], classes: List[int]) -> int:
        """
            Entrena el clasificador respecto a los parámetros

            Args:
                patterns (list[list[int]]): Contiene los patrones de entrenamiento.
                classes (list[int]): Contiene las clases en orden de los patrones.
        """
        self.__classifier.fit(patterns, classes)

    def classify(self, pattern: List[List]) -> None:
        """
            Clasifica el patrón recibido

            Args:
                pattern (list[int]): Contiene el patrón a clasificar en formato [B,G,R].
        """
        print(
            f"El patron {pattern[0][::-1]} pertenece a la clase {self.__classifier.predict(pattern)[0]}")

    def estadistics(self, patterns_unknow: List[List], patterns: List[List]) -> None:
        """
            Muestra las estadísticas del clasificador respecto a patrones desconocidos.

            Args:
                patterns_unknow (list[list[int]]): Contiene los patrones desconocidos
                patterns (list[int]): Contiene las clases conocidas
        """
        # Obtiene la lista de las predicciones
        predicts = self.__classifier.predict(patterns_unknow)
        matriz = confusion_matrix(predicts, patterns)
        print(f"Matriz de confusion: \n{ matriz }")
        # Obtiene la precisión del clasificador comparando las predicciones con los patrones conocidos
        precision = precision_score(predicts, patterns, average="macro")
        print(f"Precision score: \n{ precision * 100 }%")
