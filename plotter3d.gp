set term post eps color
set out "plotter_3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set ylabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d1_12000.txt" u 1:2:3 lt 9 notitle w points, \
"cluster3d2_12000.txt" u 1:2:3  lt 2 notitle  w points, \
"cluster3d3_12000.txt" u 1:2:3 lt 4 notitle  w points, \
"cluster3d4_12000.txt" u 1:2:3 lt 3 notitle  w points, \
"cluster3d5_12000.txt" u 1:2:3 lt 5 notitle  w points, \
"cluster3d6_6000.txt" u 1:2:3 title 'centroids' w points pointtype 10,\
 "cluster3d6_9000.txt" u 1:2:3 notitle  w points pointtype 10, \
 "cluster3d6_12000.txt" u 1:2:3 notitle  w points pointtype 10

set out "cent_plot_3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d6_6000.txt" u 1:2:3 title 'centroids' w points, \
"cluster3d6_9000.txt" u 1:2:3 notitle  w points,\
 "cluster3d6_12000.txt" u 1:2:3 notitle  w points

set out "plotter2_3d.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [60:75]
plot "stat_plot3d.txt" u 1:2 title 'Convergence' w p

set out "datapoints3d.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "datapoints3d12000x.txt" u 1:2:3 title 'datapoints' w points

