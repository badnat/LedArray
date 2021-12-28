from Model import Model
import numpy as np
import sys
# Model
class Diffuse(Model):
    def __init__(self, width: int):
        Model.__init__(self, width)
        self.pix2 = np.zeros((self.width, self.width))

    def update(self) -> None:
        self.pix2 = np.copy(self.pix2d)
        for i in range(self.width):
            for j in range(self.width):
                self.pix2d[i, j] = self.diff(i, j)

    def setup(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                if(j <= 8):
                    self.pix2d[i, j] = (255, 0, 0)
    
    def help(self) -> None:
        print("This effect takes 2 params all probabilities from 0 to 100, <prob of led turning off> <prob of the led changing>")

# update Logic
    def diff(self, i, j):
        if(i == 0 and j == 0):
            n = -1 * self.pix2[i, j][0] + self.pix2[i+1, j][0] + self.pix2[i, j+1][0]
            print(n)
            return (n, 0, 255 - n)
        elif(i == 0 and j == 15):
            n = -1 * self.pix2[i, j][0] + self.pix2[i+1, j][0] + self.pix2[i, j-1][0]
            return (n, 0, 255 - n)
        elif(i == 15 and j == 15):
            n = -1 * self.pix2[i, j][0] + self.pix2[i-1, j][0] + self.pix2[i, j-1][0]
            return (n, 0, 255 - n)
        elif(i == 15 and j == 0):
            n = -1 * self.pix2[i, j][0] + self.pix2[i-1, j][0] + self.pix2[i, j+1][0]
            return (n, 0, 255 - n)
        elif(i == 0):
            n = -2 * self.pix2[i, j][0] + self.pix2[i+1, j][0] + self.pix2[i, j+1][0] + self.pix2[i, j-1][0]
            return (n, 0, 255 - n)
        elif(i == 15):
            n = -2 * self.pix2[i, j][0] + self.pix2[i-1, j][0] + self.pix2[i, j+1][0] + self.pix2[i, j-1][0]
            return (n, 0, 255 - n)
        elif(j == 0):
            n = -2 * self.pix2[i, j][0] + self.pix2[i, j+1][0] + self.pix2[i+1, j][0] + self.pix2[i-1, j][0]
            return (n, 0, 255 - n)
        elif(j == 15):
            n = -2 * self.pix2[i, j][0] + self.pix2[i, j-1][0] + self.pix2[i+1, j][0] + self.pix2[i-1, j][0]
            return (n, 0, 255 - n)
        else:
            n = -3 * self.pix2[i, j][0] + self.pix2[i+1, j][0] + self.pix2[i-1, j][0] + self.pix2[i, j+1][0] + self.pix2[i, j-1][0]
            return (n, 0, 255 - n)

