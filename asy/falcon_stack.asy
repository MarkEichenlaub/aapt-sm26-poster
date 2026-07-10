// Falcon-dive plots stacked vertically, workbook style, no letter labels
// (top to bottom: |acceleration|, speed, height — so the matching lines cross)
unitsize(2cm);

import graph;

real tau = 1;
real v_term = 1;

real v(real t){
return v_term*tanh(t/tau);
}

real y(real t){
return tau*v_term*(2-log(cosh(t/tau)))/2;
}

real a(real t){
return v_term/tau* (1/cosh(t))^2;
}

path axes = (0,1.1)--(0,0)--(2,0);

real dy = 0;
draw(shift(0,dy)*axes);
draw(shift(0,dy)*graph(a, 0, 2), blue+linewidth(0.8pt));
label("$t$",(2,dy),S);

dy = -1.8;
draw(shift(0,dy)*axes);
draw(shift(0,dy)*graph(v,0,2), blue+linewidth(0.8pt));
label("$t$",(2,dy),S);

dy = -3.6;
draw(shift(0,dy)*axes);
draw(shift(0,dy)*graph(y,0,2), blue+linewidth(0.8pt));
label("$t$",(2,dy),S);
