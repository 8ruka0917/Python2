# 画像と画素位置(x,y)を読み込み、
# その画素を中心とするサイズ5x5の窓領域における勾配を計算し出力せよ。
#
# > python exer09.py input.png x_in y_in output.txt
# input.png  : 入力画像のファイル名
# x_in, y_in : 画素位置
# output.txt : 出力テキストファイル名

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
x_in      = int(sys.argv[2])
y_in      = int(sys.argv[3])
fname_out = sys.argv[4]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = np.float64( cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) )


#画像全体のSobelフィルタ結果は以下の通り
img_sobel_x = np.zeros_like( img)
img_sobel_y = np.zeros_like( img)

for y in range( 1, img.shape[0] - 1 ) :
    for x in range( 1, img.shape[1] - 1 ) :
        img_sobel_x[y,x] = -1.0 * img[y-1,x-1] + 0.0 * img[y-1,x ] + 1.0 * img[y-1,x+1] + \
                           -2.0 * img[y  ,x-1] + 0.0 * img[y  ,x ] + 2.0 * img[y  ,x+1] + \
                           -1.0 * img[y+1,x-1] + 0.0 * img[y+1,x ] + 1.0 * img[y+1,x+1]
        img_sobel_y[y,x] = -1.0 * img[y-1,x-1] - 2.0 * img[y-1,x ] - 1.0 * img[y-1,x+1] + \
                            0.0 * img[y  ,x-1] + 0.0 * img[y  ,x ] + 0.0 * img[y  ,x+1] + \
                            1.0 * img[y+1,x-1] + 2.0 * img[y+1,x ] + 1.0 * img[y+1,x+1]
img_sobel_x = img_sobel_x / 4
img_sobel_y = img_sobel_y / 4



#----------------------
#注目画素 (x_in, y_in)の周囲の勾配ベクトルをラスタスキャン順に出力する
#Sobel filterは上で計算済み
#25個の2次元ベクトルを１行に一つずつ書き出す
#1行にひとつのベクトルを書き出し，ベクトルのx成分とy成分の間には半角スペースを配置

fp = open(fname_out, "w")

#fp.write( str(123.5) ) のようにするとファイルへ文字列を出力できる
for i in range(y_in - 2, y_in + 3):
    for j in range(x_in - 2, x_in + 3):
        fp.write( str(img_sobel_x[i,j]) )
        fp.write( str(" ") )
        fp.write( str(img_sobel_y[i,j]) )
        fp.write( str("\n") )
fp.close()
#----------------------
