import time
from models import *
from Model import Model
from View import View
from Controller import Controller
import board
import sys

models = {"Conway": Conway}

def main():
    param = "" + sys.stdin[0]
    if (param == "help"):
        print("possible params include : " + models.keys())

    # m: Model = models[sys.stdin](16)
    # v: View = View(16, 0.05, board.D12)
    # c: Controller = Controller(m, v)
    # c.random(0.25)

    # time.sleep(1)
    # try:
    #     while 1:
    #         c.update()
    #         time.sleep(0.2)
    # except KeyboardInterrupt:
    #     c.clear()
    #     print("\n" + "has been interupted")

if __name__ == "__main__":
    main()