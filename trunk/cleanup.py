#!/usr/bin/env python
import sys, math, random
import os
import shutil
import time
# This program cleans a partial run and prepares for new run

def main(args):
    os.system('bin/hadoop dfs -rmr data-output')
    os.system('bin/hadoop dfs -rmr centroidinput.txt')
    os.system('bin/hadoop dfs -rmr datapoints.txt')

if __name__ == "__main__": main(sys.argv)

