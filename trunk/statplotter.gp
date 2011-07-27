set term post eps
set out "plotter2.ps"
set xlabel "Number of Datapoints"
set ylabel "Time to Converge (seconds)"
set xrange [0:3500]
set yrange [0:500]
plot "stat_plot.txt" u 1:2 w lines

