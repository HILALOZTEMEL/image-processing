#Renk Uzayı basitçe belirli renk organizasyonlarına verilen isimdir.
#resimler belirli renklerin bir araya gelmeleri ile oluşurlar.
#renklerin çok fazla olması onların daha kullanışlı hale gelmelerini
#ve erişilebilir hale gelmeleri için oları sınıflandırma ihtiyacını doğurmuştur.
#bu şekildede rek uzayı kavramı ortaya çıkmıştır.
import  cv2

img=cv2.imread("b.jpg")
cv2.namedWindow("BGR'a göre",cv2.WINDOW_NORMAL)

#bgr dan rgb ye dönüştürme
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.namedWindow("RCB'ye göre",cv2.WINDOW_NORMAL)

#bgr dan hsv ye dönüştürme
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("HSV'ye göre",cv2.WINDOW_NORMAL)

#bgr dan gray ye dönüştürme
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("GRAY'ye göre",cv2.WINDOW_NORMAL)

cv2.imshow("BGR'a göre",img)
#cv2.imshow("RCB'ye göre",img1)
#cv2.imshow("HSV'ye göre",img2)
cv2.imshow("GRAY'ye göre",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()