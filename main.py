from imagen import Imagen


def main():
    imagen = Imagen('./image/3-regiones.png', 1)
    imagen.clasificar_clic()
    print("after")


if __name__ == '__main__':
    main()
