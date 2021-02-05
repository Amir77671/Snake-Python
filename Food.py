from random import *

class Food:
    def __init__(self):
        self.wspX = 0
        self.wspY = 0
        self.RandPos()
    def RandPos(self):
        self.wspY = randint(0, 39)
        self.wspX = randint(0, 53)
