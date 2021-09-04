#OpenCV pencereine istediğiniz rengi atamak
import cv2
import numpy as np

def nothing(x):
    pass

#np.zeros((512,512,3)) ->512 ye 512 lik bir pecere, kanal değeride 3 yaptım
# np.uint8->veri tipi
img=np.zeros((512,512,3),np.uint8)
#oluşturulan pencereye bir ad veriyoruz
cv2.namedWindow("image")
#tracbar oluşturma
 #R,G,B diye üç adet kızak oluşturucamve bir tanede switch yani anahtar.
 #Anahtar açık olduğu sürece renkler değiştirilebiliyor olacak
 #cv2.createTrackbar("kızak adı","pencere adı",
 #                    başlangıç degeri,
 #                    bitiş değeri,
 #                    fonksiyon adı)
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
switch="0: OFF ,1: ON"
cv2.createTrackbar(switch,"image",0,1,nothing)

while True:

    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

    r=cv2.getTrackbarPos("R","image")
    b=cv2.getTrackbarPos("B","image")
    g=cv2.getTrackbarPos("G","image")
    s=cv2.getTrackbarPos(switch,"image")

    if s==0:
        img[:]=[0,0,0]
    if s==1:
      img[:]=[b,g,r]


cv2.destroyAllWindows()
