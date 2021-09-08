import cv2

img=cv2.imread("contour.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#kordinatları bulma
cont=contours[0]
area=cv2.contourArea(cont)
print(area)
perimeter=cv2.arcLength(cont,True)
print(perimeter)