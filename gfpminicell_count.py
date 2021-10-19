################################################
#### Counting Minicells from the GFP images ####
####### Author: Abhay Koushik, CRI Paris #######
######## iGEM Paris Bettencourt 2021 ###########
################################################

# library imports
import numpy as np 
import argparse
import cv2
import os

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# removing pixel-length borders to clean the images
image = image[2:-2,2:-2]
cv2.imshow('Cleaned-original image', image)
cv2.imwrite(os.path.join('/home/abhay','Cleaned image.png'), image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# using normal thresholding (rather than inverse thresholding)
(T, thresh) = cv2.threshold(blurred, 25, 255, cv2.THRESH_BINARY) # based on 4, 6 and 8.png

# contour mapping and counting
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
count = len(contours)
cv2.imshow("Contour-ready image with cell-count: "+str(count) +" cell(s)", thresh)
cv2.imwrite(os.path.join('/home/abhay',"Contour-ready.png"), thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("The number of minicells in Fluorescent(GFP) image " + str(args["image"]) + " is ")
print(count)
