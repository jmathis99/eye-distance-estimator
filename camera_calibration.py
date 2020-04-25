"""
camera_calibration.py
"""

import constants
import cv2 as cv
import pickle

def load_pickle_data(calib_loc):
    """
    get_calibration_matrix
    Returns 
    """
    with open(calib_loc, 'rb') as file:
        return pickle.load(file)
        

def undistort_img(img, camera_matrix, dist_coefs, crop=True):
    """
    undistort_and_crop()
    given an image, camera matrix, and distortion coefficients, undistorts the image and crops out the invalid space
    if crop = False, cropping will not be applied
    """
    # get image dimensions
    h, w = img.shape[:2]

    # undistort
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (wL, hL), 1, (wL, hL))
    dst = cv.undistort(imgR, camera_matrix, dist_coefs, None, newcameramtx)

    # crop and save the image
    if crop:
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

    return dst

