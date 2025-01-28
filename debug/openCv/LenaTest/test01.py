import cv2

# https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html

print(cv2.__version__)

fileName = 'lena.jpg'

original = cv2.imread(fileName, cv2.IMREAD_COLOR)
gray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchage', unchange)

cv2.waitKey(0)
cv2.destroyAllWindows()
