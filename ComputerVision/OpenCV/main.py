import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('./media/linhas/video_teste.mp4')

while True:
    _, frame = cap.read()
    _, norm = cap.read()

    escalaX = 0.2
    escalaY = 0.2
    frame = cv2.resize(frame, None, fx=escalaX, fy=escalaY, interpolation= cv2.INTER_AREA)
    norm = cv2.resize(norm, None, fx=escalaX, fy=escalaY, interpolation= cv2.INTER_AREA)

    # Convertendo de BGR para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Filtros de cores
    # Amarelo
    lower_yellow = np.array([20,50,70])
    upper_yellow = np.array([35,255,255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Branco
    lower_white = np.array([0, 0, 130])
    upper_white = np.array([130,25,255])
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    # Resultado do filtro
    combined_mask = cv2.bitwise_or(mask_yellow, mask_white)
    result = cv2.bitwise_or(frame, frame, mask=combined_mask)

    # Imagem cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Histograma equalizado
    equalized = cv2.equalizeHist(gray)
    # Thresh para binário
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # Erosão - Diminuição das linhas brancas
    erosion = cv2.erode(thresh, (3,3), iterations=1)
    # Testar aplicando a dilatação
    
    # Bordas da imagem
    edges = cv2.Canny(erosion, 127, 255)
    # Inserindo as linhas
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 127, minLineLength=5, maxLineGap=30)

    # Caso nenhuma linha tenha sido detectada
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    else:
        print("Nenhuma linha foi detectada.")

    # Resultado das imagens
    # cv2.imshow('Branca', mask_white)
    # cv2.imshow('Amarela', mask_yellow)
    cv2.imshow('Edges', edges)
    cv2.imshow('original', norm)
    # Resultado do bitwise    
    cv2.imshow('Máscaras', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()