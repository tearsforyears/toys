import numpy as np
import sys
import matplotlib.pyplot as plt


def draw(a=-10, b=10, n=4096):
    x = np.linspace(a, b, n)
    f = lambda x: eval(input("function:"))
    plt.plot(x, f(x))


def main():
    if len(sys.argv) < 2:
        draw()
        plt.show()
    if "draw" == sys.argv[1]:
        draw(int(input("from:")), int(input("to:")))
        plt.show()
    elif "double" == sys.argv[1]:
        draw(int(input("from:")), int(input("to:")))
        draw(int(input("from:")), int(input("to:")))
        plt.show()
    else:
        print("wrong command")


if __name__ == '__main__':
    main()
