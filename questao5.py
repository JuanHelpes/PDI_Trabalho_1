import numpy as np
import cv2
from matplotlib import pyplot as plt

#imagem que cola a marca d'agua sobre um fundo, com a posicao a ser inserida
def addBlendingEffect(fundo, marca, weight, translationForegroundW, translationForegroundH):

    #obtendo o tamanho da marca e separando um pedaco do fundo onde ela sera colocada
    marcaH, marcaF, _ = marca.shape
    crop = fundo[translationForegroundW : marcaH + translationForegroundW, translationForegroundH : marcaF + translationForegroundH]
    
    #obtendo a mascara da marca d'agua
    marcaCinza = cv2.cvtColor(marca, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(marcaCinza, 100, 255, cv2.THRESH_BINARY)

    copyImg = crop.copy()
    altura, largura, = mask.shape

    #colocando pixel a pixel a marca no pedaco de fundo selecionado
    for y in range(0, altura):
        for x in range(0, largura):
            if mask.item(y, x) == 255:
                blendingPixelBlue = crop.item(y, x, 0) * (1.0 - weight) + marca.item(y, x, 0) * weight
                blendingPixelGreen = crop.item(y, x, 1) * (1.0 - weight) + marca.item(y, x, 1) * weight
                blendingPixelRed = crop.item(y, x, 2) * (1.0 - weight) + marca.item(y, x, 2) * weight
                copyImg.itemset((y, x, 0), blendingPixelBlue)
                copyImg.itemset((y, x, 1), blendingPixelGreen)
                copyImg.itemset((y, x, 2), blendingPixelRed)

    #inserindo a marca aplicada a imagem final e a retornando
    imgFinal = fundo.copy()
    imgFinal[translationForegroundW : marcaH + translationForegroundW, translationForegroundH : marcaF + translationForegroundH] = copyImg
    
    return imgFinal

#carregando a imagem de fundo e a marca. Chamando a funcao em seguida, com a opacidade da marca e onde sera posicionada
fundo = cv2.imread("/content/drive/MyDrive/Images/ceu.jpg")
marca = cv2.imread("/content/drive/MyDrive/Images/marca.png")

nova = addBlendingEffect(fundo, marca, 0.4, 80, 50)
nova = cv2.cvtColor(nova, cv2.COLOR_BGR2RGB)
plt.imshow(nova)
