#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
# This program runs the test for 2d points in a loop -
#starts with 100 points, 500, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <2000:
        num_points +=500
        coords, lower, upper = 2,1, 900
    	# Create num_points random Points in n-dimensional space
    	pointx = makeRandomPoint(num_points, lower, upper)
    	shutil.copy("centroid2d.txt","centroidinput.txt")
        os.system("python kmeans.py")

        newfilename = "statistics_" + `num_points` +".txt"
        os.rename("statistics.txt", newfilename)

    DP = open("datapoints.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <2000:
        num_points +=500
        coords, lower, upper = 3,1, 900
    	# Create num_points random Points in n-dimensional space
    	pointx = makeRandom3dPoint(num_points, lower, upper)
    	shutil.copy("centroid3d.txt","centroidinput.txt")
        os.system("python kmeans3d.py")

        newfilename = "statistics3d_" + `num_points` +".txt"
        os.rename("statistics.txt", newfilename)

def makeRandomPoint(num_points, lower, upper):
    datapoints = ''
    coordX = ''
    coordY = ''
    for i in range(num_points):
	coordX=random.randint(lower, upper)
 	coordY=random.randint(lower, upper)
	datapoints +=`coordX`+','+`coordY`
	datapoints += ' '
    DP = open("datapoints.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints

def makeRandom3dPoint(num_points, lower, upper):
    datapoints = ''
    coordX = ''
    coordY = ''
    coordZ = ''
    for i in range(num_points):
	coordX=random.randint(lower, upper)
 	coordY=random.randint(lower, upper)
	coordZ=random.randint(lower, upper)
	datapoints +=`coordX`+','+`coordY`+','+`coordZ`
	datapoints += ' '
    DP = open("datapoints.txt","w")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints


if __name__ == "__main__": main(sys.argv)

