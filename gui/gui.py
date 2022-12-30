from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import imutils
from PIL import Image, ImageTk


def select_image():
    path_image = filedialog.askopenfilename(
        filetypes=[("image", ".jpg"), ("image", ".png"), ("image", ".jpeg")])

    if len(path_image) > 0:
        global image

        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)

        imageToShow = imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        labelInputImage.configure(image=img)
        labelInputImage.image = img

        labelInfo1 = Label(tab_ruido, text="IMAGEN DE ENTRADA")
        labelInfo1.grid(column=0, row=1, padx=5, pady=5)

    else:
        print("Please select an image")


image = None
# Configuration of tkinter window
root = Tk()
# root.geometry("400x400")
root.title("Pattern Recognition Projects")

# Create a notebook for use tabs
notebook = ttk.Notebook()
notebook.pack(fill="both", expand="yes")

# Create tabs that be added to notebook
tab_ruido = Frame(notebook)
tab_memoria = Frame(notebook)

# Add tabs to notebook
notebook.add(tab_ruido, text="Ruido")
notebook.add(tab_memoria, text="Memoria")

# Functions for managing scale widget
current_value = DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


# Add content to tab_ruido
btn = Button(tab_ruido, text="Elegir imagen", command=select_image)
btn.grid(column=0, row=0, padx=5, pady=5)
labelInputImage = Label(tab_ruido)
labelInputImage.grid(column=0, row=2)
labelParameters = Label(tab_ruido, text="Parametros para generar ruido")
labelParameters.grid(column=0, row=3, padx=5, pady=5)
selected = IntVar()
ruido_aditivo = Radiobutton(
    tab_ruido,
    text="Ruido Aditivo",
    width=25,
    value=1,
    variable=selected).grid(column=0, row=4, padx=5, pady=5)
ruido_sustractivo = Radiobutton(
    tab_ruido,
    text="Ruido Sustractivo",
    width=25,
    value=2,
    variable=selected).grid(column=0, row=5, padx=5, pady=5)
ruido_mixto = Radiobutton(
    tab_ruido,
    text="Ruido Mixto",
    width=25,
    value=3,
    variable=selected).grid(column=0, row=6, padx=5, pady=5)
#  slider
# current_value = IntVar()
slider = Scale(
    tab_ruido,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current_value
).grid(column=0, row=7, padx=5, pady=5)
value_label = ttk.Label(
    tab_ruido,
    text=get_current_value()
)
value_label.grid(column=0, row=8, padx=5, pady=5)

label2 = Label(
    tab_memoria, text="Esta etiqueta va en el tab de la memoria asociativa")
label2.place(x=20, y=20)

# mainloop must be at end
root.mainloop()
