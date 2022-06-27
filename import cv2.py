import cv2
filePath = 'legaspi.jpg'
windowTitle = 'power power power'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()