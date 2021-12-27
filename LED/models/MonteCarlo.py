from Model import Model
import numpy as np
import sys
# Model
class MonteCarlo(Model):
    def __init__(self, width: int):
        Model.__init__(self, width)
        self.offProb: int = 0
        self.changeProb: int = 100
        try:
            if(sys.argv[2] == 'help'):
                self.help()
                pass
        except IndexError:
            pass

    def update(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                self.pix2d[i, j] = self.mc(i, j)

    #no set up needed for this bad boy
    def setup(self) -> None:
        pass
    
    def help(self) -> None:
        print("This effect takes 2 params all probabilities from 0 to 100, <prob of led turning off> <prob of the led changing>")

# update Logic
    def mc(self, i, j):
        try:
            self.offProb = int(sys.argv[2])
            self.changeProb = int(sys.argv[3])
        except IndexError:
            pass
        if (np.random.uniform(0, 1) * 100 < self.offProb):
            return (0, 0, 0)
        else:
            if (np.random.uniform(0, 1) * 100 < self.changeProb):
                r = int(np.random.uniform(0, 1) * 255)
                g = int(np.random.uniform(0, 1) * 255)
                b = int(np.random.uniform(0, 1) * 255)
                return (r, g, b)
            else:
                return self.pix2d[i, j]

    