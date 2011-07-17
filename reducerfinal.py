#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys

def main(args):
  
  point2centroid = defaultdict(list)

  
  # input comes from STDIN
  for line in sys.stdin:
    	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py into a dictionary
	
	centroid, point = line.split('\t')
	point2centroid[centroid].append(point)
	
   		
  print point2centroid
  	
if __name__ == "__main__": main(sys.argv)	


