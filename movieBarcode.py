#!usr/bin/python
#-*-coding:utf-8-*-

import sys,os,time
from converter import Converter
tps1 = time.clock()
moviePath = '/Users/christophe/Movies/201211_musk.mp4'
savePath = '/Users/christophe/Movies/musk.jpg'
framesNumber = 1000
tempFolder = '/Users/christophe/Movies/tmp/'


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
frameTime = 1
#get asked number of movie frames
for i in range (0,1000):
	movie.thumbnail(moviePath, frameTime, '/Users/christophe/Movies/tmp/%i.jpeg' %i,movieResolution)
	frameTime=frameTime+frameScale
	#print 'frame %i at %f seconds' %(i,round(frameTime,2))

tps2 = time.clock()
print(tps2 - tps1)