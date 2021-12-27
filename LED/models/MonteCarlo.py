from Model import Model
import numpy as np
# Model
class MonteCarlo(Model):
    def __init__(self, width: int):
        Model.__init__(self, width)

    def update(self) -> None:
        for i in range(self.width):
            for j in range(self.width):
                self.pix2d[i, j] = self.mc()

    #no set up needed for this bad boy
    def setup(self,param: str) -> None:
        pass
    
    def help(self) -> None:
        print("This effect doesn't take any params")

# update Logic
    def mc(self):
        r = int(np.random.uniform(0, 1) * 255)
        g = int(np.random.uniform(0, 1) * 255)
        b = int(np.random.uniform(0, 1) * 255)

        return (r, g, b)

    