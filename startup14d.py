#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time

import kmeans4d
import kmeans4dsimple
#import plot

# starting point for the system
#This program runs the test for 2d points in a loop -
#starts with 100 points, 500, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    SP = open("stat_plot.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=12000
    pointx = ''
    while num_points <12500:

        num_iter = 4
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


        while num_iter <5:
            num_iter +=1

            filename = "centroid4d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	   # shutil.copy("datapoints.txt", datafilename)
    	    shutil.copy(datafilename,"datapoints.txt")
    	   # shutil.copy(datafilename,"datapoints.txt")
            kmeans4dsimple.main(num_points)
            # final clustering of the datapoints
           # os.system("python mapperfinal.py")
            #Renaming and finalizing of files
            newfilename = "statistics_4d_simp" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics.txt", newfilename)
#            newname = "cluster1_" + `num_points` +".txt"
 #           os.rename("cluster1.txt", newname)
  #          newname = "cluster2_" + `num_points` +".txt"
   #         os.rename("cluster2.txt", newname)
    #        newname = "cluster3_" + `num_points` +".txt"
     #       os.rename("cluster3.txt", newname)
      #      newname = "cluster4_" + `num_points` +".txt"
       #     os.rename("cluster4.txt", newname)
            if os.path.exists("cluster5.txt"):
                newname = "cluster5_" + `num_points` +".txt"
                os.rename("cluster5.txt", newname)
        #    newname = "cluster6_" + `num_points` +".txt"
         #   os.rename("cluster6.txt", newname)
    #plot.main()



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

