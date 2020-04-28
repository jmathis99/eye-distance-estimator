import cv2
import argparse
import os

left_num = 0

parser = argparse.ArgumentParser(prog="capture",
    description= "Capture frames for calibration")
parser.add_argument('-p', '--prefix', default='left', help="Filename prefix")
parser.add_argument('-c', '--capture', default=0, help="Camera number")
parser.add_argument('-e', '--ext', default='.jpg', help="File extension")
parser.add_argument('-d', '--dir', default='data', help="File folder")
args = parser.parse_args()

cap = cv2.VideoCapture(args.capture)

if not os.path.isdir(args.dir):
    os.mkdir(args.dir)

while(True):
    _, frame = cap.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        filename = args.dir + os.path.sep + args.prefix + str(left_num) + args.ext
        cv2.imwrite(filename, frame)
        print("Saving " + filename)
        left_num += 1

    if key == ord('q'):
        exit(0)
