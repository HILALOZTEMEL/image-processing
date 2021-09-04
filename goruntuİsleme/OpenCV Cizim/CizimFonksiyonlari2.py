import cv2
import numpy as np
img=cv2.imread("../OpenCV Giris/indir.jpg", 1)

#rectangle() ->dikdörtgen çizmemi sağlayan fonksiyon
#cv2.rectangle(img,başlangıç noktası,bitiş noktası,renk rgb değeri,kalınlık)
img2=cv2.rectangle(img,(15,15),(200,200),(0,255,0),5)
cv2.imshow("dikdörtgen",img2)
#cv2.circle(img,merkez,yarı çap,renk rgb değeri,kalınlık)
#circle->daire çizmemi sağlayan fonkşyon
img3=cv2.circle(img2,(100,150),40,(0,0,255),4)
cv2.imshow("daire",img3)
#içi boyalı dikdörtgen için -1 komutu vardır
img2=cv2.rectangle(img,(15,15),(200,200),(0,255,0),-1)
cv2.imshow("dikdörtgen",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
