import time
import board
import neopixel
import numpy as np

pixPin = board.D12

numPix = 16**2
 
pixels = neopixel.NeoPixel(
    pixPin, numPix, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
)

def main():

    for i in range(len(pixels)):
        pixels[i] = (255, 255, 255)
        pixels.show()
        time.sleep(0.1)

main()