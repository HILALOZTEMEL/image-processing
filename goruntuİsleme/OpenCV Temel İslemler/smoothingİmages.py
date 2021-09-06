#resimler üzerindeki gürültüleri ve pürüzleri azaltmayı amaçlıyoruz
import  cv2
import numpy as np

imgFilter=cv2.imread("filter.png")
imgMedian=cv2.imread("median.png")
imgBilateral=cv2.imread("bilateral.png")

blur=cv2.blur(imgFilter,(5,5))
gaussianBlur=cv2.GaussianBlur(imgFilter,(5,5),cv2.BORDER_DEFAULT)

medianBlur=cv2.medianBlur(imgMedian,5)

bilateralBlur=cv2.bilateralFilter(imgBilateral,9,75,75)

#cv2.imshow("original",imgFilter)
#cv2.imshow("blur",blur)
#cv2.imshow("gaussianBlur",gaussianBlur)
#cv2.imshow("imgMedian",imgMedian)
#cv2.imshow("medianBlur",medianBlur)
cv2.imshow("imgBilateral",imgBilateral)
cv2.imshow("bilateralBlur",bilateralBlur)


cv2.waitKey(0)
cv2.destroyAllWindows()