# 画像を読み込み以下の手順でHough変換画像を計算せよ。
# 1) 入力画像をグレースケール画像化し、勾配強度画像を計算する
#   右図のsobel filterにより勾配強度を計算
#   最大値で全体を除算し[0,1]に正規化する
# 2) 勾配強度画像を閾値により二値化
# 3) 全ての前景画素(y, x) について、Hough変換画像へ投票する
#  θ の値域は[0,360]とする（1画素の幅が1度に対応）
#  ρ の値域は[0,A]とする（1画素の幅が1画素分に対応、Aは画像の対角方向の長さ）
#  投票方法は講義中に解説したものを利用すること
#  Hough変換画像の全体を、その最大値で除算することで[0,255]に正規化する
#
# $python exer12.py input.png output.png
# input.png  : 入力画像のファイル名
# output.png : 出力画像(Hough変換画像)のファイル名

import numpy as np
import math
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


#勾配強度画像の計算
img_gradmag = np.zeros(img.shape, dtype = np.float64)
for y in range( 1, img.shape[0] - 1 ) :
    for x in range( 1, img.shape[1] - 1 ) :
        fx = -1.0 * img[y-1,x-1] + 0.0 * img[y-1,x ] + 1.0 * img[y-1,x+1] + \
             -2.0 * img[y  ,x-1] + 0.0 * img[y  ,x ] + 2.0 * img[y  ,x+1] + \
             -1.0 * img[y+1,x-1] + 0.0 * img[y+1,x ] + 1.0 * img[y+1,x+1]

        fy = -1.0 * img[y-1,x-1] - 2.0 * img[y-1,x ] - 1.0 * img[y-1,x+1] + \
              0.0 * img[y  ,x-1] + 0.0 * img[y  ,x ] + 0.0 * img[y  ,x+1] + \
              1.0 * img[y+1,x-1] + 2.0 * img[y+1,x ] + 1.0 * img[y+1,x+1]
        fx /= 4
        fy /= 4
        img_gradmag[y,x] = math.sqrt(fx*fx + fy*fy )

img_gradmag = img_gradmag / np.max(img_gradmag)

#ここからHough 変換画像の計算を開始する
A = int( math.sqrt( img.shape[0] ** 2 + img.shape[1] ** 2) )
img_hough = np.zeros((A,360), float)

#---------------------------------------------
#hough変換画像の正規化
for y in range(1, img.shape[0] - 1):
    for x in range(1, img.shape[1] - 1):
        if img_gradmag[y,x] >= 0.35:
            img_gradmag[y,x] = 1.0 
        elif img_gradmag[y,x] < 0.35:
            img_gradmag[y,x] = 0


for y in range(1, img.shape[0] - 1):
    for x in range(1, img.shape[1] - 1):
        if img_gradmag[y,x] == 1.0:
            for a in range(0, 360):
                b = int( x * math.cos(math.pi * a / 180) + y * math.sin(math.pi * a / 180))
                if b >= 0:
                    img_hough[b,a] = img_hough[b,a] + 1

img_hough = img_hough / np.max(img_hough)
img_hough = img_hough * 255
#---------------------------------------------

cv2.imwrite( fname_out, np.uint8( img_hough ) )
