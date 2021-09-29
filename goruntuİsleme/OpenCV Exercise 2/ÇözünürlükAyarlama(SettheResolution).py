#kameradan aldığımız nir görüntünün çözünürlük değerlerini ayarlama
import cv2

cv2.namedWindow("webcam")

cap=cv2.VideoCapture(0)

#çözünürlük değerlerine ulaşma
print("Width : "+str(cap.get(3)))
print("Height : "+str(cap.get(4)))

#çözünürlük değerlerini değiştirme
cap.set(3,1280)
cap.set(4,270)

while(cap.isOpened()):
    ret , frame=cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow("webcam",frame)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()