import json

d = json.load(open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\dragdrop_widget.json", encoding="utf-8"))
css = open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\mathjax_styles.css", encoding="utf-8").read()
links = "\n".join('<link rel="stylesheet" href="%s">' % s for s in d["sheets"])
html = """<!DOCTYPE html><html><head><meta charset="utf-8">
<base href="https://artofproblemsolving.com/">
%s
<style>%s</style>
<style>body { background: #fff; margin: 24px; }</style>
</head><body>%s</body></html>""" % (links, css, d["html"])
open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\dragdrop_render.html", "w", encoding="utf-8").write(html)
print("written", len(html))
