#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time

def main(args):
	# maximum delta is set to 2.
	maxDelta = 3
	oldCentroid = ''
	currentCentroid = ''

	# variables to generate random data points
  	num_points, n, lower, upper = 100,3,1, 900
	#num_points, n, lower, upper = 1000,2,1, 900
    	# Create num_points random Points in n-dimensional space
  	pointx = makeRandomPoint(num_points, lower, upper)
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
					dist = (((int(cSplit[0]) - int(oSplit[0]))**2) + ((int(cSplit[1]) - int(oSplit[1]))**2) + ((int(cSplit[2]) - int(oSplit[2]))**2))**.5

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

  	    os.system('bin/hadoop jar ~/hadoop/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar -file ~/hadoop/mapper13d.py -mapper ~/hadoop/mapper13d.py -file ~/hadoop/reducer13d.py -reducer ~/hadoop/reducer13d.py -input datapoints.txt -file centroidinput.txt -file mapoutput1.txt -file ~/hadoop/defdict.py -output data-output')

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


	# final clustering of the datapoints
	os.system('bin/hadoop dfs -put ~/hadoop/centroidinput.txt centroidinput.txt')

  	os.system('bin/hadoop jar ~/hadoop/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar -file ~/hadoop/mapper13d.py -mapper ~/hadoop/mapper13d.py -file ~/hadoop/reducerfinal.py -reducer ~/hadoop/reducerfinal.py -input datapoints.txt -file centroidinput.txt -file mapoutput1.txt -file ~/hadoop/defdict.py -output data-output')

	# output is copied to local files for later lookup and the hdfs version is deleted for next iteration.
	os.system('bin/hadoop dfs -copyToLocal /user/grace/data-output ~/hadoop/output')
	os.rename("output/part-00000", "finalcluster.txt")
	cfile = open("finalcluster.txt", "r")
	currentCluster = cfile.readline()
	cfile.close()
	statistics += '\n New Cluster: ' + `currentCluster`
	FILE = open("statistics.txt","w")
    	# Write all the lines for statistics at once:
    	FILE.writelines(statistics)
    	FILE.close()
	shutil.rmtree('output')
	os.system('bin/hadoop dfs -rmr data-output')
	os.system('bin/hadoop dfs -rmr centroidinput.txt')
	os.system('bin/hadoop dfs -rmr datapoints.txt')
def makeRandomPoint(num_points, lower, upper):
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
    FILE = open("datapoints.txt","w")
    # Write all the lines for datapoints at once:
    FILE.writelines(datapoints)
    FILE.close()

    return datapoints


if __name__ == "__main__": main(sys.argv)

