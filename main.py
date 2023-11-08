import tkinter as tk
from random import * 
from math import * 

import point
import drawer

CONVERT = 180/pi

WIN_HEIGHT = 800
WIN_WIDTH = 800

root = tk.Tk()
root.geometry(str(WIN_HEIGHT) + "x" + str(WIN_WIDTH))

canvas = tk.Canvas(root, height=WIN_HEIGHT, width=WIN_WIDTH, bg="white")
canvas.pack()
d = drawer.Drawer(canvas)

collection = []
canvas_collection = [[],[],[],[],[]]

iter = 0

for i in range(1000):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT, canvas))

def vec_field(x,y) -> (float, float):
    Vx = 0.1 * y
    Vy = -0.1 * y

    return (Vx, Vy)

def update():
    global iter

    if(iter == 4):
        iter = 0
    else:
        iter += 1

    for line in canvas_collection[iter]:
        canvas.delete(line)

    for p in collection:
        p.V = vec_field(p.x, p.y)
        line = p.update()

        canvas_collection[iter].append(line)

    root.after(10, update)
    
update()
root.mainloop()
