from tkinter import Frame, Canvas, Label, Button, Tk
from turtle import TurtleScreen, RawTurtle
from os import system as cmd
from pynput.keyboard import Key, Controller
from threading import Thread
from win32gui import IsWindowVisible, EnumWindows, GetWindowText

class Mythread1(Thread):
    def __init__(self, threadID, aplicacion):
        Thread.__init__(self)
        self.threadID = threadID
        self.aplicacion = aplicacion

    def comandos(self):
        verifica = Mythread2(2)
        verifica.revisar_pantalla()
        verifica.start()
        verifica.join()
        control = Controller()
        control.press(Key.ctrl)
        control.press(Key.cmd)
        control.press('d')
        control.release(Key.cmd)
        control.release(Key.ctrl)
        control.release('d')
        control.press(Key.cmd)
        control.press(self.aplicacion)
        control.release(Key.cmd)
        control.release(self.aplicacion)
        root.quit()

class Mythread2(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.threadID = threadID

    def revisar_pantalla(self):
        def ventanas(hwnd, list):
            if IsWindowVisible(hwnd):
                r = {'nombre': GetWindowText(hwnd)}
                if 'Nueva pestaña - Google Chrome' == r.get('nombre'):
                    list.append(0)

        while True:
            list = []
            EnumWindows(ventanas, list)
            try:
                if list[0] == 0:
                    break
            except:
                continue

class MainAplication(Frame):
    def __init__(self, parent):
        Frame.__init__(self, master=parent)
        self.parent = parent

        # Caracteristicas de la ventana
        self.parent.title("選べ")
        self.parent.iconbitmap("ENG.ico")
        #self.parent.iconbitmap(".icon\\ENG.ico") Para version de escritorio
        self.parent.resizable(False, False)
        self.parent.config(bg='black')
        # Caracteristicas de la ventana

        # Centra la ventana
        window_width = 400
        window_height = 350
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.parent.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        # Centra la ventana

        # Logotipo
        canvas = Canvas(master=self.parent, width=150, height=150)
        canvas.pack(pady=20)
        canvas.update()

        screen = TurtleScreen(canvas)
        screen.bgcolor('black')
        dibujo = RawTurtle(screen)
        dibujo.color('white')
        dibujo.hideturtle()
        dibujo.penup()
        dibujo.setposition(0, -50)
        dibujo.write("伍", align='center', font=("Times New Roman", 70, "bold"))
        # Logotipo

        #Procesos
        def python_development():
            cmd('start chrome')
            verificador = Mythread1(1, '5')
            verificador.comandos()
            verificador.start()

        def sin_conf():
            root.quit()

        def conf_escolar():
            cmd('start chrome https://classroom.google.com/')
            cmd('start C:\\Users\\Wuchang\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
            root.quit()

        def conf_visual():
            cmd('start chrome')
            verificador = Mythread1(1, '3')
            verificador.comandos()
            verificador.start()
        # Procesos

        # Botones
        saludo_label = Label(parent, text='Hola, elige una configuración',fg="white", bg='black').place(x=120, y=200)
        boton_python = Button(parent, text="Conf. Python", command=python_development).place(x=70, y=260)
        boton_sin_configuracion = Button(parent, text="Sin configuración", command=sin_conf).place(x=70, y=300)
        boton_escolar = Button(parent, text="Conf. Escolar", command=conf_escolar).place(x=250, y=300)
        boton_visual = Button(parent, text='Conf. VSC', command=conf_visual).place(x=250, y=260)
        # Botones

if __name__ == '__main__':
    root = Tk()
    MainAplication(root)
    root.mainloop()