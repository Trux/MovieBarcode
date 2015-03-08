#!usr/bin/python
#-*-coding:utf-8-*-
import sys,os,time,shutil,datetime
import cv2
import cv2.cv as cv

tempFolder = '/home/christophe/movie'
if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)
   
stream = cv2.VideoCapture('video.mp4')

#get number of frames
frames = stream.get(cv.CV_CAP_PROP_FRAME_COUNT)
width = stream.get(cv.CV_CAP_PROP_FRAME_WIDTH)
height  = stream.get(cv.CV_CAP_PROP_FRAME_HEIGHT )

count = 0;
while count < 10:
  success,image = stream.read()
  cv2.imwrite(tempFolder + "/frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1


print frames
print width
print height
#cv2.imwrite("frame.jpg", image) 
print stream.get(cv.CV_CAP_PROP_POS_MSEC)