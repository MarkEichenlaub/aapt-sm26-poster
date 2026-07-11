"""Trim and place motor captures into assets/img/."""
from PIL import Image, ImageChops
import os

CAP = r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures"
OUT = r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\assets\img"

def trim(im, pad=14):
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im.convert("RGB"), bg.convert("RGB"))
    bbox = diff.getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - pad); y0 = max(0, y0 - pad)
    x1 = min(im.width, x1 + pad); y1 = min(im.height, y1 + pad)
    return im.crop((x0, y0, x1, y1))

jobs = [
    ("pendulum_motor_test.png", "motor_click_image.png"),
    ("column_connect.png", "motor_column_connect.png"),
    ("dragdrop_mathjax.png", "motor_dragdrop_eq.png"),
    ("fountain_full.png", "motor_slider_graph.png"),
]
for src, dst in jobs:
    im = Image.open(os.path.join(CAP, src)).convert("RGB")
    t = trim(im)
    t.save(os.path.join(OUT, dst))
    print(dst, t.size)
