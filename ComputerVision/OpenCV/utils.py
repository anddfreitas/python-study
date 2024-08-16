import cv2
import numpy as np
import matplotlib.pyplot as plt

# Funções
def threshold_binary(img, min, max):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret, thresh = cv2.threshold(gray, min, max, cv2.THRESH_BINARY)
    return thresh

