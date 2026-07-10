unitsize(2cm);
dot((0,0),(8+black));
real dx = .06;
draw(shift(0,-dx)*((0,0)--(0,-1)), arrow = Arrow(6), red);
label("$m\vec{g}$",(0,-1-dx),S,red);

draw(shift(0,dx)*((0,0)--(0,.3)), arrow = Arrow(6), red);
label("$\vec{F}_{\rm drag}$", (0,.3+dx),N,red);

label("(A)",(0,-1.5));

real s = 1;
dot((s,0),(8+black));

draw(shift(s,-dx)*((0,0)--(0,-1)), arrow = Arrow(6), red);
label("$m\vec{g}$",(s,-1-dx),S,red);

draw(shift(s,dx)*((0,0)--(0,1)), arrow = Arrow(6), red);
label("$\vec{F}_{\rm drag}$", (s,1+dx),N,red);

label("(B)",(s,-1.5));


real s = 2;
dot((s,0),(8+black));

draw(shift(s,-dx)*((0,0)--(0,-1)), arrow = Arrow(6), red);
label("$m\vec{g}$",(s,-1-dx),S,red);

draw(shift(s,dx)*((0,0)--(0,5)), arrow = Arrow(6), red);
label("$\vec{F}_{\rm drag}$", (s,5+dx),N,red);

label("(C)",(s,-1.5));
