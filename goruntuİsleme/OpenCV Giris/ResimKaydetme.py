import cv2
import numpy as np

resim=cv2.imread("indir.jpg", 0)
cv2.imshow("Yazgit",resim )
#resmi kaydetmek
cv2.imwrite("opencvLogosuGriHali.jpg", resim)