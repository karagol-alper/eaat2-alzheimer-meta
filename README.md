# EAAT2 / SLC1A2 in Alzheimer's disease — analysis and document code

Code accompanying *"Transporter abundance is preserved while transport fails:
re-examining EAAT2/SLC1A2 in the Alzheimer brain through the lens of estimand specification."*

Alper Karagöl ([0009-0001-7864-0732](https://orcid.org/0009-0001-7864-0732)) and
Taner Karagöl ([0009-0005-1011-7661](https://orcid.org/0009-0005-1011-7661))
Istanbul University Istanbul Medical Faculty, Istanbul, Turkey

## Contents

| File | Purpose |
|---|---|
| `EAAT2_analysis_S1_to_S13.py` | All statistics. Contains the extraction matrix and regenerates every number in the main text and supplement. |
| `make_figures.py` | Regenerates Figures 1–4 and Supplementary Figure S1 into `figs/`. |
| `manuscript.md` | Manuscript source. |
| `supplementary.md` | Supplementary Material source (Sections S1–S13, Tables S1–S12, Figure S1). |
| `peer_review.md` | Internal pre-submission review (two-reviewer format) and point-by-point response. Not a journal peer review. |
| `requirements.txt` | Python dependencies. |
| `CITATION.cff` | Citation metadata. |
| `build_documents.sh` | Rebuilds everything end to end. |

`manuscript.md` and `supplementary.md` are the single source of truth. The PDF is
rendered from the `.docx`, so the two renderings cannot drift apart.

## Requirements

Python 3 with `numpy`, `scipy`, `matplotlib`; `pandoc` for the Word files and
LibreOffice (`soffice`) to render the PDF.

    pip install -r requirements.txt

## Reproducing everything

    ./build_documents.sh

Or individually:

    python3 make_figures.py                # -> figs/
    python3 EAAT2_analysis_S1_to_S13.py    # -> all statistics to stdout
    pandoc manuscript.md -o manuscript.docx --standalone --toc

## Analyses included

**S1–S2** extraction matrix and reference verification.
**S3** leave-one-out sensitivity of the implied effect size (d = 0.72–0.99).
**S4** moderator robustness under six alternative preparation codings.
**S5** conditional exact CI for the moderator odds ratio (zero cell).
**S6** Monte Carlo calibration of the compositional model (400,000 draws).
**S7** denominator bias from neuronal loss.
**S8** vote-counting failure simulation and publication-bias stress test.
**S9** sample size for the proposed IPD design.
**S11** publication-bias adjustment of the implied effect size (d = 0.83 is an upper bound).
**S12** power of the two largest studies re-benchmarked against plausible abundance effects.
**S13** preparation moderator under direction-specific coding (p = 1.00; claim withdrawn).

Sections S11–S13 were added after internal pre-submission review (`peer_review.md`).
All three returned results unfavourable to claims made in the earlier draft, and
the manuscript was changed rather than the analyses. The manuscript and
supplementary text state their conclusions directly and do not narrate this
history; `peer_review.md` is where it is recorded.

## Notes on the data

No primary data were generated. All inputs are summary-level values extracted
from published reports; provenance for each is in the extraction matrix. Two
errors in the source literature (an author-name misspelling and an author-order
error, both in the reference list of Wood et al. 2022) were identified and
corrected against publisher records — see Supplementary Section S2.

Random seeds are fixed, so all reported values reproduce exactly.

Generated figures in `figs/` are tracked so that the documents build without
first running `make_figures.py`. Build outputs (`.docx`, `.pdf`) are not tracked;
see `.gitignore`.

## Key reported values

Running `EAAT2_analysis_S1_to_S13.py` should reproduce, among others:

| Quantity | Value |
|---|---|
| Implied true effect size (no publication bias) | d = 0.83 |
| Implied effect under moderate bias (*w* = 0.5) | d = 0.60 |
| Leave-one-out range | 0.72–0.99 |
| Preparation moderator, any-abnormality coding | p = 0.0476 |
| Preparation moderator, direction-specific coding | p = 1.0000 |
| Region moderator | p = 0.5921 |
| Compositional model, consistent prior fraction | 6.9% |

