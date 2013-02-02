#!usr/bin/python
#-*-coding:utf-8-*-

import sys,os,res
from converter import Converter

moviePath = '/Users/christophe/Movies/201211_musk.mp4'
savePath = '/Users/christophe/Movies/musk.jpg '
movieResolution = 0
framesNumber = 1000
tempFolder = '/Users/christophe/Movies/tmp/'


movie = Converter()


#get movie length
info = movie.probe(moviePath)
movieDuration = info.format.duration
movieWidth = info.video.video_width
movieHeight = info.video.video_height


print 'durée:'+movieDuration