# eye-distance-estimator

## Background
This code was written for a final project in EECE 4354 Computer Vision at Vanderbilt University
in Nashville. The files in this repo provide methods for estimating the distance to eyes in a photo
using a single image. 

## References
The facial detection model used is the dlib model trained on the iBUG 300-W dataset, which is free
for academic use and is available
[here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).

## Dependencies
- Python 3.7 (3.8 and greater is not supported by dlib at the time of writing)
- dlib >= 19.19
- OpenCV w/ Python bindings >= 4.2.0
- imutils >= 0.5.3