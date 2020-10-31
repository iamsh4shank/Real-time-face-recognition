import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one unique numeric face id
face_id = input('\n enter user id and press <return> -->  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")


while(True):
    imgTest = cv2.imread('test2.jpg')
    #ret, img = cam.read()
    gray = cv2.cvtColor(imgTest, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(imgTest, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("images/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 50: # Take 50 face sample and stop video
         break


print("\n [INFO] Exiting Program.")
