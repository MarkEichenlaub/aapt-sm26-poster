css = open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\widget_styles.css", encoding="utf-8").read()

IMG = ("https://cdn.artofproblemsolving.com/school/crypt/"
       "00540-e12599cedadfdc40445dca22ddd227e6417975d2/files/"
       "05_script_05_script_click_on_coin_image.png")

html = """<!DOCTYPE html><html><head><meta charset="utf-8">
<style>%s</style>
<style>
body { background: #fff; margin: 20px; font-family: Roboto, "Segoe UI", sans-serif; }
p.prompt { font-size: 15px; color: #333; margin: 0 0 8px; }
.wrap { width: 300px; }
svg.motor { width: 100%%; display: block; }
</style></head><body>
<div class="wrap">
<p class="prompt">Click on the image of the coin.</p>
<svg class="motor SVGGraph-module_main__3zFw3 SVGGraph-module_cartesian__eWk2n" viewBox="-6 -4.7 12.24 9.16"
  style="background-image: url(%s); background-repeat: no-repeat; background-position: 0%% 100%%; background-size: 98.039%% 97.380%%;">
<g class="SVGGraph-module_container__2wwDJ">
<circle class="view-module_latt__2Dpsa view-module_selectable__2PhOB view-module_isSelected__3_wXc" cx="2.9" cy="-2.32" r="0.2" fill="rgb(142, 204, 210)" stroke-width="0.1"/>
</g></svg></div></body></html>""" % (css, IMG)

open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\coin_render.html", "w", encoding="utf-8").write(html)
print("written", len(html))
