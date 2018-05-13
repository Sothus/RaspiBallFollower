import cv2
import numpy as np

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 800
params.maxArea = 99999999
params.filterByInertia = False
params.filterByCircularity  = False
params.filterByConvexity  = False
params.filterByColor = False

detector = cv2.SimpleBlobDetector_create(params)

tracker = cv2.TrackerBoosting_create()

cap = cv2.VideoCapture(0)

i = 10
while(i):
    ret, frame = cap.read() #camera init
    i = i - 1
#while(True):
ret, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
a, b, c = cv2.split(hsv)
ret,thresh1 = cv2.threshold(b,120,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
thresh1 = cv2.erode(thresh1,kernel,iterations = 2)
keypoints = detector.detect(thresh1)
print(keypoints[0].pt[0])
boxObject = ( keypoints[0].pt[0]-30, keypoints[0].pt[1]-30 , 60 , 60 )
p1 = (int(boxObject[0]), int(boxObject[1]))
p2 = (int(boxObject[0] + boxObject[2]), int(boxObject[1] + boxObject[3]))
tracker.init(frame, boxObject)
cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

while(True):
	ret, frame = cap.read()
	ok, boxObject = tracker.update(frame)
	p1 = (int(boxObject[0]), int(boxObject[1]))
	p2 = (int(boxObject[0] + boxObject[2]), int(boxObject[1] + boxObject[3]))
	cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
	#print(boxObject)
	cv2.imshow('frame', frame)
	cv2.waitKey(10)
