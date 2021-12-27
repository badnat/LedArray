import numpy as np

# Model
class Model:
    # constructor
    def __init__(self, width: int):
        self.pix2d: np.ndarray = np.zeros((width, width, 3))
        self.width: int = width
    
    def update(self):
        pass
    
    def setup(self):
        pass

    def help(self):
        pass

    # each model needs an update method, setup method, and help method