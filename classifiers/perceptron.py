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

__author__ = ["Vega Gloria Carlos Raymundo"]
__copyright__ = "Copyright 2023, Carlos Vega"
__credits__ = ["Carlos Vega"]
__version__ = "1.0.1"
__maintainer__ = "Carlos Vega"

from typing import List
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, precision_score


class Perceptron():
    def __init__(self):
        self.__model = MLPClassifier(hidden_layer_sizes=(
            64, 32), activation="relu", solver="adam")

    def training(self, patterns: List[List], classes: List):
        self.__model.fit(patterns, classes)

    def classify(self, pattern: List):
        print(
            f"El patron {pattern[0][::-1]} pertenece a la clase {self.__model.predict(pattern)[0]}")

    def estadistics(self, patterns_unknow: List[List], patterns: List[List]) -> None:
        predicts = self.__model.predict(patterns_unknow)
        matriz = confusion_matrix(predicts, patterns)
        print(f"Matriz de confusion: \n{ matriz }")
        precision = precision_score(predicts, patterns, average="macro")
        print(f"Precision score: \n{ precision * 100 }%")
