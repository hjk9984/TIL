# -*- coding: utf-8 -*-
import cv2
import numpy as np

print(cv2.__version__)

# openCV에서 이미지를 구성하는 요소는 이미지 크기, 정밀도, 채널로 구성됨
# 이미지끼리의 연산의 경우 이 3가지를 모두 일치해야 하는 경우가 많다.


# 이미지의 크기를 나타낼 때 wh or rc로 표현
height, width = 120, 100
rows, colunms = 120, 100
color = np.zeros((height, width, 3), np.uint8);
grey = np.zeros((rows, colunms, 1), np.uint8);


# 정밀도 표현
# np.uint8 >> 0~255     제일 많이 사용
# np.uint16, np.float32 등등

# 채널
# 보통 RGB + alpha, 이외에도 Hue Saturation Value 등이 있다.
# RGB 이미지를 채널별로 나눠서 보면 해당 색 채널에 가까운 색들이 흰색에 가깝다.
# 255 >> 흰색

# RGB to Grey scale
# 0.299R + 0.587G + 0.144B


# python openCV histogram example
image = cv2.imread("./openCV/sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result = np.zeros((image.shape[0], 256), dtype=np.uint8)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

for x, y in enumerate(hist):
    cv2.line(result, (int(x), image.shape[0]),(int(x), image.shape[0] - int(y)), 255)

dst = np.hstack([image[:, :, 0], result])
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

