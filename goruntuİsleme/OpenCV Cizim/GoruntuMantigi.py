import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

img[0,1]=(255,20,123)
img
#px büyütme
img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)
cv2.imshow("arka plan ",img)
cv2.waitKey(0)
cv2.destroyAllWindows()