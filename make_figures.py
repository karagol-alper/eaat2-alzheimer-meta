#!/usr/bin/env python3
"""
make_figures.py
===============
Regenerates all five figures for:

  "Transporter abundance is preserved while transport fails: re-examining
   EAAT2/SLC1A2 in the Alzheimer brain through the lens of estimand
   specification"

  Alper Karagöl and Taner Karagöl

Outputs to ./figs/
  fig1_flow.png        Figure 1  - evidence base assembly
  fig2_harvest.png     Figure 2  - harvest plot by tissue preparation
  fig3_power.png       Figure 3  - power reconstruction
  fig4_model.png       Figure 4  - compositional model
  figS1_calibration.png  Supplementary Figure S1 - model calibration

Run:  python3 make_figures.py
Deps: matplotlib, numpy, scipy
"""

import math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scipy import stats

os.makedirs("figs", exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.linewidth": 0.8,
                     "axes.spines.top": False, "axes.spines.right": False})
DOWN, NULL = "#B2182B", "#8C8C8C"
FRAC, HOM, IMG = "#2166AC", "#D6604D", "#4D9221"


# ===================== FIGURE 1 : evidence base =====================
# Only counts documented in the two source reviews are shown. Intermediate
# screening counts are deliberately omitted: the two searches used different,
# partly overlapping inclusion criteria, so a combined PRISMA count would be
# fabricated rather than derived.
def figure1():
    fig, ax = plt.subplots(figsize=(6.0, 6.0)); ax.axis("off")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    def box(x, y, w, h, txt, fc="#F2F2F2"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                                    fc=fc, ec="#333", lw=0.9))
        ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=8)
    def arrow(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=11, lw=0.9, color="#333"))
    box(0.8, 8.4, 8.4, 1.2,
        "Records screened by the two source systematic searches\n"
        "Soares 2024: n = 6,936 screened, 63 studies retained\n"
        "Wood 2022: n = 506 screened, 29 studies retained", "#E8EEF5")
    arrow(5, 8.4, 5, 7.8)
    box(0.8, 6.4, 8.4, 1.4,
        "Human post-mortem studies entering this synthesis (n = 21)\n"
        "Protein or ligand-binding abundance comparisons (n = 10)\n"
        "Fraction-resolved preparations (n = 5)\n"
        "Transcript comparisons (n = 6)   ·   Stage-stratified datasets (n = 4)", "#EAF3EA")
    arrow(5, 6.4, 5, 5.8)
    box(0.8, 4.2, 8.4, 1.6,
        "Transcriptomic reconciliation datasets (n = 5)\n"
        "Lau 2020  ·  Smith 2022  ·  Sadick 2022\n"
        "Dai 2023  ·  SEA-AD / Gabitto 2024\n"
        "(84 to ~1,670 donors; single-nucleus and bulk)", "#EAF3EA")
    arrow(5, 4.2, 5, 3.6)
    box(0.8, 2.0, 8.4, 1.6,
        "Quantitative synthesis\n"
        "Directional sign test  ·  excess-significance analysis\n"
        "moderator Fisher test  ·  a priori power reconstruction\n"
        "(pooled SMD not computable - see Methods 2.4)", "#F5EFE0")
    ax.text(5, 1.4, "Intermediate screening counts are not reported because the two source\n"
                    "searches used different, partly overlapping inclusion criteria.",
            ha="center", va="center", fontsize=6.8, style="italic", color="#666")
    plt.tight_layout(); plt.savefig("figs/fig1_flow.png", dpi=300, bbox_inches="tight"); plt.close()


# ===================== FIGURE 2 : harvest plot =====================
def figure2():
    rows = [
        ("Abdul 2009 (MCI+AD)", "Fraction-resolved", "down", 30),
        ("Woltjer 2010",        "Fraction-resolved", "down", 35),
        ("Tian 2010",           "Fraction-resolved", "down", 17),
        ("Sasaki 2009",         "Fraction-resolved", "down", 7),
        ("Li 1997",             "Total homogenate",  "down", 16),
        ("Beckstrom 1999",      "Total homogenate",  "null", 20),
        ("Kirvell 2010",        "Total homogenate",  "null", 15),
        ("Garcia-Esparcia 2018","Total homogenate",  "null", 59),
        ("Poirel 2018",         "Total homogenate",  "null", 171),
        ("Hoshi 2018",          "In situ imaging",   "down", 13),
        ("Kobayashi 2018",      "In situ imaging",   "down", 47),
        ("Simpson 2010",        "In situ imaging",   "down", 42),
        ("Thal 2010",           "In situ imaging",   "down", 380),
        ("Yeung 2021",          "In situ imaging",   "null", 13),
    ]
    preps = ["Fraction-resolved", "Total homogenate", "In situ imaging"]
    cols = dict(zip(preps, [FRAC, HOM, IMG]))
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.4), sharey=True)
    for ax, prep in zip(axes, preps):
        sub = [r for r in rows if r[1] == prep]
        for d, xpos in (("down", 0), ("null", 1)):
            grp = [r for r in sub if r[2] == d]
            for i, r in enumerate(grp):
                h = 0.35 + 0.55*math.log10(r[3])/math.log10(380)
                x = xpos + (i - (len(grp)-1)/2)*0.24
                ax.bar(x, h, width=0.21, edgecolor="#333", linewidth=0.6,
                       color=cols[prep] if d == "down" else "#CFCFCF")
                ax.text(x, h+0.03, r[0].split()[0], rotation=90,
                        ha="center", va="bottom", fontsize=6.2)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["EAAT2\nreduced", "No\nchange"], fontsize=8)
        ax.set_xlim(-0.62, 1.62); ax.set_ylim(0, 1.65); ax.set_yticks([])
        ax.set_title(prep, fontsize=9, color=cols[prep], fontweight="bold")
    axes[0].set_ylabel("Study (bar height $\\propto$ log sample size)", fontsize=8.5)
    fig.suptitle("Direction of EAAT2 finding by tissue preparation, not by brain region",
                 fontsize=10.5, fontweight="bold", y=1.0)
    fig.text(0.5, -0.02, "Fisher exact test, fraction-resolved vs. total homogenate: p = 0.048",
             ha="center", fontsize=8, style="italic")
    plt.tight_layout(); plt.savefig("figs/fig2_harvest.png", dpi=300, bbox_inches="tight"); plt.close()


# ===================== FIGURE 3 : power =====================
def power_uneq(d, n1, n2, a=0.05):
    df = n1 + n2 - 2
    ncp = d*math.sqrt(n1*n2/(n1+n2))
    c = stats.t.ppf(1-a/2, df)
    return 1 - stats.nct.cdf(c, df, ncp) + stats.nct.cdf(-c, df, ncp)

def figure3():
    st = [("Li 1997",4,12,1), ("Beckstrom 1999",10,10,0), ("Abdul 2009",12,18,1),
          ("Kirvell 2010",8,7,0), ("Tian 2010",11,6,1), ("Garcia-Esparcia 2018",39,20,0),
          ("Hoshi 2018",5,8,1), ("Kobayashi 2018",19,18,1), ("Poirel 2018",38,133,0),
          ("Yeung 2021",7,6,0)]
    st = sorted(st, key=lambda s: power_uneq(0.75, s[1], s[2]))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.2),
                                 gridspec_kw={"width_ratios": [1.15, 1]})
    pw = [power_uneq(0.75, s[1], s[2]) for s in st]
    a1.barh(range(len(st)), pw, edgecolor="#333", lw=0.6,
            color=[DOWN if s[3] else NULL for s in st])
    a1.set_yticks(range(len(st)))
    a1.set_yticklabels([f"{s[0]}  (n={s[1]}/{s[2]})" for s in st], fontsize=7.5)
    a1.axvline(0.8, ls="--", c="#333", lw=0.9)
    a1.text(0.81, 0.3, "80%", fontsize=7.5, rotation=90)
    a1.set_xlim(0, 1.02)
    a1.set_xlabel("Statistical power at the pooled reuptake effect (d = 0.75)", fontsize=8.5)
    a1.set_title("A  Per-study power", fontsize=9.5, fontweight="bold", loc="left")
    a1.legend(handles=[mpatches.Patch(color=DOWN, label="Reported significant reduction"),
                       mpatches.Patch(color=NULL, label="Reported no change")],
              fontsize=7, loc="lower right", frameon=False)
    ns = np.arange(4, 201)
    for d, c, ls in [(0.3,"#92C5DE","-"), (0.5,"#4393C3","-"),
                     (0.75,"#B2182B","-"), (1.0,"#67001F","--")]:
        a2.plot(ns, [power_uneq(d, n, n) for n in ns], color=c, ls=ls, lw=1.6, label=f"d = {d}")
    a2.axhline(0.8, ls="--", c="#333", lw=0.9)
    a2.axvline(10, ls=":", c="#B2182B", lw=1.4)
    a2.text(12, 0.06, "median group size\nin this literature (n = 10)", fontsize=7, color="#B2182B")
    a2.set_xlabel("n per group", fontsize=8.5); a2.set_ylabel("Power", fontsize=8.5)
    a2.set_xlim(0, 200); a2.set_ylim(0, 1.02)
    a2.legend(fontsize=7.5, frameon=False, loc="lower right")
    a2.set_title("B  Power as a function of sample size", fontsize=9.5, fontweight="bold", loc="left")
    plt.tight_layout(); plt.savefig("figs/fig3_power.png", dpi=300, bbox_inches="tight"); plt.close()


# ===================== FIGURE 4 : compositional model =====================
def figure4():
    fig, (b1, b2) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    x = np.array([0, 1, 2]); lab = ["Braak 0-II", "Braak III-IV", "Braak V-VI"]
    homeo = np.array([0.78, 0.60, 0.40]); react = 1 - homeo
    b1.bar(x, homeo, 0.55, color="#4393C3", edgecolor="#333", lw=0.7,
           label="$SLC1A2$-high homeostatic\nprotoplasmic astrocytes")
    b1.bar(x, react, 0.55, bottom=homeo, color="#D6604D", edgecolor="#333", lw=0.7,
           label="$GFAP$/$CRYAB$-high\nreactive astrocytes")
    b1.set_xticks(x); b1.set_xticklabels(lab, fontsize=8)
    b1.set_ylabel("Fraction of astrocyte pool", fontsize=8.5); b1.set_ylim(0, 1.55)
    b1.legend(fontsize=6.6, frameon=False, loc="upper center", ncol=2, columnspacing=1.0)
    b1.set_title("A  Compositional shift\n(observed: Lau, Smith, Sadick, Dai, SEA-AD)",
                 fontsize=8.8, fontweight="bold", loc="left")
    xs = np.linspace(0, 2, 100)
    b2.plot(xs, np.full_like(xs, 1.0), color="#8C8C8C", lw=2.4, label="Total tissue EAAT2 (bulk)")
    b2.plot(xs, 1-0.24*xs, color="#4393C3", lw=2.2, label="EAAT2 per astrocyte")
    b2.plot(xs, 1-0.30*xs, color="#2166AC", lw=2.2, ls="--", label="Surface / raft-associated EAAT2")
    b2.plot(xs, 1-0.33*xs, color="#B2182B", lw=2.4, label="Glutamate reuptake capacity")
    b2.set_xticks([0, 1, 2]); b2.set_xticklabels(lab, fontsize=8)
    b2.set_ylabel("Relative to Braak 0-II", fontsize=8.5); b2.set_ylim(0.2, 1.18)
    b2.legend(fontsize=7, frameon=False, loc="lower left")
    b2.set_title("B  Predicted divergence of estimands", fontsize=8.8, fontweight="bold", loc="left")
    fig.text(0.5, -0.03, "Panel B is a falsifiable model prediction, not measured data.",
             ha="center", fontsize=7.5, style="italic")
    plt.tight_layout(); plt.savefig("figs/fig4_model.png", dpi=300, bbox_inches="tight"); plt.close()


# ============ SUPPLEMENTARY FIGURE S1 : model calibration ============
def figureS1():
    rng = np.random.default_rng(7); N = 400000
    f0 = rng.uniform(0.60, 0.92, N); f1 = rng.uniform(0.25, 0.90, N)
    rho = rng.uniform(0.05, 0.90, N); glia = rng.uniform(1.00, 1.80, N)
    nloss = rng.uniform(0.05, 0.50, N); nprot = rng.uniform(0.40, 0.60, N)
    srat = rng.uniform(0.40, 1.00, N); cv = rng.uniform(0.25, 0.90, N)
    protein = 1 - nprot*nloss
    bulk = (glia*(f1 + (1-f1)*rho))/(f0 + (1-f0)*rho)/protein
    astro = (f1 + (1-f1)*rho)/(f0 + (1-f0)*rho)
    upt = astro*srat
    db, du = np.log(bulk)/cv, np.log(upt)/cv
    ok = (np.abs(db) < 0.30) & (du < -0.55) & (du > -1.05)
    fig, axes = plt.subplots(1, 4, figsize=(11, 2.9))
    panels = [(cv, "Assay CV", (0.25, 0.90)),
              (rho, "Relative EAAT2 in\nreactive astrocytes", (0.05, 0.90)),
              (srat, "Surface fraction ratio\n(late/early)", (0.40, 1.00)),
              (f1, "Homeostatic fraction,\nlate stage", (0.25, 0.90))]
    for ax, (v, nm, pr) in zip(axes, panels):
        ax.hist(v, bins=40, range=pr, density=True, color="#CCCCCC", label="prior")
        ax.hist(v[ok], bins=40, range=pr, density=True, color="#B2182B",
                alpha=0.75, label="consistent")
        ax.set_xlabel(nm, fontsize=8); ax.set_yticks([])
    axes[0].legend(fontsize=7, frameon=False); axes[0].set_ylabel("density", fontsize=8)
    fig.suptitle("Parameter values required for the compositional model to reproduce both observations",
                 fontsize=9.5, fontweight="bold")
    plt.tight_layout(); plt.savefig("figs/figS1_calibration.png", dpi=300, bbox_inches="tight"); plt.close()
    print(f"  consistent fraction of prior space: {100*ok.mean():.2f}%")


if __name__ == "__main__":
    for name, fn in [("Figure 1", figure1), ("Figure 2", figure2), ("Figure 3", figure3),
                     ("Figure 4", figure4), ("Figure S1", figureS1)]:
        print(f"building {name} ...")
        fn()
    print("\nAll figures written to ./figs/")
