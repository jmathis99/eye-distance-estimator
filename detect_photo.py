#!/usr/bin/env python3.7

import cv2 as cv
import argparse
import eye_detect
import distance_estimation
import camera_calibration
import constants

"""
This file detects eyes in a photo passed as an argument.
"""

parser = argparse.ArgumentParser()
parser.add_argument("image")

args = parser.parse_args()

(matrix, distCoeffs) = camera_calibration.load_pickle_data(constants.CALIB_LOC)
estimator = distance_estimation.distance_estimator(matrix, constants.EYE_WIDTH/2.54/10)

image = cv.imread(args.image)
left, right = eye_detect.detectEyes(image)
for (x, y) in left:
    image[y, x] = [0, 0, 255]
print("Left Eye Distance: ", estimator.compute([left[0], left[3]]))
for (x, y) in right:
    image[y, x] = [0, 255, 0]
print("Right Eye Distance: ", estimator.compute([right[0], right[3]]))

cv.imshow("eyes", image)
cv.waitKey(0)
cv.destroyAllWindows()
