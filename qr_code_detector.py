import cv2
import numpy as np
import sys
import time
#if len(sys.argv)>1:
#    inputImage = cv2.imread(sys.argv[1])
#else:
#    inputImage = cv2.imread("qrcode-learnopencv.jpg")
# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)
qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
vid = cv2.VideoCapture(0)
while(True):
	ret, frame = vid.read()
	cv2.imshow('frame', frame)
	data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)
	if len(data)>0:
		print("Decoded Data : {}".format(data))
		break
		#display(frame, bbox)
		#rectifiedImage = np.uint8(rectifiedImage);
		#cv2.imshow("Rectified QRCode", rectifiedImage);
	else:
		print("QR Code not detected")
		#cv2.imshow("Results", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
vid.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()
