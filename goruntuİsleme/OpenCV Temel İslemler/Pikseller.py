import cv2
import numpy as np

#her bir piksel 3 adet rengi tutar
#R ->red
#G->green
#B->blue
img=cv2.imread("a.jfif")

#örnek resimdeki her hangi bir pikseldeki renk değerine erişmek
color= img[150,186 ]
print("BGR : ",color)

blue=img[150,186,0 ]
print ("Blue : ",blue)

green=img[150,186,1 ]
print ("Green : ",green)

red=img[150,186,2 ]
print ("Red : ",red)

#renk değiştirme
img.itemset((150,186,0),172)#0. indexteki mavi değeri artık 172 olacak
print ("new blue : ",img[150,186,0 ])

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
