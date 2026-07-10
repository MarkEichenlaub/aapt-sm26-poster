"""Extract hints + core motor config for specific problems."""
import json, re

PATH = r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\problems.jsonl"
PIDS = {44236: "road", 44107: "falcon", 41523: "pendulum", 43753: "fountain",
        43754: "fountain_algebra", 52702: "obscura", 38870: "len_area_vol",
        53232: "interference", 53267: "noise_cancel"}

with open(PATH, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        if r["problem_id"] not in PIDS:
            continue
        name = PIDS[r["problem_id"]]
        print(f"########## {name}  pid={r['problem_id']} {r['course']} L{r['lesson']} #{r['order']} "
              f"type={r['problem_type']}/{r['answer_type']}")
        print("ANSWER:", r["answer"])
        h = r["hints"] or ""
        print("HINTS:", h.strip() if h.strip() else "(none)")
        # pull motor json problemText and options, skipping problem_text_fmt
        try:
            arr = json.loads(r["problem_text"])
            for m in arr:
                if isinstance(m, dict) and "motor_json" in m:
                    mj = json.loads(m["motor_json"])
                    mj.pop("problem_text_fmt", None)
                    print("MOTOR_TYPE:", m.get("motor_type"))
                    print("MOTOR:", json.dumps(mj, ensure_ascii=False)[:2500])
        except Exception as e:
            print("PROBLEM_TEXT (raw):", re.sub(r"\s+", " ", str(r["problem_text"]))[:1200])
        print()
