import  cv2

vid=cv2.VideoCapture('../../test_videos/faces.mp4')

#cascade'i dahil etmek
face_cascade=cv2.CascadeClassifier('../../haarCascade/frontalface.xml')

while( vid.isOpened()):
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame,1.4,2)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(w,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("vid",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

