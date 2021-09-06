import  numpy as np
import cv2

img=cv2.imread("a.jfif",0)
row,col=img.shape

M=np.float32([[1,0,10],[0,1,100]])

#resmi kaydırma
dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()