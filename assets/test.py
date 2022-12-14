import random
import os
import numpy as np
from typing import List
from clases import *

c1_2 = [
    [200, 160, 120],
    [210, 170, 130],
    [215, 172, 133],
    [210, 165, 134],
    [198, 177, 138]
]


def media(clase: List[int]) -> List[int]:
    media = [0, 0, 0]

    for i in clase:
        for j in range(len(i)):
            media[j] += i[j]

    for i in range(len(media)):
        media[i] /= len(clase)

    return media


def mahalanobis(patron: List[int], clases: List[List[int]]):
    distancias = []
    for clase in clases:
        clase = np.array(clase)
        media2 = media(clase)
        covarianza = np.cov(clase.T)
        diferencia = np.subtract(patron, media2)
        distancia = diferencia @ np.linalg.inv(covarianza) @ diferencia.T
        distancias.append(distancia)

    print(distancias)
    distancia_minima = distancias.index(min(distancias))
    print(
        f"El patron { patron } pertenece a la clase { distancia_minima + 1 }")


def init(clases):
    files = []
    for clase in clases:
        filename = f"dataClass{clases.index(clase) + 1}.txt"
        files.append(filename)
        np.savetxt(filename, clase)

    for file in files:
        data = np.loadtxt(file)
        print(f"Datos de clase {file} -> {data}")
    # print(files)


patron = [236, 231, 228]
patron2 = [4, 58, 44]
patron3 = [173, 212, 237]
c1_2 = np.array(c1_2)
clases = [c1, c2, c3]
# mahalanobis(patron3, clases)

# init(clases)


def getFiles():
    contentPath = os.listdir(os.getcwd()+"/../")
    print(os.getcwd())
    print(contentPath)
    # filesTXT = [file if ".txt" in file else "" for file in contentPath]
    filesTXT = [file for file in contentPath if ".txt" in file]
    print(filesTXT)


# for i in range(10):
#     print(random.uniform(0, 1))

x = [[1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 0, 1, 1, 0]]
y = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def firstPhaseOfTraining(x: list, y: list):
    matrix = []

    for list_x, list_y in zip(x, y):
        matrix_aux = []
        for i in list_y:
            aux = []
            for j in list_x:
                aux.append(i - j)
            matrix_aux.append(aux)
        matrix.append(matrix_aux)

    return matrix


matrix = firstPhaseOfTraining(x, y)
matrix = np.array(matrix)
print(f"Matrices: \n{matrix}")


def getLearningMatrix(arrays: np.array):
    matrix = []

    for sublistas in zip(*arrays):
        # print(sublistas)
        for fila in zip(*sublistas):
            # print(filas)
            matrix.append(
                max(fila))

    return np.array(matrix)


final = getLearningMatrix(matrix)
# print(final)
final = final.reshape(3, 5)
print(f"Memoria: \n{final}")


def classify(matrix, pattern):
    result = []

    for fila in matrix:
        aux = []
        for pos in range(len(pattern)):
            aux.append(fila[pos]+pattern[pos])
        result.append(min(aux))

    return result


value = classify(final, [1, 0, 1, 0, 1])

print(f"Resultado: \n{value}")
