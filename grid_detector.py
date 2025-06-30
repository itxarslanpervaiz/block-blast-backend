import cv2
import numpy as np

def extract_grid(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (10, 10))
    _, binary = cv2.threshold(resized, 150, 1, cv2.THRESH_BINARY_INV)
    return binary.tolist()