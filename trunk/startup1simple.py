#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import kmeanssimple
import kmeans3dsimple
#import plot

# starting point for the system for simple run without hadoop
#This program runs the test for 2d points in a loop -
#starts with 500 points, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    SP = open("stat_plotsimp.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <3000:

        num_iter = 0
        num_points +=500
        num_generated = 500
        # This program uses the same data generated for map reduce runs.


        while num_iter <5:
            num_iter +=1

            filename = "centroid2d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	    #shutil.copy("datapoints.txt", datafilename)
    	    shutil.copy(datafilename,"datapoints.txt")
            kmeanssimple.main(num_points)
            #final clustering of the datapoints
            os.system("python mapperfinal.py")
            #Renaming and finalizing of files
            newfilename = "statisticsimp_" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics.txt", newfilename)
            newname = "cluster1_simp_" + `num_points` +".txt"
            os.rename("cluster1.txt", newname)
            newname = "cluster2_simp_" + `num_points` +".txt"
            os.rename("cluster2.txt", newname)
            newname = "cluster3_simp_" + `num_points` +".txt"
            os.rename("cluster3.txt", newname)
            newname = "cluster4_simp_" + `num_points` +".txt"
            os.rename("cluster4.txt", newname)
            if os.path.exists("cluster5.txt"):
                newname = "cluster5_simp_" + `num_points` +".txt"
                os.rename("cluster5.txt", newname)
            newname = "cluster6_simp_" + `num_points` +".txt"
            os.rename("cluster6.txt", newname)
    #plot.main()

    DP = open("datapoints.txt","w").close()
    SP = open("stat_plot3dsimp.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=0
    pointx = ''
    while num_points <3000:
        num_iter = 0
        num_points +=500
        num_generated = 500
#        # uses the same datapoints already generated


        while num_iter <5:
            num_iter +=1
            print num_iter
            filename = "centroid3d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints3d" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	    #shutil.copy("datapoints.txt", datafilename)
    	    shutil.copy(datafilename, "datapoints.txt")
            kmeans3dsimple.main(num_points)
            # final clustering of the datapoints
            os.system("python mapperfinal3d.py")
            #Renaming and finalizing of files
            newfilename = "statistics3d_" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics3d.txt", newfilename)
            newname = "cluster3d1_simp_" + `num_points` +".txt"
            os.rename("cluster3d1.txt", newname)
            newname = "cluster3d2_simp_" + `num_points` +".txt"
            os.rename("cluster3d2.txt", newname)
            newname = "cluster3d3_simp_" + `num_points` +".txt"
            os.rename("cluster3d3.txt", newname)
            newname = "cluster3d4_simp_" + `num_points` +".txt"
            os.rename("cluster3d4.txt", newname)
            newname = "cluster3d5_simp_" + `num_points` +".txt"
            os.rename("cluster3d5.txt", newname)
            newname = "cluster3d6_simp_" + `num_points` +".txt"
            os.rename("cluster3d6.txt", newname)
    #plot.main()



if __name__ == "__main__": main(sys.argv)

