#resimleri birbirleri üzerine ekleyip onların ağırlıkları yoğunluklarını değiştirerel bi resim kaybolcak diğeri çıkacak
import  cv2

def nothing(x):
    pass

img=cv2.imread("aircraft.jpg")
img=cv2.resize(img,(640,480))

img2=cv2.imread("balls.jpg")
img2=cv2.resize(img2,(640,480))

#üst üste eklediğim değişken için de
output=cv2.addWeighted(img,0.5,img2, 0.5, 0)

windowName="Transition program"
cv2.namedWindow(windowName)

#alpha ve beta değerlerindeki değişimi gözlicez
cv2.createTrackbar("alpha-beta",windowName,0,1000,nothing)

while True:
    cv2.imshow(windowName,output)
    alpha=cv2.getTrackbarPos("alpha-beta",windowName)/1000
    beta=1-alpha
    output=cv2.addWeighted(img,alpha,img2, beta, 0)
    print(alpha,beta)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
