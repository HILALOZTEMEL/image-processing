#Histogram -> resmin değer noktaları hakkında bilgi verir
import  cv2
import numpy as np
from matplotlib import pyplot as plt

img=np.zeros((500,500),np.uint8)
img2=cv2.imread("g.jpg")
#Resmin BGR değerine ulaşmak
b,g,r=cv2.split(img2)

cv2.imshow("img2",img2)

#çizmemizi sağlar
#plt.hist(img2.ravel( ),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
#ekrana göstermemizi sağlar
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()