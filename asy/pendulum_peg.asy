size(6cm);

pair A = (0,0);
dot(A);
label("$A$",A,N);

real theta = 40;
pair C = (Sin(theta),-Cos(theta));
pair B = (0,-1);
pair D = (-C.x,C.y);

dot(C);
label("$C$",C,E);

dot(D);
label("$D$",D,W);

dot(B);
label("$B$",B,S);

draw(A--C);
draw(arc(A,1,-90+theta,-90-theta),dotted);

pair F = (0,-.8);

pair Ea = (0,-.53);
dot(Ea);
label("$E$",Ea,E);
