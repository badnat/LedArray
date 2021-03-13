import numpy as np

# Maps the 2d array of RGB tuples to a 1d array of pixels
# Indices flipped on assignment to deal with how wiring is set up
def readOut(pix2, pixels):
    sideLen = int(np.sqrt(len(pixels)))     
    for i in range(len(pix2)):
        for j in range(len(pix2[0])):
            if i % 2 == 0:
                pixels[sideLen * i + j] = pix2[j, i].astype(int)
            else:
                pixels[sideLen * i + (sideLen - 1 - j)] = pix2[j, i].astype(int)
    
                