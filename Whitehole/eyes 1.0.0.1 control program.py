import cv2, time
import os
import shutil

import pyautogui 

first_frame = None
_author__ = 'The control program has been written Jurijus Pacalovas.'

print(_author__)

print("Program that control computer (control program). By this program you can control computer by eyes.")
namez = input("1, 2, 3, 4, 5, 6 ")
w1=0
if namez=="6":
    w1=0
    

if namez=="1":
    w1=100
    

if namez=="2":
    w1=200
    

if namez=="3":
    w2=300
    

if namez=="4":
    w1=400
    

if namez=="5":
    w1=500

video = cv2.VideoCapture(0)

    


while True:
    check, frame = video.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) 

    if first_frame is None:
        first_frame = gray 

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 

    cnts = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for contour in cnts:
        if cv2.contourArea(contour) < 1000: 
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        

        
        w=x+w1
        h=y+w1
       
        
        time.sleep(1)  
       
        _author__ = 'Made by Jurijus Pacalovas'
        print(_author__)
       
        os.system('White_hole_1.0.0.2.0.reg')
        newpath = r'C:\Users\Public\Documents\White_hole' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.copyfile('White_hole_1.0.0.2.0.ico', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.ico')
        shutil.copyfile('White_hole_1.0.0.2.0.exe', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.exe')
        shutil.copyfile('White_hole_Start_1.0.0.2.0.exe', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_Start_1.0.0.2.0.exe')
        os.system('White_hole_Start_1.0.0.2.0.exe')
        
        
        pyautogui.click(w, h)
        pyautogui.moveTo(w, h, duration = 1) 
        
    

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows
