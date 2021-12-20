import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

def onChange(value):
    pass

#imagem carregada e sua cópia
img = cv2.imread("/content/drive/MyDrive/Images/Lenna.png", 0)
copyimg = img.copy()

#cria janela gráfica para inserir a imagem
windowTitle = "Ajuste de Limiar"
cv2.namedWindow(windowTitle)

#cria trackbar
cv2.createTrackbar("Limiar", windowTitle, 255, 255, onChange)


before_limiar = 255
update_limiar = False

counter_time = 0

while True:
    current_limiar = cv2.getTrackbarPos("Limiar", windowTitle)
    
        
    #valor de brilho do trackbar foi alterado pelo usuário
    if before_limiar != current_limiar:
        update_limiar = True
        counter_time = time.time()
        before_limiar = current_limiar

    #se tiver passado 1 segundo desde que o usuário mexeu em algum trackbar
    if time.time() - counter_time > 1:
        #se tiver sido marcado que é pra atualizar contraste ou brilho
        if update_limiar == True:
            limiar, copyimg = cv2.threshold(img, before_limiar, 255, cv2.THRESH_BINARY)
            update_limiar = False
        
    cv2.imshow(windowTitle, copyimg)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
