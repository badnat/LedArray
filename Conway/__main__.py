import time
from Conway import *
import board

def main():
    m: ConwayM = ConwayM(16, (0, 255, 0))
    v: ConwayV = ConwayV(16, 0.05, board.D12)
    c: ConwayC = ConwayC(m, v)
    c.random(0.25)

    time.sleep(1)
    try:
        while 1:
            c.update()
            time.sleep(0.2)
    except KeyboardInterrupt:
        c.clear()
        print("\nConway has been interupted")

if __name__ == "__main__":
    main()