from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter.ttk import Progressbar

from tkvalidate import *
from tkinter import *
from tkinter import ttk

window = Tk()

window.geometry("500x500")
window.title("Number Guesser")
themecolor = "#121212"
textcolor = "#d6d6d6"

window.config(bg = themecolor)

progr = IntVar()
progr.set(0)


def Animation(variable, xpos, ypos, endx, endy, steps):
    for i in range(0,steps,1):
        xchange = (endx-xpos)/15
        xpos += round(xchange,2)
        ychange = (endy-ypos)/15
        ypos += round(ychange,2)
        variable.place(x=xpos, y=ypos)
        variable.update()
        time.sleep(0.001)

    variable.place(x=endx, y=endy)

def generatenum():
    global lbl
    global ramd

    ramd = random.randint(0,100)

    lbl.place(x = 240, y = 150)
    lbl.config(text="", font=("Calibri Light", 30), bg = themecolor, fg = textcolor)

    entry.config(state='disabled')

    for i in range(1,random.randint(5,20)):
        num = random.randint(1, 100)
        lbl.config(text="", font=("Calibri Light", 30), bg = themecolor, fg = textcolor)
        lbl.config(text=str(num))
        lbl.update()
        anum = random.randint(2,10)/100
        time.sleep(anum)
        entry.delete(0, 'end')


    lbl.update()
    lbl.config(text = "Number found\n now you have to guess it", fg = textcolor)
    lbl.place(x = 60, y = 150)
    entry.config(state='normal')

def check(num):
    global ramd
    global progress

    logo = PhotoImage(file="down.png")
    image = Label(window, image=logo)

    userinput = entry.get()
    userinput = int(userinput)

    if userinput > ramd:
        logo = PhotoImage(file="down.png")
        image = Label(window, image=logo, bg = themecolor)

        entry.config(state='disabled')

        progress['value'] = userinput
        Animation(image, 400, 0, 400, 280, 100)
        Animation(image, 400, 280, 400, 600, 100)
        entry.config(state='normal')
        entry.delete(0, 'end')

    elif userinput < ramd:
        logo = PhotoImage(file="arrow.png")
        image = Label(window, image=logo, bg = themecolor)
        entry.config(state='disabled')

        progress['value'] = userinput

        Animation(image, 400, 400, 400, 280, 100)
        Animation(image, 400, 280, 400, -100, 100)
        entry.config(state='normal')
        entry.delete(0, 'end')

    elif userinput == ramd:
        logo = PhotoImage(file="goodjob.png")
        image = Label(window, image=logo, bg = themecolor)
        entry.config(state='disabled')
        progress['value'] = userinput
        Animation(image, 400, 400, 400, 280, 600)


def welcomescr():
    global lbl
    global entry
    global checkinglbl
    global progress

    entry = Entry(window, font=("Calibri Light Italic", 25), width=12, bg = textcolor, fg = themecolor, justify='center')
    entry.place(x=150, y=290)
    entry.config(state='normal')

    int_validate(entry, from_=0, to=100)

    lbl = Label(window, text = "Gonna find a number", font = ("Calibri Light",30), bg = themecolor, fg = textcolor)
    lbl.place(x = 130, y = 150)

    #checkinglbl = Label(window, text = "image = logo")
    #checkinglbl.place(x = 300, y = 250)

    instructionslbl = Label(text = "You have to guess the number.\nJust find a number from 1 to 100", font = ("Calibri Light Italic",15), bg = themecolor, fg = textcolor)
    instructionslbl.place(x = 130 , y = 50)

    wherelbl = Label(text = "by typing your guess on the white box down below", font = ("Calibri Light Italic",8), bg = themecolor, fg = textcolor)
    wherelbl.place(x = 150 , y = 100)
    generatenum()

    style = ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", backgroud="black")

    progress = Progressbar(window, orient=HORIZONTAL,length=500, mode='determinate')
    progress.place(x = 0, y = 350)

    quitbtn = Button(window, text = "Exit", width = 15, height = 4, bg = "#657796", fg = textcolor, command = quit)
    quitbtn.place(x = 335 , y =400)


    restartbtn = Button(window, text = "Restart", width = 15, height = 4,bg = "#657796", fg = textcolor, command = generatenum)
    restartbtn.place(x = 50 , y =400)

    entry.delete(0, 'end')

    window.bind("<Return>", check)

welcomescr()

window.mainloop()