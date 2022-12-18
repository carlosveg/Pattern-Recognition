from imagen import Imagen
from clases import c1, c2, c3
from clasificador import Clasificador


def main():
    clasificador = Clasificador([c1, c2, c3])
    imagen = Imagen('../image/3-regiones.png', 1, clasificador)
    imagen.show_image()


if __name__ == '__main__':
    main()
