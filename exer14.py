# 画像を読み込みCanny Filterによりエッジ画像を生成し出力せよ。
#
# >python exer10.py input.png output.png
# input.png  : 入力画像のファイル名
# output.png : 出力画像のファイル名

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#------------------------------------------------
#canny filter計算と画像の書き出を行う
dst = cv2.Canny(img, 85,165, L2gradient = True)
cv2.imwrite( fname_out, dst)
#------------------------------------------------
