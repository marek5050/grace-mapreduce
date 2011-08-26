#!/usr/bin/env python

from operator import itemgetter
import sys, math, random
from defdict import *

def main(args):
  DP = open("datapoints3d50000x.txt","w").close()
  infiledat = open("datapoints3d50000.txt", "r")
  datap = infiledat.readline()
  points = datap.split()
  newdp =''
  DP = open("datapoints3d50000x.txt","a")
  #for point in sys.stdin:
  for point in points:
  # remove leading and trailing whitespace
	point = point.strip()
    # split the line into words
	points = point.split()


	for value in points:
	        vSplit = value.split(',')
	       # newdp +=vSplit[0]+'    '+vSplit[1]
	        newdp +=vSplit[0]+'    '+vSplit[1] +'    '+vSplit[2]
	        newdp +='\n'

            # Write all the lines for datapoints at once:
  DP.writelines(newdp)
  DP.close()

if __name__ == "__main__": main(sys.argv)

