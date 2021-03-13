import time
import board
import neopixel
import numpy as np

pixPin = board.D12

numPix = 16**2
 
pixels = neopixel.NeoPixel(
    pixPin, numPix, brightness=0.8, auto_write=False, pixel_order=neopixel.GRB
)

pixels.fill((0,0,0))
pixels.show()