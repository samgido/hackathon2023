import tkinter as tk

class Drawer:

    def __init__(self, canvas: tk.Canvas):
        self.canvas: tk.Canvas = canvas

    def draw_point(self, x_real: float, y_real: float, thickness = 1):
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()

        x = x_real + (width/2)
        y = (height/2) - y_real

        return self.canvas.create_rectangle(x - thickness/2, y - thickness/2, x + thickness/2, y + thickness/2)