#!/usr/bin/env python  
import sys, math, random 
import os
import shutil

def main(args):
	# maximum delta is set to 2.
	maxDelta = 3
	#oldCentroid = '78,28 23,81 77,72 20,13 21,57'
	#currentCentroid = '79,27 22,88 77,72 20,11 22,55'
	oldCentroid = ''
	currentCentroid = ''
	# variables to generate random data points
  	num_points, n, lower, upper = 100,2,1, 100
    	# Create num_points random Points in n-dimensional space
  	pointx = makeRandomPoint(num_points, lower, upper)
	# To test intially with 7 iterations
	num_iter = 1
	# copies the  generated datapoints file and seed centroid file from local folder to hdfs and starts mapReduce
	os.system('bin/hadoop dfs -put ~/hadoop/datapoints.txt datapoints.txt')
	#while num_iter< 4 and maxDelta >2:
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
			
	
	  print maxDelta
	  print "$$$$$$$$$$$$    next iteration  $$$$$$$$$$$$$$$"
	  #checks the new delta value to avoid additional mapreduce iteration
	  if maxDelta > 2:
	    os.system('bin/hadoop dfs -put ~/hadoop/centroidinput.txt centroidinput.txt')
		
  	    os.system('bin/hadoop jar ~/hadoop/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar -file ~/hadoop/mapper1.py -mapper ~/hadoop/mapper1.py -file ~/hadoop/reducer1.py -reducer ~/hadoop/reducer1.py -input datapoints.txt -file centroidinput.txt -file mapoutput1.txt -output data-output')
		
	    #old_centroid is filled in for future delta calculation
	    cfile = open("centroidinput.txt", "r")
	    oldCentroid = cfile.readline()
	    cfile.close()
	    # output is copied to local files for later lookup and the hdfs version is deleted for next iteration.
	    os.system('bin/hadoop dfs -copyToLocal /user/grace/data-output ~/hadoop/output')
	    os.rename("output/part-00000", "centroidinput.txt")
	    shutil.rmtree('output')
	    #This part of the program can be removed for final output. Just for test run.
	    if num_iter ==1:
		
		shutil.copyfile("centroidinput.txt", "centroidinput1.txt")
	    elif num_iter ==2:
		shutil.copyfile("centroidinput.txt", "centroidinput2.txt")
		
	    elif num_iter ==3:
		shutil.copyfile("centroidinput.txt", "centroidinput3.txt")
		
	    elif num_iter ==4:
		shutil.copyfile("centroidinput.txt", "centroidinput4.txt")
		
	    elif num_iter ==5:
		shutil.copyfile("centroidinput.txt", "centroidinput5.txt")
		
	    elif num_iter ==6:
		shutil.copyfile("centroidinput.txt", "centroidinput6.txt")
		
	    elif num_iter ==7:
		shutil.copyfile("centroidinput.txt", "centroidinput7.txt")
		# prepare for next iteration and remove the existing files in dfs
  	    num_iter += 1
	    os.system('bin/hadoop dfs -rmr data-output')
	    os.system('bin/hadoop dfs -rmr centroidinput.txt')
	
	
def makeRandomPoint(num_points, lower, upper):
    datapoints = ''
    coordX = ''
    coordY = ''
    for i in range(num_points): 
	coordX=random.randint(lower, upper)
 	coordY=random.randint(lower, upper)
	datapoints +=`coordX`+','+`coordY`
	datapoints += ' '
    FILE = open("datapoints.txt","w")
    # Write all the lines for datapoints at once:
    FILE.writelines(datapoints)
    FILE.close()
    
    return datapoints	


if __name__ == "__main__": main(sys.argv)
