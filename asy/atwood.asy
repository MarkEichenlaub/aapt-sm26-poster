unitsize(1cm);

  filldraw(unitcircle, lightgray);
  dot((0,0));

  draw((-1,-5)--(-1,0)--arc((0,0),1,180,0)--(1,0)--(1,-1), linewidth(2pt));

  filldraw(box((1.5,-2),(.5,-1)), lightgray);
  label("$H$",(1,-1.5));
  filldraw(box((-1.5,-6),(-.5,-5)), lightgray);
  label("$L$",(-1,-5.5));
  draw((-2,-6)--(2,-6));
label("start heavier box at top",(0,-6.5),S);


  filldraw(shift(6,0)*unitcircle, lightgray);
  dot((6,0));

  draw((5,-3)--(5,0)--arc((6,0),1,180,0)--(7,0)--(7,-3), linewidth(2pt));

  filldraw(box((7.5,-4),(6.5,-3)), lightgray);
  label("$H$",(7,-3.5));
  filldraw(box((4.5,-4),(5.5,-3)), lightgray);
  label("$L$",(5,-3.5));
  draw((4,-6)--(8,-6));
label("start heavier box half way",(6,-6.5),S);
