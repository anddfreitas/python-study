import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('./media/linhas/video_teste.mp4')

while True:
    _, frame = cap.read()
    _, frame2 = cap.read()

    escalaX = 0.2
    escalaY = 0.2
    frame = cv2.resize(frame, None, fx=escalaX, fy=escalaY, interpolation= cv2.INTER_AREA)
    frame2 = cv2.resize(frame2, None, fx=escalaX, fy=escalaY, interpolation= cv2.INTER_AREA)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Filtros de cores
    # Amarelo
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Branco
    lower_white = np.array([0, 0, 180])
    upper_white = np.array([180,25,255])
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    # Resultado do filtro
    combined_mask = cv2.bitwise_or(mask_yellow, mask_white)
    result = cv2.bitwise_and(frame, frame, mask=combined_mask)




    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    blur = cv2.medianBlur(gray, 1)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    erosion = cv2.erode(thresh, (3,3), iterations=1)
    edges = cv2.Canny(erosion, 127, 255)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 127, minLineLength=5, maxLineGap=30)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    else:
        print("Nenhuma linha foi detectada.")

    cv2.imshow('equalizada', mask_yellow)
    cv2.imshow('original', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
