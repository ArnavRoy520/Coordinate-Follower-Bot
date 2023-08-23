


import cv2
import cv2.aruco as ar
import math

import time


time.sleep(2)
cv2.namedWindow('Frame')

x_center=0
y_center=0
current_coord=[0,0]
angle=0
anglenew=0
anglep=0
anglet=0
def click_event(event, x, y, flags, params):
    global x_center, y_center,current_coord
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        current_coord[0] = x
        current_coord[1] = y
        # displaying the coordinates
        # on the Shell
        print('x =', x, ' ', 'y =', y)
        co = [x, y]




    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print('x =', x, ' ', 'y =', y)
    cv2.imshow('Frame', frame)
def angle_diff():
    global anglenew, angle,anglep,anglet

    diff = angle - anglenew

    if abs(diff)<180:
        diff=diff
    else:
        if diff>0:
            diff=diff-360
        else:
            diff=diff+360


    return diff
def doprocess(img):
    global x_center, y_center,angle,anglep,anglet
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = ar.Dictionary_get(ar.DICT_6X6_250)
    parameters = ar.DetectorParameters_create()  #question?
    corners, ids, _ = ar.detectMarkers(gray, aruco_dict, parameters=parameters)
    if ids is not None :
        dict = {}

        for i in range(0, len(ids)):
            dict[ids[i][0]] = corners[i][0]

        for id in dict:
            grey_x = int(dict[id][0][0]);grey_y = int(dict[id][0][1])
            green_x =int (dict[id][1][0]);green_y =int (dict[id][1][1])  ###question
            pink_x =int (dict[id][2][0]);pink_y =int (dict[id][2][1])
            white_x =int(dict[id][3][0]);white_y =int (dict[id][3][1])

            cv2.circle(img,(green_x,green_y),6,(0,256,0),-1)
            cv2.circle(img,(grey_x,grey_y),6,(125,125,125),-1)  ###question
            cv2.circle(img,(pink_x,pink_y),6,(180,105,255),-1)
            cv2.circle(img,(white_x,white_y),6,(255,255,255),-1)
            x_center = int(((grey_x+pink_x)/2+(white_x+green_x)/2)/2)
            y_center = int(((grey_y+pink_y)/2+(white_y+green_y)/2)/2)

            cv2.circle(img,(int(x_center),int(y_center)),6,(0,0,255),-1)
            x_mid = int((grey_x+green_x)/2)
            y_mid = int((grey_y+green_y)/2)
            cv2.line(img,(int(x_center),int(y_center)),(int(x_mid),int(y_mid)),(255,0,0),3)
            cv2.putText(img,f"{id}",(int(pink_x+10),int(pink_y)+10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
            anglep = round(math.degrees(math.atan2((white_y-grey_y),(grey_x-white_x))))
            if angle>=0:
                angle=anglep
            else:
                angle=anglep+360

            cv2.putText(frame, 'Aruco_angle', (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20,50,250), 2)
            cv2.putText(img,f"{angle}",(50, 100),cv2.FONT_HERSHEY_SIMPLEX,0.8,(20,50,250),2)





    return img



cap = cv2.VideoCapture(0)
result = cv2.VideoWriter('RESULT_VIDEO.avi',cv2.VideoWriter_fourcc(*'MJPG'),20,(int(cap.get(3)),int(cap.get(4))))
cv2.setMouseCallback('Frame', click_event)
while(cap.isOpened()):
    ret, frame = cap.read()




    if ret==True:
        frame= doprocess(frame)
        anglet = round(math.degrees(math.atan2((  y_center-current_coord[1]), ( current_coord[0]-x_center))))
        if anglet >= 0:
            anglenew=anglet
        else :
            anglenew=anglet+360

        finalangle=angle_diff()

        cv2.putText(frame, 'Angle_diff', (50,130), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(200, 0, 200), 2)
        cv2.putText(frame, str(finalangle), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 0, 200), 2)
        cv2.putText(frame,'Click_angle', (50, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        cv2.putText(frame, str(anglenew), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 0, 0), 2)
        cv2.line(frame, (int(x_center), int(y_center)), (int(current_coord[0]), int(current_coord[1])), (255, 0, 0), 3)
        cv2.putText(frame, '-ve for Anti_Clk and +ve for Clk', (200, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 200), 2)

        cv2.imshow('Frame',frame)
        result.write(frame)
        if(cv2.waitKey(25)&0xFF == ord("q")):

            break
    else:
        break

cap.release()
result.release()
cv2.destroyAllWindows()
