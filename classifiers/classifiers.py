import numpy as np
from assets import utils
from classifiers.knn import KNNClassifier
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
