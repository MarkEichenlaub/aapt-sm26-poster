// String-around-the-Earth puzzle illustration (own artwork for poster card)
unitsize(1cm);
pen navy = rgb(0.106,0.212,0.365);

// Earth
filldraw(circle((0,0), 2.1), rgb(0.88,0.92,0.96), navy+linewidth(1.4pt));
label("Earth", (0,0), navy);

// snug string (on the surface): drawn as the circle outline itself (already navy)
// longer string, uniform height above the ground
draw(circle((0,0), 2.75), rgb(0.38,0.68,0)+linewidth(1.8pt)+linetype(new real[] {6,5}));

// height arrows
draw((2.1,0)--(2.75,0), navy+linewidth(1.1pt), Arrows(5));
label("$h$?", (2.425,0), N, navy);

label("string $6$ m longer", (0,-2.75), S, rgb(0.29,0.52,0));
