# ランダムに選択された30%の画素が黒く塗りつぶされた劣化画像を入力とし、なるべく元画像に近い画像を復元せよ。
#
# > python exer08.py input.png output.png
# input.png  : 入力画像ファイル名
# output.png : 出力画像ファイル名
#

import numpy as np
import sys
import cv2

fname_in = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み輝度画像へ変換（SSDがオーバーフローしないようfloat64にキャスト）
input_img = cv2.imread(fname_in)

# image size
H, W = input_img.shape[0], input_img.shape[1]

output_img = input_img

for i in range(1, H - 1):
  for j in range(1, W - 1):
    if not(input_img[i, j, 2] == 0 and input_img[i, j, 1] == 0 and input_img[i, j, 0] == 0):
      output_img[i, j] = input_img[i, j]     
    else:        
      red = 0
      green = 0
      blue = 0
      count = 0
                      
      R = input_img[i - 1 : i + 2, j - 1 : j + 2, 2]
      G = input_img[i - 1 : i + 2, j - 1 : j + 2, 1]
      B = input_img[i - 1 : i + 2, j - 1 : j + 2, 0]
                
      for a in range(3):
        for b in  range(3):
          if not(R[a, b] == 0 and G[a, b] == 0 and B[a, b] == 0):
            count = count + 1
            red = red + R[a, b]
            green = green + G[a, b]
            blue = blue + B[a, b]
                
      red = red / count
      green = green / count
      blue = blue / count
                
      output_img[i, j, 2] = red
      output_img[i, j, 1] = green
      output_img[i, j, 0] = blue
      
                        
for x in range(1, H - 1):
  for y in [0, W - 1]:
    if not(input_img[x, y, 2] == 0 and input_img[x, y, 1] == 0 and input_img[x, y, 0] == 0):           
      output_img[x, y] = input_img[x, y]
    else:
      if y == 0:
        output_img[x, y] = output_img[x, y + 1]
      else:
        output_img[x, y] = output_img[x, y - 1]

for x in [0, H - 1]:
  for y in range(1, W - 1):
    if not(input_img[x, y, 2] == 0 and input_img[x, y, 1] == 0 and input_img[x, y, 0] == 0):           
      output_img[x, y] = input_img[x, y]
    else:
      if x == 0:
        output_img[x, y] = output_img[x + 1, y]
      else:
        output_img[x, y] = output_img[x - 1, y]
        
if not(input_img[0, 0, 2] == 0 and input_img[0, 0, 1] == 0 and input_img[0, 0, 0] == 0):           
  output_img[0, 0] = input_img[0, 0]
else:
  output_img[0, 0] = input_img[1, 1]

if not(input_img[0, W - 1, 2] == 0 and input_img[0, W - 1, 1] == 0 and input_img[0, W - 1, 0] == 0):           
  output_img[0, W - 1] = input_img[0, W - 1]
else:
  output_img[0, W - 1] = input_img[1, W - 2]

if not(input_img[H - 1, 0, 2] == 0 and input_img[H - 1, 0, 1] == 0 and input_img[H - 1, 0, 0] == 0):           
  output_img[H - 1, 0] = input_img[H - 1, 0]
else:
  output_img[H - 1, 0] = input_img[H - 2, 1]

if not(input_img[H - 1, W - 1, 2] == 0 and input_img[H - 1, W - 1, 1] == 0 and input_img[H - 1, W - 1, 0] == 0):           
  output_img[H - 1, W - 1] = input_img[H - 1, W - 1]
else:
  output_img[H - 1, W - 1] = input_img[H - 2, W - 2]  
    
#画像を出力
cv2.imwrite(fname_out, output_img)