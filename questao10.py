import numpy as np
import cv2
from matplotlib import pyplot as plt

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId, xId].set_title(titlesArray[titleId])
            axis[yId, xId].imshow(imgMPLIB)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()

#função que recebe uma imagem e o nome do filtro e retorna a imagem com o filtro aplicado
def filtro(img, nomeFiltro):
  imgCopy = img.copy();

  if nomeFiltro == "Média" or nomeFiltro == "média":
    imgCopy = cv2.blur(imgCopy, (5,5))
  elif nomeFiltro == "Gaussiano" or nomeFiltro == "gaussiano":
    imgCopy = cv2.GaussianBlur(imgCopy, (5,5), 0)
  elif nomeFiltro == "Mediana" or nomeFiltro == "mediana":
    imgCopy = cv2.medianBlur(imgCopy, 5)
  elif nomeFiltro == "Sobel" or nomeFiltro == "sobel":
    imgCopy = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2GRAY)
    imgCopy = cv2.Sobel(imgCopy, cv2.CV_16S, 1, 0, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)
    imgCopy2 = cv2.Sobel(imgCopy, cv2.CV_16S, 0, 1, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(imgCopy)
    abs_grad_y = cv2.convertScaleAbs(imgCopy2)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    imgCopy = grad
  elif nomeFiltro == "Laplaciano" or nomeFiltro == "laplaciano":
    imgCopy = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2GRAY)
    imgCopy = cv2.Laplacian(imgCopy, cv2.CV_16S, ksize=3)
    abs_dst = cv2.convertScaleAbs(imgCopy)
    imgCopy = abs_dst
  else:
    print("Opcao invalida")
    return

  return imgCopy

#Carregando a imagem do drvie
imgTeste = cv2.imread("/content/drive/MyDrive/Images/Lenna.png")
#aplicando filtros diferentes a imagem
imgF1 = filtro(imgTeste, "Média")
imgF2 = filtro(imgTeste, "Gaussiano")
imgF3 = filtro(imgTeste, "Mediana")
imgF4 = filtro(imgTeste, "Sobel")
imgF5 = filtro(imgTeste, "Laplaciano")

imgsArray = [imgF1, imgF2, imgF3, imgF4, imgF5]
title = "Imagens com filtros"

showMultipleImageGrid(imgsArray, title, 5, 1)
