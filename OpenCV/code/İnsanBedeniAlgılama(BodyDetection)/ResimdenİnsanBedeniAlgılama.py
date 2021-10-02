import  cv2

img=cv2.imread("../../test_images/body.jpg")

body_cascade=cv2.CascadeClassifier("../../haarCascade/fullbody.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=body_cascade.detectMultiScale(gray,1.1,5)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("imges",img)
cv2.waitKey(0)
cv2.destroyAllWindows()