#!/usr/bin/env python3.7
import cv2
import numpy
import dlib
from imutils import face_utils
import numpy as np

"""
TODO: finish this so that it can return data from multiple faces. Will
      likely require a refactoring of methods that use this.
"""

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

def detectEyes(image):
    shape = None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
    if shape is not None:
        left_eye = shape[lStart:lEnd]
        right_eye = shape[rStart:rEnd]
    else:
        left_eye = None
        right_eye = None
    return left_eye, right_eye