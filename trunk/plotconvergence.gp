set term post eps color
set out "plotconvtime.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [0:1100000]
set yrange [0:420]
plot "stat_plot.txt" u 1:2 title '2d Hadoop' smooth bezier w l, \
        "stat_plot3d.txt" u 1:2 title '3d Hadoop' smooth csplines w l, \
        "stat_plotsimp.txt" u 1:2 title '2d simple'  smooth bezier w l, \
        "stat_plot3dsimp.txt" u 1:2 title '3d simple' smooth csplines w l, \
        "stat_plotm2.txt" u 1:2 title '2d map2' smooth bezier w l, \
        "stat_plot.txt" u 1:2 notitle w p , \
        "stat_plot3d.txt" u 1:2 notitle w p, \
        "stat_plotsimp.txt" u 1:2 notitle  w p, \
        "stat_plotm2.txt" u 1:2 notitle w p , \
        "stat_plot3dsimp.txt" u 1:2 notitle  w p

