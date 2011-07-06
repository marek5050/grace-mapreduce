#!/usr/bin/env python

from operator import itemgetter
from collections import defaultdict
import sys

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
	
	oldCentroid  += centroid
	oldCentroid += ' '
	for point in point2centroid[centroid]:
		pointX, pointY = point.split(',')
		sumX += int(pointX)
		sumY+=int(pointY)
		count +=1
	
	newX=sumX/count
	newY=sumY/count
	#print(newX,newY)
	#newCentroid.append(newX)
	newCentroid +=`newX`+','+`newY`
	newCentroid+= ' '

  #print 'old centroids'
  #print oldCentroid
  #print 'new centroids' 
  # output the new centroids to a file that will be used in the next mapper
  FILE1 = open("centroid1.txt","w")
    # Write all the lines at once:
  FILE1.writelines(newCentroid)			
  print newCentroid	
	
if __name__ == "__main__": main(sys.argv)	


