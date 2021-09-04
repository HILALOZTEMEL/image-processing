import cv2

cap=cv2.VideoCapture("x.mp4")
#videonun px değerlerini öğrenmek
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#yükseklik
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#en
#cap.isOpened() -> yakalama olayı başlamamış ise false döner
# (yakalama olayının kontrolünü yapar)
while(cap.isOpened()):
    ret,frame=cap.read()
    #yakalanan her bir kareye yazı yazdırma
    #cv2.rectangle(frame,başlangıç ,bitiş ,renk rgb değeri,kalınlık )
    frame=cv2.rectangle(frame,(100,100) ,(1200,700),(0,255,255 ),2)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
