#  画像を読み込み、グレースケール画像に変換後、Otsu法により画像を二値化せよ。
#
#  $python exer17.py input.png output.png
#  input.png  : 入力画像のファイル名
#  output.png : 出力画像のファイル名

import numpy as np
import sys
import cv2

# calcPixnumMeanVari関数 : ヒストグラム数列から画素数、平均、分散を計算する
# valueは、[0,1,2,3,4,...,255という数列です（ヒストグラムの横軸の画素値を表します）
# histoは、頻度が入った配列です
def calcPixnumMeanVari( histo, value ) :
    num  = np.sum(histo)
    if num == 0 :
        return 0, 0, 0
    mean = np.sum(histo * value) / num
    vari = np.sum(histo * ( (value - mean)**2) ) / num
    return num, mean, vari

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#---------------------------------------
# ヒストグラムを計算
h = img.shape[0]
w = img.shape[1]

histo = [0] * 256

for i in range(0, h):
    for j in range(0, w):
        histo[img[i,j]] = histo[img[i,j]] + 1

# ヒストグラム全体画素数・平均・分散は下記の通り計算
value = np.arange(256)
num, mean, vari = calcPixnumMeanVari(histo, value)

# Otsu法により閾値threshを計算
#スライスを使う
bmax = 0
amax = 0

black_num = 0
black_mean = 0
black_vari = 0

white_num = 0
white_mean = 0
white_vari = 0

for a in range(1,255):
    black_num, black_mean, black_vari = calcPixnumMeanVari(histo[0:a], value[0:a])
    white_num, white_mean, white_vari = calcPixnumMeanVari(histo[a:256], value[a:256])
    
    bcv = (black_num * (black_mean - mean) * (black_mean - mean) + white_num * (white_mean - mean) * (white_mean - mean)) / (black_num + white_num)
    icv = (black_num * black_vari + white_num * white_vari) / (black_num + white_num)
    
    bunrido = bcv / icv
    
    if bmax < bunrido:
        bmax = bunrido
        amax = a
        
thresh = 0
thresh = amax

#画像の二値化（pythonでは以下の表記が可能, boolean array indexingという記法です）
img[img >= thresh] = 255
img[img <  thresh] = 0
#---------------------------------------
cv2.imwrite( fname_out, img )
