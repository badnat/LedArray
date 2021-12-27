import numpy as np

# Model
class Model:
    # constructor
    def __init__(self, width: int):
        self.pix2d: np.ndarray = np.zeros((width, width, 3))
        self.width: int = width
    
    def update():
        pass
    
    def setup():
        pass

    # each model needs an update method and a setup method