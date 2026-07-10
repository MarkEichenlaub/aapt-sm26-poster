// Simple Newton's cradle illustration (own artwork for poster card)
unitsize(1cm);
real r = 0.45;
pen frame = rgb(0.106,0.212,0.365)+linewidth(1.6pt);
pen ballpen = gray(0.85);
pen strng = gray(0.45)+linewidth(0.7pt);

// frame bar
draw((-3.2,3)--(3.2,3), frame);

// four resting balls
for (int i = 0; i < 4; ++i) {
  real x = -0.9 + i*0.9;
  draw((x,3)--(x,0.45), strng);
  filldraw(circle((x,0), r), ballpen, rgb(0.106,0.212,0.365)+linewidth(1pt));
}

// incoming ball, lifted to the left
real ang = 50;
pair pivot = (-1.8,3);
pair bob = pivot + 2.55*dir(270-ang);
draw(pivot--bob, strng);
filldraw(circle(bob, r), rgb(0.773,0.863,0.435), rgb(0.106,0.212,0.365)+linewidth(1pt));
draw(arc(pivot, 1.6, 270-ang, 270), dashed+gray(0.5), arrow=Arrow(5));
