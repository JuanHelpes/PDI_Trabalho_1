import numpy as np
import cv2
from matplotlib import pyplot as plt

#carregamos as duas imagens
img1 = plt.imread("/content/drive/MyDrive/Images/depp-3.jpg")
img2 = plt.imread("/content/drive/MyDrive/Images/robert.jpg")

#garantir que as fotos do tenham as mesmas
altura, largura, _ = img1.shape
img2_ajustada = cv2.resize(img2, (largura, altura))

#soma ponderada das imagens
img_combinada = cv2.addWeighted(img2_ajustada, 0.5, img1, 0.5, 0)

#reduzir o tamanho da imagem combinada
altura1, largura1, _ = img_combinada.shape
img_combinada = cv2.resize(img_combinada, (int(largura1 * 0.5), int(altura1 * 0.5)))

plt.imshow(img_combinada)
