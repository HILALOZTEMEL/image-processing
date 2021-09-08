#image moments ile bir nesnenin bazı özelliklerini tespit edebiliriz
#image moments fonkiyonu ile bir resmin ağırlık merkezini tespit edebiliriz
import cv2

img=cv2.imread("contour.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,225,cv2.THRESH_BINARY)
M=cv2.moments(thresh)

#kordinatlarına ulaşma
x=int(M["m10"]/M["m00"])
y=int(M["m01"]/M["m00"])

#geo metri merkezin çember cizelim
cv2.circle(img,(x,y),5,(0,0,0),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()