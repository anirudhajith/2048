#! 2048 clone using  Python graphics

from graphics import *
from random import choice, random
from math import fabs as abs

tile_width = 100
color_dict = {
    0: "gray", 
    2: "#e7e2da", 
    4: "#e7decf", 
    8: "#efdcbd", 
    16: "#f6d49c", 
    32: "#f1b85b", 
    64: "#e79613", 
    128: "#d5c8d4", 
    256: "#e5a9e1", 
    512: "#e34fda", 
    1024: "#e34f73", 
    2048: "#fa0541", 
    4096: "#a20128"
}

class Tile:
    x = 0
    y = 0
    val = 0
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setVal(self, val):
        self.val = val
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getVal(self):
        return self.val

    def draw(self, graph):
        r = Rectangle(Point(self.x - tile_width/2, self.y - tile_width/2), \
        Point(self.x + tile_width/2, self.y + tile_width/2))
        r.setFill(color_dict[self.val])
        r.draw(graph)
        
        t = Text(Point(self.x, self.y), str(self.val))
        t.setSize(tile_width/10)
        t.draw(graph)

tiles = []

board = GraphWin("2048", 4 * tile_width, 4 * tile_width)

#TODO: Model swiping logic
