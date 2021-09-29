import cv2

img= cv2.imread("starwars.jpg")

#bulanık bir resim olması için resmi blurlarız
blurry_img=cv2.medianBlur(img,7)

#laplacian ile resimde blrlama var mı yok mu fark  ederiz blur artarsa Laplacian azalır.
laplacian=cv2.Laplacian(blurry_img,cv2.CV_64F).var()

if laplacian<500:
    print("blurry image")

cv2.imshow("img",img)
cv2.imshow("bulanık",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()