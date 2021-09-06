import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)
font=cv2.FONT_HERSHEY_COMPLEX
img4=cv2.putText(img,"@whoCaresCode",(100,150),font,1,(255,255,255),2,cv2.LINE_AA)


#morfolojik işlemler ile erezyon yöntemi
kernel=np.ones((5,5),np.uint8)
erosion= cv2.erode(img4,kernel,iterations=1)
dilation=cv2.dilate(img4,kernel,iterations=1)
opening=cv2.morphologyEx(img4,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img4,cv2.MORPH_CLOSE,kernel)
gradient=cv2.morphologyEx(img4,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img4,cv2.MORPH_TOPHAT,kernel)
blackHat=cv2.morphologyEx(img4,cv2.MORPH_BLACKHAT,kernel)


cv2.imshow("whoCaresCode",img4)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.imshow("blackHat",blackHat)

cv2.waitKey(0)
cv2.destroyAllWindows()