import cv2

def resizewithAspectRatio(img,widht= None,height=None,inter=cv2.INTER_AREA):
    #inter=cv2.INTER_AREA-> resmi yeniden boyutlandırıken çakışmalari önlemek için default yani varsayılan olarak gireriz.
    dimension=None
    (h,w)=img.shape[:2]

    if widht is None and height is None:
        return img

    if widht is None:
        r=height/float(h)
        dimension=(int(w*r),height)
    else:
        r=widht/float(w)
        dimension=(widht,int(h*r))
    return cv2.resize(img,dimension,interpolation=inter)
    #Interpolation iki nokta arasındaki doğru parçasından yeni noktalar çıkarmaya denir.

img=cv2.imread("indir.jpg")
img1=resizewithAspectRatio(img,widht=None,height=600,inter=cv2.INTER_AREA)

cv2.imshow("Original",img)
cv2.imshow("Resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


