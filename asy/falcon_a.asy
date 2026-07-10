unitsize(2cm);
import graph;
real tau = 1;
real a(real t){ return 1/tau*(1/cosh(t))^2; }
draw((0,1.1)--(0,0)--(2,0));
draw(graph(a, 0, 2), blue+linewidth(0.8pt));
label("$t$",(2,0),S);
