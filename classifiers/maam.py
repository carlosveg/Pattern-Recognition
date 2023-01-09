import numpy as np


class MAAM():
    __arrays = None

    def __init__(self, x: list[list], y: list[list]):
        self.__arrays = self.__firstPhaseOfTraining(x, y)

    def __firstPhaseOfTraining(self, x: list, y: list):
        arrays = []

        for list_x, list_y in zip(x, y):
            matrix_aux = []
            for i in list_y:
                aux = []
                for j in list_x:
                    aux.append(i - j)
                matrix_aux.append(aux)
            arrays.append(matrix_aux)

        return arrays

    def getLearningMatrix(self):
        matrix = []

        for sublistas in zip(*self.__arrays):
            for fila in zip(*sublistas):
                matrix.append(
                    max(fila))

        return np.array(matrix)

    def classify(self, matrix: list[list], pattern: list):
        result = []

        for fila in matrix:
            aux = []
            for pos in range(len(pattern)):
                aux.append(fila[pos]+pattern[pos])
            result.append(min(aux))

        return np.array(result)
