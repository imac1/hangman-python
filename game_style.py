import os
import sys
import time


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def animator(happy, delay=1, repeat=2):
    frames = []
    for name in happy:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.5)
            os.system("clear")


def exit():
    time.sleep(1)
    print("Hope you'll be back soon!")
    sys.exit()
