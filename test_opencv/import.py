
import cv2
filePath = 'me.png'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow("This is me, Harold", readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imread(filePath, 1)

