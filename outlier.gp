set term post eps
set out "plote.ps"
plot "cluster1.txt" u 1:2 title 'cluster1' w points lc rgb "green", "cluster2.txt" u 1:2  title 'cluster2' w points lc rgb "red", "cluster3.txt" u 1:2 title 'cluster3' w points lc rgb "purple", "cluster4.txt" u 1:2 title 'cluster4' w points lc rgb "blue", "cluster5.txt" u 1:2 title 'cluster5' w points lc rgb "orange", "cluster6.txt" u 1:2 title 'centroids' w points pointtype 10 lc "purple"
set out "plotb.ps"

plot "cluster1_500a.txt" u 1:2 title 'cluster1' w points lc rgb "green", "cluster2_500a.txt" u 1:2  title 'cluster2' w points lc rgb "red", "cluster3_500a.txt" u 1:2 title 'cluster3' w points lc rgb "purple", "cluster4_500a.txt" u 1:2 title 'cluster4' w points lc rgb "blue", "cluster5_500a.txt" u 1:2 title 'cluster5' w points lc rgb "orange", "cluster6_500a.txt" u 1:2 title 'centroids' w points pointtype 10 lc "purple"

