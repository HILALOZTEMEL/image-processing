#önce yüz sonra gülümseme
import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("../../haarCascade/frontalface.xml")
smile_cascade=cv2.CascadeClassifier("../../haarCascade/smile.xml")

while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_img=frame[y:y+h,x:x+w]
        roi_gray=gray[y:y+h,x:x+w]

        smiles=smile_cascade.detectMultiScale(roi_gray,1.4,7)
        for(ex,ey,ew,eh) in smiles:
            cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
        cv2.imshow("videos",frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()