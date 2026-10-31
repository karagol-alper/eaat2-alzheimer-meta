#!/usr/bin/env bash
# Rebuilds every deliverable from source. Run from this directory.
# manuscript.md and supplementary.md are the single source of truth;
# the PDF is rendered from the .docx so the two can never drift apart.
set -e
echo "[1/4] figures"
python3 make_figures.py
echo "[2/4] statistics (regenerates every reported number)"
python3 EAAT2_analysis_S1_to_S13.py > analysis_output.txt
echo "      -> analysis_output.txt"
echo "[3/4] Word documents"
pandoc manuscript.md    -o EAAT2_Alzheimer_manuscript.docx    --standalone -V papersize=a4
pandoc supplementary.md -o EAAT2_Alzheimer_supplementary.docx --standalone --toc --toc-depth=2 -V papersize=a4
pandoc peer_review.md   -o EAAT2_peer_review_and_response.docx --standalone --toc --toc-depth=2 -V papersize=a4
echo "[4/4] PDF rendering of the manuscript"
soffice --headless --convert-to pdf EAAT2_Alzheimer_manuscript.docx >/dev/null 2>&1
echo "Done."
