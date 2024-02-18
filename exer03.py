# サイズの同じ2枚の画像を読み込み、グレースケール化した後、
# 2枚の画像間のMean Squared Error（MSE）とPeak signal-to-noise ratio（PSNR）を出力せよ。
#
# $python exer03.py img1.png img2.png
# img1.png : 入力画像1のファイル名
# img2.png : 入力画像2のファイル名
# 2枚の入力画像のサイズは等しいものとする

import numpy as np
import sys
import cv2
import math  

#load image
fname_in1 = sys.argv[1]
fname_in2 = sys.argv[2]
img1 = cv2.imread(fname_in1)
img2 = cv2.imread(fname_in2)

#輝度画像へ変換（SSDがオーバーフローしないようfloat64にキャスト）
img1 = np.float64( cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) )
img2 = np.float64( cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY) )

if(img1.shape != img2.shape ) :
    exit(0)

#---------------------------------
#mseとpsnrを計算し、標準出力に出力する
mse = 0
psnr = 0

H = img1.shape[0]
W = img1.shape[1]

mse = np.sum(np.square(img2 - img1))
mse = mse / (W * H)

psnr = 10 * math.log( 255 * 255 / mse, 10)

print(mse)
print(psnr)

#---------------------------------
