set term post eps color
set out "plotter_3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set ylabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d1_3000.txt" u 1:2:3 lt 9 title 'cluster1' w points, \
"cluster3d2_3000.txt" u 1:2:3  lt 2 title 'cluster2' w points, \
"cluster3d3_3000.txt" u 1:2:3 lt 4 title 'cluster3' w points, \
"cluster3d4_3000.txt" u 1:2:3 lt 3 title 'cluster4' w points, \
"cluster3d5_3000.txt" u 1:2:3 lt 5 title 'cluster5' w points, \
"cluster3d6_500.txt" u 1:2:3 title 'centroids' w points pointtype 10,\
 "cluster3d6_1000.txt" u 1:2:3 title ' ' w points pointtype 10, \
 "cluster3d6_1500.txt" u 1:2:3 title ' ' w points pointtype 10, \
 "cluster3d6_2000.txt" u 1:2:3 title ' ' w points pointtype 10, \
 "cluster3d6_2500.txt" u 1:2:3 title ' ' w points pointtype 10, \
 "cluster3d6_3000.txt" u 1:2:3 title ' ' w points pointtype 10

set out "cent_plot_3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d6_500.txt" u 1:2:3 title 'centroids' w points, \
"cluster3d6_1000.txt" u 1:2:3 title ' ' w points,\
 "cluster3d6_1500.txt" u 1:2:3 title ' ' w points,\
 "cluster3d6_2000.txt" u 1:2:3 title ' ' w points, \
 "cluster3d6_2500.txt" u 1:2:3 title ' ' w points,\
 "cluster3d6_3000.txt" u 1:2:3 title ' ' w points

set out "plotter2_3d.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [0:3500]
set yrange [0:500]
plot "stat_plot3d.txt" u 1:2 title 'Convergence' w p

set out "datapoints3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "datapoints3d3000x.txt" u 1:2:3 title 'datapoints' w points

