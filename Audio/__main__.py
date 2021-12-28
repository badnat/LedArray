from __future__ import annotations
import numpy as np
import time
import board
import sys
import neopixel

pixPin = board.D12

width = 16

pix2d = np.zeros((width, width, 3))

def main():
    try:
        bars = np.zeros((width)).astype(int)
        for i in range(width):
            bars[i] = sys.argv[i+1]
        for j in range(width):
            for n in range(bars[j]):
                pix2d[-1*(n+1) , j] = (int(255 * np.exp((-1/16) * j*2)), int(255 * np.exp((-1/16) * (j-8)*2)), int(255 * np.exp((-1/16) * (j-16)*2)))
        
        pixels = neopixel.NeoPixel(
            pixPin, int(width**2), brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
        )

        update(pix2d, width)

    except IndexError:
        print("Index Error when calling Audio")

if __name__ == "__main__":
    main()

def update(pix2d, width):     
        for i in range(width):
            for j in range(width):
                if i % 2 == 0:
                    p[width * i + j] = pix2d[j, i].astype(int)
                else:
                    p[width * i + (width - 1 - j)] = pix2d[j, i].astype(int)
        p.show()