set term post eps
set out "cent_plot.ps"
set xlabel "x coordinate"
set ylabel "y coordinate"
set xrange [0:900]
set yrange [0:900]
plot "cluster6_500.txt" u 1:2 w points lc rgb "green", "cluster6_1000.txt" u 1:2 w points lc rgb "red" , "cluster6_1500.txt" u 1:2 w points lc rgb "yellow","cluster6_2000.txt" u 1:2 w points lc rgb "blue", "cluster6_2500.txt" u 1:2 w points lc rgb "orange","cluster6_3000.txt"

