# coding=utf-8
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys


def draw_points(x=None, y=None, z=None):
    '''
        this function use points to draw points in 3d space
        there is a sample with parameter equation
        x = x
        y = sin(x)
        z = cos(x)
    '''
    if x is None:
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
        y = np.sin(x)
        z = np.cos(x)
    fig = plt.figure('points')
    pic3d = Axes3D(fig)
    pic3d.scatter(x, y, z)
    plt.show()


def draw_lines(x=None, y=None, z=None):
    '''
        this function use points to draw lines in 3d space
        there is a sample with parameter equation
        x = x
        y = sin(x)
        z = cos(x)
    '''
    if x is None:
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
        y = np.sin(x)
        z = np.cos(x)
    fig = plt.figure('lines')
    pic3d = Axes3D(fig)
    pic3d.plot(x, y, z, 'g')
    plt.show()


def draw_surface():
    '''
        this function can draw a 2-variable function
        for example x
    '''
    # 创建 3D 图形对象
    fig = plt.figure()
    ax = Axes3D(fig)

    # 生成数据
    X = np.arange(-5, 5, 0.5)
    Y = np.arange(-5, 5, 0.5)

    # 生成网格的坐标
    X, Y = np.meshgrid(X, Y)
    Z = 0.5 * (X + Y + np.abs(X - Y))
    # 绘制曲面图，并使用 cmap 着色
    ax.plot_surface(X, Y, Z)
    plt.show()


def draw_function(a,n=100):
    pass


def main():
    '''
        if len(sys.argv) < 2:
            print("use python draw.py <parmeter>")
            print("parmeter:[draw] [single] [double]")
        else:
            print("wrong command")
    '''
    pass


if __name__ == '__main__':
    pass
    draw_surface()
    # main()
