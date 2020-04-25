# Code for estimating distances once the location of eyes are known

import cv2 as cv
import camera_calibration
import constants
import numpy as np


class distance_estimator:
    def __init__(self, calibration_matrix, object_size):
        """
        Initializes the distance estimator.
        calibration_matrix and object_size should be in the same units
        """
        self.calibration_matrix = calibration_matrix
        self.object_size = object_size

    def compute(self, pixel_size):
        """
        Estimates the z-axis distance from the camera.

        :param pixel_width: the width of the eye in pixels
        :param focal_length: focal_length of camera, currently assuming no distortion
        :param object_width: world width of objects, same units as focal_length
        """
        return self.object_size*self.calibration_matrix[0][0]/pixel_width

# Example using the class
if __name__ == "__main__":
    coords = []
    def getCoords(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            print('X:{}\nY:{}'.format(x,y))
            coords.append(np.array([x,y]))

    img = cv.imread('images/24in.jpg')
    camera_matrix, dist_coefs = camera_calibration.load_pickle_data(constants.CALIB_LOC)[1:3]
    
    img = camera_calibration.undistort_img(img, camera_matrix, dist_coefs)

    cv.imshow('Image', img)
    cv.setMouseCallback('Image', getCoords)
    cv.waitKey()

    # Create an estimator with object size in inches
    estimator = distance_estimator(camera_matrix, constants.EYE_WIDTH/2.54/10)

    pixel_width = np.linalg.norm(coords[0]-coords[1])
    print('Distance Estimate:')
    print(estimator.compute(pixel_width))

