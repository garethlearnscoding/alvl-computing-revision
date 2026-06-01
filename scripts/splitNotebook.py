"""
split_notebook.py
-----------------
Splits a compiled question notebook into one notebook per question.

Usage:
  python split_notebook.py <input.ipynb> [output_dir]

  output_dir defaults to the same folder as the input file.

Rules:
  - Each question starts at a cell whose source matches  # N. [SCHOOL/...]
  - Horizontal-rule cells (source == '---') are excluded from output files.
  - Output filenames: <zero-padded-number>_<SCHOOL>_<YEAR>_<EXAM>_<PAPER>_<QNUM>.ipynb
    e.g.  01_YIJC_2025_PRELIM_P2_Q4.ipynb
  - Output directory is created if it does not exist.
"""

import argparse
import copy
import json
import os
import re
import sys

# ── CLI ───────────────────────────────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Split a compiled question notebook into one file per question."
    )
    parser.add_argument("input", help="Path to the source .ipynb file")
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=None,
        help="Directory to write the split notebooks into (default: same folder as input)",
    )
    return parser.parse_args()

args = parse_args()
INPUT_PATH = args.input
OUTPUT_DIR = args.output_dir or os.path.dirname(os.path.abspath(args.input))

# ── Helpers ──────────────────────────────────────────────────────────────────
QUESTION_HEADER_RE = re.compile(r"^# (\d+)\. \[([^\]]+)\]")


def safe_filename(text: str) -> str:
    """Turn bracket content like 'NYJC_TJC_VJC/2025/PRELIM/P2/Q3' into a
    filesystem-safe string by replacing '/' with '_'."""
    return re.sub(r"[^\w\-]", "_", text).strip("_")


def is_horizontal_rule(cell: dict) -> bool:
    """Return True if the cell is a markdown cell whose entire content is '---'."""
    if cell.get("cell_type") != "markdown":
        return False
    src = "".join(cell["source"]).strip()
    return src == "---"


def make_notebook(cells: list, base_nb: dict) -> dict:
    """Wrap a list of cells in a minimal valid nbformat-4 notebook."""
    nb = {
        "nbformat": base_nb["nbformat"],
        "nbformat_minor": base_nb["nbformat_minor"],
        "metadata": copy.deepcopy(base_nb.get("metadata", {})),
        "cells": cells,
    }
    return nb


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    with open(INPUT_PATH, encoding="utf-8") as fh:
        notebook = json.load(fh)

    all_cells = notebook["cells"]
    total = len(all_cells)

    # 1. Locate question-boundary cell indices
    boundaries = []  # [(cell_index, question_number, bracket_text), ...]
    for idx, cell in enumerate(all_cells):
        src = "".join(cell["source"])
        m = QUESTION_HEADER_RE.match(src)
        if m:
            boundaries.append((idx, int(m.group(1)), m.group(2)))

    if not boundaries:
        print("ERROR: No question headers found. Check the input file.")
        sys.exit(1)

    print(f"Found {len(boundaries)} questions in {total} cells.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 2. Slice cells for each question
    written = 0
    for i, (start_idx, q_num, bracket) in enumerate(boundaries):
        # End of this question = start of next question (or end of notebook)
        end_idx = boundaries[i + 1][0] if i + 1 < len(boundaries) else total

        # Grab cells, strip horizontal rules
        question_cells = [
            copy.deepcopy(c)
            for c in all_cells[start_idx:end_idx]
            if not is_horizontal_rule(c)
        ]

        # 3. Build filename
        #    bracket  e.g. "NYJC_TJC_VJC/2025/PRELIM/P2/Q3"
        #    → safe   "NYJC_TJC_VJC_2025_PRELIM_P2_Q3"
        safe = safe_filename(bracket)
        filename = f"{q_num:02d}_{safe}.ipynb"
        filepath = os.path.join(OUTPUT_DIR, filename)

        nb = make_notebook(question_cells, notebook)
        with open(filepath, "w", encoding="utf-8") as out:
            json.dump(nb, out, indent=1, ensure_ascii=False)

        print(f"  [{q_num:02d}] {filename}  ({len(question_cells)} cells)")
        written += 1

    print(f"\nDone. {written} notebooks written to '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    main()