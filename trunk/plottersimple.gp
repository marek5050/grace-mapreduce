set term post eps color
set out "plottersimp.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster1_simp_12000.txt" u 1:2 lt 9 notitle  w points, \
"cluster2_simp_12000.txt" u 1:2  lt 2 notitle  w points, \
"cluster3_simp_12000.txt" u 1:2 lt 4 notitle  w points, \
"cluster4_simp_12000.txt" u 1:2 lt 3 notitle  w points, \
"cluster5_simp_12000.txt" u 1:2 lt 5 notitle  w points, \
"cluster6_simp_6000.txt" u 1:2 title 'centroids' w points pointtype 10,\
 "cluster6_simp_9000.txt" u 1:2 notitle  w points pointtype 10, \
 "cluster6_simp_12000.txt" u 1:2 notitle  w points pointtype 10

set out "cent_plotsimp.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster6_simp_6000.txt" u 1:2 title 'centroids' w points, \
"cluster6_simp_9000.txt" u 1:2 notitle  w points,\
 "cluster6_simp_12000.txt" u 1:2 notitle  w points

set out "plotter2simp.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [0:3]
plot "stat_plotsimp.txt" u 1:2 title 'Convergence' w p

set out "plotter_3dsimp.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set ylabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d1_simp_12000.txt" u 1:2:3 lt 9 notitle  w points, \
"cluster3d2_simp_12000.txt" u 1:2:3  lt 2 notitle  w points, \
"cluster3d3_simp_12000.txt" u 1:2:3 lt 4 notitle  w points, \
"cluster3d4_simp_12000.txt" u 1:2:3 lt 3 notitle  w points, \
"cluster3d5_simp_12000.txt" u 1:2:3 lt 5 notitle  w points, \
"cluster3d6_simp_6000.txt" u 1:2:3 title 'centroids' w points pointtype 10,\
 "cluster3d6_simp_9000.txt" u 1:2:3 notitle  w points pointtype 10, \
 "cluster3d6_simp_12000.txt" u 1:2:3 notitle  w points pointtype 10

set out "cent_plot_3dsimp.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set zlabel "z coordinate"
set xrange [0:900]
set yrange [0:900]
set zrange [0:900]
splot "cluster3d6_simp_6000.txt" u 1:2:3 title 'centroids' w points, \
"cluster3d6_simp_9000.txt" u 1:2:3 title ' ' w points,\
 "cluster3d6_simp_12000.txt" u 1:2:3 title ' ' w points

set out "plotter2_3dsimp.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [5000:13000]
set yrange [0:2]
plot "stat_plot3dsimp.txt" u 1:2 title 'Convergence' w p

