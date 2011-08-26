set term post eps color
set out "plotterthird.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster1_third_12000.txt" u 1:2 lt 9 title 'cluster1' w points, \
"cluster2_third_12000.txt" u 1:2  lt 2 title 'cluster2' w points, \
"cluster3_third_12000.txt" u 1:2 lt 4 title 'cluster3' w points, \
"cluster4_third_12000.txt" u 1:2 lt 3 title 'cluster4' w points, \
"cluster5_third_12000.txt" u 1:2 lt 5 title 'cluster5' w points, \
"cluster6_third_6000.txt" u 1:2 title 'centroids' w points pointtype 10,\
 "cluster6_third_9000.txt" u 1:2 title ' ' w points pointtype 10, \
 "cluster6_third_12000.txt" u 1:2 title ' ' w points pointtype 10

set out "cent_plotthird.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster6_third_6000.txt" u 1:2 title 'centroids' w points, \
"cluster6_third_9000.txt" u 1:2 title ' ' w points,\
 "cluster6_third_12000.txt" u 1:2 title ' ' w points

set out "plotter2third.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [40:60]
plot "stat_plotthird.txt" u 1:2 title 'Convergence' w p

set out "plotter_3dthird.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set ylabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d1_third_12000.txt" u 1:2:3 lt 9 title 'cluster1' w points, \
"cluster3d2_third_12000.txt" u 1:2:3  lt 2 title 'cluster2' w points, \
"cluster3d3_third_12000.txt" u 1:2:3 lt 4 title 'cluster3' w points, \
"cluster3d4_third_12000.txt" u 1:2:3 lt 3 title 'cluster4' w points, \
"cluster3d5_third_12000.txt" u 1:2:3 lt 5 title 'cluster5' w points, \
"cluster3d6_third_6000.txt" u 1:2:3 title 'centroids' w points pointtype 10,\
 "cluster3d6_third_9000.txt" u 1:2:3 title ' ' w points pointtype 10, \
 "cluster3d6_third_12000.txt" u 1:2:3 title ' ' w points pointtype 10


set out "cent_plot_3dthird.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d6_third_6000.txt" u 1:2:3 title 'centroids' w points, \
"cluster3d6_third_9000.txt" u 1:2:3 title ' ' w points,\
 "cluster3d6_third_12000.txt" u 1:2:3 title ' ' w points

set out "plotter2_3dthird.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [40:60]
plot "stat_plot3dthird.txt" u 1:2 title 'Convergence' w p

