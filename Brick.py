from cs1lib import *
class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True

    def draw(self):
        draw_rectangle(self.x, self.y, self.width, self.height)

    def reset(self):
        self.width = 80
        self.height = 20

    def delete(self):
        self.width = 0
        self.height = 0

    #Getters and Setters
    def set_x(self,x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self,y):
        self.y = y

    def get_y(self):
        return self.y

    def set_width(self,width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self,height):
        self.height = height

    def get_height(self):
        return self.height

