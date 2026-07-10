unitsize(2cm);
import graph;
real tau = 1;
real y(real t){ return tau*(2-log(cosh(t/tau)))/2; }
draw((0,1.1)--(0,0)--(2,0));
draw(graph(y, 0, 2), blue+linewidth(0.8pt));
label("$t$",(2,0),S);
