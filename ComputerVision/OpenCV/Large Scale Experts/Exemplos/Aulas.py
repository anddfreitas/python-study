import cv2 as cv

# Começa com a leitura da imagem
img = cv.imread('./example.jpg')

# A imagem é composta por 3 matrizes, uma camada azul, uma verde e outra vermelha, para RGB
print (img)
# Imprime uma tupla com a altura, largura e quantidade de camadas da imagem
# 597 pixels de altura, 599 pixels de largura e 3 camadas de imagem
print (img.shape)
print (type(img))

# Script comumente usando para visualizar a imagem
# Método que mostra a imagem
cv.imshow('image', img)
# Key para quando pressionada feche a imagem
cv.waitKey(0)
# Método para fechar a imagem quando a tecla for pressionada
cv.destroyAllWindows()