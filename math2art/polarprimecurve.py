# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def isPrime(num):
    if num < 4:
        return num > 1
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5, int(np.ceil(np.sqrt(num))), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def main():
    n = 1000
    ls = np.arange(n)
    mask = np.array(list(map(isPrime, ls)))
    ptheta = plo = ls[mask]
    theta = lo = np.arange(n)
    px = plo * np.cos(ptheta)
    py = plo * np.sin(ptheta)
    x = lo * np.cos(theta)
    y = lo * np.sin(theta)
    plt.plot(x, y, "g.")
    plt.plot(px, py, 'r.')
    plt.show()


if __name__ == '__main__':
    main()
