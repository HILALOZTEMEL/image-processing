import cv2
import numpy as np
img=cv2.imread("../OpenCV Giris/indir.jpg", 1)

#yazı yazdırma
#cv2.putText(Hangi resim,"metin",hangi noktaya yazılacak,Font,fontun ölçeği,
# Renk rgb,çizgi kalınlığı)
font=cv2.FONT_HERSHEY_COMPLEX
img4=cv2.putText(img,"yazgit",(15,30),font,1,(255,0,0),4,cv2.LINE_AA)
cv2.imshow("yazı",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()