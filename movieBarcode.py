#!usr/bin/python
#-*-coding:utf-8-*-

import sys,os,time
from converter import Converter
from PIL import Image
tps1 = time.clock()
moviePath = '/Users/christophe/Movies/The Social Network (2010) [1080]/The Social Network (2010) 1080p BrRip x264 - 1.2GB - YIFY.mp4'
savePath = '/Users/christophe/Movies/musk.jpg'
framesNumber = 1000
frameTime = 0
tempFolder = '/Users/christophe/Movies/temporary/'
if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)

movie = Converter()


#get movie length
info = movie.probe(moviePath)
movieDuration = info.format.duration
movieWidth = info.video.video_width
movieHeight = info.video.video_height


print 'durée: %i secondes' % movieDuration
print 'résolution: %ix%i' % (movieWidth,movieHeight)
movieResolution = '%ix%i' % (movieWidth,movieHeight)
frameScale = round(movieDuration/framesNumber,2)
print frameScale


#get asked number of movie frames
for i in range (0,movieWidth-1):
	movie.thumbnail(moviePath, frameTime, tempFolder+'%i.jpeg' %i,movieResolution)
	frameTime=frameTime+frameScale
	print 'frame %i at %f seconds' %(i,round(frameTime,2))
	#print 'width %i'%w
	#print 'height %i'%h
	# left, upper, right, and lower 
	image = Image.open("/Users/christophe/Movies/temporary/%i.jpeg"%i)
	w,h = image.size
	image.crop((0,h-h,1,h)).save("/Users/christophe/Movies/temporary/A%i.jpeg"%i)
	print 'frame %i cropped' %(i)


tps2 = time.clock()
print(tps2 - tps1)