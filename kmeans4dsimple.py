#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
import mapper14dsimple

# First step into the algorithm.
# checks convergence for 3d points and calls simple 3d mapper

def main(args):
	# maximum delta is set to 2.
	maxDelta = 3
	oldCentroid = ''
	currentCentroid = ''

	# To test intially with 7 iterations
	num_iter = 1
	statistics =''
	statplot =''

# initialize starttime to calculate the total time taken to converge.

	statp = open("stat_plot4dsimp.txt","a")
	STAT = open("statistics4d.txt","w")
	start = time.time()
	while maxDelta >2:
	  #print num_iter
	  # check for delta
	  cfile = open("centroidinput.txt", "r")
	  currentCentroid = cfile.readline()
	  cfile.close()
	  if oldCentroid != '':
		maxDelta = 0
		#   remove leading and trailing whitespace
		oldCentroid = oldCentroid.strip()
    		# split the centroid into centroids
		oldCentroids = oldCentroid.split()
		#   remove leading and trailing whitespace
		currentCentroid = currentCentroid.strip()
    		# split the centroid into centroids
		currentCentroids = currentCentroid.split()
	  	# centroids are not in the same order in each iteration. So each centroid is checked against all other centroids for distance.
	   	for value in currentCentroids:
			dist = 0
			minDist = 9999
			oSplit = value.split(',')

			for c in oldCentroids:

				# split each co-ordinate of the oldCentroid and the currentCentroid
				cSplit = c.split(',')

				# To handle non-numeric value in old or new centroids
				try:

					dist = (((int(cSplit[0]) - int(oSplit[0]))**2) + ((int(cSplit[1]) - int(oSplit[1]))**2) + ((int(cSplit[2]) - int(oSplit[2]))**2)+((int(cSplit[3]) - int(oSplit[3]))**2))**.5

					if dist < minDist:
						minDist = dist
					#print minDist, value, c

				except ValueError:
					pass
			if minDist > maxDelta:
				maxDelta = minDist
	  else:
		statistics += '\n seed centroid: ' +`currentCentroid`
	  statistics += '\n num_iteration: ' +`num_iter`+';  Delta: '+`maxDelta`
	  print maxDelta
	  print num_iter
	  print "$$$$$$$$$$$$    next iteration  $$$$$$$$$$$$$$$"
	  #checks the new delta value to avoid additional mapreduce iteration
	  if maxDelta > 2:

	    #old_centroid is filled in for future delta calculation
	    cfile = open("centroidinput.txt", "r")
	    oldCentroid = cfile.readline()
	    cfile.close()
	     #call simple mapper
	    mapper14dsimple.main(num_iter)

  	    num_iter += 1

	end = time.time()
	elapsed = end -start
	print "elapsed time ", elapsed, "seconds"
	statistics += '\n  Time_elapsed: '+ `elapsed`
	statistics += '\n New Centroids: '+ `currentCentroid`

	    # Write all the lines for statistics at once:
    	STAT.writelines(statistics)
    	STAT.close()

    	# Write all the lines for statplot incrementaly:
        statplot = `args` + '  '+ `elapsed` + '  '+`num_iter` + '\n'

        statp.writelines(statplot)

if __name__ == "__main__": main(sys.argv[1])

