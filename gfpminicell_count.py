################################################
#### Counting Minicells from the GFP images ####
####### Author: Abhay Koushik, CRI Paris #######
######## iGEM Paris Bettencourt 2021 ###########
################################################

# library imports
import numpy as np 
import argparse
import cv2

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Image", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# using normal thresholding (rather than inverse thresholding)
(T, thresh) = cv2.threshold(blurred, 25, 255, cv2.THRESH_BINARY) # based on 4, 6 and 8.png
cv2.imshow("Threshold Binary", thresh)

# contour mapping and counting
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
count = len(contours)

print("The number of minicells in Fluorescent(GFP) image " + str(args["image"]) + " is ")
print(count)
cv2.waitKey(0)