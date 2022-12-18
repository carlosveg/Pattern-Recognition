import cv2
import numpy as np


class Imagen():
    def __init__(self, nombre, tipo, clasificador):
        self._imagen = cv2.imread(nombre, tipo)
        self.__clasificador = clasificador

    def abrir(self):
        cv2.imshow("imagen", self._imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_image(self):
        cv2.namedWindow("imagen")
        cv2.setMouseCallback(
            "imagen", self.clasificador_clic, param=self._imagen)

        while True:
            cv2.imshow("imagen", self._imagen)
            # Para salir del bucle presionar la tecla Esc la cual tiene el valor ASCII = 27
            # de lo contrario la ventana se seguira abriendo sin fin
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

    def clasificador_clic(self, event, x, y, flags, param):
        if (event == 1):
            print(f"{x},{y}: {param[y,x]}")
            self.__clasificador.mahalanobis(param[y, x])

    def valor_pixel(self, x, y):
        # Devolvemos el valor rgb de en formato [r,g,b] del pixel[x,y]
        return self._imagen[y, x]

    def obtener_canales(self):
        return cv2.split(self._imagen)
