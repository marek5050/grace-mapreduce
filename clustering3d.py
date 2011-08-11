#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys

# this program performs the final cluster and creates files for each cluster
def main(args):

  point2centroid = defaultdict(list)

  point2centroid = args
  datapoint = ''
  centroidpoint=''
  iter = 0
  for centroid in point2centroid:
    #print centroid

    iter +=1
    filename = "cluster3d"+`iter`+'.txt'
    cfile = open(filename,'w')
    datapoint = ''
    centroidX, centroidY, centroidZ = centroid.split(',')
    centroidpoint += centroidX + '  ' +centroidY + '  ' +centroidZ +'\n'


    for point in point2centroid[centroid]:
        #print point
        pointX, pointY, pointZ = point.split(',')
        datapoint += pointX + '  ' + pointY + '  ' + pointZ+'\n'


    cfile.writelines(datapoint)
    cfile.close()
  iter+=1
  filename="cluster3d"+`iter` + '.txt'
  #print filename
  cfile= open(filename, 'w')
  cfile.writelines(centroidpoint)
  cfile.close()
if __name__ == "__main__": main(sys.argv)

