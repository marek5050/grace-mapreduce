#!/usr/bin/env python  
import sys, math, random 
import os
import shutil

def main(args):
	
	# variables to generate random data points
  	num_points, n, lower, upper = 100,2,1, 100
    	# Create num_points random Points in n-dimensional space
  	pointx = makeRandomPoint(num_points, lower, upper)
	# To test intially with 5 iterations
	num_iter = 1
	# copies the  generated datapoints file and seed centroid file from local folder to hdfs and starts mapReduce
	os.system('bin/hadoop dfs -put ~/hadoop/datapoints.txt datapoints.txt')
	while num_iter < 6: 
		os.system('bin/hadoop dfs -put ~/hadoop/centroidinput.txt centroidinput.txt')
	
	
		os.system('bin/hadoop jar ~/hadoop/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar -file ~/hadoop/mapper1.py -mapper ~/hadoop/mapper1.py -file ~/hadoop/reducer1.py -reducer ~/hadoop/reducer1.py -input datapoints.txt -file centroidinput.txt -file mapoutput1.txt -output data-output')
	
		# output is copied to local files for later lookup and the hdfs version is deleted for next iteration.
		os.system('bin/hadoop dfs -copyToLocal /user/grace/data-output ~/hadoop/output')
		os.rename("output/part-00000", "centroidinput.txt")
		shutil.rmtree('output')
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
