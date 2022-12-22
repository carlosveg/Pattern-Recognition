from imagen import Imagen
from clases import c1, c2, c3, correctos
# from clasificador import Clasificador
from utils import doAll
from knn import KNNClassifier
import numpy as np


def main():
    """ MEDIA Y MATRIZ DE COVARIANZA DESCONOCIDAS (MAHALANOBIS) """
    # clasificador = Clasificador([c1, c2, c3])
    # imagen = Imagen('../image/3-regiones.png', 1, clasificador)
    # imagen.show_image()

    """ KNN CON DISTANCIA MINIMA """
    knn = KNNClassifier(k=1)
    data_adapted = doAll()
    knn.training(patterns=np.array(
        data_adapted[0]), classes=np.array(data_adapted[1]))
    imagen = Imagen('../image/3-regiones.png', 1, knn)
    imagen.show_image()

    print('----------------ESTADISTICAS----------------')
    # Para visualizar las estadisticas del clasificador
    patterns = c1+c2+c3
    # print(patterns)
    print(f"correctos: {len(correctos)}")
    knn.estadistics(patterns, correctos)


if __name__ == '__main__':
    main()
