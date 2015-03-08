#!usr/bin/python
#-*-coding:utf-8-*-
import sys,os,time,shutil,datetime
import cv2
import cv2.cv as cv
from PIL import Image

start = datetime.datetime.now()

moviePath = sys.argv[1]
savePath = sys.argv[2]
framesNumber = int(sys.argv[3])
BarcodeWidth= int(sys.argv[4])

frameTime = 0
width = BarcodeWidth / framesNumber
print "width of one image: " + str(width)
#create temp file
fileName = moviePath.rfind('/')
movieName = moviePath[fileName:-4]
tempFolder = str(savePath)+'/temp'

if not os.path.isdir(tempFolder):
   os.makedirs(tempFolder)
#capture  video
stream = cv2.VideoCapture(moviePath)

#get number of frames

Totalframes = stream.get(cv.CV_CAP_PROP_FRAME_COUNT)
print "total number of frames: "+ str(Totalframes)

frameInterval = Totalframes//framesNumber 

print "Interval between each frame to capture  " + str(frameInterval) +"s"


destination = str(savePath)+"/"+str(framesNumber)+'.jpeg'
#create empty output image
barcode = Image.new('RGB', (1920,1080))
barcode.save(destination)
finalBarcode= Image.open(destination)
z=0
count = 0
framePosition = 0
Barcodewidth=0
while count < framesNumber:	
	stream.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, framePosition); 
        success,image = stream.read()
        image = cv2.resize(image, (width, 1920))
        cv2.imwrite(tempFolder + "/TempFrame%d.jpg" % count, image)     # save frame as JPEG file
        print 'en cours ' + "image n° "+ str(count) +" position "+ str(framePosition)
        resizedImage = str(tempFolder + "/TempFrame%d.jpg" % count)
        framePosition = framePosition + frameInterval
        resizedImage = str(tempFolder + "/TempFrame%d.jpg" % count)
        img = Image.open(resizedImage)
        finalBarcode.paste(img,(Barcodewidth,0))
        Barcodewidth = Barcodewidth + width
        count += 1

finalBarcode.save(destination)

stop = datetime.datetime.now()

print str(start)
print str(stop)