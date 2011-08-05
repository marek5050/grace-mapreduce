#!/usr/bin/env python

from operator import itemgetter
#from collections import defaultdict
from defdict import *
import sys
import clustering
from statlib import stats

# this program removesoutliers based on abs median value
#and calls clustering.py to cluster the datapoints
# Finds the final adjusted centroid
def main(args):

  point2centroid = defaultdict(list)
  point2centroidfinal = defaultdict(list)
  point2centroidreject = defaultdict(list)
  point2centroid = args
  #point2centroid = [('278,728',['351,467','395,285','611,160','612,409','561,239']), ('778,258',['747,355','699,481','730,207','739,182','870,104','782,161'])]

  for centroid in point2centroid:
   # print 'centroid',centroid


    centroidX, centroidY = centroid.split(',')

    distlist=[]
    finallist=[]
    pdevlist =[]
    rejectlist=[]
    newX =0
    newY =0
    sumX=0
    sumY=0
    count=0
    ctrrej=0

    for point in point2centroid[centroid]:
        #print point
        pointX, pointY = point.split(',')
        #datapoint += pointX + '  ' + pointY +'\n'
        dist = (((int(centroidX) - int(pointX))**2) + ((int(centroidY) - int(pointY))**2))**.5
        distlist.append(dist)


    pmed = stats.medianscore(distlist)
    #print 'pmed',pmed
    for p in distlist:
      pdev = abs(p-pmed)
      pdevlist.append(pdev)

    med_pdev = stats.medianscore(pdevlist)
    #print "med_pdev", med_pdev
    for p in distlist:
        if med_pdev >0:
            test_stat = abs(p-pmed)/med_pdev
            #print test_stat
            if test_stat<2:
               finallist.append(p)
            else:
                ctrrej +=1
                rejectlist.append(p)
    #print 'distlist', distlist
    #print 'finallist', finallist
    #print 'rejectlist', rejectlist
    #print 'ctrrej', ctrrej

    for point in point2centroid[centroid]:

        #print point
        pointX, pointY = point.split(',')

        dist = (((int(centroidX) - int(pointX))**2) + ((int(centroidY) - int(pointY))**2))**.5
        if dist in rejectlist and dist >100:
            point2centroidreject[centroid].append(point)
        else:
            point2centroidfinal[centroid].append(point)
            sumX += int(pointX)
            sumY +=int(pointY)
            count +=1

    newX=sumX/count
    newY=sumY/count
    newCentroid = `newX`+','+`newY`
    #print newCentroid
    point2centroidfinal[newCentroid]=point2centroidfinal[centroid]
    del point2centroidfinal[centroid]
  #print 'final',point2centroidfinal
  #print 'reject', point2centroidreject
  clustering.main(point2centroidfinal)

if __name__ == "__main__": main(sys.argv)

