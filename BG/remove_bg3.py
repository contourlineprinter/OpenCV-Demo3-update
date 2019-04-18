import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUR = 15
DILATE = 8
ERODE = 8
THRESH1 = 15
THRESH2 = 180
COLOR = (1.0, 1.0, 1.0)

type = 3

img_file = 'bg3.jpg'
x1 = 0.1
x2 = 0.9
y1 = 0.0
y2 = 0.8

img = cv2.imread(img_file)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height, width = image_rgb.shape[:2]
rectangle = (int(width*x1), int(height*y1), int(width*x2), int(height*y2))

mask = np.zeros(image_rgb.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.grabCut(image_rgb, mask, rectangle,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

cv2.imwrite("output.jpg", image_rgb_nobg)
plt.imshow(image_rgb_nobg), plt.axis("off")
plt.show()
