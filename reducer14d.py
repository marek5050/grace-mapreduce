#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys

# reducer for 4d points
def main(args):

  point2centroid = defaultdict(list)


  # input comes from STDIN
  for line in sys.stdin:
    	# remove leading and trailing whitespace
	line = line.strip()

    	# parse the input we got from mapper.py into a dictionary

	centroid, point = line.split('\t')
	point2centroid[centroid].append(point)

  #print point2centroid.items()
  pointX =pointY =pointZ=pointXX=0

  newCentroid= oldCentroid=''


  for centroid in point2centroid:
	sumX =sumY=sumZ=sumXX=count=newX=newY=newZ=newXX=0

	oldCentroid  += centroid
	oldCentroid += ' '
	for point in point2centroid[centroid]:
		pointX, pointY, pointZ, pointXX = point.split(',')
		sumX += int(pointX)
		sumY +=int(pointY)
		sumZ +=int(pointZ)
		sumXX +=int(pointXX)
		count +=1

	newX=sumX/count
	newY=sumY/count
	newZ=sumZ/count
	newXX=sumXX/count
	#print(newX,newY)
	#newCentroid.append(newX)
	newCentroid +=`newX`+','+`newY`+','+`newZ`+','+`newXX`
	newCentroid+= ' '

  #print 'old centroids'
  #print oldCentroid
  #print 'new centroids'

  print newCentroid

if __name__ == "__main__": main(sys.argv)

