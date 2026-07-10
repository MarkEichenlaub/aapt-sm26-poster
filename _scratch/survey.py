"""Survey problems from the JSONL dump."""
import json, sys, re

PATH = r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\problems.jsonl"

def load():
    with open(PATH, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def snippet(text, n=300):
    if not text:
        return ""
    t = re.sub(r"\s+", " ", str(text))
    return t[:n]

recs = load()
mode = sys.argv[1]

if mode == "list":
    course = sys.argv[2]
    lessons = [int(x) for x in sys.argv[3].split(",")]
    for r in recs:
        if r["course"] == course and int(r["lesson"]) in lessons:
            has_hints = bool(r["hints"] and str(r["hints"]).strip() and str(r["hints"]).strip() != "[]")
            print(f"--- {r['course']} L{r['lesson']} #{r['order']} pid={r['problem_id']} "
                  f"type={r['problem_type']} ans_type={r['answer_type']} hints={'Y' if has_hints else 'n'}")
            print("   ", snippet(r["problem_text"]))
elif mode == "grep":
    pat = re.compile(sys.argv[2], re.I)
    for r in recs:
        if pat.search(str(r["problem_text"]) or ""):
            print(f"--- {r['course']} L{r['lesson']} #{r['order']} pid={r['problem_id']} type={r['problem_type']} ans_type={r['answer_type']}")
            print("   ", snippet(r["problem_text"], 200))
elif mode == "full":
    pid = int(sys.argv[2])
    for r in recs:
        if r["problem_id"] == pid:
            print(json.dumps(r, indent=1, ensure_ascii=False))
