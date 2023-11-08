import tkinter as tk
from random import * 
from math import * 

import point
import drawer
import canvas_point

WIN_HEIGHT = 700
WIN_WIDTH = 700

root = tk.Tk()
root.geometry(str(WIN_HEIGHT) + "x" + str(WIN_WIDTH))

canvas = tk.Canvas(root, height=WIN_HEIGHT, width=WIN_WIDTH, bg="white")
canvas.pack()
d = drawer.Drawer(canvas)

collection = []
canvas_collection = [[],[],[],[],[]]

iter = 0

for i in range(1000):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT))

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
        line = d.draw_line(p.x, p.y, p.prev_x, p.prev_y)
        # d.draw_point(p.x, p.y)
        p.V = vec_field(p.x, p.y)
        p.update()

        canvas_collection[iter].append(line)

    root.after(100, update)
    
update()
root.mainloop()
