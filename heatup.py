# coding=utf-8
from multiprocessing import Pool
import numpy as np


def heat():
    while 1:
        a = np.random.rand(100,100) @ np.random.rand(100,100)
        print(a)

if __name__ == '__main__':
    p = Pool(16)
    for i in range(64):
        p.apply_async(heat)
    p.close()
    p.join()
