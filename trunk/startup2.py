#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import kmeans
import kmeans3d
#import plot

# starting point for the system
#This program runs the test for 2d points in a loop -
#starts with 100 points, 500, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    SP = open("stat_plot.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=500000
    pointx = ''
    while num_points <1000000:

        num_iter = 4
        num_points +=500000
#        num_generated = 50000
        # Create num_points random Points in n-dimensional space
#        num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.1), 2,1, 900, 1,900
 #       pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
  #      num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,50, 350, 50,500
   #     pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
#
 #       num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,410, 600,10,550
  #      pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
   # 	num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,600, 890, 600,900
    #	pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
#
 #       num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.1), 2,150, 300,650,900
  #      pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)
   #     num_gen, coords, lowerx, upperx, lowery, uppery = int(num_generated*.2), 2,650, 880,50,470
    #    pointx = makeRandomPoint(num_gen, lowerx, upperx, lowery, uppery)

        while num_iter <5:
            num_iter +=1

            filename = "centroid2d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
 #   	    shutil.copy("datapoints.txt", datafilename)
    	    shutil.copy(datafilename,"datapoints.txt")
            kmeans.main(num_points)
            # final clustering of the datapoints
#            os.system("python mapperfinal.py")
            #Renaming and finalizing of files
            newfilename = "statistics_" + `num_points` +"_"+ `num_iter` +".txt"
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

#    DP = open("datapoints.txt","w").close()
 #   SP = open("stat_plot3d.txt","w").close()

    num_points=50000
    pointx = ''
    while num_points <0:
        num_iter = 4
        num_points +=50000
        num_generated = 50000
#        # Create num_points random Points in n-dimensional space

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.1), 2,1, 900, 1,900,1,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,50, 250, 50,300,50,400

    	pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
    	num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,510, 700,0,250,0,200
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)

        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,0, 200,650,900,600,750
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.2), 2,650, 880,50,470,800,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)
        num_gen, coords, lowerx, upperx, lowery, uppery,lower,upper = int(num_generated*.1), 2,800, 900,700,900,700,900
        pointx = makeRandom3dPoint(num_gen, lowerx, upperx, lowery, uppery,lower,upper)

        while num_iter <5:
            num_iter +=1
            print num_iter
            filename = "centroid3d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints3d" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	    shutil.copy("datapoints.txt", datafilename)
            kmeans3d.main(num_points)
            # final clustering of the datapoints
 #           os.system("python mapperfinal3d.py")
            #Renaming and finalizing of files
            newfilename = "statistics3d_" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics3d.txt", newfilename)
#            newname = "cluster3d1_" + `num_points` +".txt"
 #           os.rename("cluster3d1.txt", newname)
  #          newname = "cluster3d2_" + `num_points` +".txt"
   #         os.rename("cluster3d2.txt", newname)
    #        newname = "cluster3d3_" + `num_points` +".txt"
     #       os.rename("cluster3d3.txt", newname)
      #      newname = "cluster3d4_" + `num_points` +".txt"
       #     os.rename("cluster3d4.txt", newname)
        #    newname = "cluster3d5_" + `num_points` +".txt"
         #   os.rename("cluster3d5.txt", newname)
          #  newname = "cluster3d6_" + `num_points` +".txt"
           # os.rename("cluster3d6.txt", newname)
    #plot.main()

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

def makeRandomPointX(num_points, lowerx, upperx, lowery, uppery):
    datapoints = ''
    coordX = ''
    coordY = ''
    for i in range(num_points):
	coordX=random.randint(lowerx, upperx)
	coordX = coordX * -1

 	coordY=random.randint(lowery, uppery)
 	coordY=coordY * -1
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
    DP = open("datapoints.txt","a")
    # Write all the lines for datapoints at once:
    DP.writelines(datapoints)
    DP.close()

    return datapoints


if __name__ == "__main__": main(sys.argv)

