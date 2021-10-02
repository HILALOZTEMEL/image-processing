import cv2
import numpy as np
import math

vid = cv2.VideoCapture(0)

while(1):

    try:

        ret, frame = vid.read()
        frame=cv2.flip(frame,1)
        #morfolojik işlemler için kernel tanımlarız
        kernel = np.ones((3,3),np.uint8)

        roi=frame[100:300, 100:300]


        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
        #belli bir alandaki rengi diğer alanlardan ayırabilemk için hsv ye çeviremeliy,z
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


        #elimiz diğer nesnelerden ayırabilmek için elimizin üst ve alt renklerini belirlememiz gerekir 
        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)
        #ayırma işlemi
        mask = cv2.inRange(hsv, lower_skin, upper_skin)


        #ayırdıktan sonra kanlık noktaları beyaz ile doldurma
        mask = cv2.dilate(mask,kernel,iterations = 4)
        #resim üzerindeki gürültüyü gidermek adına
        mask = cv2.GaussianBlur(mask,(5,5),100)

        #sınır çizgileri Contourskları bulma 
        _,contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #contoursların max alanını belirleme
        cnt = max(contours, key = lambda x: cv2.contourArea(x))
        #contours sa daha çok yaklaşıp sınır çizgilerinin daha iyi çizilmasi sağlanır
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)


        hull = cv2.convexHull(cnt)#kordinatları elde ettik
        #hull içindeki kordinatları kullanarak alanını hesaplarız
        areaHull = cv2.contourArea(hull)#şeklin alanı
        areaCnt = cv2.contourArea(cnt)#elimin alanı

        areaRatio=((areaHull-areaCnt)/areaCnt)*100#örtünün içinde elimizin olmadığı alanı hesaplamak

        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)#kusurları tutan değişken

        l=0#TOPLAM KUSUR SAYISI=0

        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])


            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2#oluşan üçgenin alanının bulmak(kenar uzunluklarını bildiğim üçgenin alanı)
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

            d=(2*ar)/a#noktalar ve dış bükey örtü arası mesafe

            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57#iki kenar arası açı


            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)

            cv2.line(roi,start, end, [0,255,0], 2)


        l+=1

        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==1:
            if areaCnt<2000:
                cv2.putText(frame,'Put your hand in the box',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            else:
                if areaRatio<12:
                    cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                elif areaRatio<17.5:
                    cv2.putText(frame,'Best luck',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

                else:
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        elif l==2:#2 paramak kaldırırım dış bükeyde kusur 2 olur
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        elif l==3:

            if areaRatio<27:
                cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        elif l==4:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        elif l==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        elif l==6:
            cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        else :
            cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)
    except:
        pass


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
vid.release()    
    
