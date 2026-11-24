# Diagram tooling

The PNGs in `../assets/` are generated from `../CSW-SOX-Reference-Design.md` by this directory.

```bash
python3 .diagram-tools/build.py
```

Needs Python 3.10+, [Pillow](https://pypi.org/project/pillow/), and Google Chrome
(used headless to rasterise the HTML).

## Why the content is trustworthy

`extract.py` and `tree.py` read the phase table, the phase checklists, the
evidence-boundary paragraph, and the scope tree **out of the design document**.
Only the framing text in `spec.py` — the title, the takeaway, and the three
side notes — is written by hand. A diagram therefore cannot state something the
document does not say. Edit the document and re-run to change a diagram.

## Files

| File | Purpose |
|---|---|
| `build.py` | Entry point; writes the PNGs into `../assets/` |
| `spec.py` | This framework's framing text |
| `extract.py` | Pulls workflow phases and checklists out of the markdown |
| `tree.py` | Finds and renders the scope-architecture tree |
| `diagrams.py` | Layout for the evidence-workflow graphic |
| `theme.py` | Cisco palette and shared CSS |
| `render.py` | Headless-Chrome rasteriser and 2x downsample |
