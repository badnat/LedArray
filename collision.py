# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import numpy as np
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12
 
# The number of NeoPixels
num_pixels = 16**2
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=ORDER
)

size = 5

def expand(length):
    # Upon meeting, expand outward
    for i in range(int(size/2), length):
        pixels.fill((0, 0, 0))
        for j in range(0, i):
            pixels[int(num_pixels/2) - j] = (r_avg, g_avg, b_avg)
            pixels[int(num_pixels/2) + 1 + j] = (r_avg, g_avg, b_avg)
        pixels.show()
        time.sleep(.01)
    # Shrink down to nothing
    for i in range(length, 0, -1):
        pixels.fill((0, 0, 0))
        for j in range(0, i):
            pixels[int(num_pixels/2) - 1 - j] = (r_avg, g_avg, b_avg)
            pixels[int(num_pixels/2) + j] = (r_avg, g_avg, b_avg)
        pixels.show()
        time.sleep(.01)

while True:
    r1 = np.random.randint(0, 256)
    g1 = np.random.randint(0, 56)
    b1 = np.random.randint(0, 56)
    r2 = np.random.randint(0, 56)
    g2 = np.random.randint(0, 56)
    b2 = np.random.randint(0, 256)

    # Two lines move at each other and meet in middle
    for i in range(size - 1, int(num_pixels/2 + size/2)):
        pixels.fill((0, 0, 0))
        for j in range(0, size):
            pixels[i - j] = (r1, g1, b1)
            pixels[num_pixels - i + j - 1] = (r2, g2, b2)
        pixels.show()
        time.sleep(.01)
    
    # Average the two colors
    r_avg = int((r1 + r2)/2)
    g_avg = int((g1 + g2)/2)
    b_avg = int((b1 + b2)/2)
    
    expand(8)
    expand(12)
    expand(16)
    expand(12)
    expand(8)
    expand(4)