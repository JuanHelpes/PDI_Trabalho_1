import numpy as np
import cv2
from matplotlib import pyplot as plt

#carregando a imagem e obtendo suas dimensoes
obj_img = plt.imread("/content/drive/MyDrive/Images/araras_azuis.jpg")
alt, larg, canais = obj_img.shape

#criando imagens de base para cada cor
img_red = np.ones((alt, larg, canais), dtype = "uint8")
img_green = np.ones((alt, larg, canais), dtype = "uint8")
img_blue = np.ones((alt, larg, canais), dtype = "uint8")

#calculando total de pixels e variaveis acumuladoras das tonalidades
total_pixel = alt * larg
soma_blue = 0
soma_red = 0
soma_green = 0

#pegando cada cor e armazenando em sua imagem pixel a pixel
for i in range(0, alt):
  for j in range(0, larg):
    img_red[i,j,0] = obj_img[i,j, 0]
    img_green[i,j,1] = obj_img[i,j, 1]
    img_blue[i,j,2] = obj_img[i,j, 2]
    #armazenando as tonalidades
    soma_blue += img_blue[i, j, 2]
    soma_red += img_red[i, j, 0]
    soma_green += img_green[i, j, 1]

#obtendo a media
soma_blue = soma_blue/total_pixel
soma_red = soma_red/total_pixel
soma_green = soma_green/total_pixel

#informando qual a cor mais expressiva na imagem
if (soma_blue > soma_green and soma_blue > soma_red):
  print("A imagem é mais azul")
elif (soma_green > soma_blue and soma_green > soma_red):
  print("A imagem é mais verde")
else:
  print("A imagem é mais vermelha")
