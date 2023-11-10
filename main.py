import tkinter as tk
from random import * 
from math import * 

import point
import drawer

CONVERT = 180/pi

WIN_HEIGHT = 1600
WIN_WIDTH = 800
geometry = str(WIN_HEIGHT) + "x" + str(WIN_WIDTH)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry(geometry)

canvas = tk.Canvas(root, height= WIN_HEIGHT, width= WIN_WIDTH, bg="white")
canvas.pack()

modify = True

velocity_modifier = 1

collection = []

colors = [
    'blue',
    'black', 
    'red', 
    'green'
]

iter = 0
collection_count = 10

for i in range(1500):
    collection.append(point.Point(WIN_WIDTH, WIN_HEIGHT, velocity_modifier))

def escape_pressed(event):
    root.destroy()

def vec_field(x,y) -> (float, float):
    Vx = y
    Vy = y

    return (Vx, Vy)

def update():
    global iter

    if modify:
        for line in canvas.find_withtag("tag" + str(iter)):
            canvas.itemconfigure(line, width = iter)
            canvas.itemconfig(line, dash=(iter + 5, 10 - iter))
            canvas.itemconfig(line, fill = colors[iter % len(colors)])
            pass

    if(iter == collection_count - 1):
        iter = 0
    else:
        iter += 1

    canvas.delete("tag" + str(iter))

    for p in collection:
        p.V = vec_field(p.x, p.y)
        line = p.update(canvas)

        canvas.addtag_withtag("tag" + str(iter), line)

    root.after(10, update)
    
update()
root.bind('<Escape>', escape_pressed)
root.mainloop()
