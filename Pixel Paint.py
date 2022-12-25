from tkinter import *


colors = ["white","blue","red","green","yellow","orange","cyan","magenta","black","white"]

color = [[colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]],
         [colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0],colors[0]]]

def change_color(row,column):
    global color
    index = colors.index(color[row][column])
    color[row][column] = colors[index+1]
    buttons[row][column].config(bg=color[row][column])

window = Tk()
window.title("Pixel Paint")

frame = Frame(window)
frame.pack()

buttons = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


for row in range(40):
    for column in range(40):
        buttons[row][column] = Button(frame,text="",width=2,height=1,bg=color[row][column],
            command= lambda row=row, column=column: change_color(row,column),bd=0)
        buttons[row][column].grid(row=row,column=column)

window.mainloop()

