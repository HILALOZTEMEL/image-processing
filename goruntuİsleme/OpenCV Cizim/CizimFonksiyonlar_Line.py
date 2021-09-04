import cv2
import numpy as np

#siyah arka plan oluşturma
#1-sıfırlardan oluşan bir matris oluşturma "np.zeros(())"
#2-integer değere çevirme "np.uint8"
img= np.zeros((512,512,3),np.uint8)
#çizim yapabilmek
#cv2.line(img,başlangıç noktası,bitiş noktası,renk rgb değeri,kalınlık)
img2=cv2.line(img, (0,0),(512,512),(225 ,0,0),6)
cv2.imshow("çizgili",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
