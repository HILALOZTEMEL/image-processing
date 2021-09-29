import cv2
import numpy as np

path1 = "aircraft.jpg"
path2 = "aircraft1.jpg"

img1 = cv2.imread("aircraft.jpg")


img2 = cv2.imread("aircraft1.jpg")


img3 = cv2.medianBlur(img1,7)

"""
if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")
"""

# diff = difference
diff = cv2.subtract(img1,img3)#pikseller arası çıkarma işlemi yapar
b,g,r = cv2.split(diff)#pikselleri ayırır

#countNonZero()  , dizi matrisindeki sıfır olmayan piksellerin sayısını döndürür  .
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
    print("completely equal")
else:
    print("NOT completely equal")


cv2.imshow("Difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
