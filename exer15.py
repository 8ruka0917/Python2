#  Seam Carving を自作する
#
#  > python exer19.py img.png
#  img.png : 入力画像

import numpy as np
import sys
import cv2

#seam carving関数
def seam_carving(img, img_importance) :
    #img は入力画像
    #img_importanceは重要度画像
    #2枚とも縮める必要がある

    img = img[:,1:]
    img_importance = img_importance[:,1:]
    return img, img_importance


fname_in  = sys.argv[1]
img = cv2.imread(fname_in)

# gray scale画像を作成し，重要度画像を作成する
img_gray = np.float64( cv2.cvtColor(img  , cv2.COLOR_RGB2GRAY) )
img_importance = img_gray

while(1) :
    cv2.imshow("img", img)
    k = cv2.waitKey(0)
    if(k == ord('a')) :
        print("横方向にseam carvingして，imgとimg_importanceを縮める")
        img, img_importance = seam_carving(img, img_importance)
    if(k == ord('b')) :
        cv2.imwrite("out.png", img)
