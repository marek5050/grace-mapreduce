set term post eps color
set out "plotter.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster1_12000.txt" u 1:2 lt 9 notitle w points, \
"cluster2_12000.txt" u 1:2  lt 2 notitle  w points, \
"cluster3_12000.txt" u 1:2 lt 4 notitle  w points, \
"cluster4_12000.txt" u 1:2 lt 3 notitle  w points, \
"cluster5_12000.txt" u 1:2 lt 5 notitle  w points, \
"cluster6_6000.txt" u 1:2 title 'centroids' w points pointtype 10,\
 "cluster6_9000.txt" u 1:2 notitle  w points pointtype 10, \
 "cluster6_12000.txt" u 1:2 notitle w points pointtype 10

set out "cent_plot.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster6_6000.txt" u 1:2 title 'centroids' w points, \
"cluster6_9000.txt" u 1:2 notitle w points,\
 "cluster6_12000.txt" u 1:2 notitle w points

set out "plotter2.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [80:115]
plot "stat_plot.txt" u 1:2 title 'Convergence' w p

set out "datapoints.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "datapoints12000x.txt" u 1:2 title 'datapoints' w points

