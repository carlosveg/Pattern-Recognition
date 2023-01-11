import cv2
import numpy as np
from assets import utils
from classifiers.knn import KNNClassifier
from classifiers.maam import MAAM
from classifiers.perceptron import Perceptron
from classifiers.mahalanobis import Clasificador
from assets.imagen import Imagen
from assets.clases import c1, c2, c3, correctos
from matplotlib import pyplot as plt


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
    paths = utils.getImagesFromPath(
        "assets/image/Digitos-Imagen-pequena/")
    images = utils.getImages(paths, 0)
    classes = ["uno", "tres", "siete", "seis", "ocho",
               "nueve", "dos", "cuatro", "cinco", "cero"]

    X_train = []
    for image in images:
        # _, img = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
        img = np.array(image).flatten()
        # img = img / 255
        X_train.append(img)

    """
        Este bloque de código es para mostrar el ejemplo del
        porque se aplicó la umbralización a las imágenes
    """
    # _, ax = plt.subplots(2)
    # ax[0].imshow(images[0], cmap="gray")
    # ax[0].set_title("Imagen original")
    # ax[0].axis("off")
    # _, image = cv2.threshold(images[0], 160, 255, cv2.THRESH_BINARY)
    # ax[1].imshow(image, cmap="gray")
    # ax[1].set_title("Imagen umbralizada")
    # plt.show()
    # print(np.shape(X_train[0]))
    # print(X_train[0])

    maam = MAAM(X_train, X_train)
    matrix = maam.getLearningMatrix()
    matrix = matrix.reshape(2500, 2500)

    # este código es para probar con una imagen con ruido
    image = cv2.imread("assets/image/Ruido/ruido_ad/imagead99.bmp", 0)
    # _, img = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
    img = np.array(image).flatten()
    # img = img / 255

    result = maam.classify(matrix, img)
    result = result.reshape(50, 50)
    cv2.imshow("Resultado", result)
    cv2.waitKey()
    cv2.destroyAllWindows()
