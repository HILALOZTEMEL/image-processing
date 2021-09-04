import cv2

img=cv2.imread("indir.jpg")

#pencereyi yeniden boyutlandırma
#cv2.namedWindow("pencere adı",pencernin yeniden boyutlandırılabilir olduğunu gösteren flag değeri)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()