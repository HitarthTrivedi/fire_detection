import cv2 as cv2
import smtplib



fire_cascade = cv2.CascadeClassifier('fire_detection.cml')

cap = cv2.VideoCapture(0)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('*sender_email.com*', '*password*')
    server.sendmail('sender_email.com', to, content)
    server.close()
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected")
        content="FIRE WAS DETECTED AT YOUR PLACE!!! FIRE FIRE FIRE FIRE.FIRE WAS DETECTED AT YOUR PLACE!!! FIRE FIRE FIRE FIRE.FIRE WAS DETECTED AT YOUR PLACE!!! FIRE FIRE FIRE FIRE."
        to = "recievers_email@gmail.com"
        sendEmail(to, content)
        print("Email has been sent")




    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





