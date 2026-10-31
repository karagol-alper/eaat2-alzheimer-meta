#!/usr/bin/env python3
"""
Supplementary File S1
=====================
Extraction matrix and reproducible analysis code for:

  "Transporter abundance is preserved while transport fails: re-examining
   EAAT2/SLC1A2 in the Alzheimer brain through the lens of estimand
   specification"

  Alper Karagöl and Taner Karagöl

Run:  python3 S1_extraction_matrix_and_analysis.py
Deps: scipy

Every statistic reported in the manuscript Results is regenerated below.
No new primary data are used; all inputs are extracted from published reports.
Sections S1-S10. Regenerates every statistic reported in the main text and in
Supplementary File S3.

Run:  python3 EAAT2_analysis_S1_to_S10.py
Deps: scipy, numpy
"""

import math
import numpy as np
from scipy import stats

# ============================================================================
# TABLE S1. Extraction matrix - human post-mortem EAAT2 studies
# ----------------------------------------------------------------------------
# prep classes:  fraction   = membrane / lipid raft / detergent-insoluble / IP
#                homogenate = whole-lysate Western blot or ELISA
#                imaging    = IHC / quantitative immunofluorescence
#                binding    = ligand binding or uptake kinetics
# direction:     -1 reduced in AD, 0 no change, +1 increased in AD
# sig:           significant at alpha = 0.05 as reported by the authors
# ============================================================================

EXTRACTION = [
    # study,                yr,   region,            prep,         n_ctrl, n_ad, direction, sig, note
    ("Rothstein",          1992, "multiregion",     "binding",       17,   15,   0, False, "Vmax/Kt unchanged in AD"),
    ("Masliah",            1996, "neocortex",       "binding",     None, None,  -1, True,  "~30% reduction, D-aspartate binding"),
    ("Li",                 1997, "frontal",         "homogenate",     4,   12,  -1, True,  "protein down; mRNA unchanged"),
    ("Beckstrom",          1999, "inf temporal",    "homogenate",    10,   10,   0, False, "high inter-individual variance"),
    ("Lauderback",         2001, "inf parietal",    "fraction",       7,    4,  -1, True,  "HNE-adducted GLT-1"),
    ("Thai",               2002, "multiregion",     "imaging",     None, None,  -1, True,  "neuronal EAAT2 accumulation"),
    ("Jacob",              2007, "front/hipp/cbl",  "homogenate",    10,   22,  -1, True,  "platform-discordant, see manuscript 3.2"),
    ("Abdul",              2009, "hippocampus",     "fraction",      12,   18,  -1, True,  "membrane fraction; deficit present at MCI"),
    ("Sasaki",             2009, "temporal",        "fraction",       3,    4,  -1, True,  "insoluble EAAT2, co-IP with p-tau"),
    ("Pow & Cook",         2009, "temporal",        "imaging",        3,    3,  -1, True,  "exon-9 skipping variant, neuronal"),
    ("Kirvell",            2010, "frontal BA9/20",  "homogenate",     8,    7,   0, False, ""),
    ("Tian",               2010, "frontal BA9/10",  "fraction",      11,    6,  -1, True,  "reduced lipid raft association"),
    ("Woltjer",            2010, "hipp + frontal",  "fraction",      33,   77,  -1, True,  "detergent-insoluble EAAT2 increased"),
    ("Thal",               2010, "occipital",       "imaging",      309,   71,  -1, True,  "perivascular; capillary CAA subgroup only"),
    ("Simpson",            2010, "lat temporal",    "imaging",     None,   42,  -1, False, "inverse GFAP-EAAT2 p=0.015; Braak trend ns"),
    ("Scott",              2011, "4 cortical",      "homogenate",    15,   12,  -1, True,  "mRNA; variants rise with severity"),
    ("Garcia-Esparcia",    2018, "frontal BA8",     "homogenate",    39,   20,   0, False, "GLT1 flat; GFAP & ALDH1L1 up; ratios fall"),
    ("Hoshi",              2018, "temporal",        "imaging",        5,    8,  -1, True,  "plaque-like GLT-1/AQP4 co-deposits"),
    ("Kobayashi",          2018, "entorhinal",      "imaging",       19,   18,  -1, True,  "AD-D only; AD-N preserved at matched pathology"),
    ("Poirel",             2018, "frontal BA9",     "homogenate",    38,  133,   0, False, "no CDR correlation"),
    ("Yeung",              2021, "medial temporal", "imaging",        7,    6,   0, False, "increased neuropil signal"),
]

# The ten comparisons that test EAAT2 ABUNDANCE against a control group with
# extractable group sizes. This is the primary analysis set.
ABUNDANCE = [(s[0], s[4], s[5], s[3], s[7]) for s in EXTRACTION if s[0] in
             {"Li", "Beckstrom", "Abdul", "Kirvell", "Tian",
              "Garcia-Esparcia", "Hoshi", "Kobayashi", "Poirel", "Yeung"}]


# ============================================================================
# Helper: two-sample power via the noncentral t distribution
# ============================================================================
def power_two_sample(d, n1, n2, alpha=0.05):
    """Power to detect standardised effect d with unequal group sizes."""
    df = n1 + n2 - 2
    ncp = d * math.sqrt(n1 * n2 / (n1 + n2))
    crit = stats.t.ppf(1 - alpha / 2, df)
    return 1 - stats.nct.cdf(crit, df, ncp) + stats.nct.cdf(-crit, df, ncp)


def line(c="-", n=78):
    print(c * n)


# ============================================================================
# RESULT 3.3  Power reconstruction
# ============================================================================
line("=")
print("RESULT 3.3  -  A PRIORI POWER RECONSTRUCTION")
line("=")
sizes = [n for _, n1, n2, _, _ in ABUNDANCE for n in (n1, n2)]
sizes.sort()
median_n = (sizes[len(sizes)//2 - 1] + sizes[len(sizes)//2]) / 2
print(f"Median group size across abundance comparisons: {median_n:.0f}\n")

print(f"{'Study':<20}{'n ctrl/AD':>12}{'power @ d=0.75':>16}   reported")
line()
for name, n1, n2, prep, sig in sorted(ABUNDANCE, key=lambda s: power_two_sample(0.75, s[1], s[2])):
    p = power_two_sample(0.75, n1, n2)
    print(f"{name:<20}{f'{n1}/{n2}':>12}{p:>16.3f}   {'SIGNIFICANT' if sig else 'no change'}")

print("\nPower at the median group size (n = 10 per arm):")
for d in (0.3, 0.4, 0.5, 0.75, 1.0):
    print(f"   d = {d:<5} ->  power = {power_two_sample(d, 10, 10):.3f}")

print("\nGroup size required for 80% power (alpha = 0.05, two-sided):")
z = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)
for d in (0.25, 0.3, 0.4, 0.5, 0.75):
    print(f"   d = {d:<5} ->  n = {math.ceil(2 * z**2 / d**2)} per group")


# ============================================================================
# RESULT 3.4  Excess significance and implied effect size
# ============================================================================
line("=")
print("RESULT 3.4  -  EXCESS-SIGNIFICANCE ANALYSIS")
line("=")
observed = sum(1 for *_, sig in ABUNDANCE if sig)
k = len(ABUNDANCE)
print(f"Observed significant findings: {observed} / {k}\n")

print(f"{'assumed d':>10}{'expected sig':>15}{'observed':>11}{'excess-sig p':>15}")
line()
for d in (0.2, 0.3, 0.4, 0.5, 0.75, 1.0):
    exp = sum(power_two_sample(d, n1, n2) for _, n1, n2, _, _ in ABUNDANCE)
    p = stats.binomtest(observed, k, exp / k, alternative="greater").pvalue
    print(f"{d:>10}{exp:>15.2f}{observed:>11}{p:>15.4f}")

# Invert: which d reproduces the observed significance count?
lo, hi = 0.01, 3.0
for _ in range(100):
    mid = (lo + hi) / 2
    e = sum(power_two_sample(mid, n1, n2) for _, n1, n2, _, _ in ABUNDANCE)
    lo, hi = (mid, hi) if e < observed else (lo, mid)
implied = (lo + hi) / 2
print(f"\nImplied true effect size reproducing {observed} significant findings: d = {implied:.2f}")
print("Independently pooled glutamate reuptake effect (Soares 2024):        d = 0.75")
print("-> Two methodologically unrelated routes to an effect size converge.")


# ============================================================================
# RESULT 3.4  Directional sign test
# ============================================================================
line("=")
print("RESULT 3.4  -  DIRECTIONAL SIGN TEST")
line("=")
sig_findings = [s for s in EXTRACTION if s[7]]
down = sum(1 for s in sig_findings if s[6] == -1)
up = sum(1 for s in sig_findings if s[6] == +1)
print(f"Significant findings in the full corpus: {len(sig_findings)}")
print(f"   direction reduced : {down}")
print(f"   direction increased: {up}")
core = 7  # independent significant abundance/binding findings, manuscript 3.4
print(f"\nRestricting to the {core} independent significant abundance/binding findings:")
print(f"   two-sided sign test, {core}/{core} downward: p = {2 * 0.5 ** core:.4f}")
print("   CAVEAT: publication bias inflates this statistic; treat as suggestive.")


# ============================================================================
# RESULT 3.5  Moderator analysis - preparation vs region
# ============================================================================
line("=")
print("RESULT 3.5  -  MODERATOR ANALYSIS")
line("=")

frac = [s for s in EXTRACTION if s[3] == "fraction"]
homo = [s for s in EXTRACTION if s[3] == "homogenate" and s[0] != "Scott" and s[0] != "Jacob"]
imag = [s for s in EXTRACTION if s[3] == "imaging"]

def rate(group, label):
    hit = sum(1 for s in group if s[7])
    print(f"   {label:<42}{hit}/{len(group)}  ({100*hit/len(group):.0f}%)")
    return hit, len(group) - hit

print("Detection of an EAAT2 abnormality by preparation class:")
f_hit, f_miss = rate(frac, "Fraction-resolved (membrane/raft/insoluble)")
h_hit, h_miss = rate(homo, "Total homogenate (whole lysate)")
i_hit, i_miss = rate(imag, "In situ imaging")

odds, p = stats.fisher_exact([[f_hit, f_miss], [h_hit, h_miss]])
print(f"\nFisher exact, fraction-resolved vs total homogenate: p = {p:.4f}")
print(f"   odds ratio = {'infinite (zero cell)' if odds == float('inf') else f'{odds:.2f}'}")

print("\nSame test by region (medial temporal vs frontal):")
mt = [s for s in EXTRACTION if s[2] in {"hippocampus", "entorhinal", "medial temporal",
                                        "temporal", "inf temporal", "lat temporal"}]
fr = [s for s in EXTRACTION if s[2].startswith("frontal")]
m_hit, m_miss = rate(mt, "Medial/lateral temporal")
r_hit, r_miss = rate(fr, "Frontal")
_, p_region = stats.fisher_exact([[m_hit, m_miss], [r_hit, r_miss]])
print(f"\nFisher exact by region: p = {p_region:.4f}")
print("-> Preparation is the better-supported moderator; region is confounded with it.")


# ============================================================================
# Summary
# ============================================================================
line("=")
print("SUMMARY OF REPORTED STATISTICS")
line("=")
print(f"  Median group size                          : {median_n:.0f}")
print(f"  Power at d = 0.40, n = 10/group            : {power_two_sample(0.4, 10, 10):.2f}")
print(f"  Power at d = 0.75, n = 10/group            : {power_two_sample(0.75, 10, 10):.2f}")
print(f"  Poirel 2018 power at d = 0.75              : {power_two_sample(0.75, 38, 133):.2f}  (reported null)")
print(f"  Garcia-Esparcia 2018 power at d = 0.75     : {power_two_sample(0.75, 39, 20):.2f}  (reported null)")
print(f"  Observed / total significant               : {observed}/{k}")
print(f"  Implied true effect size                   : d = {implied:.2f}")
print(f"  Excess-significance p vs d = 0.4           : "
      f"{stats.binomtest(observed, k, sum(power_two_sample(0.4, n1, n2) for _, n1, n2, _, _ in ABUNDANCE)/k, alternative='greater').pvalue:.4f}")
print(f"  Sign test, 7/7 downward                    : p = {2*0.5**7:.4f}")
print(f"  Preparation moderator (Fisher)             : p = {p:.4f}")
line("=")


##############################################################################
# EXTENDED ANALYSES S3-S10
# (leave-one-out, moderator robustness, exact CI, compositional-model
#  calibration, denominator bias, vote-counting failure, sample size)
##############################################################################

OUT = {}
rng = np.random.default_rng(20260907)

STUDIES = [("Li 1997",4,12,True),("Beckstrom 1999",10,10,False),("Abdul 2009",12,18,True),
           ("Kirvell 2010",8,7,False),("Tian 2010",11,6,True),("Garcia-Esparcia 2018",39,20,False),
           ("Hoshi 2018",5,8,True),("Kobayashi 2018",19,18,True),("Poirel 2018",38,133,False),
           ("Yeung 2021",7,6,False)]

def power(d,n1,n2,a=0.05):
    df=n1+n2-2; ncp=d*math.sqrt(n1*n2/(n1+n2)); c=stats.t.ppf(1-a/2,df)
    return 1-stats.nct.cdf(c,df,ncp)+stats.nct.cdf(-c,df,ncp)

def implied_d(studies):
    obs=sum(1 for *_,s in studies if s)
    if obs==0: return None
    if obs==len(studies): return float('inf')
    lo,hi=0.01,4.0
    for _ in range(100):
        m=(lo+hi)/2
        e=sum(power(m,a,b) for _,a,b,_ in studies)
        lo,hi=(m,hi) if e<obs else (lo,m)
    return (lo+hi)/2

# ============ S3. LEAVE-ONE-OUT SENSITIVITY ============
full = implied_d(STUDIES)
loo=[]
for i,(nm,*_ ) in enumerate(STUDIES):
    sub=[s for j,s in enumerate(STUDIES) if j!=i]
    loo.append((nm, implied_d(sub)))
OUT["S3"]={"full":full,"loo":loo,
           "range":(min(v for _,v in loo if v!=float('inf')), max(v for _,v in loo if v!=float('inf')))}

# ============ S4. MODERATOR ROBUSTNESS UNDER ALTERNATIVE CODING ============
# Base coding: fraction-resolved 5 sig / 0 ns ; homogenate 1 sig / 4 ns
codings = {
 "Primary (as reported)":                       [[5,0],[1,4]],
 "Lauderback recoded as imaging":               [[4,0],[1,4]],
 "Woltjer & Sasaki excluded (insoluble only)":  [[3,0],[1,4]],
 "Insoluble-fraction studies excluded entirely":[[2,0],[1,4]],
 "Li 1997 recoded as fraction-resolved":        [[6,0],[0,4]],
 "Most conservative (fraction = Abdul, Tian)":  [[2,0],[1,4]],
}
OUT["S4"]={k:{"table":v,"p":stats.fisher_exact(v)[1]} for k,v in codings.items()}

# ============ S5. EXACT CI FOR THE ODDS RATIO (ZERO CELL) ============
# Conditional exact (Fisher) CI via profile on the noncentral hypergeometric
def fisher_exact_ci(table, alpha=0.05):
    a,b = table[0]; c,d = table[1]
    n1,n2,t = a+b, c+d, a+c
    lo_k, hi_k = max(0,t-n2), min(n1,t)
    def pmf(psi):
        ks=np.arange(lo_k,hi_k+1)
        w=np.array([math.comb(n1,int(k))*math.comb(n2,int(t-k)) for k in ks],dtype=float)
        return ks, w*np.power(psi,ks.astype(float))
    def pl(psi):   # P(K >= a)
        ks,w=pmf(psi); return w[ks>=a].sum()/w.sum()
    def pu(psi):   # P(K <= a)
        ks,w=pmf(psi); return w[ks<=a].sum()/w.sum()
    lo=0.0
    if a>lo_k:
        x0,x1=1e-6,1e6
        for _ in range(200):
            m=math.sqrt(x0*x1)
            if pl(m)<alpha/2: x0=m
            else: x1=m
        lo=math.sqrt(x0*x1)
    hi=float('inf')
    if a<hi_k:
        x0,x1=1e-6,1e6
        for _ in range(200):
            m=math.sqrt(x0*x1)
            if pu(m)>alpha/2: x0=m
            else: x1=m
        hi=math.sqrt(x0*x1)
    return lo,hi
OUT["S5"]={"table":[[5,0],[1,4]],"ci":fisher_exact_ci([[5,0],[1,4]]),
           "midp_note":"upper limit infinite because of the zero cell"}

# ============ S6. MONTE CARLO OF THE COMPOSITIONAL MODEL ============
# Does a homeostatic->reactive astrocyte shift reproduce (bulk flat) + (uptake down ~0.75 SD)?
NSIM=200000
f0   = rng.uniform(0.70,0.90,NSIM)      # homeostatic fraction, Braak 0-II
f1   = rng.uniform(0.30,0.55,NSIM)      # homeostatic fraction, Braak V-VI
rho  = rng.uniform(0.15,0.45,NSIM)      # EAAT2 per reactive astrocyte, relative to homeostatic
glia = rng.uniform(1.10,1.60,NSIM)      # astrocyte number fold-change (gliosis)
nloss= rng.uniform(0.15,0.45,NSIM)      # neuronal loss fraction at Braak V-VI
nprot= rng.uniform(0.40,0.60,NSIM)      # neuronal share of total cortical protein
surf0= rng.uniform(0.75,0.90,NSIM)      # surface-localised fraction, early
surf1= rng.uniform(0.40,0.65,NSIM)      # surface-localised fraction, late
cv   = 0.35                             # between-subject CV of the bulk measure

protein_ratio = 1 - nprot*nloss                       # total protein falls with neuron loss
eaat2_early   = 1.0*(f0 + (1-f0)*rho)
eaat2_late    = glia*(f1 + (1-f1)*rho)
bulk_ratio    = (eaat2_late/eaat2_early)/protein_ratio  # per mg total protein
per_astro     = (f1+(1-f1)*rho)/(f0+(1-f0)*rho)         # per astrocyte
uptake_ratio  = per_astro*(surf1/surf0)                 # surface-localised, per astrocyte

d_bulk   = np.log(bulk_ratio)/cv
d_uptake = np.log(uptake_ratio)/cv
consistent = (np.abs(d_bulk)<0.30) & (d_uptake<-0.55) & (d_uptake>-1.05)
OUT["S6"]={"n":NSIM,
  "bulk_median_d":float(np.median(d_bulk)),
  "bulk_iqr":[float(np.percentile(d_bulk,25)),float(np.percentile(d_bulk,75))],
  "uptake_median_d":float(np.median(d_uptake)),
  "uptake_iqr":[float(np.percentile(d_uptake,25)),float(np.percentile(d_uptake,75))],
  "per_astro_median_d":float(np.median(np.log(per_astro)/cv)),
  "pct_consistent":float(100*consistent.mean()),
  "pct_bulk_undetectable":float(100*(np.abs(d_bulk)<0.30).mean()),
  "pct_uptake_in_band":float(100*((d_uptake<-0.55)&(d_uptake>-1.05)).mean())}

# ============ S7. DENOMINATOR BIAS FROM NEURONAL LOSS ============
rows=[]
for nl in (0.10,0.20,0.30,0.40,0.50):
    for ns in (0.45,0.55):
        infl = 1/(1-ns*nl)
        # true per-astrocyte decline that a total-protein-normalised assay would read as zero
        masked = (infl-1)*100
        rows.append((nl,ns,infl,masked))
OUT["S7"]=rows

# ============ S8. WHY VOTE-COUNTING FAILS ============
def vote_count_sim(true_d, reps=20000):
    correct=0; majority=0
    for _ in range(reps):
        sig=0
        for _,n1,n2,_ in STUDIES:
            se=math.sqrt(1/n1+1/n2)
            obs=rng.normal(true_d,se)
            tstat=obs/se
            if abs(tstat)>stats.t.ppf(0.975,n1+n2-2): sig+=1
        if sig>len(STUDIES)/2: majority+=1
    return majority/reps
OUT["S8"]={f"d={d}": vote_count_sim(d) for d in (0.0,0.4,0.83,1.2)}

# ============ S9. SAMPLE SIZE FOR THE PROPOSED IPD DESIGN ============
z=stats.norm.ppf(0.975)+stats.norm.ppf(0.80)
main=lambda d: math.ceil(2*z**2/d**2)
inter=lambda d: math.ceil(8*z**2/d**2)   # interaction needs 4x per arm
OUT["S9"]=[(d,main(d),inter(d),inter(d)*3,inter(d)*3*4) for d in (0.25,0.30,0.40,0.50)]

# ============ S10. PUBLICATION-BIAS STRESS TEST ON THE SIGN TEST ============
stress=[]
for m in range(0,8):
    k=7
    p=stats.binomtest(k,k+m,0.5,alternative="two-sided").pvalue
    stress.append((m,k+m,p))
OUT["S10"]=stress

# ---------------- print ----------------
def hr(t): print("\n"+"="*76+f"\n{t}\n"+"="*76)

hr("S3. LEAVE-ONE-OUT SENSITIVITY OF THE IMPLIED EFFECT SIZE")
print(f"Full set (10 studies): implied d = {full:.2f}")
for nm,v in loo: print(f"  omitting {nm:<22} -> d = {'inf' if v==float('inf') else f'{v:.2f}'}")
print(f"Range across leave-one-out (finite): {OUT['S3']['range'][0]:.2f} to {OUT['S3']['range'][1]:.2f}")

hr("S4. MODERATOR ROBUSTNESS UNDER ALTERNATIVE PREPARATION CODING")
for k,v in OUT["S4"].items(): print(f"  {k:<46} {v['table']}  p = {v['p']:.4f}")

hr("S5. EXACT CONFIDENCE INTERVAL FOR THE MODERATOR ODDS RATIO")
lo,hi=OUT["S5"]["ci"]; print(f"  Conditional exact 95% CI for OR: {lo:.2f} to infinity (zero cell)")

hr("S6. MONTE CARLO OF THE COMPOSITIONAL MODEL (200,000 draws)")
s=OUT["S6"]
print(f"  bulk EAAT2      : median d = {s['bulk_median_d']:+.2f}  IQR [{s['bulk_iqr'][0]:+.2f}, {s['bulk_iqr'][1]:+.2f}]")
print(f"  per-astrocyte   : median d = {s['per_astro_median_d']:+.2f}")
print(f"  uptake capacity : median d = {s['uptake_median_d']:+.2f}  IQR [{s['uptake_iqr'][0]:+.2f}, {s['uptake_iqr'][1]:+.2f}]")
print(f"  bulk change undetectable (|d|<0.30) : {s['pct_bulk_undetectable']:.1f}% of parameter space")
print(f"  uptake in observed band (d -0.55..-1.05): {s['pct_uptake_in_band']:.1f}%")
print(f"  BOTH simultaneously                 : {s['pct_consistent']:.1f}%")

hr("S7. DENOMINATOR INFLATION FROM NEURONAL LOSS")
print(f"  {'neuron loss':>12}{'neuronal % protein':>20}{'inflation':>12}{'masked decline':>16}")
for nl,ns,infl,mk in OUT["S7"]:
    print(f"  {nl*100:>11.0f}%{ns*100:>19.0f}%{infl:>12.3f}{mk:>15.1f}%")

hr("S8. PROBABILITY THAT VOTE-COUNTING DECLARES AN EFFECT")
for k,v in OUT["S8"].items(): print(f"  true {k:<8} -> majority-significant in {v*100:5.1f}% of replications")

hr("S9. SAMPLE SIZE FOR THE PROPOSED IPD DESIGN (80% power)")
print(f"  {'d':>6}{'n/arm (main)':>16}{'n/arm (interaction)':>22}{'per region':>13}{'4 regions':>12}")
for d,m,i,pr,tot in OUT["S9"]: print(f"  {d:>6}{m:>16}{i:>22}{pr:>13}{tot:>12}")

hr("S10. PUBLICATION-BIAS STRESS TEST ON THE SIGN TEST")
print("  unpublished significant INCREASES needed to break the sign test:")
for m,n,p in OUT["S10"]:
    flag="  <-- p exceeds 0.05" if p>0.05 else ""
    print(f"    {m} additional -> {7}/{n} downward, two-sided p = {p:.4f}{flag}")




##############################################################################
# EXTENDED ANALYSES S11-S13  (added in revision, in response to peer review)
# Each of these three analyses returned a result unfavourable to a claim made
# in the original submission. All three are reported in the revised manuscript.
##############################################################################

STUDIES_R = [("Li 1997",4,12,True),("Beckstrom 1999",10,10,False),
             ("Abdul 2009",12,18,True),("Kirvell 2010",8,7,False),
             ("Tian 2010",11,6,True),("Garcia-Esparcia 2018",39,20,False),
             ("Hoshi 2018",5,8,True),("Kobayashi 2018",19,18,True),
             ("Poirel 2018",38,133,False),("Yeung 2021",7,6,False)]

def _pw(d, n1, n2, alpha=0.05):
    df = n1 + n2 - 2
    ncp = d * math.sqrt(n1*n2/(n1+n2))
    crit = stats.t.ppf(1 - alpha/2, df)
    return 1 - stats.nct.cdf(crit, df, ncp) + stats.nct.cdf(-crit, df, ncp)

def _solve_for_S(target_S):
    """Effect size whose summed power across the corpus equals target_S."""
    lo, hi = 0.001, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        tot = sum(_pw(mid, a, b) for _, a, b, _ in STUDIES_R)
        lo, hi = (mid, hi) if tot < target_S else (lo, mid)
    return (lo + hi) / 2

line("=")
print("S11. PUBLICATION-BIAS ADJUSTMENT OF THE IMPLIED EFFECT SIZE")
line("=")
print("The inversion in S3 assumes publication is independent of significance.")
print("Let null results be published with probability w relative to significant")
print("results. Expected published-significant fraction = S/(S + w(k-S)).")
print("Setting this to the observed 0.50 gives S = k*w/(1+w).\n")
k = len(STUDIES_R)
print(f"{'w':>8}{'required S':>14}{'implied d':>13}{'regime':>26}")
line()
for w in (1.0, 0.75, 0.50, 0.33, 0.25, 0.10):
    S = k*w/(1+w)
    d = _solve_for_S(S)
    regime = ("none (original assumption)" if w == 1.0 else
              "mild" if w >= 0.75 else "moderate" if w >= 0.33 else "severe")
    print(f"{w:>8.2f}{S:>14.2f}{d:>13.2f}{regime:>26}")
print("\n  -> d = 0.83 is an UPPER BOUND, not a point estimate.")
print("     Plausible range 0.41-0.83. A negligible effect (d<=0.2) would require")
print("     ~9 of every 10 null studies to go unpublished, so exclusion of a")
print("     very small effect is robust even though the point estimate is not.")

line("=")
print("S12. POWER OF THE TWO LARGEST STUDIES, RE-BENCHMARKED")
line("=")
print("Original text called these 'adequately powered' using d = 0.75, the pooled")
print("REUPTAKE effect. That is circular: the paper's thesis is that the abundance")
print("effect is smaller than the functional effect.\n")
print(f"{'true d':>9}{'Poirel (38/133)':>18}{'Garcia-Esp (39/20)':>21}{'>=80% power?':>15}")
line()
for d in (0.20, 0.30, 0.40, 0.50, 0.75):
    p1, p2 = _pw(d, 38, 133), _pw(d, 39, 20)
    verdict = "both" if min(p1, p2) >= 0.8 else ("Poirel only" if p1 >= 0.8 else "neither")
    print(f"{d:>9.2f}{p1:>18.2f}{p2:>21.2f}{verdict:>15}")
print("\n  -> Neither study reaches 80% power against any abundance effect < ~0.5.")
print("     The claim that they establish preservation is WITHDRAWN.")

line("=")
print("S13. PREPARATION MODERATOR UNDER DIRECTION-SPECIFIC CODING")
line("=")
print("The published coding scores any abnormality as 'detection', including")
print("INCREASES in aberrant species (insoluble EAAT2, HNE adducts). Fraction-")
print("resolved studies are designed to find such species, making the test")
print("near-tautological. Recoded so only a REDUCTION in normal transporter counts:\n")
codings_r = {
    "Any abnormality (as originally published)":   [[5, 0], [1, 4]],
    "Reduction of normal transporter only":        [[2, 3], [1, 4]],
    "Reduction only, insoluble studies excluded":  [[2, 1], [1, 4]],
}
for label, tbl in codings_r.items():
    _, p = stats.fisher_exact(tbl)
    flag = "  <-- as published" if p < 0.05 else ""
    print(f"  {label:<46} {tbl}  p = {p:.4f}{flag}")
print("\n  -> The association does NOT survive direction-specific coding.")
print("     The positive claim that preparation is the operative moderator is")
print("     WITHDRAWN. What survives: region shows no association under any")
print("     coding (p = 0.59), and region and preparation cannot be separated")
print("     in the existing corpus.")
line("=")
