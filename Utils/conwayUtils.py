import numpy as np
# Returns true if alive, false if dead
# array is a 16 by 16 by 3 array to be mapped to the 1d pixels array. The 3 by 1 arrays are RGB
def getState(element):
    return element[0] != 0 or element[1] != 0 or element[2] != 0

# sets element to "alive" by turning the led on
def setAlive(array, x, y, color):
    array[x, y] = color

# sets element to "dead" by turning led off
def setDead(array, x, y):
    array[x, y] = (0, 0, 0)

# cell is dead in next generation unless
# 1: it is alive and has 2 or 3 neighbors that are alive
# 2: it is dead and has 3 neightbors that are alive
def gameRule(num, state):
    return (state and (num == 2 or num == 3)) or (not state and num == 3)

# returns the number of neighbors that are alive
def getNumLiveNeighbors(array, x, y):
    end = len(array) - 1
    n = 0
    if x ==  0 and y == 0:
        neighbors = [array[x, y+1], array[x+1, y+1], array[x+1, y]]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif x ==  end and y == 0:
        neighbors = [array[x-1, y], array[x-1, y+1], array[x, y+1]]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n
            
    elif x ==  end and y == end:
        neighbors = [array[x, y-1], array[x-1, y-1], array[x-1, y]]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif x ==  0 and y == end:
        neighbors = [array[x, y-1], array[x+1, y-1], array[x+1, y]]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif x == 0:
        neighbors = [
                    array[x, y-1], array[x, y+1],
                    array[x+1, y-1], array[x+1, y], array[x+1, y+1]
                    ]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif x == end:
        neighbors = [
                    array[x-1, y-1], array[x-1, y], array[x-1, y+1],
                    array[x, y-1], array[x, y+1],
                    ]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif y == 0:
        neighbors = [
                    array[x+1, y], array[x+1, y+1],
                    array[x, y+1],
                    array[x-1, y], array[x-1, y+1]
                    ]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    elif y == end:
        neighbors = [
                    array[x+1, y-1], array[x+1, y],
                    array[x, y-1],
                    array[x-1, y-1], array[x-1, y]
                    ]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

    else:
        neighbors = [
                    array[x+1, y-1], array[x+1, y], array[x+1, y+1],
                    array[x, y-1], array[x, y+1],
                    array[x-1, y-1], array[x-1, y], array[x-1, y+1]
                    ]
        for neigh in neighbors:
            if getState(neigh):
                n +=1
        return n

# Set up functions
# ======================

def glider(pix2, color):
    pix2[0, 1] = color
    pix2[1, 2] = color
    pix2[2, 0] = color
    pix2[2, 1] = color
    pix2[2, 2] = color
# element set to alive with chance of the weight
def random(pix2, color):
    length = len(pix2)
    for i in range(length):
        for j in range(length):
            if(np.random.uniform(0, 1) < 0.5):
                pix2[i, j] = color
    