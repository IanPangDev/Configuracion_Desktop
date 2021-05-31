from tkinter import *
import turtle
from os import system as cmd
from pynput.keyboard import Key, Controller
from threading import Thread
from _thread import interrupt_main
from time import time, sleep
from win32gui import IsWindowVisible, EnumWindows, GetWindowText

def revision_de_ventana():

    def winEnumHandler(hwnd, list):
        if IsWindowVisible(hwnd):
            r = {'nombre': GetWindowText(hwnd)}
            if 'Nueva pestaña - Google Chrome' == r.get('nombre'):
                print('Está')
                list.append(0)
            else:
                print('No está')

    inicio = time()
    while True:
        list = []
        EnumWindows(winEnumHandler, list)
        try:
            if list[0] == 0:
                print(list)
                final = time() - inicio
                print(f'{final}')
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
    control.press('5')
    control.release(Key.cmd)
    control.release('5')
    interrupt_main()


root = Tk()
root.title("選べ")
root.iconbitmap("ENG.ico")
root.resizable(False, False)

#Centra la ventana
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#Centra la ventana

principal_frame = Frame(root, width="400", height="350", bg='black')

saludo_label = Label(principal_frame, text='Hola, elige una configuración',
                     fg="white", bg='black').place(x=120, y=200)

def python_development():
    cmd('start chrome')
    verificador = Thread(target=revision_de_ventana)
    verificador.start()

boton_python = Button(root, text="Conf. Python", command=python_development).place(x=70, y=260)

def sin_conf():
    exit()

boton_sin_configuracion = Button(root, text="Sin configuración", command=sin_conf).place(x=70, y=300)

def conf_escolar():
    cmd('start chrome https://classroom.google.com/')
    cmd('start C:\\Users\\Wuchang\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    exit()

boton_escolar = Button(root, text="Conf. Escolar", command=conf_escolar).place(x=250, y=300)

def conf_visual():
    pass

boton_visual = Button(root, text='Conf. VSC', command=conf_visual()).place(x=250, y=260)

principal_frame.pack()

root.mainloop()