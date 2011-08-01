#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import kmeans

# starting point for the system
#This program runs the test for 2d points in a loop -
#starts with 100 points, 500, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    SP = open("stat_plot.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <3000:
        print "num of points"
        print num_points
        num_iter = 0
        num_points +=500
        num_generated = 500
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

        while num_iter <5:
            num_iter +=1

            filename = "centroid2d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	    shutil.copy("datapoints.txt", datafilename)
            kmeans.main(num_points)
            # final clustering of the datapoints
            os.system("python mapperfinal.py")
            #Renaming and finalizing of files
            newfilename = "statistics_" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics.txt", newfilename)

            newname = "cluster1_" + `num_points` +".txt"
            os.rename("cluster1.txt", newname)
            newname = "cluster2_" + `num_points` +".txt"
            os.rename("cluster2.txt", newname)
            newname = "cluster3_" + `num_points` +".txt"
            os.rename("cluster3.txt", newname)
            newname = "cluster4_" + `num_points` +".txt"
            os.rename("cluster4.txt", newname)
            newname = "cluster5_" + `num_points` +".txt"
            os.rename("cluster5.txt", newname)
            newname = "cluster6_" + `num_points` +".txt"
            os.rename("cluster6.txt", newname)

#    DP = open("datapoints.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <0:
        num_points +=500
#        # Create num_points random Points in n-dimensional space

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.4), 2,1, 900, 1,900,1,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,50, 300, 50,450,50,600

    	pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
    	num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,410, 600,10,550,100,200
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
    	num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,600, 890, 0,200,10,300
    	pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,100, 500,650,900,600,700
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,650, 880,50,470,800,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_points*.1), 2,800, 900,750,900,800,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
       	shutil.copy("centroid3d.txt","centroidinput.txt")
        os.system("python kmeans3d.py")

        newfilename = "statistics3d_" + `num_points` +".txt"
        os.rename("statistics.txt", newfilename)

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

def makeRandom3dPoint(num_points, lowerx, upperx, lowery, uppery,lowerz,upperz):
    datapoints = ''
    coordX = ''
    coordY = ''
    coordZ = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
 	coordY=random.randint(lowery, uppery)
	coordZ=random.randint(lowerz, upperz)
	datapoints +=`coordX`+','+`coordY`+','+`coordZ`
	datapoints += ' '
    DP = open("datapoints.txt","w")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints


if __name__ == "__main__": main(sys.argv)

