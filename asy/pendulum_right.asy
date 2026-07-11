// Right panel: same ceiling and arc; pendulum descended toward vertical
// (still right of vertical); small brown peg on the vertical below the pivot.
unitsize(2.4cm);

pair A = (0,0);
real theta = 40;
real phi = 16;
pair bob = (Sin(phi),-Cos(phi));
pair E = (0,-0.53);

// ceiling
draw((-0.78,0)--(0.78,0), linewidth(1.6pt));

// swing arc
draw(arc(A,1,-90-theta,-90+theta), dotted+linewidth(1.5pt));

// string
draw(A--bob, linewidth(0.9pt));

// bob
filldraw(circle(bob,0.065), gray(0.6), black+linewidth(0.7pt));

// peg: small brown circle, labeled away from the string
pen brown = rgb(0.55,0.33,0.13);
filldraw(circle(E,0.042), brown, rgb(0.35,0.2,0.08)+linewidth(0.7pt));
label("peg", E + (-0.06,0), W);

dot(A);

// invisible frame so both panels share identical bounds
draw((-1.12,0.22)--(1.12,0.22), invisible);
draw((-1.12,-1.15)--(1.12,-1.15), invisible);
