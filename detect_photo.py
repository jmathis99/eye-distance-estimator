#!/usr/bin/env python3.7

import cv2 as cv
import argparse
import eye_detect

"""
This file detects eyes in a photo passed as an argument.
"""

parser = argparse.ArgumentParser()
parser.add_argument("image")

args = parser.parse_args()

image = args.image
left, right = eye_detect.detectEyes(image)
for (x, y) in left:
    image[y, x] = [0, 0, 255]
for (x, y) in right:
    image[y, x] = [0, 255, 0]

cv.imshow("eyes", image)
cv.waitKey(0)
cv.destroyAllWindows()
