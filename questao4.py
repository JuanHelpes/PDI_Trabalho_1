import numpy as np
import cv2
from matplotlib import pyplot as plt

#carregando a imagem preto e branco e exibindo seu histograma com plt.hist
img  = cv2.imread("/content/drive/MyDrive/Images/gato.png")
plt.hist(img.ravel(), 256, [0,256])
plt.show()

#carregando a imagem colorida
img_colorida = cv2.imread("/content/drive/MyDrive/Images/araras_azuis.jpg")
color = ('b', 'g', 'r')

#exibindo em uma mesma imagem os histogramas de azul, verde e vermelho
for i, col in enumerate(color):
  histr = cv2.calcHist([img_colorida], [i], None, [256], [0,256])
  plt.plot(histr, color = col)
  plt.xlim([0, 256])
plt.show()
