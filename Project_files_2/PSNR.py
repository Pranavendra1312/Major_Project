from math import log10, sqrt
import cv2
import numpy as np

def PSNR(original_image, embedded_image):
    original = cv2.imread(original_image)
    embedded = cv2.imread(embedded_image)
    mse = np.mean((original - embedded) ** 2)
    err = np.sum((original.astype("float") - embedded.astype("float")) ** 2)
    err /= float(original.shape[0] * original.shape[1])
    if (mse == 0):
        print("MSE : 0")
        print("PSNR : 100")
        return
    max_pixel = 255.0
    
    print("MSE :", round(mse,4))
    psnr = 20 * log10(max_pixel / sqrt(mse))
    print("PSNR is :",round(psnr,4),"dB")


