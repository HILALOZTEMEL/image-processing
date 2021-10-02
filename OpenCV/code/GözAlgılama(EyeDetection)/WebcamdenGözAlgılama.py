import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("../../haarCascade/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("../../haarCascade/eye.xml")

while (cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.4,7)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

        frame2=frame[y:y+h , x:x+w]
        gray2=gray[y:y+h , x:x+w]

        eyes=eye_cascade.detectMultiScale(gray2)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)

        cv2.imshow("videos",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()