#!usr/bin/python
#-*-coding:utf-8-*-
#the code takes 3 arguments movie location, output image location, number of desired frames
import sys,os,time,shutil,datetime
from converter import Converter
from PIL import Image
start = datetime.datetime.now()

moviePath = sys.argv[1]
savePath = sys.argv[2]
framesNumber = sys.argv[3]
frameTime = 0
tempFolder = '/Users/christophe/Movies/temporary/'
if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)


#create an object to use converter library
movie = Converter()

#get movie length
info = movie.probe(moviePath)
movieDuration = info.format.duration
movieWidth = info.video.video_width
movieHeight = info.video.video_height

print os.path.splitext(moviePath)[0]
print 'durée: %i secondes' % movieDuration
print 'résolution: %ix%i' % (movieWidth,movieHeight)
movieResolution = '%ix%i' % (movieWidth,movieHeight)
frameScale = round(movieDuration/framesNumber,1)
print '%s secondes entre chaque capture d\'image '%frameScale

#create empty output image
barcode = Image.new('RGB', (movieWidth,movieHeight))

x=movieWidth
y=movieHeight
cropInterval = int(movieWidth)/int(framesNumber)
print 'largeur en px de chaque bande: %i' %cropInterval

z=0
for i in range (0,framesNumber-1):
	movie.thumbnail(moviePath, frameTime, tempFolder+'%i.jpeg' %i,movieResolution)
	# left, upper, right, and lower 
	image = Image.open(tempFolder+"%i.jpeg"%i)
	w,h = image.size
	image.crop((0,h-h,cropInterval,h)).save(tempFolder+"crop%i.jpeg"%i)
	crop = Image.open(tempFolder+"crop%i.jpeg"%i)
	frameTime=frameTime+frameScale
	barcode.paste(crop, (z,cropInterval))

	#move each crop 'interval' pixels from previous crop
	z=z+int(cropInterval)
	print 'framed %i at %f seconds and cropped' %(i,frameTime)	


#delete temp folder
shutil.rmtree(tempFolder)

barcode.save(savePath)

OUT = Converter()


#print out.jpg size
img = Image.open(savePath)
# get the image's width and height in pixels
width, height = img.size
print width
print height

stop = datetime.datetime.now()

#print when the soft started and ended
print str(start)
print str(stop)