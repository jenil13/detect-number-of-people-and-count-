import cv2

import numpy as np


cap =cv2.VideoCapture('video.mp4)
countlineposition =550
min_width = 80 
min_height = 80
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def centerhandle(x,y,w,h):
	x1 =int(w/2)
	x2=int(h/2)
	cx=x+x1
	cy=y+1
	return cx,cy

detect = []

offset = 6
counter = 0
while True:
	ret,frame1 =  cap.read()
	grey = cv2.cvtColor(frame1 , cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(grey,(3,3),5)
	img_sub = algo.apply(blur)
	dilat = cv2.dilate(img_sub , np.ones((5,5))))
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))


	DILATEE = cv2.morphologyEx(dilat,cv2.MORPH_CLOSE ,kernel)

	DILATEE = cv2.morphologyEx(DILATEE,cv2.MORPH_CLOSE ,kernel)
	
 	counter,h = cv2.findCountours(DILATEE,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 	cv2.imshow("detetct",DILATEE)

	cv2.line(frame1 , (25,countlineposition),(1200,countlineposition),(255,127,0),3))
	
	for(i,c) in enumerate(counter)
		(x,y,w,h) = cv2.boundingRect(c)
		validatecounter = (w>=min_width) and (h>=min_height)
		if not validatecounter:
			continue
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
		

		center = centerhandle(x,y,w,h)
		detect.append(center)

		cv2.circle(frame1,center,4,(0,0,255),-1)
		
		for(x,y) in detect:
			if Y<(countlineposition+offset) and y>(countlineposition-offset)
				counter = counter +1
			cv2.line(frame1,(25,countlineposition),(1200,countlineposition),(0,127,255),3)
			detect.remove((x,y))

			
	cv2.putText(frame1,"counter"+str(counter),(450,70),cv2.FONT-HERSHEY_SIMPLEX,2,(0,0,255),5))

	cv2.imshow('video orginal',frame1)

	IF cv2,waitkey(1)=13:
		break


cv2.destroyAllWindows()

cap.release	