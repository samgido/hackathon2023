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
canvas_collection = []

for i in range(1000):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT))

def vec_field(x,y) -> (float, float):
    Vx = 0.1 * y
    Vy = -0.1 * y

    return (Vx, Vy)

def update():
    for p in collection:
        # d.draw_line(p.x, p.y, p.prev_x, p.prev_y)
        id = d.draw_point(p.x, p.y)
        p.V = vec_field(p.x, p.y)
        p.update()

        canvas_collection.append(canvas_point.CanvasPoint(id))
            
    for cp in canvas_collection:
        if cp.age >= 5:
            canvas.delete(cp.id)
        else:
            cp.age += 1

    root.after(40, update)
    
update()
root.mainloop()
