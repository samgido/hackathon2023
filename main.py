import tkinter as tk
from random import * 
from math import * 

import point
import drawer

modify = False

velocity_modifier = 1

CONVERT = 180/pi

WIN_HEIGHT = 1600
WIN_WIDTH = 800
geometry = str(WIN_HEIGHT) + "x" + str(WIN_WIDTH)

root = tk.Tk()
root.geometry(geometry)

canvas = tk.Canvas(root, height= WIN_HEIGHT, width= WIN_WIDTH, bg="white")
canvas.pack()

collection = []
canvas_collection = [[],[],[],[],[],[],[],[],[],[]]

iter = 0
collection_count = 10

for i in range(2000):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT, velocity_modifier))

def vec_field(x,y) -> (float, float):
    Vx = 0.1 * x
    Vy = -0.1 * y

    return (Vx, Vy)

def update():
    global iter

    if modify:
        for line in canvas_collection[iter]:
            canvas.itemconfigure(line, width = iter + 5)
            canvas.itemconfig(line, dash=(iter+1, 10 - iter))
            pass

    if(iter == collection_count - 1):
        iter = 0
    else:
        iter += 1

    for line in canvas_collection[iter]:
        canvas.delete(line)

    for p in collection:
        p.V = vec_field(p.x, p.y)
        line = p.update(canvas)

        canvas_collection[iter].append(line)

    root.after(10, update)
    
update()
root.mainloop()
