import cv2
import numpy as np
resim=cv2.imread("indir.jpg", -1)
#  0 ->resmi griye çevirir
#  1 ->varsayılan olarak gelir resim tamamen aynı kalır
# -1 ->alfa kanalı dahil olarak gelir

cv2.imshow("Yazgit",resim )#resmi görebilmek için
cv2.waitKey(0)#ben bir tuşa basan kadar bekle "0 -> sonsuza kadar bekle"
cv2.destroyAllWindows()#tüm pecereleri kapat