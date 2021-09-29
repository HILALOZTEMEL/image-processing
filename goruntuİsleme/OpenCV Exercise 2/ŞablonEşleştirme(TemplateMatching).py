import cv2
import numpy as np

image_path="starwars.jpg"
teplate_path="starwars2.jpg"

img=cv2.imread(image_path)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template=cv2.imread(teplate_path,cv2.IMREAD_GRAYSCALE)
h,w=template.shape[::]

#.. fonksiyon benim şablonumu resimdeki uygun bir yere eşleştirecek
result=cv2. matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)

#np.where -> kordinatları bulma
location=np.where(result>=0.9)#0.9 değeri arttıkça teplateti bulmaya o kadar yaklaşırız

#location içindeki kordinatlar array halinde bulunurken bu şekide onları kordinatlar haline getiririz
for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)

cv2.imshow("result",result)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

