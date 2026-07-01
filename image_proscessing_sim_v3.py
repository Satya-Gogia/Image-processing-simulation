import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
    exit()

# 1. Brightness Increase
bright = np.clip(image + 50, 0, 255).astype(np.uint8)

# 2. Negative Image
negative = 255 - image

# 3. Grayscale using NumPy
gray = np.mean(image, axis=2).astype(np.uint8)

# 4. Horizontal Flip
horizontal = image[:, ::-1]

# 5. Vertical Flip
vertical = image[::-1, :]

cv2.imshow("Original", image)
cv2.imshow("Bright", bright)
cv2.imshow("Negative", negative)
cv2.imshow("Gray", gray)
cv2.imshow("Horizontal Flip", horizontal)
cv2.imshow("Vertical Flip", vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()
