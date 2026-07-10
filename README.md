# Auto-Graded Homework that Invites Students to Think Broadly

Poster for the **AAPT Summer Meeting 2026** (Pasadena, CA).

**Mark Eichenlaub · Art of Problem Solving**

- **Site:** https://markeichenlaub.github.io/aapt-sm26-poster/
- **Poster PDF (48″ × 36″):** [poster.pdf](poster.pdf)
- **Live interactive demos:** [try/](https://markeichenlaub.github.io/aapt-sm26-poster/try/)
- **Abstract:** https://planion.events/e/aapt/sm26/abstracts/51445/

## Contents

- `poster.html` — poster source (HTML/CSS + KaTeX), printed to PDF at 48in × 36in via headless Chrome
- `poster.pdf` — print-ready poster (fits AAPT's 4′ × 4′ poster boards)
- `try/` — self-contained re-implementations of four auto-graded interactives
  (drag-into-categories, column-connect, click-on-image, multi-select)
- `asy/` — Asymptote sources and rendered SVGs for the problem diagrams
- `assets/` — AoPS brand assets, problem images, QR codes

## Rebuilding the PDF

```powershell
chrome --headless=new --no-pdf-header-footer --virtual-time-budget=25000 `
  --print-to-pdf="poster.pdf" "file:///.../poster.html"
```

Problems © Art of Problem Solving, from *Introduction to Physics*, *Physics 1: Mechanics*,
and *Middle School Physics*. Moon photographs: NASA.
