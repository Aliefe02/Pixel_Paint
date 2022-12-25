from tkinter import *

ROW = 40
COLUMN = 40

colors = ["white","blue","red","green","yellow","orange","cyan","magenta","black","white"]
color = []
for i in range(ROW):
    column = []
    for j in range(COLUMN):
        column.append(colors[0])
    color.append(column)

def change_color(row,column):
    global color
    index = colors.index(color[row][column])
    color[row][column] = colors[index+1]
    buttons[row][column].config(bg=color[row][column])

window = Tk()
window.title("Pixel Paint")

frame = Frame(window)
frame.pack()

buttons = []
for i in range(ROW):
    col = []
    for j in range(COLUMN):
        col.append(0)
    buttons.append(col)

for row in range(40):
    for column in range(40):
        buttons[row][column] = Button(frame,text="",width=2,height=1,bg=color[row][column],
            command= lambda row=row, column=column: change_color(row,column),bd=0)
        buttons[row][column].grid(row=row,column=column)

window.mainloop()

