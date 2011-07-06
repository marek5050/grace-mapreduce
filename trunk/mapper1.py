#!/usr/bin/env python  
import sys, math, random 
class Point:
    # Instance variables
    # self.coords is a list of coordinates for this Point
    # self.n is the number of dimensions this Point lives in (ie, its space)
    # self.reference is an object bound to this Point
    # Initialize new Points
    def __init__(self, coords, reference=None):
        self.coords = coords
        self.n = len(coords)
        self.reference = reference
    # Return a string representation of this Point
    def __repr__(self):
        return str(self.coords)


def main(args): 
  
  #centroid = "5,4 110,10 25,11 69,678 92,78"
  # variable to hold map output
  outputmap = ''
  # variables to generate random data points
  num_points, n, lower, upper = 1000,2,1, 1000
    # Create num_points random Points in n-dimensional space
  pointx = makeRandomPoint(num_points, lower, upper)
    
  #print points
  inputfile = "datapoints.txt"
  infiledat = open(inputfile, "r")
  datapoints = infiledat.readline()
  points = datapoints.split()  
 
 #centroid details are stored in an input file
  cfile = "centroidpoints.txt"
  infilecen = open(cfile,"r") 
  centroid = infilecen.readline()	
  #for point in sys.stdin: 
  for point in points: 
  # remove leading and trailing whitespace  
	point = point.strip()  
    # split the line into words  
	points = point.split()  

#   remove leading and trailing whitespace  
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
		
		outputmap += `bestCent`+'   '+`value`
		
       	 	print '%s\t%s' % (bestCent, value)
	outfile = open("mapoutput.txt","w")
	outfile.writelines(outputmap)
	outfile.close() 
def makeRandomPoint(num_points, lower, upper):
    seed = "5,4 110,10 25,11 69,678 92,78"
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
    
    FILE1 = open("centroidpoints.txt","w")
    # Write all the lines for centroids at once:
    FILE1.writelines(seed)
    FILE1.close()
    return datapoints

if __name__ == "__main__": main(sys.argv)

