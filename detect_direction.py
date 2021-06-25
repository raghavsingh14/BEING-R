from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import sys
import time

def process_image(image):
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

	for cnt in contour:
		areas.append(cv2.contourArea(cnt))
	full_areas = np.sum(areas)
	return full_areas

def rotate_right():
	#code here
	#time.sleep(5)
	print("rotate right")
	#return True

def test():
	video_capture = cv2.VideoCapture(0)
	retn = True
	while retn:
		ret, image = video_capture.read()
		save = image
		retn = False
	video_capture.release()	
	return save

def process_surrounding():
	max = area_list[0]
	dir_counter = 0
	direc = "u"
	for i in range(len(area_list)):
		if(area_list[i] > max):
			dir_counter = i
			max = area_list[i]
	if dir_counter == 0 :
		direc = "f"
	elif dir_counter == 1 :
		direc = "r"
	elif dir_counter == 2 :
		dir = "b"
	else:
		direc = "l"
	return direc
	

img_list = []
area_list = []
direction = 0
#count = 1
print("yo")
area_list.append(process_image(test()))
print("rotate")
time.sleep(4)
area_list.append(process_image(test()))
print("rotate")
time.sleep(4)
area_list.append(process_image(test()))
print("rotate")
time.sleep(4)
area_list.append(process_image(test()))
print(process_surrounding())

cv2.destroyAllWindows()