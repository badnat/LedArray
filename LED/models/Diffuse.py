from Model import Model
import numpy as np
import sys
# Model
class Diffuse(Model):
    def __init__(self, width: int):
        Model.__init__(self, width)
        self.d2A = np.zeros((self.width, self.width))
        self.d2B = np.zeros((self.width, self.width))

    def update(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                self.d2A[i, j] = self.d2B[i, j] + self.diff(i, j)/4
                self.pix2d[i, j] = (255 * self.d2A[i, j], 0, 255 * (1 - (self.d2A[i, j])))
        self.d2B = np.copy(self.d2A)
        print(self.d2A)

    def setup(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                if(i == 8 and j == 8):
                    self.d2A[i, j] = 1
                    self.d2B[i, j] = 1
                else:
                    self.d2A[i, j] = 0
                    self.d2B[i, j] = 0
    
    def help(self) -> None:
        print("This effect takes 2 params all probabilities from 0 to 100, <prob of led turning off> <prob of the led changing>")

# update Logic
    def diff(self, i, j):
        if(i == 0 and j == 0):
            return -2 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i, j + 1]
        elif(i == 0 and j == 15):
            return -2 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i, j - 1]
        elif(i == 15 and j == 15):
            return -2 * self.d2B[i, j] + self.d2B[i - 1, j] + self.d2B[i, j - 1]
        elif(i == 15 and j == 0):
            return -2 * self.d2B[i, j] + self.d2B[i - 1, j] + self.d2B[i, j + 1]
        elif(i == 0):
            return -3 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i, j + 1] + self.d2B[i, j - 1]
        elif(i == 15):
            return -3 * self.d2B[i, j] + self.d2B[i - 1, j] + self.d2B[i, j + 1] + self.d2B[i, j - 1]
        elif(j == 0):
            return -3 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i - 1, j] + self.d2B[i, j + 1]
        elif(j == 15):
            return -3 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i - 1, j] + self.d2B[i, j - 1]
        else:
            return -4 * self.d2B[i, j] + self.d2B[i + 1, j] + self.d2B[i - 1, j] + self.d2B[i, j + 1] + self.d2B[i, j - 1]

