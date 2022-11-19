import cv2
from histograma import Histograma
from imagen import Imagen


def main():
    imagen = Imagen('./image/3-regiones.png', 1)
    hist = Histograma('./image/3-regiones.png', 0)
    print(imagen.clasificar_move())
    print(hist.matriz_covarianza())
    [b, g, r] = imagen.obtener_canales()
    cv2.imshow("Canal azul", b)
    cv2.imshow("Canal verde", g)
    cv2.imshow("Canal rojo", r)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
