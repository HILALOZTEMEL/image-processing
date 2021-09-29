import  cv2

img=cv2.imread('../../test_images/face.png')

#cascade'i dahil etmek
face_cascade=cv2.CascadeClassifier('../../haarCascade/frontalface.xml')

#2. etap resmi gri tonlara çevirmek
#Resimlerdeki aydınlık ve karanlığı daha iyi tespit etmek için
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#resimdeki yüzleri algılayacağız bunun için
#detectMultiScale() -> func kullanılacak bu func resin üzerinde yüzlerin bulunduğu kordinatları vericek
#face_cascade i kullanarak yüzlerin kordinatlarını ver deriz
faces=face_cascade.detectMultiScale(gray,1.3,7) #kordinatlar faces in içinde tuples olarak saklanır

#bu değerleri kullanarak yüz üzerine dikdörtgen çizeceğiz
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("yüz algılama",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
