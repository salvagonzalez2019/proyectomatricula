from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import time
#import picamera
root = Tk()
root.title("tesji matricula")
root.geometry('500x400')
tablacontrol = ttk.Notebook(root)
tabRegistro = ttk.Frame(tablacontrol)
tabScanner = ttk.Frame(tablacontrol)

tablacontrol.add(tabRegistro, text = "Registro")
tablacontrol.add(tabScanner, text = "Scaneo")

tablacontrol.pack(expand=1, fill="both")


def insert():
    id = e_id.get()
    nombrealumno = e_nombre_alumno.get();
    apellidoalumno = e_apellido_alumno.get();
    matricula = e_matricula.get();

    if (id == "" or nombrealumno == " " or apellidoalumno == " " or matricula == " "):
        MessageBox.showwarning("Error", "Inserte Bien Los Datos")
    else:
        con = mysql.connect(host='db4free.net',
                            database='alumnostecjilo',
                            user='rootmatricula',
                            password='equiporasberry')
        custor = con.cursor()
        custor.execute(
            "Insert into alumno values('" + id + "','" + nombrealumno + "','" + apellidoalumno + "','" + matricula + "')")
        custor.execute("commit");
        e_id.delete(0, 'end')
        e_nombre_alumno.delete(0, 'end')
        e_apellido_alumno.delete(0, 'end')
        e_matricula.delete(0, 'end')
        muestra()
        MessageBox.showinfo("Tesji", " Exito !!! Se Agrego Con Exito El Usuario")
        con.close();


def borrar():
    if (e_id.get() == ""):
        MessageBox.showerror("Error", "El ID Para Borrar No Se Ha Introduncido bien")
    else:
        con = mysql.connect(host='db4free.net',
                            database='alumnostecjilo',
                            user='rootmatricula',
                            password='equiporasberry')
        custor = con.cursor()
        custor.execute("delete from alumno where id ='" + e_id.get() + "'")
        custor.execute("commit");
        e_id.delete(0, 'end')
        e_nombre_alumno.delete(0, 'end')
        e_apellido_alumno.delete(0, 'end')
        e_matricula.delete(0, 'end')
        muestra()
        MessageBox.showinfo("Tesji", "Se Elimino Con Exito El Usuario")
        con.close();


def actualiza():
    id = e_id.get()
    nombrealumno = e_nombre_alumno.get();
    apellidoalumno = e_apellido_alumno.get();
    matricula = e_matricula.get();

    if (id == "" or nombrealumno == "" or apellidoalumno == "" or matricula == ""):
        MessageBox.showerror("Error", "Los Datos No Estan Completos")
    else:
        con = mysql.connect(host='db4free.net',
                            database='alumnostecjilo',
                            user='rootmatricula',
                            password='equiporasberry')
        custor = con.cursor()
        custor.execute(
            "update alumno set  nombrealumno ='" + nombrealumno + "', apellidoalumno ='" + apellidoalumno + "', matricula ='" + matricula + "' where id= '" + id + "'")
        custor.execute("commit");
        e_id.delete(0, 'end')
        e_nombre_alumno.delete(0, 'end')
        e_apellido_alumno.delete(0, 'end')
        e_matricula.delete(0, 'end')
        muestra()
        MessageBox.showinfo("Estatus de Actualizacion", "Se Actualizo Con Exito El Usuario")
        con.close();


def obtener():
    if (e_id.get() == ""):
        MessageBox.showinfo("Error","No Se Introdujo El ID Del Usuario Correctamente")
    else:
        con = mysql.connect(host='db4free.net',
                            database='alumnostecjilo',
                            user='rootmatricula',
                            password='equiporasberry')
        custor = con.cursor()
        custor.execute("select * from alumno where id ='" + e_id.get() + "'")
        rows = custor.fetchall()
        for row in rows:
            e_nombre_alumno.insert(0, row[1])
            e_apellido_alumno.insert(0, row[2])
            e_matricula.insert(0, row[3])
        con.close();
def muestra():
    con = mysql.connect(host='db4free.net',
                        database='alumnostecjilo',
                        user='rootmatricula',
                        password='equiporasberry')
    custor = con.cursor()
    custor.execute("select * from alumno")
    rows = custor.fetchall()
    list.delete(0,list.size())
    for row in rows:
        insertData = str(row[0])+' '+row[1]+' '+row[2]+' '+row[3]
        list.insert(list.size()+1, insertData)
        con.close();

id = Label(tabRegistro, text='Id Alumno', font=('bold', 10))
id.place(x=20, y=30)
nombrealumno = Label(tabRegistro, text='Nombre Del Alumno', font=('bold', 10))
nombrealumno.place(x=20, y=60)
apellidoalumno = Label(tabRegistro, text='Apellido Del Alumno', font=('bold', 10))
apellidoalumno.place(x=20, y=90)
matricula = Label(tabRegistro, text='Matricula', font=('bold', 10))
matricula.place(x=20, y=120)
e_id = Entry(tabRegistro)
e_id.place(x=200, y=30)
e_nombre_alumno = Entry(tabRegistro)
e_nombre_alumno.place(x=200, y=60)
e_apellido_alumno = Entry(tabRegistro)
e_apellido_alumno.place(x=200, y=90)
e_matricula = Entry(tabRegistro)
e_matricula.place(x=200, y=120)

insert = Button(tabRegistro, text="Insertar", font=('italic', 10), bg="white", command=insert)
insert.place(x=20, y=180)
borrar = Button(tabRegistro, text="Borrar", font=('italic', 10), bg="white", command=borrar)
borrar.place(x=100, y=180)
actualiza = Button(tabRegistro, text="Actualiza", font=('italic', 10), bg="white", command=actualiza)
actualiza.place(x=170, y=180)
obtener = Button(tabRegistro, text="Buscar", font=('italic', 10), bg="white", command=obtener)
obtener.place(x=260, y=180)

list = Listbox(tabRegistro)
list.place(x=352, y=20,width=200, height=120)
muestra()


def butonescan():
    # with picamera.PiCamera() as picam:
    #    picam.resolution = (2592, 1944)
    #   picam.start_preview()
    #  time.sleep(3)
    # picam.capture('foto.jpg',resize=(1024,768))
    # picam.stop_preview()
    # picam.close()

    img = cv2.imread('foto2.jpg', cv2.IMREAD_COLOR)

    img = cv2.resize(img, (710, 400))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convertir a escala de grises
    # cv2.imshow('gray',gray)#pone gris la imagen
    gray = cv2.bilateralFilter(gray, 5, 75, 75)  # Desenfoque para reducir el ruido
    edged = cv2.Canny(gray, 300, 150)
    # Realizar detección de bordes
    # encontrar contornos en la imagen de borde, mantener solo el más grande
    # ones, e inicializa nuestro contorno de pantalla
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None

    # bucle sobre nuestros contornos
    for c in cnts:
        # aproximar el contorno
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is None:
        detected = 0
        print("o contour detected")
    else:
        detected = 1

    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

    # Enmascarar la parte que no sea la placa de matrícula

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)

    # Ahora recortar

    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
    # Leer la matrícula

    text =pytesseract.image_to_string(Cropped, config='--psm 11')
    print("La placa es:", text)
    matricula=str(text)
    nombrebase = Label(tabScanner, text="PLACA: ", font=('bold', 10)).place(x=230,y=100)
    matc = Label(tabScanner, text=matricula, font=('bold', 10)).place(x=320,y=100)

    con = mysql.connect(host='db4free.net',
                        database='alumnostecjilo',
                        user='rootmatricula',
                        password='equiporasberry')
    custor = con.cursor()
    custor.execute("select nombrealumno, apellidoalumno from alumno where matricula ='" + matricula + "'")
    rows = custor.fetchall()
    print("engtrando")
    for matricula in rows:
        if matricula in rows:
            nombrebase = Label(tabScanner, text="Nombre: ", font=('bold', 10)).place(x=230, y=130)
            nombreal = Label(tabScanner, text=matricula, font=('bold', 10)).place(x=320, y=130)
    print("engtrando")
    if matricula not in rows:
            print("engtro")
            resultado = MessageBox.askquestion("Error",
                                               "¿Este Usuario No Esta Registrado Desea Hacerlo?")
            if resultado == "yes":
                tablacontrol.select(tabRegistro)  # regresa a la tabla 1
            else:
                resultado2 = MessageBox.askquestion("Warning", "Esta Seguro")
                if resultado2 == "yes":
                    MessageBox.showinfo("¡Gracias Por Confirmar!")
                else:
                    tablacontrol.select(tabRegistro)

                    # cv2.imshow('image', img)
                    # #cv2.imshow('Cropped', Cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    con.close();
butonescan= Button(tabScanner,text='Empezar Scaneo',font=('italic', 10), bg="white", command =butonescan)
butonescan.place(x=40,y=100)
def regreso(tabregistro):
    tabRegistro.winfo_parent().deiconify()


root.mainloop()