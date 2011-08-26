#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import test
# generates randon points

def main(args):
    DP = open("datapoints.txt","w").close()
    num_points=12000
    pointx = ''
    while num_points <12500:
        num_points +=500
        num_generated = 12000
         # Create num_points random Points in n-dimensional space
        num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz, lower,upper = int(num_generated*.1), 2,1, 900, 1,900,1,900,1,900
        pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper = int(num_generated*.2), 2,50, 250, 50,300,50, 250,50,400

    	pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)
    	num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper = int(num_generated*.2), 2,510, 700,0,250,0,250,0,200
        pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)

        num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper = int(num_generated*.2), 2,0, 200,650,900,650,800,600,750
        pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper = int(num_generated*.2), 2,650, 880,50,470,50, 270, 800,900
        pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper = int(num_generated*.1), 2,800, 900,700,900,700,900, 700,900
        pointx = makeRandom4dPoint(num_gen, lowerx, upperx, lowery, uppery,lowerz, upperz,lower,upper)

        #os.system("python test.py")
        test.main(num_points)


    #DP = open("datapoints.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <0:
        num_points +=500
         # Create num_points random Points in n-dimensional space

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.1), 2,1, 900, 1,900,1,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,50, 250, 50,300,50, 250,50,400

    	pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
    	num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,510, 700,0,250,0,250, 0,200
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,0, 200,650,900,650,800,600,750
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,650, 880,50,470,50,270,800,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.1), 2,800, 900,700,900,700,900,700,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)

        #os.system("python test.py")
        test.main(num_points)

def makeRandomPoint(num_points, lowerx, upperx, lowery, uppery):
    datapoints = ''
    coordX = ''
    coordY = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
 	coordY=random.randint(lowery, uppery)
	datapoints +=`coordX`+','+`coordY`
	datapoints += ' '
    DP = open("datapoints.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints

def makeRandom4dPoint(num_points, lowerx, upperx, lowery, uppery,lowerz,upperz, lowera, uppera):
    datapoints = ''
    coordX = ''
    coordY = ''
    coordZ = ''
    coordA = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
 	coordY=random.randint(lowery, uppery)
	coordZ=random.randint(lowerz, upperz)
	coordA=random.randint(lowera, uppera)
	datapoints +=`coordX`+','+`coordY`+','+`coordZ`+','+`coordA`
	datapoints += ' '
    DP = open("datapoints.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints

if __name__ == "__main__": main(sys.argv)

