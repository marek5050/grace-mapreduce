#!/usr/bin/env python  
import sys, math, random 
import ast
# This file assigns the final clusters.

def main(): 
  
  
  # variable to hold map output
  #outputmap = {}
  outputmap =''
  cfile = "centroidinput.txt"
  infilecen = open(cfile,"r") 
  centroid = infilecen.readline()
  #pfile = "datapoints.txt"
  #infiledat = open(pfile,"r") 
  #points = infiledat.readline()
  
 # print centroid
  #print points
  #print centroid	
  for point in sys.stdin: 
  #for point in points: 
  # remove leading and trailing whitespace  
	point = point.strip()  
    # split the line into words  
	points = point.split()  
	#print points
#   remove leading and trailing whitespace  
	centroid = centroid.strip()  
    # split the centroid into centroids 
	centroids = centroid.split()
        #print centroids
	outfile = open("mapoutput1.txt","w")  
	   # increase counters  
	for value in points:
		dist = 0
		minDist = 999999
		bestCent = 0
	
		for c in centroids:
			# split each co-ordinate of the centroid and the point
			cSplit = c.split(',')
			vSplit = value.split(',')
			#print cSplit
			#print vSplit
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
					  
    # write the results to STDOUT (standard output) and store in a variable to write to an output file;  
    # what we output here will be the input for the  
    # Reduce step, i.e. the input for reducer.py  
    #  
    # tab-delimited
		#outputmap[bestCent] =  value
		outputmap += `bestCent`+':'+`value`+' '
		#list = outputmap.split()
    		#dic = {}
    		#for entry in list:
       		# key, val = entry.split(':')
        	# dic[key] = val
		#print outputmap 
		#ast.literal_eval(outputmap)
		#outfile.writelines(outputmap)
       	 	print '%s\t%s' % (bestCent, value)
	#outfile = open("mapoutput1.txt","w")
	outfile.write(outputmap)
	outfile.close() 

if __name__ == "__main__": main()
