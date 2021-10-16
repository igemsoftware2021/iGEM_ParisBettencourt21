################################################
#### Counting Minicells from the GFP images ####
####### Author: Abhay Koushik, CRI Paris #######
######## iGEM Paris Bettencourt 2021 ###########
################################################

# library imports
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

# removing pixel-length borders to clean the images
img = img[2:-2,2:-2]
cv2.imshow('Cleaned-original image', img)

# subsampling from image for test
# img = img[:300,:300]

# Load in image, convert to gray scale, and Otsu's threshold
image = cv2.pyrMeanShiftFiltering(img,15,30)

# Grayscaling
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# Sharpening
sharpen_kernel1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpen_kernel2 = np.array([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,25,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
sharpen_kernel3 = np.array([[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,49,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel3)
# cv2.imshow('sharpen', sharpen)

# Thresholding Level 1
(T, thresh1) = cv2.threshold(sharpen, 160, 255, cv2.THRESH_BINARY) # based on 4, 6 and 8.png
#cv2.imshow("Threshold Binary 1", thresh1)

# Gaussian Blur
blur = cv2.GaussianBlur(thresh1,(5,5),cv2.BORDER_DEFAULT)
#cv2.imshow("Gaussian Blur", blur)

# Thresholding Level 2
(T, thresh2) = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY) # based on 4, 6 and 8.png
cv2.imshow("Threshold Binary 2", thresh2)

# Contour mapping and counting
contours, hier = cv2.findContours(thresh2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
count = len(contours)
# cv2.drawContours(thresh, contours, -1, (0,255,0), 3)
print("The number of cells in Fluorescent(GFP) image " + str(args["image"]).split("/")[-1] + " is ")
print(count)
cv2.waitKey(0)

