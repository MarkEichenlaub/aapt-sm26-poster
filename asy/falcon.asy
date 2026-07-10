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

draw(axes);
draw(graph(a, 0, 2), blue);
label("(A)",(1,-.1),S);
label("$t$",(2,0),S);

real dy = -0;
real dx = 3;

draw(shift(dx,dy)*axes);
draw(shift(dx,dy)*graph(v,0,2), blue);
label("(B)",(1+dx,-.1+dy),S);
label("$t$",(2+dx,dy),S);

real dy = -0;
dx = 6;

draw(shift(dx,dy)*axes);
draw(shift(dx,dy)*graph(y,0,2), blue);
label("(C)",(1+dx,-.1+dy),S);
label("$t$",(2+dx,dy),S);
