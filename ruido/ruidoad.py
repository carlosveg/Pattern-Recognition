import numpy as np
import cv2
import random
from tkinter import filedialog 
#funcion para la aditividad
def sp_noise(image,prob):
    output=np.zeros(image.shape,np.uint8)
    thres = 1 -prob
    for i in range(image.shape[0]):
        for j in range (image.shape[1]):
            rdn=random.random()
            if rdn>thres:
            
                output[i][j]=255
            else:
                output[i][j]=image[i][j]

    return output


imagen = filedialog.askopenfilename()
dir_img = imagen
fra=cv2.imread(imagen)
# Cambiar a escala de grises
gr=cv2.cvtColor(fra, cv2.COLOR_BGR2GRAY)
# Abrir imagen
cv2.imshow('imagen original',gr)

k=cv2.waitKey(0)

nois=sp_noise(gr,0.50)

cv2.imshow('imagen con ruido',nois)
k=cv2.waitKey(0)