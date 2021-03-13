import time
import board
import neopixel
import numpy as np

pixPin = board.D12

numPix = 16**2
 
pixels = neopixel.NeoPixel(
    pixPin, numPix, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB
)

def mc():
    r = int(np.random.uniform(0, 1) * 255)
    g = int(np.random.uniform(0, 1) * 255)
    b = int(np.random.uniform(0, 1) * 255)

    return (r, g, b)

def main():
    try:
        while 1:
            for i in range(len(pixels)):
                pixels[i] = mc()
            pixels.show()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped monteCarlo")
        pixels.fill((0,0,0))
        pixels.show()
main()