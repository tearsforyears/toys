# coding=utf-8
import numpy as np
from numpy.linalg import svd
import cv2


def comp(k=100, f='1.jpg'):
    mat = cv2.imread(f)
    size1 = mat.shape[0] * mat.shape[1] * mat.shape[2]
    print("the origin size of img is", size1)
    rgb = cv2.split(mat)
    res = []
    var = 0
    for pic in rgb:
        u, s, v = svd(pic)
        u = u[:, :k]
        var = np.sum(s[:k]) / np.sum(s)
        s = np.diag(s[:k])
        v = v[:k, :]
        res.append(u @ s @ v)
    size2 = (u.shape[0] * u.shape[1] + s.shape[0] + v.shape[0] * v.shape[1]) * 3
    print('use size', size2)
    print('compress rate', size2 / size1)
    print('variance value is', var)
    print('**' * 50)
    img = cv2.merge(res)
    cv2.imshow("{file}".format(file=f), img / 256.)
    cv2.waitKey(10)


if __name__ == '__main__':
    # cv2.imshow('1.jpg', cv2.imread('1.jpg'))
    # cv2.waitKey(1000)
    cv2.imshow('image.jpg', cv2.imread('image.jpg'))
    cv2.waitKey(1000)
    # compress the matix of an jpg image
    for k in [x for x in range(1, 500)]:
        comp(k, 'image.jpg')
