from tkinter import *
import sys

sys.argv

if len(sys.argv) > 1:
    ROW = int(sys.argv[1])
    COLUMN = int(sys.argv[2])
    if len(sys.argv) > 3:
        BD = sys.argv[3]
    else:
        BD = 0

else:
    ROW = 20
    COLUMN = 30
    BD = 0
    

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

for row in range(ROW):
    for column in range(COLUMN):
        buttons[row][column] = Button(frame,text="",width=2,height=1,bg=color[row][column],
            command= lambda row=row, column=column: change_color(row,column),bd=BD)
        buttons[row][column].grid(row=row,column=column)

window.mainloop()

