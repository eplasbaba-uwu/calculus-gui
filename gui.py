## Importing Libraries ##
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from symtable import Symbol
import sympy
from sympy import *
from sympy.plotting import plot
from tkinter import *
from tkinter import messagebox
import math
import os 

## Variable Declaration ##

x = Symbol('x')
i = sqrt(-1)
e = math.e
pi = math.pi

## Tkinter window ##

win = Tk()
win.title("calculus calculator")
win.state("zoomed")
win.tk.call('tk', 'scaling', 2.0)
win.configure(bg='#221C35')

text1 = Text(win, height=5, width=70)
text1.pack()

## Basic Functions ##
def clear():
    text1.delete(1.0, END)

def reload():
    win.destroy()
    os.system('python .\gui.py')

## Main Functions ##

    # Calculator Code
def calculator():
    inp_func = entered_func.get()
    inp_func = inp_func.replace("^", "**")

    if inp_func == "exit":
        win.destroy()
    else:
        clear() # function call early
        f = eval(inp_func)
        df1 = f.diff(x)
        df = str(f.diff(x))
        integral_f1 = integrate(f,x)
        integral_f = str(integrate(f,x))
        ddf = str(df1.diff(x))

        ## PRETTY-PRINTING(FOR OUTPUT)
        df = df.replace("2.71828182845905", "e")
        df = df.replace("**", "^")
        df = df.replace("1.0*", "")
        df = df.replace("*", "⋅")
        df = df.replace("3.14159265358979", "\u03C0")
        integral_f = integral_f.replace("2.71828182845905", "e")
        integral_f = integral_f.replace("**", "^")
        integral_f = integral_f.replace("1.0*", "")
        integral_f = integral_f.replace("*", "⋅")
        integral_f = integral_f.replace("3.14159265358979", "\u03C0")
        integral_f = integral_f.replace("-0.318309886183791", "-(\u03C0^-1)")
        ddf = ddf.replace("2.71828182845905", "e")
        ddf = ddf.replace("**", "^")
        ddf = ddf.replace("1.0*", "")
        ddf = ddf.replace("*", "⋅")
        ddf = ddf.replace("3.14159265358979", "\u03C0")
        text1.insert(END, "DERIVATIVE: ")
        text1.insert(END, df)
        text1.insert(END, "\n")
        text1.insert(END, "-------------------------------------------------------------------")
        text1.insert(END, "\n")
        text1.insert(END, "SECOND ORDER: ")
        text1.insert(END, ddf)
        text1.insert(END, "\n")
        text1.insert(END, "-------------------------------------------------------------------")
        text1.insert(END, "\n")

        # Checking for success in integration
        if type(integral_f1) != sympy.integrals.integrals.Integral:
            text1.insert(END, "INDEFINITE INTEGRAL: ")
            text1.insert(END, integral_f)
            text1.insert(END, "\n")
            text1.insert(END, "\n")
        else:
            text1.insert(END, "\n")
            text1.insert(END, "\n")
            return messagebox.showinfo("note", "sorry, the function could not be integrated.")


    # Grapher Code
def grapher():
    inp_func = entered_func.get()
    inp_func1 = inp_func.replace("^", "**")

    if inp_func1 == "exit":
        win.destroy()
    else:
        f = eval(inp_func1)
        df = f.diff(x)
        ddf = df.diff(x)
        int_f = integrate(f,x)
        fig = Figure(figsize = (4, 4), dpi = 100)
        plot1 = fig.add_subplot(111)

        if type(int_f) != sympy.integrals.integrals.Integral:
            canvas = FigureCanvasTkAgg(fig,master = win)
            line1, line2, line3, line4 = plot(f, df, ddf, int_f, show=False)
            x1,y1 = line1.get_points()
            x2,y2 = line2.get_points()
            x3,y3 = line3.get_points()
            x4,y4 = line4.get_points()
            plot1.plot(x1,y1, 'r')
            plot1.plot(x2,y2, 'g')
            plot1.plot(x3,y3, 'b')
            plot1.plot(x4,y4, '#000000')
            plot1.legend(["function", "derivative", "second order", "integral"])

            def save_fig():
                fig.savefig(f"{inp_func}.png")
                reload()
            b4 = Button(win, text="save and reload", command=save_fig)
            b4.pack()
            b4.place(relx=1, rely=0, anchor="ne")

            canvas.draw()
            var1 = canvas.get_tk_widget()
            var1.pack()
            toolbar = NavigationToolbar2Tk(canvas, win)
            toolbar.update()
            var1.pack()
        else:
            line1, line2, line3 = plot(f, df, ddf, show=False)
            x1,y1 = line1.get_points()
            x2,y2 = line2.get_points()
            x3,y3 = line3.get_points()
            plot1.plot(x1,y1)
            plot1.plot(x2,y2)
            plot1.plot(x3,y3)
            plot1.legend(["function", "derivative", "second order"], bbox_to_anchor=(0.75, 1.15), ncol=2)
            canvas = FigureCanvasTkAgg(fig,master = win)
            canvas.draw()
            canvas.get_tk_widget().pack()
            toolbar = NavigationToolbar2Tk(canvas, win)
            toolbar.update()
            canvas.get_tk_widget().pack()
            return messagebox.showinfo("info", "integral cannot be graphed")


## Tkinter Widgets ##

    # Tkinter Entry for function input
Label(win, text="enter function").pack()
entered_func = Entry(win)
entered_func.config(bg="gray")
entered_func.pack()

    # All buttons
b1 = Button(win, text="compute", command=calculator)
b1.pack()

b2 = Button(win, text="graph", command=grapher)
b2.pack()
b3 = Button(win, text="reload", command=reload)
b3.pack()
b3.place(x=0,y=0)

## Infinite loop ##
win.mainloop()
