import cv2
import numpy as np

# membaca gambar
img = cv2.imread("./image.jpeg")

# mengambil tinggi dan lebar gambar
height, width = img.shape[:2]

# jumlah pixel yang digeser
translationX = 50
translationY = 50
# membuat matriks
matrix = np.float64([[1, 0, translationX], [0, 1, translationY]])

# membuat gambar menjadi berpindah
skewed_img = cv2.warpAffine(img, matrix, (width, height))

# menampilkan gambar
cv2.imshow("skewed image", skewed_img)
cv2.imshow("original image", img)

cv2.waitKey(0)
cv2.destroyAllWindows
