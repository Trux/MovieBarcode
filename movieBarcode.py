#!usr/bin/python
#-*-coding:utf-8-*-
#the code takes 3 arguments movie location, output image location, number of desired frames
import sys,os,time,shutil,datetime
from converter import Converter
from PIL import Image
start = datetime.datetime.now()

moviePath = sys.argv[1]
savePath = sys.argv[2]
framesNumber = int(sys.argv[3])
frameTime = 0

print moviePath
print savePath
print framesNumber

tempFolder = '/tmp/barcodeMovie/'
if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)


#create an object to use converter library
movie = Converter()

#get movie length and resolution
info = movie.probe(moviePath)
movieDuration = int(info.format.duration)
movieWidth = info.video.video_width
movieHeight = info.video.video_height

print 'durée: %i secondes' % movieDuration
print 'résolution: %ix%i' % (movieWidth,movieHeight)
movieResolution = '%ix%i' % (movieWidth,movieHeight)
frameScale = movieDuration/framesNumber
print '%s secondes entre chaque capture d\'image '%frameScale

#create empty output image
barcode = Image.new('RGB', (movieWidth,movieHeight))

x=movieWidth
y=movieHeight
cropInterval = int(movieWidth)/int(framesNumber)
print 'largeur en px de chaque bande: %i' %cropInterval

z=0
print movieWidth%cropInterval
if movieWidth%cropInterval != 0:
	print 'movie resolution must be proportionna to framescale*number of frames'
else:
	for i in range (0,framesNumber-1):
		#Take a screenshot
		movie.thumbnail(moviePath, frameTime, tempFolder+'%i.jpeg' %i,movieResolution)
		# resize image
		im = Image.open(tempFolder+'%i.jpeg' %i)
		croppedImage = im.resize((cropInterval,movieHeight))
		croppedImage.save(tempFolder+"crop%i.jpeg"%i)
		#add  resized image to final image 
		frameTime=frameTime+frameScale
		barcode.paste(croppedImage, (z,cropInterval))
		#move each crop 'interval' pixels from previous crop
		z=z+int(cropInterval)
		print 'framed %i at %f seconds and cropped' %(i,frameTime)	


#delete temp folder
shutil.rmtree(tempFolder)

barcode.save(savePath)

stop = datetime.datetime.now()

#print when the soft started and ended
print str(start)
print str(stop)