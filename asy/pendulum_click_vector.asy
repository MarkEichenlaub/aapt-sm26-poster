// Vector recreation of the click-on-image canvas from I2P12 Problem 2 [41523]
// (pendulum released at C, string catches peg at E, bob mid-swing around peg)
size(9cm);

pair A = (0,0);
real theta = 40;
pair C = (Sin(theta),-Cos(theta));
pair B = (0,-1);
pair D = (-C.x,C.y);
pair E = (0,-.53);
real rEB = 1 - 0.53;
pair bob = E + rEB*dir(241);

// dotted original swing arc from bob's angular position through B up to C
draw(arc(A,1,-104,-90+theta), dotted);

// string: pivot to peg, peg to bob
draw(A--E, linewidth(0.9pt));
draw(E--bob, linewidth(0.9pt));

dot(A);  label("$A$",A,N);
dot(E);  label("$E$",E,E);
dot(C);  label("$C$",C,E);
dot(D);  label("$D$",D,W);
dot(B);  label("$B$",B,S);
dot(bob);
