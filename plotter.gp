set term post eps
set out "plotter.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster1_3000.txt" u 1:2 title 'cluster1' w points lc rgb "green", "cluster2_3000.txt" u 1:2 w points lc rgb "red", "cluster3_3000.txt" u 1:2 w points lc rgb "purple", "cluster4_3000.txt" u 1:2 w points lc rgb "blue", "cluster5_3000.txt" u 1:2 w points lc rgb "orange", "cluster6_500.txt" u 1:2 w points pointtype 10 lc "purple", "cluster6_1000.txt" u 1:2 w points pointtype 10, "cluster6_1500.txt" u 1:2 w points pointtype 10, "cluster6_2000.txt" u 1:2 w points pointtype 10, "cluster6_2500.txt" u 1:2 w points pointtype 10, "cluster6_3000.txt" u 1:2 w points pointtype 10

