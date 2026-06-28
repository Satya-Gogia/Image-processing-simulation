import cv2 as c
import numpy as np

img = c.imread('sample.jpg')

if img is None:
    print("Image not found ")
    exit()

brightness= 50 
contrast = 1.5

image = img.astype(np.float32)
image = image * contrast + brightness

image = np.clip(image,0,256)

image = image.astype(np.int8)

c.imshow("original", img)
c.imshow("Enhanced", image)

c.waitKey(0)
c.destroyAllWindows()