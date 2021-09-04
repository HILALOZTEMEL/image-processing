#roi ->region of interest-->ilgi alanı
 #örneğin resimdeki yü de algılama ile ilgileniyoruz
 # ,resimde ilk once yüzdeki kordinatları buluruz.
 #sonra bu kordinatları resimden ayırırız ve roimizi elde etmiş oluruz
 #img[dikey eksen,yatay eksen]

import  cv2

img=cv2.imread("a.jfif")

roi=img[50:100,60:150]
cv2.imshow("roi",roi)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()