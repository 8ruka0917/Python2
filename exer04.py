#  ターゲット画像とテンプレート画像を読み込みTemplate Matchingを計算せよ。
#
#  $python exer04.py target.png template.png output.png 
#
#  target.png   : ターゲット画像のファイル名
#  template.png : テンプレート画像のファイル名
#  output.png   : 出力画像 (正規化したSSD画像) のファイル名

import numpy as np
import sys
import cv2

fname_in1 = sys.argv[1]
fname_in2 = sys.argv[2]
fname_out = sys.argv[3]

#画像を読み込み輝度画像へ変換（SSDがオーバーフローしないようfloat64にキャスト）
target_img   = cv2.imread(fname_in1)
template_img = cv2.imread(fname_in2)
target_img   = np.float64( cv2.cvtColor(target_img  , cv2.COLOR_RGB2GRAY) )
template_img = np.float64( cv2.cvtColor(template_img, cv2.COLOR_RGB2GRAY) )

# image size
H, W = target_img  .shape[0], target_img  .shape[1]
h, w = template_img.shape[0], template_img.shape[1]


#-----------------------------------
#ssd_imgの各画素値を計算
ssd_img = np.zeros((H - h + 1, W - w + 1))

for i in range(H - h + 1):
        for j in range(W - w + 1):
                ssd_img[i,j] = np.sum(np.square(target_img[i:i+h, j:j+w] - template_img)) 
                
#-----------------------------------


#最大値を利用して正規化
maxv = np.max(ssd_img)
ssd_img = ssd_img / maxv * 255.0
cv2.imwrite( fname_out, np.uint8(ssd_img) )
