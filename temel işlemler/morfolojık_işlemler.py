import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)
kernel = np.ones((5,5), np.uint8)
erezyon = cv2.erode(img,kernel,iterations=1)

cv2.imshow("orijinal",img)
cv2.imshow("erezyon", erezyon)




cv2.waitKey(0)
cv2.destroyAllWindows()