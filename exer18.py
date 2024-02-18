# 画像・シード画素位置・閾値を読み込み、画像をグレースケール化後，
# シードより領域成⻑を⾏い画像を⼆値化せよ
#
# > python exer18.py img.png seed_x seed_y t output.png
# img.png    : 入力画像のファイル名
# seed_x     : seed画素のx座標
# seed_y     : seed画素のy座標
# t          : 閾値
# output.png : 出力画像のファイル名

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
seed_x    = int(sys.argv[2])
seed_y    = int(sys.argv[3])
thresh    = int(sys.argv[4])
fname_out = sys.argv[5]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


#---------------------------------------
list = []
bin_img = np.zeros_like(img)
list.append([seed_y, seed_x])

while list:
      y, x = list.pop()
      if img[y+1, x] >= thresh and not bin_img[y+1, x] == 255:
            bin_img[y+1, x] = 255
            list.append([y+1, x])
      if img[y-1, x] >= thresh and not bin_img[y-1, x] == 255:
            bin_img[y-1, x] = 255
            list.append([y-1, x])
      if img[y, x+1] >= thresh and not bin_img[y, x+1] == 255:
            bin_img[y, x+1] = 255
            list.append([y, x+1])
      if img[y, x-1] >= thresh and not bin_img[y, x-1] == 255:
            bin_img[y, x-1] = 255
            list.append([y, x-1])
cv2.imwrite(fname_out, bin_img)
#---------------------------------------
