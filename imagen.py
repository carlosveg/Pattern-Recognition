import cv2
import matplotlib.pyplot as plt
import matplotlib.image as img

# clasificador_move imprime la clase del pixel en el que se encuentrea el mouse
# con tan solo moverlo, o hacer clic
def clasificador_move(event,x,y,flags,param):
    # Favor de insertar clasificador
    if (event==0):
        print(f"{x},{y}: {param[y,x]}")

# clasificador_click imprime la clase del pixel de la imagen en el que hace clic
def clasificador_clic(event,x,y,flags,param):
    # Favor de insertar clasificador
    if (event==1):
        print(f"{x},{y}: {param[y,x]}")
    

class Imagen():
    def __init__(self,nombre,tipo):
        # Abrimos la imgaen con el metdo imread de cv2
        # este metodo nos devuelve una matriz 2x2 cada elemento de la matriz
        # es una lista de 3 valores (rgb) equivalentes al color de ese pixel
        # tambien puede ser vista como una matriz 2x2x3
        self._imagen=cv2.imread(nombre,tipo)

    def abrir(slef):
        cv2.imshow("imagen",slef._imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def clasificar_move(self):
        cv2.namedWindow("imagen")
        
        cv2.setMouseCallback("imagen",clasificador_move,param=self._imagen)
        while True:
            cv2.imshow("imagen",self._imagen)
            # Para salir del bucle presionar la tecla Esc la cual tiene el valor ASCII = 27
            # de lo contrario la ventana se seguira abriendo sin fin
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        
        cv2.destroyAllWindows()
    
    def clasificar_clic(self):
        cv2.namedWindow("imagen")
        
        cv2.setMouseCallback("imagen",clasificador_clic,param=self._imagen)
        while True:
            cv2.imshow("imagen",self._imagen)
            # Para salir del bucle presionar la tecla Esc la cula tiene el valor ASCII = 27
            # de lo contrario la ventana se seguira abriendo sin fin
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        
        cv2.destroyAllWindows()

    def valor_pixel(self,x,y):
        # Devolvemos el valor rgb de en formato [r,g,b] del pixel[x,y]
        return self._imagen[y,x]