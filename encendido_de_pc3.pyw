import tkinter as tk
import turtle
from os import system as cmd
from pynput.keyboard import Key, Controller
from threading import Thread
from time import sleep
from win32gui import IsWindowVisible, EnumWindows, GetWindowText

class Modos():
    def python_development(self):
        cmd('start chrome')
        verificador = Thread(target=self.revision_de_ventana('5'))
        verificador.start()
    def sin_conf(self):
        self.quit()

    def conf_escolar(self):
        cmd('start chrome https://classroom.google.com/')
        cmd('start C:\\Users\\Wuchang\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        self.quit()

    def conf_visual(self):
        cmd('start chrome')
        self.verificador = Thread(target=self.revision_de_ventana('3'))
        self.verificador.start()

    def revision_de_ventana(self, aplicacion):

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
        self.quit()

class MainAplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)

        # Centra la ventana
        window_width = 400
        window_height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        # Centra la ventana

        canvas = tk.Canvas(master=root, width=150, height=150)
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

        saludo_label = tk.Label(parent, text='Hola, elige una configuración',
                                fg="white", bg='black').place(x=120, y=200)

        boton_python = tk.Button(parent, text="Conf. Python", command=Modos.python_development).place(x=70, y=260)

        boton_sin_configuracion = tk.Button(parent, text="Sin configuración", command=Modos.sin_conf).place(x=70, y=300)

        boton_escolar = tk.Button(parent, text="Conf. Escolar", command=Modos.conf_escolar).place(x=250, y=300)

        boton_visual = tk.Button(parent, text='Conf. VSC', command=Modos.conf_visual).place(x=250, y=260)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("選べ")
    root.iconbitmap("ENG.ico")
    root.resizable(False, False)
    root.config(bg='black')
    MainAplication(root).pack()
    root.mainloop()