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

## Dependencies
- Python 3.7 (3.8 and greater is not supported by dlib at the time of writing)
- dlib >= 19.19
- OpenCV w/ Python bindings >= 4.2.0
- imutils >= 0.5.3