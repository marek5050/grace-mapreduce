#!/usr/bin/env python  
import sys  
# input comes from STDIN (standard input) 
#line = "foo foo quux labs foo bar quux" 
#centroid = "2 27 100 45 78 97"
#centroid = "(5,2) (11,4) (25,9) (69,49) (92,45)" 
centroid = "5,4 11,10 25,11 69,67 92,78" 	
for point in sys.stdin: 
#for line in sys.stdin: 
# remove leading and trailing whitespace  
	point = point.strip()  
    # split the line into words  
	points = point.split()  

# remove leading and trailing whitespace  
	centroid = centroid.strip()  
    # split the centroid into centroids 
	
	centroids = centroid.split()  
	   # increase counters  
	for value in points:
		dist = 0
		minDist = 999999
		bestCent = 0
		for c in centroids:
			# split each co-ordinate of the centroid and the point
			cSplit = c.split(',')
			vSplit = value.split(',')
			#print cSplit[0]
			#print vSplit[0]
			# To handle non-numeric value in centroid or input points
			try:
				#dist = abs(int(cSplit[0]) - int(vSplit[0]))
				dist = (((int(cSplit[0]) - int(vSplit[0]))**2) + ((int(cSplit[1]) - int(vSplit[1]))**2))**.5
				#print dist
				if dist < minDist:
					minDist = dist
					bestCent = c
			except ValueError:
				pass
					  
    # write the results to STDOUT (standard output);  
    # what we output here will be the input for the  
    # Reduce step, i.e. the input for reducer.py  
    #  
    # tab-delimited; the trivial word count is 1  
       	 	print '%s\t%s' % (bestCent, value) 
