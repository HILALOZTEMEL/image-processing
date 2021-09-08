#Dış Bükey kusurları
import cv2
import numpy as np

img=cv2.imread("star.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(gray,127,255,0)

contours,ret=cv2.findContours(threshold,2,1)#sınır kordinatları bulunur

cnt=contours[0]
hull=cv2.convexHull(cnt,returnPoints=False)#dış bükey kısımları bulur
defects=cv2.convexityDefects(cnt,hull)#dış bükey kusurlarını bulur

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    #s->start point,e->end point,f->farzed point ,d->distance
    start= tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1 )

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()