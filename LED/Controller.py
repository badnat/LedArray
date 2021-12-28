from __future__ import annotations
from View import View
from Model import Model

# Controller
class Controller:
    # constructor
    def __init__(self, model: Model, view: View):
        self.model: ConwayM = model
        self.view: ConwayV = view
    
    def update(self) -> None:
        self.model.update()
        self.view.update(self.model.pix2d)
        return
    
    def clear(self) -> None:
        self.view.clear()
        return

    def setup(self) -> None:
        self.model.setup()
        return