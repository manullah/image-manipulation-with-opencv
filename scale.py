import cv2

img = cv2.imread("./image.jpeg")
height, width = img.shape[:2]

center = (width / 2, height / 2)

M = cv2.getRotationMatrix2D(center, angle=30, scale=1)
rotated_img = cv2.warpAffine(img, M, (width, height))

cv2.imshow("ori", img)
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
