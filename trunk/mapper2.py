#!/usr/bin/env python
import sys, math, random
from defdict import *

# mapper for 2d points
class Point:
    # Instance variables
    # self.coords is a list of coordinates for this Point
    # self.n is the number of dimensions this Point lives in (ie, its space)
    # self.reference is an object bound to this Point
    # Initialize new Points
    def __init__(self, coords, reference=None):
        self.coords = coords
        self.n = len(coords)
        self.reference = reference
    # Return a string representation of this Point
    def __repr__(self):
        return str(self.coords)


def main(args):


  # variable to hold map output
  outputmap = ''
  point2centroid = defaultdict(list)

  cfile = "centroidinput.txt"
  infilecen = open(cfile,"r")
  centroid = infilecen.readline()
  #print centroid
  for point in sys.stdin:

	point = point.strip()
    # split the line into words
	points = point.split()

	centroid = centroid.strip()
    # split the centroid into centroids
	centroids = centroid.split()

	for value in points:
		dist = 0
		minDist = 999999
		bestCent = 0


		for c in centroids:
			# split each co-ordinate of the centroid and the point
			cSplit = c.split(',')
			vSplit = value.split(',')

			# To handle non-numeric value in centroid or input points
			try:
				#dist = abs(int(cSplit[0]) - int(vSplit[0]))
				dist = (((int(cSplit[0]) - int(vSplit[0]))**2) + ((int(cSplit[1]) - int(vSplit[1]))**2))**.5
				#print dist
				if dist < minDist:
					minDist = dist
					bestCent = c

			except ValueError:
				pass

       	 	#print '%s\t%s' % (bestCent, value)
       	 	point2centroid[bestCent].append(value)


        pointX= pointY =0
       # print point2centroid

        newCentroid= oldCentroid=''


        for centroid in point2centroid:
	        sumX= sumY= count= newX=newY =0

	        for point in point2centroid[centroid]:

		        pointX, pointY = point.split(',')


		        sumX += int(pointX)
		        sumY +=int(pointY)
		        count +=1

	        newX=sumX/count
	        newY=sumY/count
	        newCentroid =`newX`+','+`newY`

	        print '%s\t%s' % (centroid, newCentroid)

def makeCentroids():
	cfile = open("centroidinput.txt", "r")
	seed = cfile.readline()
	cfile.close()
	#seed = "43,211 130,62 387,253 454,734 545,920"
	FILE1 = open("centroidpoints.txt","w")
    # Write all the lines for seed = "15,40 110,10 25,9 69,678 240,78"  centroids at once:
    	FILE1.writelines(seed)
    	FILE1.close()
    	return seed
if __name__ == "__main__": main(sys.argv)

