#  Harrisのコーナー検出法により入力画像からコーナーを検出し、コーナーに円を描画した画像を出力せよ。 
#
#  >python exer11.py input.png  output.ong
#  input.png  : 入力画像のファイル名
#  output.png : 出力画像のファイル名


import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換
img_color = cv2.imread(fname_in)
img_gray  = np.float64( cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY) )

#画像全体のsobel filter
img_sobel_x = np.zeros_like( img_gray)
img_sobel_y = np.zeros_like( img_gray)

for y in range( 1, img_gray.shape[0] - 1 ) :
    for x in range( 1, img_gray.shape[1] - 1 ) :
        img_sobel_x[y,x] = -1.0 * img_gray[y-1,x-1] + 0.0 * img_gray[y-1,x ] + 1.0 * img_gray[y-1,x+1] + \
                           -2.0 * img_gray[y  ,x-1] + 0.0 * img_gray[y  ,x ] + 2.0 * img_gray[y  ,x+1] + \
                           -1.0 * img_gray[y+1,x-1] + 0.0 * img_gray[y+1,x ] + 1.0 * img_gray[y+1,x+1]
        img_sobel_y[y,x] = -1.0 * img_gray[y-1,x-1] - 2.0 * img_gray[y-1,x ] - 1.0 * img_gray[y-1,x+1] + \
                            0.0 * img_gray[y  ,x-1] + 0.0 * img_gray[y  ,x ] + 0.0 * img_gray[y  ,x+1] + \
                            1.0 * img_gray[y+1,x-1] + 2.0 * img_gray[y+1,x ] + 1.0 * img_gray[y+1,x+1]
img_sobel_x = img_sobel_x / 4
img_sobel_y = img_sobel_y / 4

gauss = np.array([[1, 4, 6, 4,1],
                  [4,16,24,16,4],
                  [6,24,36,24,6],
                  [4,16,24,16,4],
                  [1, 4, 6, 4,1] ])
gauss = gauss / 256.0


#------------------------------------
#検出位置に円（半径3・色(255,0, 0)・線幅1）を描画する
for y_in in range(2, img_gray.shape[0] - 2):
    for x_in in range(2, img_gray.shape[1] - 2):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        a = -1
        for i in range(y_in - 2, y_in + 3):
            a = a + 1
            b = 0   
            for j in range(x_in - 2, x_in + 3):
                sum1 = sum1 + img_sobel_x[i,j] * img_sobel_x[i,j] * gauss[a,b]
                sum2 = sum2 + img_sobel_x[i,j] * img_sobel_y[i,j] * gauss[a,b]
                sum3 = sum3 + img_sobel_x[i,j] * img_sobel_y[i,j] * gauss[a,b]
                sum4 = sum4 + img_sobel_y[i,j] * img_sobel_y[i,j] * gauss[a,b]
                b = b + 1
        det = sum1 * sum4 - sum2 * sum3
        tr = sum1 + sum4
        r = det - 0.15 * tr *tr
        if r > 260000:
            img_color = cv2.circle(img_color, (x_in, y_in), 3, (255, 0, 0), 1)
#------------------------------------

cv2.imwrite(fname_out, img_color)
