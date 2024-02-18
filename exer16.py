# 画像を読み込み、グレースケール化した後、そのヒストグラムを出力せよ。
#
# >python exer16.py input.png output.txt
# input.png  : 入力画像ファイル名
# output.txt : 出力ファイル名

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


#---------------------------------------------
# ファイルの各行の書き込みは 以下のようにするとよい
# f.write(str(i) + " " + str(histo[i]) + "\n")
f = open(fname_out, "w")

h = img.shape[0]
w = img.shape[1]

histo = [0] * 256
for i in range(0, h):
        for j in range(0, w):
                histo[img[i,j]] += 1
for a in range(0, 256):
        f.write(str(a) + " " + str(histo[a]) + "\n")

#---------------------------------------------
