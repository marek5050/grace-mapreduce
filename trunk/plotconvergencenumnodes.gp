set term post eps color
set out "plotconvnodes.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [0:510000]
set yrange [0:270]
plot "stat_plotm2_1n.txt" u 1:2 title '1node' smooth bezier w l, \
         "stat_plotm2_2n.txt" u 1:2 title '2nodes'  smooth bezier w l, \
                "stat_plotm2_3n.txt" u 1:2 title '3nodes' smooth bezier w l, \
                "stat_plotm2_4n.txt" u 1:2 title '4nodes'  smooth bezier w l, \
                "stat_plotm2_1n.txt" u 1:2 notitle w p , \
                "stat_plotm2_2n.txt" u 1:2 notitle  w p, \
        "stat_plotm2_3n.txt" u 1:2 notitle w p , \
               "stat_plotm2_4n.txt" u 1:2 notitle w p


set out "plotconvnodes3d.ps"
set xlabel "Number of Data points"
set ylabel "Time to Converge (seconds)"
set xrange [0:510000]
set yrange [0:270]
plot      "stat_plot3d_1n.txt" u 1:2 title '3d 1node' smooth csplines w l, \
                "stat_plot3d_2n.txt" u 1:2 title '3d 2nodes' smooth csplines w l, \
                "stat_plot3d_3n.txt" u 1:2 title '3d 3nodes' smooth csplines w l, \
               "stat_plot3d_4n.txt" u 1:2 title '3d 4nodes' smooth csplines w l, \
               "stat_plot3d_1n.txt" u 1:2 notitle w p, \
               "stat_plot3d_2n.txt" u 1:2 notitle  w p,\
               "stat_plot3d_3n.txt" u 1:2 notitle  w p,\
        "stat_plot3d_4n.txt" u 1:2 notitle  w p

