import cv2
from histograma import Histograma
from imagen import Imagen
def main():
    imagen = Imagen('./image/3-regiones.png',1)
    print(imagen.clasificar_move())
    


if __name__ == '__main__':
    main() 
    