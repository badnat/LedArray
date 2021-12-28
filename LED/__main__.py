from __future__ import annotations
import time
from models import *
from Model import Model
from View import View
from Controller import Controller
import board
import sys

models = {"Conway": Conway.Conway, "MonteCarlo": MonteCarlo.MonteCarlo, "Diffuse": Diffuse.Diffuse}

def main():
    param = ""
    brightness = 0.05
    try:
        brightness = float(sys.argv[1])/100
        param = param + sys.argv[2]
    except IndexError:
        print("please add a param to select effect. use param <help> if you want a list of possible params! EX: python3 LED <brightness 0 to 100> Conway help")
        return
    if (param == "help"):
        print("possible params include : " + str(list(models.keys())))
    else:
        m: Model = models.get(param)(16)
        v: View = View(16, brightness, board.D12)
        c: Controller = Controller(m, v)
        c.setup()
        # handle setup args later

        time.sleep(1)
        try:
            while 1:
                # try:
                #     c.update()
                # except:
                #     break
                # time.sleep(0.2)
                c.update()
        except KeyboardInterrupt:
            c.clear()
            print("\n" + param + " has been interupted")

if __name__ == "__main__":
    main()