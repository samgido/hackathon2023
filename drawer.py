import tkinter as tk

class Drawer:

    def __init__(self, canvas: tk.Canvas):
        self.canvas: tk.Canvas = canvas

    def draw_point(self, x_real: float, y_real: float, thickness = 0):
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()

        x = x_real + (width/2)
        y = (height/2) - y_real

        return self.canvas.create_rectangle(x - thickness/2, y - thickness/2, x + thickness/2, y + thickness/2, )

    def draw_line(self, x0_real: float, y0_real: float, x1_real, y1_real, thickness = 1):
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()

        x0 = x0_real + (width/2)
        y0 = (height/2) - y0_real
        x1 = x1_real + (width/2)
        y1 = (height/2) - y1_real

        return self.canvas.create_line(x0, y0, x1, y1)