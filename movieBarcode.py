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

tempFolder = '/tmp/barcodeMovie/'
if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)


print moviePath
print savePath
print framesNumber

#create an object to use converter library
movie = Converter()

#get movie length and resolution
info = movie.probe(moviePath)
movieDuration = int(info.format.duration)
movieWidth = info.video.video_width
movieHeight = info.video.video_height
cropInterval = int(movieWidth)/int(framesNumber)

#display movie info
print 'largeur en px de chaque bande: %i' %cropInterval
print 'durée: %i secondes' % movieDuration
print 'résolution: %ix%i' % (movieWidth,movieHeight)
movieResolution = '%ix%i' % (movieWidth,movieHeight)
frameScale = movieDuration/framesNumber
print '%s secondes entre chaque capture d\'image '%frameScale


#create empty output image
barcode = Image.new('RGB', (movieWidth,movieHeight))

z=0
if movieWidth%cropInterval != 0:
	print 'movie resolution must be proportionnal to framescale*number of frames'
else:
	for i in range (0,framesNumber):
		#Take a screenshot
		movie.thumbnail(moviePath, frameTime, tempFolder+'%i.jpeg' %i,movieResolution)
		# resize image
		im = Image.open(tempFolder+'%i.jpeg' %i)
		croppedImage = im.resize((cropInterval,movieHeight))
		croppedImage.save(tempFolder+"crop%i.jpeg"%i)
		#add  resized image to final image		
		barcode.paste(croppedImage, (z,0))
		#get next X position on the output image
		z=z+int(cropInterval)
		#get position of the next frame to extract
		frameTime=frameTime+frameScale
		print 'framed %i at %f seconds and cropped' %(i,frameTime)	

barcode.save(savePath)
#delete temp folder
#shutil.rmtree(tempFolder)

stop = datetime.datetime.now()

#print when the soft started and ended
print str(start)
print str(stop)