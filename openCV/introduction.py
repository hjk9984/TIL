# -*- coding: utf-8 -*-
import cv2
import numpy as np

print(cv2.__version__)

# openCV���� �̹����� �����ϴ� ��Ҵ� �̹��� ũ��, ���е�, ä�η� ������
# �̹��������� ������ ��� �� 3������ ��� ��ġ�ؾ� �ϴ� ��찡 ����.


# �̹����� ũ�⸦ ��Ÿ�� �� wh or rc�� ǥ��
height, width = 120, 100
rows, colunms = 120, 100
color = np.zeros((height, width, 3), np.uint8);
grey = np.zeros((rows, colunms, 1), np.uint8);


# ���е� ǥ��
# np.uint8 >> 0~255     ���� ���� ���
# np.uint16, np.float32 ���

# ä��
# ���� RGB + alpha, �̿ܿ��� Hue Saturation Value ���� �ִ�.
# RGB �̹����� ä�κ��� ������ ���� �ش� �� ä�ο� ����� ������ ����� ������.
# 255 >> ���

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

