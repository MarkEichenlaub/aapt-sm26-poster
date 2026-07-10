unitsize(2cm);
import graph;
real tau = 1;
real v(real t){ return tanh(t/tau); }
draw((0,1.1)--(0,0)--(2,0));
draw(graph(v, 0, 2), blue+linewidth(0.8pt));
label("$t$",(2,0),S);
