#video okuma
#video kare kare resimlerin birleşiminden olan olaydır
#mesela FPS değeri 70 ise -> saniyede 70 kare gösterim
# yani kare oranı ne kadar artarsa akıcılıkta o kadar artar
import  cv2
import numpy as np

cap=cv2.VideoCapture(0)#0 bilgisayarın webcam'ınden görüntü almak

while(True):
    ret,frame=cap.read()
    #cap.read() ->okuma yapar cap değişkeninden
    #frame ->okunan kareleri tutar
    #ret ->değer döndürür(0 veya 1 ,true veya false)

    #yakaladığı kareleri gösterebilmesi için ->
    cv2.imshow("Webcam",frame)

    #pencera kapanmaması için -
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
#cv2.waitKey(1) -> 1 çünkü 1 den yukarı video donuk gibi olur ,0 da resimler için kullanırız
#yakaladığımız cap leri bırakması için
cap.release()

cv2.destroyAllWindows()