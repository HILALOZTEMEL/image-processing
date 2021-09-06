import  numpy as np
import cv2

img=cv2.imread("a.jfif",0)
row,col=img.shape

M=cv2.getRotationMatrix2D((col/2,row/2),90,1)
M1=cv2.getRotationMatrix2D((col/2,row/2),180,1)
M2=cv2.getRotationMatrix2D((col/2,row/2),270,1)
M3=cv2.getRotationMatrix2D((col/2,row/2),360,1)


#resmi döndürme
dst=cv2.warpAffine(img,M,(row,col))
dst1=cv2.warpAffine(img,M1,(row,col))
dst2=cv2.warpAffine(img,M2,(row,col))
dst3=cv2.warpAffine(img,M3,(row,col))

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()