# ターゲット画像とテンプレート画像を読み込み、Template Matchingにより
# テンプレートと最も似た領域『3か所』を発見しその部分に矩形を描画せよ。
# 
# > python exer07.py target.png template.png output.png
# target.png   : ターゲット画像のファイル名
# template.png : テンプレート画像のファイル名
# output.png   : 出力画像のファイル名

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


#-------------------------------------------
# Template matching (SSD画像)を計算
ssd_img = np.zeros((H - h + 1, W - w + 1))

for i in range(H - h + 1):
        for j in range(W - w + 1):
                ssd_img[i,j] = np.sum(np.square(target_img[i:i+h, j:j+w] - template_img)) 
                             
#TODO2 SSDが最小となる画素位置を3箇所探す
min = ssd_img[0,0]
for i in range(H - h + 1):
        for j in range(W - w + 1):
                if ssd_img[i,j] < min:
                        min = ssd_img[i,j]
                        x1 = j
                        y1 = i
                        
for n in range(y1 - h, y1 + h):
        for m in range(x1 - w, x1 + w):
                ssd_img[n,m] = 10000000000 

min = ssd_img[0,0]          
for a in range(H - h + 1):
        for b in range(W - w + 1):
                if ssd_img[a,b] < min:
                        min = ssd_img[a,b]
                        x2 = b
                        y2 = a
                        
for n in range(y2 - h, y2 + h):
        for m in range(x2 - w, x2 + w):
                ssd_img[n,m] = 1000000000000 

min = ssd_img[0,0]
for c in range(H - h + 1):
        for d in range(W - w + 1):
                if ssd_img[c,d] < min:
                        min = ssd_img[c,d]
                        x3 = d
                        y3 = c


# 発見した3箇所に四角形（線幅2・線の色(255,0,0)）を描く
target_img = cv2.imread(fname_in1)
cv2.rectangle(target_img, (x1, y1), (x1 + w, y1 + h), (255,0,0), 2) 
cv2.rectangle(target_img, (x2, y2), (x2 + w, y2 + h), (255,0,0), 2) 
cv2.rectangle(target_img, (x3, y3), (x3 + w, y3 + h), (255,0,0), 2) 
#-------------------------------------------

#画像を出力
cv2.imwrite(fname_out, target_img)
