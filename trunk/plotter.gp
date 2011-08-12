set term post eps color
set out "plotter.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster1_3000.txt" u 1:2 lt 9 title 'cluster1' w points, \
"cluster2_3000.txt" u 1:2  lt 2 title 'cluster2' w points, \
"cluster3_3000.txt" u 1:2 lt 4 title 'cluster3' w points, \
"cluster4_3000.txt" u 1:2 lt 3 title 'cluster4' w points, \
"cluster5_3000.txt" u 1:2 lt 5 title 'cluster5' w points, \
"cluster6_500.txt" u 1:2 title 'centroids' w points pointtype 10,\
 "cluster6_1000.txt" u 1:2 title ' ' w points pointtype 10, \
 "cluster6_1500.txt" u 1:2 title ' ' w points pointtype 10, \
 "cluster6_2000.txt" u 1:2 title ' ' w points pointtype 10, \
 "cluster6_2500.txt" u 1:2 title ' ' w points pointtype 10, \
 "cluster6_3000.txt" u 1:2 title ' ' w points pointtype 10

set out "cent_plot.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster6_500.txt" u 1:2 title 'centroids' w points, \
"cluster6_1000.txt" u 1:2 title ' ' w points,\
 "cluster6_1500.txt" u 1:2 title ' ' w points,\
 "cluster6_2000.txt" u 1:2 title ' ' w points, \
 "cluster6_2500.txt" u 1:2 title ' ' w points,\
 "cluster6_3000.txt" u 1:2 title ' ' w points

set out "plotter2.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [0:3500]
set yrange [0:300]
plot "stat_plot.txt" u 1:2 title 'Convergence' w p

set out "datapoints.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "datapoints3000x.txt" u 1:2 title 'datapoints' w points

