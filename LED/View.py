from __future__ import annotations
import neopixel

# View
class View:
    # constructor
    def __init__(self, width: int, brightness: float, pixPin):
        self.width: int = width
        self.numPix: int = self.width**2
        self.pixels = neopixel.NeoPixel(
            pixPin, self.numPix, brightness=brightness, auto_write=False, pixel_order=neopixel.GRB
        )

    #Maps 2d array to snaking 1d LED addresses
    def update(self, pix2d: Model.pix2d):     
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