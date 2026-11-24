"""Regenerate this repo's diagrams from the design document.

    python3 .diagram-tools/build.py

Requires Python 3.10+, Pillow, and Google Chrome. Every number and bullet in the
output is read out of the design markdown, so editing the document and re-running
is the way to change a diagram.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import diagrams
import render
import tree as treemod
from extract import phase_timeline_spec, workflow_spec
from spec import DESIGN, PHASES, TREE, WORKFLOW
from theme import base_css

REPO = HERE.parent
MD = REPO / DESIGN
ASSETS = REPO / "assets"
ASSETS.mkdir(exist_ok=True)
W = 1600


def build_tree() -> None:
    block = treemod.find_scope_tree(MD.read_text())
    if not block:
        print("  scope architecture: no scope tree found in the design")
        return
    nodes = treemod.parse_tree(block)
    spec = dict(TREE, nodes=nodes, cols=1)
    h = int(treemod.HEAD_H + treemod.layout_height(nodes, 1) + treemod.FOOT_H)
    out = ASSETS / "csw-scope-architecture.png"
    render.render(render.page(treemod.scope_tree(spec), base_css(), W, h), out, W, h)
    print(f"  {out.name}  {W}x{h}  {out.stat().st_size // 1024} KB")


def build_workflow() -> None:
    spec = workflow_spec(MD, **WORKFLOW)
    rows = max(len(p["actions"]) for p in spec["phases"])
    h = int(96 + 22 + (300 + rows * 26) + 16 + 58 + 92)
    out = ASSETS / "csw-evidence-workflow.png"
    render.render(render.page(diagrams.evidence_workflow(spec), base_css(), W, h), out, W, h)
    print(f"  {out.name}  {W}x{h}  {out.stat().st_size // 1024} KB")


def build_phases() -> None:
    """For designs laid out as numbered project phases rather than the house
    four-phase evidence table."""
    spec = phase_timeline_spec(MD, **PHASES)
    for ph in spec["phases"]:
        ph["export"] = ""
    w, card_h = spec["width"], spec["card_h"]
    h = int(96 + 22 + card_h + 16 + 58 + 92)
    out = ASSETS / "csw-delivery-phases.png"
    render.render(render.page(diagrams.evidence_workflow(spec), base_css(), w, h), out, w, h)
    print(f"  {out.name}  {w}x{h}  {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    print(f"{MD.name}:")
    if TREE:
        build_tree()
    if WORKFLOW:
        build_workflow()
    if PHASES:
        build_phases()
