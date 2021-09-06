import cv2
import numpy as np

img=cv2.imread("text.png")
img2=cv2.imread("contour.png")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#grayi doğrudan  cornersta işlem yapamam bu nedenle grayi float 32 tipine çevirmem lazım
gray=np.float32(gray)

#köşeleri bulma
corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)

#bulduğuz köşeleri çizmeliyiz,önce int e çevirirz çünkü çember çizerken float sayılar kullanılmaz
corners=np.int0(corners)
for corner in corners:
    #cornerı tek satıra çevirme
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("corners",img)

cv2.waitKey(0)
cv2.destroyAllWindows()