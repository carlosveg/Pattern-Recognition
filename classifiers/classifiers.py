import csv
from typing import List
import cv2
import numpy as np
from assets import utils
from classifiers.knn import KNNClassifier
from classifiers.maam import MAAM
from classifiers.perceptron import Perceptron
from classifiers.mahalanobis import Clasificador
from assets.imagen import Imagen
from assets.clases import c1, c2, c3, correctos


def mahalanobis():
    clasificador = Clasificador([c1, c2, c3])
    imagen = Imagen('assets/image/3-regiones.png', 1, clasificador)
    imagen.show_image()


def knn() -> None:
    knn = KNNClassifier(k=1)
    patterns, classes = utils.doAll('assets/data.csv')
    knn.training(np.array(patterns), np.array(classes))
    imagen = Imagen('assets/image/3-regiones.png', 1, knn)
    imagen.show_image()

    print('----------------ESTADISTICAS----------------')
    patterns = c1+c2+c3
    print(f"Patrones para obtener estadísticas: {len(correctos)}")
    knn.estadistics(patterns, correctos)


def perceptron() -> None:
    perceptron = Perceptron()
    patterns, classes = utils.doAll('assets/data.csv')
    perceptron.training(np.array(patterns), np.array(classes))
    imagen = Imagen('assets/image/3-regiones.png', 1, perceptron)
    imagen.show_image()

    print('----------------ESTADISTICAS----------------')
    patterns = c1+c2+c3
    print(f"Patrones para obtener estadísticas: {len(correctos)}")
    perceptron.estadistics(patterns, correctos)


def maam() -> None:
    maam = MAAM()
    paths = utils.getImagesFromPath(
        "assets/image/Digitos-Imagen-pequena/")
    # print(f"Training data: {paths}")
    images = utils.getImages(paths, 0)
    classes = ["uno", "tres", "siete", "seis", "ocho",
               "nueve", "dos", "cuatro", "cinco", "cero"]
    X_train = []
    y_train = []

    for i in range(10):
        img = cv2.imread(paths[i], 0)
        # img = cv2.resize(img, (28, 28))
        img = img / 255.0  # Normalizamos la escala de grises a valores entre 0 y 1
        img = np.array(img).flatten()  # Aplanamos la imagen en un array 1D
        X_train.append(img)
        y_train.append(classes[i])

    X_train = np.array(X_train, dtype='float32')
    y_train = np.array(y_train)

    maam.training(X_train, y_train)
    imageTest = cv2.resize(images[2], (50, 50))
    imageTest = imageTest / 255.0
    imageTest = np.array(imageTest).flatten()
    imageTest = imageTest.reshape(50, 50)
    imageToPredict = imageTest.reshape(-1, 2500)
    image = cv2.imread("assets/image/cinco4.png", 0)
    image = cv2.resize(image, (50, 50))
    image = image / 255.0
    image = np.array(image).flatten()
    image = image.reshape(50, 50)
    imageToPredict = image.reshape(-1, 2500)
    maam.classify(imageToPredict)
