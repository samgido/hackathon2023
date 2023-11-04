import tkinter as tk
from random import * 
import math

import point
import drawer

WIN_HEIGHT = 600
WIN_WIDTH = 600

root = tk.Tk()
root.geometry(str(WIN_HEIGHT) + "x" + str(WIN_WIDTH))

canvas = tk.Canvas(root, height=WIN_HEIGHT, width=WIN_WIDTH, bg="white")
canvas.pack()
d = drawer.Drawer(canvas)

collection = []

for i in range(1000):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT))

def vec_field(x,y) -> (float, float):
    Vx = x * math.cos(x)
    Vy = y * math.sin(y)

    return (Vx, Vy)

def update():
    for p in collection:
        d.draw_point(p.x, p.y)
        p.V = vec_field(p.x, p.y)
        p.update()

    root.after(40, update)
    
update()
root.mainloop()
