#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys

# reducer for 4d points without hadoop
def main(args):

  point2centroid = defaultdict(list)
  point2centroid = args

  pointX =0
  pointY =0
  pointZ =0
  pointXX =0
  newCentroid=''
  oldCentroid=''

  for centroid in point2centroid:
	sumX =0
	sumY=0
	sumZ=sumXX=0
	count=0
	newX =0
	newY=0
	newZ=newXX=0
	oldCentroid  += centroid
	oldCentroid += ' '
	for point in point2centroid[centroid]:
		pointX, pointY, pointZ ,pointXX= point.split(',')
		sumX += int(pointX)
		sumY +=int(pointY)
		sumZ +=int(pointZ)
		sumXX +=int(pointXX)
		count +=1

	newX=sumX/count
	newY=sumY/count
	newZ=sumZ/count
	newXX=sumXX/count

	newCentroid +=`newX`+','+`newY`+','+`newZ`+','+`newXX`
	newCentroid+= ' '

  print newCentroid
  cfile= open("centroidinput.txt", 'w')
  cfile.writelines(newCentroid)
  cfile.close()

if __name__ == "__main__": main(sys.argv)

