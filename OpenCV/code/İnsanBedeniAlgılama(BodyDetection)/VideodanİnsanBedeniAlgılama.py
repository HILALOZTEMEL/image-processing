import  cv2

cap=cv2.VideoCapture("../../test_videos/body.mp4")

body_cascade=cv2.CascadeClassifier("../../haarCascade/fullbody.xml")

while cap.isOpened():
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=body_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if  cv2.waitKey(1) & 0xFF==ord("q"):
        break
    cv2.imshow("videos ",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()