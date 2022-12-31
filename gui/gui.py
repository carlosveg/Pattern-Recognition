from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, filedialog, messagebox
import cv2
import imutils
from PIL import Image, ImageTk
# from ruido import ruidoad


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

        labelInputImageInfo = Label(tab_noise, text="IMAGEN DE ENTRADA")
        labelInputImageInfo.grid(column=0, row=1, padx=5, pady=5)

        labelOutputImage.image = ""
        selected.set(0)
    else:
        messagebox.showinfo("Informacion", "Seleccione una imagen!!")


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def generate_noise():
    global current_value, selected, image, imageWithNoise

    if selected.get() == 0:
        messagebox.showinfo("Informacion", "Seleccione un tipo de ruido!!")
        return

    print(f"Generating noise {selected.get()}: {current_value.get()}")
    imageToShow = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShow)
    img = ImageTk.PhotoImage(image=im)

    labelOutputImage.configure(image=img)
    labelOutputImage.image = img

    labelOutputImageInfo = Label(tab_noise, text="IMAGEN DE SALIDA")
    labelOutputImageInfo.grid(column=1, row=0, padx=5, pady=5)


def save_image():
    import random
    global imageWithNoise

    if imageWithNoise == None:
        messagebox.showinfo(
            "Informacion", "No se ha generado una imagen para guardar!!")
        return

    path_image = f"assets/image/"
    image_name = f"image{int(random.uniform(0, 1000000))}.png"
    print(f"Saving image on path: {path_image+image_name}")
    # cv2.imwrite(path_image+image_name, imageWithNoise)
    messagebox.showinfo("Informacion", "Imagen guardada como " + image_name)


image = None
imageWithNoise = None
# Configuration of tkinter window
root = Tk()
root.title("Pattern Recognition Projects")

# Create a notebook for use tabs
notebook = ttk.Notebook()
notebook.pack(fill="both", expand="yes")

# Create tabs that be added to notebook
tab_noise = Frame(notebook)
tab_memory = Frame(notebook)

# Add tabs to notebook
notebook.add(tab_noise, text="Generador de Ruido")
notebook.add(tab_memory, text="Memoria Asociativa")

""" Functions for managing scale widget """
current_value = IntVar()


def slider_changed(event):
    labelNoiseValue.configure(text=get_current_value())


# Add content to tab_noise
btn = Button(tab_noise, text="Elegir imagen", command=select_image)
btn.grid(column=0, row=0, padx=5, pady=5)
labelInputImage = Label(tab_noise)
labelInputImage.grid(column=0, row=2)
labelOutputImage = Label(tab_noise)
labelOutputImage.grid(column=1, row=1, rowspan=10)
labelParameters = Label(tab_noise, text="Parametros para generar ruido")
labelParameters.grid(column=0, row=3, padx=5, pady=5)
selected = IntVar()
ruidoAditivo = Radiobutton(
    tab_noise,
    text="Ruido Aditivo",
    width=25,
    value=1,
    variable=selected).grid(column=0, row=4, padx=5, pady=5)
ruidoSustractivo = Radiobutton(
    tab_noise,
    text="Ruido Sustractivo",
    width=25,
    value=2,
    variable=selected).grid(column=0, row=5, padx=5, pady=5)
ruidoMixto = Radiobutton(
    tab_noise,
    text="Ruido Mixto",
    width=25,
    value=3,
    variable=selected).grid(column=0, row=6, padx=5, pady=5)
slider = Scale(
    tab_noise,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current_value
).grid(column=0, row=7, padx=5, pady=5)
labelNoiseValue = ttk.Label(
    tab_noise,
    text=get_current_value()
)
labelNoiseValue.grid(column=0, row=8, padx=5, pady=5)
btnGenerateNoise = Button(
    tab_noise,
    text="Generar ruido",
    command=generate_noise).grid(column=0, row=9, padx=5, pady=5)
if imageWithNoise != None:
    saveImage = Button(
        tab_noise,
        text="Guardar imagen",
        command=save_image).grid(column=0, row=10, padx=5, pady=5)


# Tab memory
label2 = Label(
    tab_memory, text="Esta etiqueta va en el tab de la memoria asociativa")
label2.place(x=20, y=20)

# mainloop must be at end
root.mainloop()
