import cv2 
import numpy as np

canvas = np.zeros((512,512,3), dtype= np.uint8) + 255 # +255 işlemi siyah tuval ekranını beyaza çevirmek için kullanılır.

cv2.imshow("Tuval ekrani",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()