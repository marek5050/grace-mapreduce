#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys
import clustering
from statlib import stats

# this program removes outliers based on distance from centroid and c
#alls clustering.py to cluster the datapoints
def main(args):

  point2centroid = defaultdict(list)
  point2centroidfinal = defaultdict(list)
  point2centroidreject = defaultdict(list)
  point2centroid = args
  #point2centroid = [('278,728',['351,467','395,285','611,160','612,409','561,239']), ('778,258',['747,355','699,481','730,207','739,182','870,104','782,161'])]


  for centroid in point2centroid:
   # print 'centroid',centroid
    filename = "newcluster"+`iter`+'.txt'
    cfile = open(filename,'w')
    centroidX, centroidY = centroid.split(',')

    distlist=[]
    finallist=[]
    pdevlist =[]
    rejectlist=[]
    ctrrej=0

    for point in point2centroid[centroid]:
        #print point
        pointX, pointY = point.split(',')

        dist = (((int(centroidX) - int(pointX))**2) + ((int(centroidY) - int(pointY))**2))**.5
        if dist > 180:
            point2centroidreject[centroid].append(point)
        else:
            point2centroidfinal[centroid].append(point)
  #print 'final',point2centroidfinal
  #print 'reject', point2centroidreject

  clustering.main(point2centroidfinal)
if __name__ == "__main__": main(sys.argv)

