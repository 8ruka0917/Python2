# サイズの同じ2枚の画像を読み込み，グレースケール画像に変換後，
# 2枚の画像間のSSD値を出力せよ
#
#  $python exer2.py img1.png img2.png
#  img1.png : 入力画像1のファイル名
#  img2.png : 入力画像2のファイル名
#  2枚の入力画像のサイズは等しいものとする

import numpy as np
import sys
import cv2

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
#sum_squre_diffを計算
sum_square_diff = 0
sum_square_diff = np.sum(np.square(img2 - img1))
#---------------------------------


#値を標準出力に書き出し
print(sum_square_diff)
