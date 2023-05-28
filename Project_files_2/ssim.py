import skimage
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np

def SSIM(i,j):
        img1 = skimage.io.imread(i)
        img2 = skimage.io.imread(j)


        if len(img1.shape) > 2:
            img1 = skimage.color.rgb2gray(img1)
            # print("==")
        if len(img2.shape) > 2:
            img2 = skimage.color.rgb2gray(img2)

        # Calculate the SSIM
        ssim_value,diff = ssim(img1,img2,full=True,data_range=256)
        

        # Display the result
        print(f"SSIM between the two images: {ssim_value}")
