#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
# This program runs the test for 2d points in a loop -
#starts with 100 points, 500, 1000, 1500, 2000, 3000, 5000 points

# to plot in Gnuplot window plot "samples.txt" u 1:2 w points pointtype 6 lc rgb "red"

def main(args):
    DP = open("samples2.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <3000:
        num_points +=3000
        num_generated = 3000
        # Create num_points random Points in n-dimensional space
        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.1), 2,1, 900, 1,900
        pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,50, 350, 50,500
        pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,410, 600,10,550
        pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
    	num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,600, 890, 600,900
    	pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)

        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.1), 2,150, 300,650,900
        pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,650, 880,50,470
        pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)


def makeRandomPoint(num_points, lowerx, upperx, lowery, uppery):
    datapoints = ''
    coordX = ''
    coordY = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
 	coordY=random.randint(lowery, uppery)
	datapoints +=`coordX`+' '+`coordY`
	datapoints += '\n'
    DP = open("samples2.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints

def makeRandom3dPoint(num_points, lowerx, upperx, lowery, uppery,lowerz,upperz):
    datapoints = ''
    coordX = ''
    coordY = ''
    coordZ = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
 	coordY=random.randint(lowery, uppery)
	coordZ=random.randint(lowerz, upperz)
	datapoints +=`coordX`+' '+`coordY`+' '+`coordZ`
	datapoints += '\n'
    DP = open("samples.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints


if __name__ == "__main__": main(sys.argv)

