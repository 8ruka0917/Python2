# MNISTのトレーニングデータを読み n番目の画像とラベルを出力せよ
#
# ソースファイル（exer20.py）があるフォルダのひとつ上のフォルダに『mnist』という
# 名前のフォルダを作成し，MNISTデータはそこから読むこと出力画像のファイル名は，
# [n]_[label].pngとする
#
# > python exer20.py  n
# n : データの番号[0,5999]

import numpy as np
import sys
import cv2
import gzip

def open_mnist_image(fname) :
    f = gzip.open(fname, 'rb')
    data = np.frombuffer( f.read(), np.uint8, offset=16)
    f.close()
    return data.reshape((-1, 784)) # (n, 784)の行列に整形, nは自動で決定

def open_mnist_label(fname):
    f = gzip.open(fname, 'rb')
    data = np.frombuffer( f.read(), np.uint8, offset=8 )
    f.close()
    return data.flatten() # (n, 1)の行列に整形, nは自動で決定


#LOAD MNIST
fname_train_img   = "../mnist/train-images-idx3-ubyte.gz"
fname_train_label = "../mnist/train-labels-idx1-ubyte.gz"
x_train = open_mnist_image( fname_train_img   )
t_train = open_mnist_label( fname_train_label )


#-------------------------------------------------------------------
fname_in  = sys.argv[1]
arg = int(sys.argv[1])

img = x_train[arg].reshape([28,28])
label = str(t_train[arg])

fname_out = fname_in + "_" + label + ".png"

cv2.imwrite(fname_out, img) 

#-------------------------------------------------------------------
