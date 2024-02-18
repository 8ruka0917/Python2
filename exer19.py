#  画像内の種の個数を数え標準出⼒に書き出すプログラムを作成せよ
#
#  $python exer19.py img.png
#  img.png  : 入力画像のファイル名

import numpy as np
import sys
import cv2

#load image
fname_in  = sys.argv[1]
img = cv2.imread(fname_in)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = 70
ret, dst = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
count,  hiererchy = cv2.findContours(dst, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print(len(count))