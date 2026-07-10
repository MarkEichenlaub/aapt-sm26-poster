// Accelerating car with helium balloon (tied to floor) and air-filled balloon
// (hanging from ceiling) — own artwork for poster card
unitsize(1cm);
pen navy = rgb(0.106,0.212,0.365);
pen carpen = navy+linewidth(1.6pt);

// car body (side view, front at right)
draw((-4,0)--(4,0), carpen);              // floor
draw((-4,3)--(4,3), carpen);              // ceiling
draw((-4,0)--(-4,3), carpen);             // back wall
draw((4,0)--(4,3), carpen);               // front wall
filldraw(circle((-2.6,-0.45),0.45), gray(0.3), navy);
filldraw(circle((2.6,-0.45),0.45), gray(0.3), navy);

// acceleration arrow
draw((4.6,1.5)--(6.1,1.5), navy+linewidth(2pt), arrow=Arrow(8));
label("$\vec{a}$", (5.35,1.5), N, navy);

// helium balloon tied to floor, leaning FORWARD (toward front)
pair anchor1 = (-2.2,0);
pair bal1 = anchor1 + 2.1*dir(72);   // leans toward +x
draw(anchor1--bal1, gray(0.45));
filldraw(shift(bal1)*rotate(-18)*scale(0.55,0.7)*unitcircle, rgb(0.98,0.62,0.15), navy);
label("He", bal1, navy);

// air-filled balloon hanging from ceiling, leaning BACKWARD
pair anchor2 = (1.8,3);
pair bal2 = anchor2 + 1.9*dir(255);  // hangs, leans toward -x
draw(anchor2--bal2, gray(0.45));
filldraw(shift(bal2)*rotate(15)*scale(0.55,0.7)*unitcircle, rgb(0.94,0.87,0.28), navy);
label("air", bal2, navy);
