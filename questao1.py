import numpy as np
import cv2
from matplotlib import pyplot as plt

#função que corta a imagem
def crop (img,x,y,altura,largura):
  imgCorte = img[y:y+altura, x:x+largura]
  return imgCorte

#função que cola duas imagens
def paste (src, dst, x , y):
  imgCola = np.copy(dst)
  alt, larg, c = src.shape
  a = -1
  b = -1
  for i in range(y, y+alt):
    a +=1
    for j in range(x, x+larg):
      b+=1
      imgCola[i,j] = src[a,b]
    b=-1
  return imgCola

obj_img = plt.imread("/content/drive/MyDrive/Images/messi.jpg")
plt.imshow(paste(crop(obj_img, 336,287,163,52), obj_img,220,75))
