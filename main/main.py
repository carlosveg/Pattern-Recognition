import numpy as np
from imagen import Imagen
import assets
from classifiers.knn import KNNClassifier
from assets.clases import c1, c2, c3, correctos


def main():
    knn = KNNClassifier(k=1)
    data_adapted = assets.doAll()
    knn.training(patterns=np.array(
        data_adapted[0]), classes=np.array(data_adapted[1]))
    imagen = Imagen('../image/3-regiones.png', 1, knn)
    imagen.show_image()

    print('----------------ESTADISTICAS----------------')
    patterns = c1+c2+c3
    # print(patterns)
    print(f"correctos: {len(correctos)}")
    knn.estadistics(patterns, correctos)


if __name__ == '__main__':
    main()
