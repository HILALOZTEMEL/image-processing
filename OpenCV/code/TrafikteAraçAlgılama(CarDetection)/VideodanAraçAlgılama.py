import  cv2

cap=cv2.VideoCapture("../../test_videos/car.mp4")

car_cascade=cv2.CascadeClassifier("../../haarCascade/car.xml")

while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.2,2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if  cv2.waitKey(1) & 0xFF==ord("q"):
        break
    cv2.imshow("videos ",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()