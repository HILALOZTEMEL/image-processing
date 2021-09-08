#CONVEX HULL dış bükey örtü demektir
import cv2
import  numpy as np

img=cv2.imread("q.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))
ret,thresh=cv2.threshold(blur,40,255,cv2.THRESH_BINARY)
#Sınırların kordinatlarını bulma
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours hull noktalarını tutabilmek için boş bir dizi oluşturduk
hull=[]
#contours hull noktalarını bulmak
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))#False dedimiz için contours un index leri döner sadece
    #hull.append -> alınan her değeri hull=[] içine atarak saklanmasını sağlar
bg=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(0,255,0),3,8,hierarchy)#8 kesintisiz çizgi türü,kıtanın çizgileri
    cv2.drawContours(bg,hull,i,(0,0,255),1,8)#8 kesintisiz çizgi türü,konvex çizgileri
cv2.imshow("image",bg)
cv2.waitKey(0)
cv2. destroyAllWindows()
