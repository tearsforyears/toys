# coding=utf-8
import numpy as np
from numpy.fft import ifft
from numpy import ones
import matplotlib.pyplot as plt

'''parameters'''
num_ofdm = 8
# 数据的OFDM符号数
M_ary = 4
# QAM调制方式
Nt = 1
# 发射天线数量
Nr = 1
# 接收天线数量
NFFT = 16
# FFT点数
L = 5
# 时域信道冲击响应长度
K = 5
# 时域信道稀疏度
SNR = np.arange(1, 31, 5)
# 信噪比取值
length_snr = SNR.shape[0]
# 信噪比取值的点数
loop = 100
# 循环次数
BER_LS = ones((loop, length_snr))
SER_LS = BER_LS.copy()
BER_LMMSE = BER_LS.copy()
SER_LMMSE = BER_LS.copy()
MSE_LS = BER_LS.copy()
MSE_LMMSE = BER_LS.copy()
