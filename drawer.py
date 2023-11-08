import tkinter as tk

def draw_point(x_real: float, y_real: float, canvas: tk.Canvas, thickness = 0):
    height = canvas.winfo_height()
    width = canvas.winfo_width()

    x = x_real + (width/2)
    y = (height/2) - y_real

    return canvas.create_rectangle(x - thickness/2, y - thickness/2, x + thickness/2, y + thickness/2, )

def draw_line(x0_real: float, y0_real: float, x1_real, y1_real, canvas: tk.Canvas, thickness = 1):
    height = canvas.winfo_height()
    width = canvas.winfo_width()

    x0 = x0_real + (width/2)
    y0 = (height/2) - y0_real
    x1 = x1_real + (width/2)
    y1 = (height/2) - y1_real

    return canvas.create_line(x0, y0, x1, y1, width=thickness)