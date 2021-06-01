import turtle
from tkinter import *

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
canvas.pack()
canvas.update()

screen = turtle.TurtleScreen(canvas)
screen.bgcolor('black')
dibujo = turtle.RawTurtle(screen)
dibujo.color('white')
dibujo.speed(1)
dibujo.hideturtle()
dibujo.penup()
dibujo.setposition(0,-45)
dibujo.write("伍", align='center', font=("Times New Roman", 70, "bold"))

root.mainloop()