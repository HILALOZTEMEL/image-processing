import cv2

cap=cv2.VideoCapture("../../test_videos/eye.mp4")

face_cascade=cv2.CascadeClassifier("../../haarCascade/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("../../haarCascade/eye.xml")

while (cap.isOpened()):
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.4,7)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    frame2=frame[y:y+h,x:x+w]
    grey2=grey[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(grey2)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)

    cv2.imshow("videos",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()