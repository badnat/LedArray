from __future__ import annotations
import time
import board
import neopixel
import numpy as np
import sys

# Model
class ConwayM:
    # constructor
    def __init__(self, width: int, color: list):
        self.pix2d: np.ndarray = np.zeros((width, width, 3))
        self.width: int = width
        self.color = color
    
    def update(self) -> None:
        pix2: np.ndarray = np.zeros((self.width, self.width, 3))
        for i in range(self.width):
            for j in range(self.width):
                n = self.getNumLiveNeighbors(i, j)
                if self.gameRule(n, self.getState(self.pix2d[i, j])):
                    self.setAlive(pix2, i, j, self.color)
        self.pix2d = pix2

    # ** GAME LOGIC **
    # Returns true if alive, false if dead
    def getState(self, element) -> bool:
        return (element[0] != 0 or element[1] != 0 or element[2] != 0)

    # sets element to "alive" by turning the led on
    def setAlive(self, array, x, y, color) -> None:
        array[x, y] = color

    # sets element to "dead" by turning led off
    def setDead(self, x, y) -> None:
        self.pix2d[x, y] = (0, 0, 0)

    # cell is dead in next generation unless
    # 1: it is alive and has 2 or 3 neighbors that are alive
    # 2: it is dead and has 3 neightbors that are alive
    def gameRule(self, num, state) -> None:
        return (state and (num == 2 or num == 3)) or (not state and num == 3)

    # returns the number of neighbors that are alive
    def getNumLiveNeighbors(self, x, y) -> int:
        end = len(self.pix2d) - 1
        n = 0
        if x ==  0 and y == 0:
            neighbors = [self.pix2d[x, y+1], self.pix2d[x+1, y+1], self.pix2d[x+1, y]]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif x ==  end and y == 0:
            neighbors = [self.pix2d[x-1, y], self.pix2d[x-1, y+1], self.pix2d[x, y+1]]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n
                
        elif x ==  end and y == end:
            neighbors = [self.pix2d[x, y-1], self.pix2d[x-1, y-1], self.pix2d[x-1, y]]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif x ==  0 and y == end:
            neighbors = [self.pix2d[x, y-1], self.pix2d[x+1, y-1], self.pix2d[x+1, y]]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif x == 0:
            neighbors = [
                        self.pix2d[x, y-1], self.pix2d[x, y+1],
                        self.pix2d[x+1, y-1], self.pix2d[x+1, y], self.pix2d[x+1, y+1]
                        ]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif x == end:
            neighbors = [
                        self.pix2d[x-1, y-1], self.pix2d[x-1, y], self.pix2d[x-1, y+1],
                        self.pix2d[x, y-1], self.pix2d[x, y+1],
                        ]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif y == 0:
            neighbors = [
                        self.pix2d[x+1, y], self.pix2d[x+1, y+1],
                        self.pix2d[x, y+1],
                        self.pix2d[x-1, y], self.pix2d[x-1, y+1]
                        ]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        elif y == end:
            neighbors = [
                        self.pix2d[x+1, y-1], self.pix2d[x+1, y],
                        self.pix2d[x, y-1],
                        self.pix2d[x-1, y-1], self.pix2d[x-1, y]
                        ]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

        else:
            neighbors = [
                        self.pix2d[x+1, y-1], self.pix2d[x+1, y], self.pix2d[x+1, y+1],
                        self.pix2d[x, y-1], self.pix2d[x, y+1],
                        self.pix2d[x-1, y-1], self.pix2d[x-1, y], self.pix2d[x-1, y+1]
                        ]
            for neigh in neighbors:
                if self.getState(neigh):
                    n +=1
            return n

# View
class ConwayV:
    # constructor
    def __init__(self, width: int, brightness: float, pixPin):
        self.width: int = width
        self.numPix: int = self.width**2
        self.pixels = neopixel.NeoPixel(
            pixPin, self.numPix, brightness=brightness, auto_write=False, pixel_order=neopixel.GRB
        )

    def update(self, pix2d: ConwayM.pix2d):     
        for i in range(self.width):
            for j in range(self.width):
                if i % 2 == 0:
                    self.pixels[self.width * i + j] = pix2d[j, i].astype(int)
                else:
                    self.pixels[self.width * i + (self.width - 1 - j)] = pix2d[j, i].astype(int)
        self.pixels.show()

    def clear(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

# Controller
class ConwayC:
    # constructor
    def __init__(self, model: ConwayM, view: ConwayV):
        self.model: ConwayM = model
        self.view: ConwayV = view
    
    def update(self):
        self.model.update()
        self.view.update(self.model.pix2d)
    
    def clear(self):
        self.view.clear()

    # **Set ups**
    # randomly set cells to dead or alive
    def random(self, weight: float):
        for i in range(self.model.width):
            for j in range(self.model.width):
                if(np.random.uniform(0, 1) < weight):
                    self.model.pix2d[i, j] = self.model.color
    # sets up a glider in the top left corner
    def glider(self):
        self.model.pix2d[0, 1] = self.model.color
        self.model.pix2d[1, 2] = self.model.color
        self.model.pix2d[2, 0] = self.model.color
        self.model.pix2d[2, 1] = self.model.color
        self.model.pix2d[2, 2] = self.model.color

