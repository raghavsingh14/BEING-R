from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import sys
import time
#acc_X = 0
#acc_Y = 0
#width = 0
#height = 0
def process_image_live(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=4)
	labels = measure.label(thresh, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")
	for label in np.unique(labels):
		if label == 0:
			continue
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255
		numPixels = cv2.countNonZero(labelMask)
		if numPixels > 300:
			mask = cv2.add(mask, labelMask)
	contour = cv2.findContours(mask, cv2.RETR_TREE,   cv2.CHAIN_APPROX_SIMPLE)
	contour = imutils.grab_contours(contour)
	areas = []
	centersX = []
	centersY = []

	for cnt in contour:
		areas.append(cv2.contourArea(cnt))
		M = cv2.moments(cnt)
		centersX.append(int(M["m10"] / M["m00"]))
		centersY.append(int(M["m01"] / M["m00"]))
	full_areas = np.sum(areas)
	acc_X = 0
	acc_Y = 0
	for i in range(len(areas)):
		acc_X += centersX[i] * (areas[i]/full_areas)
		acc_Y += centersY[i] * (areas[i]/full_areas)
	#dimensions = image.shape
	height = image.shape[0] / 2
	width = image.shape[1] / 2
	#print (acc_X, acc_Y)
	cv2.circle(image, (int(width), int(height)), 5, (255,0,0), -1)
	cv2.circle(image, (int(acc_X), int(acc_Y)), 5, (255, 0, 0), -1)
	if(acc_X < width - 10):
		return 1
	elif(acc_X > width + 10):
		return 2
	else:
		return 0 
video_capture = cv2.VideoCapture(0)

while True:
	ret, image = video_capture.read()
	
	if (process_image_live(image) == 0):
		break
	if (process_image_live(image) == 1):
		print("left")
	if (process_image_live(image) == 2):
		print("right")
	cv2.imshow("video", image)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()