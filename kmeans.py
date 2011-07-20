#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time

# First step into the algorithm.
# checks convergence and calls mapReduce

def main(args):
	# maximum delta is set to 2.
	maxDelta = 3
	oldCentroid = ''
	currentCentroid = ''

	# To test intially with 7 iterations
	num_iter = 1
	statistics =''

	# copies the  generated datapoints file and seed centroid file from local folder to hdfs and starts mapReduce
	os.system('bin/hadoop dfs -put ~/hadoop/datapoints.txt datapoints.txt')
	# initialize starttime to calculate the total time taken to converge.
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
					#dist = abs(int(cSplit[0]) - int(vSplit[0]))
					dist = (((int(cSplit[0]) - int(oSplit[0]))**2) + ((int(cSplit[1]) - int(oSplit[1]))**2))**.5

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
	    os.system('bin/hadoop dfs -put ~/hadoop/centroidinput.txt centroidinput.txt')

  	    os.system('bin/hadoop jar ~/hadoop/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar -file ~/hadoop/mapper1.py -mapper ~/hadoop/mapper1.py -file ~/hadoop/reducer1.py -reducer ~/hadoop/reducer1.py -input datapoints.txt -file centroidinput.txt -file ~/hadoop/defdict.py -output data-output')

	    #old_centroid is filled in for future delta calculation
	    cfile = open("centroidinput.txt", "r")
	    oldCentroid = cfile.readline()
	    cfile.close()
	    # output is copied to local files for later lookup and the hdfs version is deleted for next iteration.
	    os.system('bin/hadoop dfs -copyToLocal /user/grace/data-output ~/hadoop/output')
	    os.rename("output/part-00000", "centroidinput.txt")
	    shutil.rmtree('output')

  	    num_iter += 1
	    os.system('bin/hadoop dfs -rmr data-output')
	    os.system('bin/hadoop dfs -rmr centroidinput.txt')
	end = time.time()
	elapsed = end -start
	print "elapsed time ", elapsed, "seconds"
	statistics += '\n  Time_elapsed: '+ `elapsed`
	statistics += '\n New Centroids: '+ `currentCentroid`
	STAT = open("statistics.txt","w")
    	# Write all the lines for statistics at once:
    	STAT.writelines(statistics)
    	STAT.close()
	os.system('bin/hadoop dfs -rmr datapoints.txt')

if __name__ == "__main__": main(sys.argv)
