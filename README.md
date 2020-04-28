# eye-distance-estimator

## Background
This code was written for a final project in EECE 4354 Computer Vision at Vanderbilt University
in Nashville. The files in this repo provide methods for estimating the distance to eyes in a photo
using a single image. 

## References
The facial detection model used is the dlib model trained on the iBUG 300-W dataset, which is free
for academic use and is available
[here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).

## Files and Usage
- video_stream.py
  - This file runs eye detection on frames coming in from a webcam stream in order to perform
  distance estimation. Runs with no parameters (edit the camera number in the script if needed).
  Distance for each eye, if eyes are found, is drawn on the image at top left, along with framerate and frame latency.
  - Usage: `python video_stream.py`

- detect_photo.py
  - This file runs eye detection on a single image. Takes one argument, which is the path to
  the image. Distances for both eyes if found are printed to the console.
  - Usage: `python detect_photo.py path/to/image.ext`

- constants.py
  - This file contains various constants used in loading calibration data and distance estimation.
  It should not be run on its own.

- distance_estimation.py
  - This file contains methods for estimating distances to eyes based on calibration parameters
  and eye corner pixels. This file should not be run on its own.

- capture.py
  - This file contains a program to capture a set of images used for camera calibration. 
  - Since OpenCV treats video streams differently from static images, the images taken for calibration must be captured with this tool.
  - Press spacebar to capture an image, q to quit.
  - Usage: `python capture.py -p  filename_prefix -c camera_number -e file_extension -d file/folder/path`
  - Example: `python capture.py -d ./images -e .png -p capture` will save  images to ./images in .png format.

- calibrate.py
  - This file contains helper functions to undistort images as well as to get a camera calibration matrix from a set of photos.
  - This should be run to generate a file containing the calibration matrix after running `capture.py`.
  - Usage: `python camera_calibration.py -p pattern_size -s square_size -d path/to/input -t num_threads -o output_filename`.
  - Example: `python camera_calibration.py -p 8 6 -d images -t 8 -o calibrationdata` will calibrate using the images for an 8x6 checkerboard in the `images` directory and save the calibration matrix to a file `calibrationdata.pickle`.


## Dependencies
- Python 3.7 (3.8 and greater is not supported by dlib at the time of writing)
- dlib >= 19.19
- OpenCV w/ Python bindings >= 4.2.0
- imutils >= 0.5.3