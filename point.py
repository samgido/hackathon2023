from random import * 
import tkinter as tk

import drawer

class Point:

    def __init__(self, width, height, canvas: tk.Canvas):
        self.window_info = (width, height)
        self.x = width * uniform(-1., 1.)
        self.y = height * uniform(-1., 1.)
        self.V: (float, float) = (0., 0.)
        self.reset_chance = 0.1

        self.prev_x = self.x
        self.prev_y = self.y

        self.d: drawer.Drawer = drawer.Drawer(canvas)

    def update(self):
        multiplier = 500
            
        if randrange(0, multiplier) < (self.reset_chance * multiplier):
            width = self.window_info[0]
            height = self.window_info[1]

            self.x = width * uniform(-1., 1.)
            self.y = height * uniform(-1., 1.)
            self.prev_x = self.x
            self.prev_y = self.y

            return self.d.draw_line(0,0,0,0)
        else:
            self.prev_x = self.x        
            self.prev_y = self.y

            self.x += self.V[0]
            self.y += self.V[1]

            return self.d.draw_line(self.x, self.y, self.prev_x, self.prev_y)