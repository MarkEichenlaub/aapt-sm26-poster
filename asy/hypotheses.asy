// Galileo vs Impetus hypotheses sketch (own artwork for poster card)
// shading = density; arrows = predicted acceleration
unitsize(1cm);
pen navy = rgb(0.106,0.212,0.365);

real r = 0.34;
pen lo = gray(0.92);   // low density
pen mid = gray(0.62);
pen hi = gray(0.25);   // high density

// --- Galileo panel: equal arrows for all ---
label("\textbf{Galileo}", (1.5,1.5), navy);
pair[] gx = {(0.4,0.3), (1.5,0.3), (2.6,0.3)};
pen[] fills = {lo, mid, hi};
for (int i = 0; i < 3; ++i) {
  filldraw(circle(gx[i], r), fills[i], navy);
  draw(gx[i]+(0,-r-0.12) -- gx[i]+(0,-r-0.95), navy+linewidth(1.4pt), arrow=Arrow(6));
}

// --- Impetus panel: arrow scales with density; lightest floats up ---
real dx = 4.6;
label("\textbf{Impetus}", (1.5+dx,1.5), navy);
pair[] ix = {(0.4+dx,0.3), (1.5+dx,0.3), (2.6+dx,0.3)};
real[] len = {0.45, 0.75, 1.25};   // lightest, middle, densest
// lightest: accelerates upward
filldraw(circle(ix[0], r), lo, navy);
draw(ix[0]+(0,r+0.12) -- ix[0]+(0,r+0.55), navy+linewidth(1.4pt), arrow=Arrow(6));
// middle and dense: downward, scaled
for (int i = 1; i < 3; ++i) {
  filldraw(circle(ix[i], r), fills[i], navy);
  draw(ix[i]+(0,-r-0.12) -- ix[i]+(0,-r-0.12-len[i]), navy+linewidth(1.4pt), arrow=Arrow(6));
}
