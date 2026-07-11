import json

d = json.load(open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\fountain_widget.json", encoding="utf-8"))
links = "\n".join('<link rel="stylesheet" href="%s">' % s for s in d["sheets"])
html = """<!DOCTYPE html><html><head><meta charset="utf-8">
<base href="https://artofproblemsolving.com/">
%s
<style>%s</style>
<style>body { background: #fff; margin: 16px; }</style>
</head><body>%s</body></html>""" % (links, d["styles"], d["html"])
open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\captures\fountain_render.html", "w", encoding="utf-8").write(html)
print("written", len(html))
