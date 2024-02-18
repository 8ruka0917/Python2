# ターゲット画像とテンプレート画像を読み込み、Template Matchingにより
# 最もテンプレートと適合する領域を発見し矩形を描くプログラムを作成せよ。
# - ターゲット画像中の最も適合する領域にテンプレートと同じサイズの四角形を描画し出力すること
# - 四角形はテンプレートと同じサイズで，線幅2, 色(B:255,G:0,R:0)とすること
#
#  python exer05.py target.png template.png output.png 
#  target.png   : ターゲット画像のファイル名
#  template.png : テンプレート画像のファイル名
#  output.png   : 出力画像のファイル名


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
                

# SSDが最小となる画素位置を取得
min = ssd_img[0,0]

for i in range(H - h + 1):
        for j in range(W - w + 1):
                if ssd_img[i,j] < min:
                        min = ssd_img[i,j]
                        min_x = j
                        min_y = i

# 四角形を描く
# target_imgはグレースケールにしてしまったのでもう一回読んでから書き込む
target_img = cv2.imread(fname_in1)
# 線幅2，線の色(255,0,0)
# 左上の座標は(min_x, min_y),　右下の座標は(min_x + w, min_y + h)
cv2.rectangle(target_img, (min_x, min_y), (min_x + w, min_y + h), (255,0,0), 2) 
#-------------------------------------------

#画像を出力
cv2.imwrite(fname_out, target_img)
