#!/usr/bin/env python3.7
import cv2 as cv
import eye_detect
import distance_estimation
import constants
import camera_calibration

"""
This file in its present state reads a video stream from camera 0
and attempts to find eyes in the image using eye_detect.py.
Dependencies:
- OpenCV python bindings (cv2)
- dlib python bindings (NOTE: dlib does not yet support python 3.8, use 3.7)
- Adrian Rosebrock's imutils package

Other considerations:
- dlib facial feature detection is slow, so this script has a very low framerate.
"""

cap = cv.VideoCapture(0)
(matrix, distCoeffs) = camera_calibration.load_pickle_data(constants.CALIB_LOC)
estimator = distance_estimation.distance_estimator(matrix, constants.EYE_WIDTH/2.54/10)
while True:
    ret, image = cap.read()
    left, right = eye_detect.detectEyes(image)
    if left is not None and right is not None:
        for (x, y) in left:
            image[y, x] = [0, 0, 255]
        leftDistance = estimator.compute([left[0], left[3]])
        #print("Left Eye Distance: ", estimator.compute([left[0], left[3]]))
        for (x, y) in right:
            image[y, x] = [0, 255, 0]
        rightDistance = estimator.compute([right[0], right[3]])
        #print("Right Eye Distance: ", estimator.compute([right[0], right[3]]))
        cv.putText(image, "Left Eye Distance: {}".format(leftDistance), 
            (0, 50), cv.FONT_HERSHEY_SIMPLEX, .5, [255,0,0])
        cv.putText(image, "Right Eye Distance: {}".format(rightDistance), 
            (0, 75), cv.FONT_HERSHEY_SIMPLEX, .5, [255,0,0])
    cv.imshow("video", image)
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()