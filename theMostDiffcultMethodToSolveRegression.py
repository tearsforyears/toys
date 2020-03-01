# coding=utf-8
import time
import numpy as np


def f(*args):  # 函数随便改
    x, y, z = args
    return (x - 5) ** 2 + (y - 3) ** 2 + (z - 4) ** 2


def partial_derivative(func, paraindex, *args):  # 指定对第几个参数求偏导数默认为0
    dx = 1e-8
    arglist = list(args)
    arglist[paraindex] += dx
    arglist = tuple(arglist)
    return (func(*arglist) - func(*args)) / dx


def gradientDescent(f, turns, *args, a=1e-6):  # 迭代次数,函数参数,a学习率
    argslis = list(args)
    for _ in range(turns):
        for i in range(len(argslis)):
            argslis[i] -= a * partial_derivative(f, i, *tuple(argslis))
    return argslis


n = 100
xi = np.arange(n)
# yi = np.array([1, 2.31969, 4.50853, 6.90568, 6.00512, 5.56495, 5.32807, 7.56101, 8.9392, 9.5817])
yi = xi + 0.1 * np.random.rand(n)


def f1(*args):  # 最小二乘法的优化函数
    a, b = args
    sum = 0
    for i in range(len(xi)):
        sum += (yi[i] - (a * xi[i] + b)) ** 2
    return sum


if __name__ == '__main__':
    tic = time.time()
    # res=gradientDescent(f,1000,1.,2.,0.)
    res = gradientDescent(f1, 20000, 1., -1.)  # 一阶最小二乘拟合
    tok = time.time()
    print(res)
    print(tok - tic)
