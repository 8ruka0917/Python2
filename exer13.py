# 入力画像を読み込み、前課題で作成したHough変換画像を利用して直線を検出し、
# 検出した直線を入力画像に描画せよ。
#
# 1. 前課題の手順でHough変換画像を作成（Hough変換画像は正規化しない）
# 2. 投票数が閾値以上の(ρ, θ) の組に対する直線を描く
#  - 直線は，色(B=255, G=0, R=0)，線幅1とする
# 3. 直線を描画した画像を出力する
#
# $python exer13.py input.png output.png
#  input.png  : 入力画像のファイル名
#  output.png : 出力画像のファイル名

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
for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
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

#hough変換
A = int( math.sqrt( img.shape[0] ** 2 + img.shape[1] ** 2) )
img_hough = np.zeros((A,360), float)

#------------------------------------
# 投票（Hough変換画像を生成する）
#前課題を利用する
for y in range(1,img.shape[0]-1):
    for x in range(1,img.shape[1]-1):
        if img_gradmag[y,x] >= 0.35:
            img_gradmag[y,x] = 1.0 
        elif img_gradmag[y,x] < 0.35:
            img_gradmag[y,x] = 0

for y in range(1,img.shape[0]-1):
    for x in range(1,img.shape[1]-1):
        if img_gradmag[y,x] == 1.0:
            for a in range(0,360):
                b = int( x * math.cos(math.pi * a / 180) + y * math.sin(math.pi * a / 180))
                if b >= 0:
                    img_hough[b,a] = img_hough[b,a] + 1


# 開票（投票数が閾値以上の直線を描画）
# imgは一度グレースケールにしてしまったのでカラーの直線を書き込めない
# 再読み込みすると良い
img = cv2.imread(fname_in)

for n in range(0,A):
    for m in range(0,360):
        if img_hough[n,m] >= 78:
            j1 = int( n * math.cos(math.pi * m / 180) / math.tan(math.pi * m / 180) + n * math.sin(math.pi * m / 180))
            j2 = int(( n * math.cos(math.pi * m / 180) + 1 - img.shape[1]) / math.tan(math.pi * m / 180) + n * math.sin(math.pi * m / 180))
            
            cv2.line(img, (0,j1), (img.shape[1] - 1, j2), (255, 0, 0), 1)
#-------------------------------------

cv2.imwrite( fname_out, np.uint8( img ) )
