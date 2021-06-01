from tkinter import *
import turtle
from os import system as cmd
from pynput.keyboard import Key, Controller
from threading import Thread
from time import sleep
from win32gui import IsWindowVisible, EnumWindows, GetWindowText

def revision_de_ventana(aplicacion):

    def winEnumHandler(hwnd, list):
        if IsWindowVisible(hwnd):
            r = {'nombre': GetWindowText(hwnd)}
            if 'Nueva pestaña - Google Chrome' == r.get('nombre'):
                list.append(0)

    while True:
        list = []
        EnumWindows(winEnumHandler, list)
        try:
            if list[0] == 0:
                break
        except:
            continue

    sleep(.5)

    control = Controller()
    control.press(Key.ctrl)
    control.press(Key.cmd)
    control.press('d')
    control.release(Key.cmd)
    control.release(Key.ctrl)
    control.release('d')
    control.press(Key.cmd)
    control.press(aplicacion)
    control.release(Key.cmd)
    control.release(aplicacion)
    root.quit()


root = Tk()
root.title("選べ")
root.iconbitmap("ENG.ico")
root.resizable(False, False)
root.config(bg='black')

#Centra la ventana
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#Centra la ventana

canvas = Canvas(master=root, width=150, height=150)
canvas.pack(pady=20)
canvas.update()

screen = turtle.TurtleScreen(canvas)
screen.bgcolor('black')
dibujo = turtle.RawTurtle(screen)
dibujo.color('white')
dibujo.hideturtle()
dibujo.penup()
dibujo.setposition(0,-50)
dibujo.write("伍", align='center', font=("Times New Roman", 70, "bold"))

saludo_label = Label(root, text='Hola, elige una configuración',
                     fg="white", bg='black').place(x=120, y=200)

def python_development():
    cmd('start chrome')
    verificador = Thread(target=revision_de_ventana('5'))
    verificador.start()

boton_python = Button(root, text="Conf. Python", command=python_development).place(x=70, y=260)

def sin_conf():
    root.quit()

boton_sin_configuracion = Button(root, text="Sin configuración", command=sin_conf).place(x=70, y=300)

def conf_escolar():
    cmd('start chrome https://classroom.google.com/')
    cmd('start C:\\Users\\Wuchang\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    root.quit()

boton_escolar = Button(root, text="Conf. Escolar", command=conf_escolar).place(x=250, y=300)

def conf_visual():
    cmd('start chrome')
    verificador = Thread(target=revision_de_ventana('3'))
    verificador.start()


boton_visual = Button(root, text='Conf. VSC', command=conf_visual).place(x=250, y=260)

root.mainloop()