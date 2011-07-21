#!/usr/bin/env python
import sys
import os

# This program calls the gnuplotter

os.system('gnuplot -persist plotter.gp')
os.system('gnuplot -persist cent_plot.gp')

