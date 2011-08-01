#!/usr/bin/env python
import sys
import os

# This program calls the gnuplotter to plot centroid convergence(cent_plot.ps),
# datapoints and centroids (plotter.ps) and statistics (plotter2.ps) plot.

os.system('gnuplot -persist plotter.gp')
#os.system('gnuplot -persist cent_plot.gp')
#os.system('gnuplot -persist statplotter.gp')

