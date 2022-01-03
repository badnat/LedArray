from __future__ import annotations
import numpy as np
import time
import board
import sys
import neopixel
import os

pixPin = board.D12

width = 16

pix2d = np.zeros((width, width, 3))

pixels = neopixel.NeoPixel(
            pixPin, int(width**2), brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
        )

def update(pix2d, width):     
        for i in range(width):
            for j in range(width):
                if i % 2 == 0:
                    pixels[width * i + j] = pix2d[j, i].astype(int)
                else:
                    pixels[width * i + (width - 1 - j)] = pix2d[j, i].astype(int)
        pixels.show()

def main():
    try:
        while 1:
            bars = np.zeros(width).astype(int)
            f = open("./Audio/amps", 'r')
            bars = f.readlines()
            for line in sys.stdin:
            for j in range(width):
                for n in range(width):
                    if (n > 15 - int(bars[j])):
                        pix2d[n, j] = (int(255 * np.exp((-1/16) * j**2)), int(255 * np.exp((-1/8) * (j-8)**2)), int(255 * np.exp((-1/16) * (j-16)**2)))
                    else:
                        pix2d[n, j] = (0, 0, 0)

            update(pix2d, width)
    except KeyboardInterrupt:
        print("\nAudio Visulizer Stopped")
        pixels.fill((0,0,0))
        pixels.show()
        return


if __name__ == "__main__":
    main()