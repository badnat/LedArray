from Model import Model
import numpy as np
# Model
class MonteCarlo(Model):
    def __init__(self, width: int):
        Model.__init__(self, width)
        self.offProb: int = 0
        self.changeProb: int = 100

    def update(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                self.pix2d[i, j] = self.mc()

    #no set up needed for this bad boy
    def setup(self) -> None:
        pass
    
    def help(self) -> None:
        print("This effect takes 2 params all probabilities from 0 to 100, <prob of led turning off> <prob of the led changing>")

# update Logic
    def mc(self):
        try:
            self.offProb = sys.argv[2]
            self.changeProb = sys.argv[3]
        except IndexError:
            pass
        if (np.random.uniform(0, 1) * 100 < self.changeProb):
            if (np.random.uniform(0, 1) * 100 < self.offProb):
                return (0, 0, 0)
            else:
                r = int(np.random.uniform(0, 1) * 255)
                g = int(np.random.uniform(0, 1) * 255)
                b = int(np.random.uniform(0, 1) * 255)
                return (r, g, b)

    