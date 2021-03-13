import time
import board
import neopixel
import numpy as np
import sys

from ledUtils import *
from conwayUtils import *

pixPin = board.D12

numPix = 16**2
 
pixels = neopixel.NeoPixel(
    pixPin, numPix, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
)

# loop through array -> check game rule for element -> return new array with state n+1      
def update(array, color):
    length = len(array)
    pix2 = np.zeros((length, length, 3))
    for i in range(length):
        for j in range(length):
            n = getNumLiveNeighbors(array, i, j)
            if gameRule(n, getState(array[i, j])):
                setAlive(pix2, i, j, color)
    return pix2

def glider(pix2, color):
    pix2[0, 1] = color
    pix2[1, 2] = color
    pix2[2, 0] = color
    pix2[2, 1] = color
    pix2[2, 2] = color

def main():
    length = 16
    color = (0, 255, 0)
    delay = 0.1
    pix2 = np.zeros((length, length, 3))
    init = {'random': random, "glider": glider}

    initialize = init[sys.argv[1]](pix2, color)

    readOut(pix2, pixels)
    pixels.show()

    time.sleep(delay)
    try:
        while 1:
            pix2Update = np.zeros((length, length, 3))
            pix2Update = update(pix2, color)

            readOut(pix2Update, pixels)
            pixels.show()

            pix2 = pix2Update
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nStopped conway")
        pixels.fill((0,0,0))
        pixels.show()
main()