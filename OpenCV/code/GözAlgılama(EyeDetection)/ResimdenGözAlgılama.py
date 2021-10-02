#1. yüz algılyacağız bir değişken içine atarız , 2. yüzün içinde gözü ara
import cv2

img=cv2.imread("../../test_images/eye.png")

face_cascade=cv2.CascadeClassifier("../../haarCascade/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("../../haarCascade/eye.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,7)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#Dikdörtgene aldığımız bölgeyi değişkene atarız ve orada göz arayacağız
img2=img[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+w]

eyes=eye_cascade.detectMultiScale(gray2)
for (ex,ey,ew,eh)in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()