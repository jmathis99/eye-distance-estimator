"""
camera_calibration.py
"""

import cv2 as cv
import pickle
import sys
import getopt
from glob import glob
import pickle
import numpy as np

def load_pickle_data(calib_loc):
    """
    Returns data loaded from pickle file.
    """
    with open(calib_loc, 'rb') as file:
        return pickle.load(file)
        

def undistort_img(img, camera_matrix, dist_coefs, crop=True):
    """
    Given an image, camera matrix, and distortion coefficients, undistorts the image and crops out the invalid space.
    
    :param img: the image to undistort
    :param camera_matrix: the 3x3 camera matrix. Can be found with calibrate()
    :param dist_coefs: the distortion coefficients. Can be found with calibrate()
    :param crop: If True, the output image will be cropped to its region of interest.
    :returns: The undistorted image
    """
    # get image dimensions
    h, w = img.shape[:2]

    # undistort
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))
    dst = cv.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

    # crop and save the image
    if crop:
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

    return dst

def calibrate(img_dir, pattern_size, square_size=1, threads=1, filename=None):
    """
    Calibrate images from a set of photos of a chessboard pattern. Most code from OpenCV calibrate.py

    :param img_dir: the directory where the chessboard photos are located
    :param pattern_size: a tuple containing number of checkers in width and heigh
    :param square_size: the size of a side of the checkerboard square. Calibration matrix will turn out in these units.
    :param threads: the number of threads to use.
    :param filename: specify if you would like the output to be saved to a pickle file
    :returns 
    """

    def processImage(fn):
        # Taken from OpenCV calibrate.py
        print('processing %s... ' % fn)
        img = cv.imread(fn, 0)
        if img is None:
            print("Failed to load", fn)
            return None

        assert w == img.shape[1] and h == img.shape[0], ("size: %d x %d ... " % (img.shape[1], img.shape[0]))
        found, corners = cv.findChessboardCorners(img, pattern_size)
        if found:
            term = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 30, 0.1)
            cv.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

        if not found:
            print('chessboard not found')
            return None

        print('           %s... OK' % fn)
        return (corners.reshape(-1, 2), pattern_points)
    
    img_names = glob(img_dir + '/*')
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = cv.imread(img_names[0], cv.IMREAD_GRAYSCALE).shape[:2]

    if threads <= 1:
        chessboards = [processImage(fn) for fn in img_names]
    else:
        print("Run with %d threads..." % threads)
        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(threads)
        chessboards = pool.map(processImage, img_names)

    chessboards = [x for x in chessboards if x is not None]
    for (corners, pattern_points) in chessboards:
        img_points.append(corners)
        obj_points.append(pattern_points)

    # calculate camera coefficients
    rms, camera_matrix, dist_coefs, rvecs, tvecs = cv.calibrateCamera(obj_points, img_points, (w, h), None, None)

    # save camera and dist coeff to pickle file
    if filename is not None:
        with open('{}.pickle'.format(filename), 'wb') as file:
            pickle.dump((camera_matrix, dist_coefs), file)
    
    return camera_matrix, dist_coefs

if __name__ == "__main__":
    import argparse
    import os

    left_num = 0

    parser = argparse.ArgumentParser(prog="camera_calibration",
        description= "Run calibration")
    parser.add_argument('-p', '--pattern', nargs=2, metavar=('height', 'width'), type=int, help="Pattern Size")
    parser.add_argument('-s', '--size', default=1, type=int, help="Square Size")
    parser.add_argument('-d', '--dir', default='data', help="Input File folder")
    parser.add_argument('-t', '--threads', default=1, type=int, help="Number of Threads")
    parser.add_argument('-o', '--output', default=None, help="Output File Name")

    args = parser.parse_args()

    calibrate(args.dir, (args.pattern[0], args.pattern[1]), args.size, args.threads, args.output)