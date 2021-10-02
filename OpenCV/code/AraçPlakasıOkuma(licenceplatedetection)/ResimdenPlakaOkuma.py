import  cv2
import numpy
import numpy as np
import pytesseract
import imutils

#maskeleme işlemleri için numpy import numpy
#metin okumak için import pytesseract
#görüntü üzerinde yapılacak bazı temel işlemler için import imutils

img=cv2.imread("../../test_images/licence_plate.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#fotoğrafı yumuşatmak adına bilateralFilter ,plaka dışındaki her yer gürültü kabul edilir
filtered=cv2.bilateralFilter(gray,5,250,250)

#rsimdeki köşerin tespiti için canny
edged=cv2.Canny(filtered,30,200)

#plakanın contourları tespit etemek için
contours=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#uygun kontourları yakala
cnts=imutils.grab_contours(contours)

#uygun contoursları alana göre sırala
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screen=None

#plaka dikdörtgendir bizde cnts de dikdörtgen arayacağız
for c in cnts:
    epsilon=0.018*cv2.arcLength(c,True)#cv2.arcLength(1,2) -> contour ların yay uzunluğunu bulmaktır 1. de contours değerlerini çeker 2.de boşluk var mı yok mu ona bakar True boşluk yok ise devam et demek
    approx=cv2.approxPolyDP(c,epsilon,True)#hatalı sınır tespitlerini en aza indire bilmek için
    if len(approx)==4: #4 köşe tespit edildiyse
        screen=approx
        break
#maske uygulayıp kırptıktan sonra sadece plaka olan bir roi kalır
mask=np.zeros(gray.shape,np.uint8)
new_img=cv2.drawContours(mask,[screen],0,(255,255,255),-1)#plaka alanınını beyaza boyadık
new_img=cv2.bitwise_and(img,img,mask=mask)#plaka alanaındaki yazıyı buraya yapıştırcaz

#new_img ı kırpmalıyız
(x,y)=np.where(mask==255)
(topx,topy)=(np.min(x),np.min(y))
(bottomx,bottomy)=(np.max(x),np.max(y))
cropped=gray[topx:bottomx+1,topy:bottomy+1]#kırpma işlemi

#bu görintüyüde pytserect işlemine tabi tutup okuruz
text=pytesseract.image_to_string(cropped,lang="eng")
print("detected text :"+text)

cv2.waitKey(0)
cv2.destroyAllWindows()