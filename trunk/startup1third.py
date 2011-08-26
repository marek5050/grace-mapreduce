#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import kmeansthird
import kmeans3dthird
#import plot

# starting point for the system for simple run with hadoop only in the last round
#This program runs the test for 2d and 3d points in a loop -
#starts with 500 points, 1000, 1500, 2000, 3000, 5000 points

def main(args):
    DP = open("datapoints.txt","w").close()
    SP = open("stat_plotthird.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=3000
    pointx = ''
    while num_points <12000:

        num_iter = 0
        num_points +=3000
        num_generated = 3000
        # This program uses the same data generated for map reduce runs.


        while num_iter <5:
            num_iter +=1

            filename = "centroid2d_" + `num_iter` +".txt"
    	    shutil.copy(filename,"centroidinput.txt")
    	    datafilename = "datapoints" + `num_points` + ".txt"
    	    #shutil.copy("datapoints1000.txt","datapoints.txt")
    	    #shutil.copy("datapoints.txt", datafilename)
    	    shutil.copy(datafilename,"datapoints.txt")
            kmeansthird.main(num_points)
            #final clustering of the datapoints
            os.system("python mapperfinal.py")
            #Renaming and finalizing of files
            newfilename = "statisticsthird_" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics.txt", newfilename)
            newname = "cluster1_third_" + `num_points` +".txt"
            os.rename("cluster1.txt", newname)
            newname = "cluster2_third_" + `num_points` +".txt"
            os.rename("cluster2.txt", newname)
            newname = "cluster3_third_" + `num_points` +".txt"
            os.rename("cluster3.txt", newname)
            newname = "cluster4_third_" + `num_points` +".txt"
            os.rename("cluster4.txt", newname)
            if os.path.exists("cluster5.txt"):
                newname = "cluster5_third_" + `num_points` +".txt"
                os.rename("cluster5.txt", newname)
            newname = "cluster6_third_" + `num_points` +".txt"
            os.rename("cluster6.txt", newname)
        os.system('bin/hadoop dfs -rmr datapoints.txt')
    #plot.main()

    DP = open("datapoints.txt","w").close()
    SP = open("stat_plot3dthird.txt","w").close()
    ST = open("statistics.txt","w").close()
    num_points=3000
    pointx = ''
    while num_points <12000:
        num_iter = 0
        num_points +=3000
        num_generated = 3000
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
            kmeans3dthird.main(num_points)
            # final clustering of the datapoints
            os.system("python mapperfinal3d.py")
            #Renaming and finalizing of files
            newfilename = "statistics3d_third" + `num_points` +"_"+ `num_iter` +".txt"
            os.rename("statistics3d.txt", newfilename)
            newname = "cluster3d1_third_" + `num_points` +".txt"
            os.rename("cluster3d1.txt", newname)
            newname = "cluster3d2_third_" + `num_points` +".txt"
            os.rename("cluster3d2.txt", newname)
            newname = "cluster3d3_third_" + `num_points` +".txt"
            os.rename("cluster3d3.txt", newname)
            newname = "cluster3d4_third_" + `num_points` +".txt"
            os.rename("cluster3d4.txt", newname)
            newname = "cluster3d5_third_" + `num_points` +".txt"
            os.rename("cluster3d5.txt", newname)
            newname = "cluster3d6_third_" + `num_points` +".txt"
            os.rename("cluster3d6.txt", newname)
        os.system('bin/hadoop dfs -rmr datapoints.txt')
    #plot.main()



if __name__ == "__main__": main(sys.argv)

