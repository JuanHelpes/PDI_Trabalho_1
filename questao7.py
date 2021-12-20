import numpy as np
import cv2
from matplotlib import pyplot as plt

#leitura das imagens
img_S1 = cv2.imread("/content/drive/MyDrive/Images/Questao 7/S1.jpg")
img_S2 = cv2.imread("/content/drive/MyDrive/Images/Questao 7/S2.jpg")
img_D1 = cv2.imread("/content/drive/MyDrive/Images/Questao 7/D1.jpg")
img_D2 = cv2.imread("/content/drive/MyDrive/Images/Questao 7/D2.png")
img_D3 = cv2.imread("/content/drive/MyDrive/Images/Questao 7/D3.png")

#convertendo para HSV
hsv_img_S1 = cv2.cvtColor(img_S1, cv2.COLOR_BGR2HSV)
hsv_img_S2 = cv2.cvtColor(img_S2, cv2.COLOR_BGR2HSV)
hsv_img_D1 = cv2.cvtColor(img_D1, cv2.COLOR_BGR2HSV)
hsv_img_D2 = cv2.cvtColor(img_D2, cv2.COLOR_BGR2HSV)
hsv_img_D3 = cv2.cvtColor(img_D3, cv2.COLOR_BGR2HSV)

hsv_half_down = hsv_img_S1[hsv_img_S1.shape[0]//2:,:]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists
# Use the 0-th and 1-st channels
channels = [0, 1]


#calculando os histogramas
hist_half = cv2.calcHist([hsv_half_down], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_half, hist_half, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_S1 = cv2.calcHist([hsv_img_S1], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_S1, hist_S1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_S2 = cv2.calcHist([hsv_img_S2], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_S2, hist_S2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_D1 = cv2.calcHist([hsv_img_D1], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_D1, hist_D1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_D2 = cv2.calcHist([hsv_img_D2], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_D2, hist_D2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_D3 = cv2.calcHist([hsv_img_D3], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hist_D3, hist_D3, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

soma_S1_S2 = 0
soma_S1_D1 = 0
soma_S1_D2 = 0
soma_S1_D3 = 0

#laço aplicando os metodos e guardando a soma ao quadrado
for compare_method in range(4):
  if(compare_method != 3):
    S1_S1 = cv2.compareHist(hist_S1, hist_S1, compare_method)
    S1_half = cv2.compareHist(hist_S1, hist_half, compare_method)
    S1_S2 = cv2.compareHist(hist_S1, hist_S2, compare_method)
    soma_S1_S2 += (S1_S2)*(S1_S2)
    S1_D1 = cv2.compareHist(hist_S1, hist_D1, compare_method)
    soma_S1_D1 += (S1_D1)*(S1_D1)
    S1_D2 = cv2.compareHist(hist_S1, hist_D2, compare_method)
    soma_S1_D2 += (S1_D2)*(S1_D2)
    S1_D3 = cv2.compareHist(hist_S1, hist_D3, compare_method)
    soma_S1_D3 += (S1_D3)*(S1_D3)
  
#fazendo as raizes
soma_S1_S2 = np.sqrt(soma_S1_S2)
soma_S1_D1 = np.sqrt(soma_S1_D1)
soma_S1_D2 = np.sqrt(soma_S1_D2)
soma_S1_D3 = np.sqrt(soma_S1_D3)

#comparando os valores para achar o menor
if (soma_S1_S2 < soma_S1_D1 and soma_S1_S2 < soma_S1_D2 and soma_S1_S2 < soma_S1_D3):
  img = cv2.cvtColor(img_S2, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
elif (soma_S1_D1 < soma_S1_S2 and soma_S1_D1 < soma_S1_D2 and soma_S1_D1 < soma_S1_D3):
  img = cv2.cvtColor(img_D1, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
elif (soma_S1_D2 < soma_S1_S2 and soma_S1_D2 < soma_S1_D1 and soma_S1_D2 < soma_S1_D3):
  img = cv2.cvtColor(img_D2, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
else:
  img = cv2.cvtColor(img_D3, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
