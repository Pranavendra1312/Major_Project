import matplotlib.pyplot as plt
import cv2
def Histogram(i,j,no):
        # Load the two images
        image1 = cv2.imread(i)
        image2 = cv2.imread(j)

        # Calculate the histograms of the two images using the cv2.calcHist() function
        hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

        # Plot the histograms on the subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.hist(image1.ravel(), 256, [0, 256], color='red')
        ax1.set_title(f'Histogram of input image-{no}')
        ax1.set_xlabel('Pixel Intensity')
        ax1.set_ylabel('Frequency')
        ax2.hist(image2.ravel(), 256, [0, 256], color='green')
        ax2.set_title(f'Histogram of stego image-{no}')
        ax2.set_xlabel('Pixel Intensity')
        ax2.set_ylabel('Frequency')

        # Display the figure
        plt.show()
