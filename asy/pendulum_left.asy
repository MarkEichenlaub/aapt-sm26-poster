// Left panel: pendulum at release, bob right of vertical at the C position.
// No lettered points. Labels: "bob" and "pivot" only.
unitsize(2.4cm);

pair A = (0,0);
real theta = 40;
pair C = (Sin(theta),-Cos(theta));

// ceiling
draw((-0.78,0)--(0.78,0), linewidth(1.6pt));

// swing arc
draw(arc(A,1,-90-theta,-90+theta), dotted);

// string
draw(A--C, linewidth(0.9pt));

// bob: small gray circle, larger than a dot
filldraw(circle(C,0.065), gray(0.6), black+linewidth(0.7pt));
label("bob", C + 0.065*dir(-35), dir(-35));

dot(A);
label("pivot", A, N);

// invisible frame so both panels share identical bounds
draw((-1.12,0.22)--(1.12,0.22), invisible);
draw((-1.12,-1.15)--(1.12,-1.15), invisible);
