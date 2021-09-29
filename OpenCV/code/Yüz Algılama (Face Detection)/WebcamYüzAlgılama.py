import cv2

webcam=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier('../../haarCascade/frontalface.xml')
while(webcam.isOpened()):
    ret ,frame=webcam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.4,7)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()