# ターゲット画像とテンプレート画像を読み込み、Template Matchingにより
# 最もテンプレートと適合する領域を発見し矩形を描くプログラムを作成せよ。
# - 入力と出力の仕様は課題4と同様
# - OpenCVの関数（cv2.matchTemplate()やcv2.minMaxLoc()など）を利用すること
#
#  python exer06.py target.png template.png output.png 
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
target_img   = cv2.cvtColor(target_img  , cv2.COLOR_RGB2GRAY)
template_img = cv2.cvtColor(template_img, cv2.COLOR_RGB2GRAY)

#-------------------------------------------
#以下を編集
w, h = template_img.shape[::-1]
#TODO1 Template matching (SSD画像)を計算
ssd_img = cv2.matchTemplate(target_img, template_img,  cv2.TM_CCORR_NORMED)
                
#TODO2 SSDが最小となる画素位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(ssd_img)
top_left = max_loc
bottom_right = (top_left[0]+ w, top_left[1] + h)              
#TODO3 発見した場所に四角形（線幅2・線の色(255,0,0)）を描く
target_img = cv2.imread(fname_in1)
cv2.rectangle(target_img, top_left, bottom_right, (255,0,0), 2) 

#-------------------------------------------

#画像を出力
cv2.imwrite(fname_out, target_img)
