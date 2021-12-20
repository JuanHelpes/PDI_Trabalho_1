import numpy as np
import cv2
from matplotlib import pyplot as plt

#carregando a imagem, convertendo para cinza, equalizando o histograma e convertendo de volta para rgb
src = cv2.imread("/content/drive/MyDrive/Images/Q6.png")
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst = cv2.equalizeHist(src)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.imshow(dst)
