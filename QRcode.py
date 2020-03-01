# coding=utf-8
import qrcode as q
import numpy as np
import cv2


def gen_qrcode_with_image(data="hello f*ck world"):
    arr = np.array(q.make(data), dtype=np.float32)
    cv2.imwrite("qrcode.png", arr * 256)
    cv2.imshow("name", arr)
    cv2.waitKey(1000)


def main():
    gen_qrcode_with_image()


if __name__ == '__main__':
    main()
