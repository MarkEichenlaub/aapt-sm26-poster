import json, re

with open(r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\problems.jsonl", encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        t = str(r["problem_text"])
        m = re.search(r'"motor_type":"(\w+)"', t)
        if not m:
            continue
        mt = m.group(1)
        if mt in ("SelectGraph", "DynamicGraph", "ColumnConnection", "DragDropMathjax"):
            snip = re.sub(r"\s+", " ", t)
            i = snip.find("problemText")
            print(f"{mt}: {r['course']} L{r['lesson']} #{r['order']} pid={r['problem_id']} :: {snip[i+16:i+150]}")
