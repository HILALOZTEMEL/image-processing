#Videoyu griye çevirme
import  cv2
import numpy as np

cap=cv2.VideoCapture("x.mp4")
#cap.isOpened() -> yakalama olayı başlamamış ise false döner
# (yakalama olayının kontrolünü yapar)
while(cap.isOpened()):
    ret,frame=cap.read()
    #yakalanan her bir kareyi griye döndürme
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",gray)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()

cv2.destroyAllWindows()