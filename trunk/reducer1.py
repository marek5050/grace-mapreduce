#!/usr/bin/env python

from operator import itemgetter
from collections import defaultdict
import sys

# maps words to their counts
point2centroid = defaultdict(list)

#line = "foo	foo	quux	labs	foo	bar	quux"
# input comes from STDIN

for line in sys.stdin:
    	# remove leading and trailing whitespace
	line = line.strip()
	
    	# parse the input we got from mapper.py into a dictionary
	
	centroid, point = line.split('\t')
	point2centroid[centroid].append(point)
	
#print point2centroid.items()
pointX =0
pointY =0
newCentroid=''
oldCentroid=''

for centroid in point2centroid:
	sumX =0
	sumY=0
	count=0
	newX =0
	newY=0
	
	#centroid =1
	#print centroid
	oldCentroid  += centroid
	oldCentroid += ' '
	for point in point2centroid[centroid]:
		pointX, pointY = point.split(',')
		sumX = sumX + int(pointX)
		sumY+=int(pointY)
		count +=1
	
	newX=sumX/count
	newY=sumY/count
	#print(newX,newY)
	#newCentroid.append(newX)
	newCentroid +=`newX`+','+`newY`
	newCentroid+= ' '

print 'old centroids'
print oldCentroid
print 'new centroids'			
print newCentroid	
	
	


