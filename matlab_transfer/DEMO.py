# coding=utf-8
import numpy as np
from numpy import diag
from numpy.linalg import svd, norm, pinv, qr
from toyz.clock import runtime

epsilon = 1e-5
n = 1000  # the columns or rows of the random matrix
A = np.random.rand(n, n)
rate = 0.5
k = int(n * rate)


@runtime
def normal_pinv(A): return pinv(A)


@runtime
def svd_pinv(A):
    U, S, V = svd(A)
    S = np.clip(S, epsilon, 1 / epsilon)
    return V.T @ diag(1. / S) @ U.T


@runtime
def pca_pinv(A):
    U, S, V = svd(A)
    # test data
    print('features rate', np.sum(S[:k]) / np.sum(S))
    # print('mse', norm(A - U[:, :k] @ diag(S[:k]) @ V[:k, :]) / n * n)
    # print('pseudo-inverse mse',
    #       norm(np.eye(n) - (A @ V[:k, :].T @ diag(1. / S[:k]) @ U[:, :k].T)) / n * n)
    return V[:k, :].T @ diag(1. / S[:k]) @ U[:, :k].T


@runtime
def qr_pinv(A):
    Q, R = qr(A)
    print(A)
    print(Q @ R)


if __name__ == '__main__':
    normal_pinv(A)
    p2 = pca_pinv(A)
    print('multiply F=', norm(np.eye(n) - A @ p2))
    print('api F=', norm(pinv(A) - p2))
