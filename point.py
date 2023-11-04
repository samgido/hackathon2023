from random import * 

class Point:

    def __init__(self, width, height):
        self.window_info = (width, height)
        self.x = width * uniform(-1., 1.)
        self.y = height * uniform(-1., 1.)
        self.V: (float, float) = (0., 0.)
        self.reset_chance = 0.3

    def update(self):
        self.x += self.V[0]
        self.y += self.V[1]

        chance = uniform(0, 100)

        if(chance < self.reset_chance):
            self = Point(self.window_info)