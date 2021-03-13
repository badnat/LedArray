import time
import board
import neopixel
import numpy as np

from ledUtils import *

pixPin = board.D12
numPix = 16**2
 
pixels = neopixel.NeoPixel(
    pixPin, numPix, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
)

def main():
    pix2 = np.zeros((16, 16, 3))
    for i in range(16):
        for j in range(16):
            pix2[i, j] = (0, 255, 0)
            readOut(pix2, pixels)
            pixels.show()
            time.sleep(0.01)
    
main()