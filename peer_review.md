---
title: "Internal Pre-submission Review and Author Response"
subtitle: "Review of the draft originally titled: Transporter abundance is preserved while transport fails: a region- and stage-stratified synthesis of EAAT2/SLC1A2 in the Alzheimer brain"
---

**Status of this document.** This is an internal critique written before journal submission, in the format of a two-reviewer report, to stress-test the draft. It is not a journal peer review, no editorial decision was issued, and it should not be described or submitted as one. Its recommendation was major revision, and the manuscript was revised accordingly.

Both reviewers regard the central question as important and the assembly of evidence as careful. Both, however, identify a common structural problem: the manuscript builds three novel quantitative claims on a corpus that cannot support them at the stated confidence, and in two cases the analyses are internally inconsistent with the manuscript's own arguments. The synthesis of existing evidence is sound; the new inferential scaffolding is not. Revision should retain the former and substantially qualify the latter.

\newpage

# Reviewer 1 — Neuropathology and clinical neurology

## General assessment

This is a thoughtful and unusually self-critical synthesis of a genuinely confused literature. The core reframing — that investigators have measured transporter per gram of tissue when the meaningful quantity is transporter per astrocyte, at the membrane, in a defined cell state — is correct and worth publishing. The identification of the denominator problem, and its quantification in Supplementary S7, is the strongest contribution and is something the field has largely ignored.

My concerns are that several biological alternatives are not seriously considered, that one key inference has a confound the authors have not addressed, and that the title promises a stage-stratification the data do not deliver.

## Major comments

**R1.1 — The Kobayashi resilience argument has an unaddressed confound.**
Section 3.8.2 treats Kobayashi et al. (2018) as the closest thing to a natural experiment, on the grounds that amyloid and tangle burden are matched between AD-N and AD-D while GLT-1 differs. But the authors themselves note, two sentences later, that neuron number and synaptic density were *higher* in AD-N. GLT-1-positive **area** in a section is not independent of how much neuropil is present. If AD-D cortex has lost neurons and neuropil, GLT-1-positive area will fall even if transporter per surviving astrocyte process is unchanged. This is the same denominator problem the authors identify elsewhere, and it undermines the single strongest human argument in the paper. It must be stated explicitly.

**R1.2 — Neuronal EAAT2 is acknowledged and then ignored.**
The introduction correctly cites Petr et al. (2015) and Danbolt et al. (2016) to the effect that neuronal GLT-1 contributes the majority of measurable uptake in synaptosome preparations. Thal (2002) and Pow and Cook (2009) both report neuronal EAAT2 appearing in AD tissue. Yet the compositional model in §3.9 and Figure 4 is entirely astrocytic. If a substantial part of the pooled reuptake deficit is neuronal, the astrocyte-composition explanation is at best partial. The model should either incorporate a neuronal compartment or explicitly state that it addresses only the astrocytic contribution.

**R1.3 — Masliah 1996 is not an EAAT2-specific measurement.**
Sodium-dependent D-aspartate binding reports total high-affinity glutamate transport, to which EAAT1, EAAT2 and EAAT3 all contribute. Counting it among "significant EAAT2 findings" in the sign test of §3.5 is not defensible. The same applies to Rothstein et al. (1992), a uptake-kinetics study whose AD arm is incidental to an ALS paper. Recompute the sign test with these reclassified.

**R1.4 — The title oversells the stage stratification.**
"Region- and stage-stratified" implies a stratified analysis. In fact only four datasets stratify by stage at all, only one (Simpson) reports a Braak trend for EAAT2, and that trend is non-significant. The paper's own §3.8 concedes this is "the principal gap in the field." The title should not claim what §3.8 disclaims.

**R1.5 — Region and preparation are not the only confound.**
The manuscript argues that region and preparation are confounded, which is correct. But there is a third variable: which astrocytic compartment is sampled. EAAT2 does its work in fine perisynaptic processes, which are poorly preserved in post-mortem tissue, differentially so by post-mortem interval, and are systematically under-represented in both homogenates and nuclear dissociation. Regional differences in PMI and in process preservation could generate the apparent regional pattern independently of preparation. This deserves at least a paragraph.

**R1.6 — Antibody epitope is raised as a risk-of-bias domain but never used.**
Table 7 lists antibody epitope as high risk. Given that Scott et al. (2011) and Gebhardt et al. (2010) establish that exon-skipping variants are present and functionally significant, whether a given antibody detects those variants determines what "total EAAT2" means in each study. The authors should state, where recoverable, which studies used N-terminal, C-terminal or variant-discriminating reagents, and acknowledge where it is unrecoverable.

## Minor comments

**R1.7** Kirvell et al. (2010) is a study of vesicular glutamate transporters in vascular dementia; EAAT2 is a secondary outcome. Its inclusion as a primary abundance comparison should be justified or it should be moved to a secondary set.

**R1.8** Thal et al. (2010) reports reduced perivascular EAAT2 only in the capillary-CAA subgroup. Listing it in Table 2 without that qualifier in the direction column is misleading; the qualifier appears only in the note.

**R1.9** The manuscript alternates between "Braak stage" and "pathological severity" when describing Scott et al. (2011), which used a different grading. Standardise or state the mapping.

**R1.10** Section 4.4 asserts that reported serum EAAT2 reductions "require replication." No serum study is cited. Either cite one or delete the sentence.

\newpage

# Reviewer 2 — Biostatistics and computational methods

## General assessment

The statistical work is transparent, the code is provided and runs, and the authors have pre-empted several objections in their own supplement. I commend the inclusion of a calibration analysis that reports its own failure (S6). However, two of the three novel quantitative claims are, on inspection, internally inconsistent with arguments the manuscript makes elsewhere, and the third dissolves under a coding change the authors do not test. I do not think any of these are fatal to the paper, but the abstract and the headline claims must be rewritten.

## Major comments

**R2.1 — The excess-significance inversion assumes exactly the condition the paper argues against.**
This is my principal concern. The implied effect size of d = 0.83 is obtained by equating the observed number of significant findings with the sum of per-study powers. That equation is valid only if publication is independent of significance. The manuscript argues at length — correctly — that this literature is subject to publication bias, and uses that argument to discount its own sign test in §3.5. The two positions cannot both hold. Under publication bias, significant studies are over-represented among published studies, the observed significance rate is inflated, and the implied d is biased upward.

The correction is straightforward and the authors should implement it. Let null results be published with probability *w* relative to significant results. Then the expected published-significant fraction is S/(S + w(k − S)) where S is the sum of powers. Solving across plausible *w* will show how much of d = 0.83 survives. I expect a substantial reduction. The value should be reported as an upper bound with an explicit bias-adjusted range, and the claimed "convergence" with the independent reuptake estimate of 0.75 should be presented as conditional on no bias rather than as corroboration.

**R2.2 — The "two adequately powered nulls" argument is circular.**
Section 3.4 declares Poirel (2018) and Garcia-Esparcia (2018) adequately powered on the basis of 98% and 76% power *at d = 0.75*. But d = 0.75 is the pooled effect for **reuptake**, and the entire thesis of the paper is that the abundance effect is smaller than the functional effect. You cannot benchmark abundance studies against the functional effect size while simultaneously arguing that the two differ. If the true abundance effect is d = 0.3 — entirely plausible under the authors' own model — Poirel's power is approximately 0.37 and Garcia-Esparcia's approximately 0.19, and neither is a credible null.

Since the claim that "bulk frontal EAAT2 abundance is genuinely preserved" is one of the paper's pivotal inferences (§3.6 explicitly builds on it), this needs to be recomputed across a range of assumed abundance effects and the conclusion adjusted.

**R2.3 — The preparation moderator does not survive direction-specific coding.**
Table 5 counts a study as having "detected an abnormality" if it found *any* deviation, including an **increase** in detergent-insoluble EAAT2 (Woltjer), the presence of insoluble species (Sasaki) or HNE adduction (Lauderback). These are increases in aberrant species, not reductions in functional transporter, and they are pooled with genuine reductions (Abdul, Tian) against homogenate studies scored only on whether normal transporter fell.

This makes the test close to tautological: a study that fractionates tissue specifically to look for an aberrant species will almost always find one. I asked what happens if only a reduction in normal transporter counts as detection. The table becomes [[2,3],[1,4]] and Fisher's exact p = 1.00. Dropping the insoluble studies entirely gives p = 0.46.

The headline claim that "tissue preparation, not brain region, predicts detection" therefore rests entirely on a coding decision that equates an increase in aggregated protein with a decrease in functional protein. This must be reported and the claim downgraded accordingly. Supplementary S4 tests six codings but not this one, which is the one that matters.

**R2.4 — The pivotal null is never quantified.**
The paper's central premise is that Soares et al. (2024) found EAAT2 abundance unchanged. Nowhere is a point estimate, confidence interval or number of contributing studies given for that null. "Not significant" is not "no effect." If the EAAT2 estimate were, say, SMD −0.40 with a wide interval from three studies, it would be entirely compatible with a real effect of the magnitude the authors infer, and the framing of "abundance preserved" would be unsupported. The authors must report k and the interval, or state plainly that these are not recoverable from the source and weaken the claim accordingly.

**R2.5 — Multiplicity.**
The manuscript performs, by my count, at least fifteen hypothesis tests across the main text and supplement without any adjustment. Given that the two significant results are at p = 0.048 and p = 0.016, and both are shown elsewhere to be fragile, the absence of any multiplicity discussion is conspicuous. A brief statement is needed even if formal correction is declined on the grounds that the analyses are exploratory.

**R2.6 — The calibration treats a measurable quantity as free.**
Supplementary S6 concludes that the compositional model requires an assay CV of about 0.73 and correctly flags this as unverified. But CV is estimable: Beckstrøm et al. (1999) reported inter-individual variability explicitly, and several studies show individual data points. The authors should attempt to bound CV empirically rather than leaving it as a free parameter; the model's viability depends on it.

## Minor comments

**R2.7** The vote-counting simulation (S8.1) uses a normal approximation while the power analysis uses the noncentral t. Harmonise, or state that the discrepancy is immaterial at these sample sizes.

**R2.8** Independence across the ten abundance comparisons is assumed but never checked. It appears to hold — each comes from a distinct group — but this should be stated rather than left implicit.

**R2.9** Table 2 mixes estimands (abundance, localisation, binding) in a single "direction of finding" column. Add an estimand column so readers can see which quantity each row reports.

**R2.10** The exact odds-ratio interval in S5 has a lower bound of 1.02. Given R2.3, this should be presented alongside the direction-specific recoding rather than in isolation.

**R2.11** Seeds are fixed and the code reproduces — this is done well and should be retained.

\newpage

# Author response

We thank both reviewers. The two structural criticisms — R2.1 and R2.3 — identified genuine internal inconsistencies, and R2.2 identified circular reasoning at a load-bearing point in the argument. We have implemented all three requested analyses, and the results were unfavourable in each case. We have rewritten the abstract, three results sections and the discussion accordingly, and downgraded two of our three novel claims. We have not attempted to defend positions the new analyses undermine.

## Response to Reviewer 1

**R1.1 (Kobayashi confound).** Accepted, and this is an important catch. GLT-1-positive area is not independent of neuropil preservation, and the reviewer is right that this is our own denominator argument turned against our strongest human evidence. Section 3.8.2 now states the confound explicitly and the discussion no longer describes this study as a natural experiment. We note it remains suggestive, because the astrocyte morphology differences reported in the same study are not obviously reducible to neuropil volume, but we no longer rest the resilience argument on it alone.

**R1.2 (neuronal EAAT2).** Accepted. Section 3.9 and the Figure 4 legend now state that the model addresses the astrocytic contribution only, and §4.5 notes that if a substantial fraction of the pooled uptake deficit is neuronal the compositional account is partial rather than complete.

**R1.3 (Masliah not EAAT2-specific).** Accepted. Masliah 1996 and Rothstein 1992 have been reclassified as non-EAAT2-specific transport measures. The sign test in §3.5 is recomputed on the six remaining EAAT2-specific significant findings; two-sided p rises from 0.016 to 0.031. Table S1 now carries an estimand column marking these rows.

**R1.4 (title).** Accepted. The title has been changed to remove "stage-stratified," which we agree we cannot deliver. The revised title reflects what the paper actually establishes.

**R1.5 (perisynaptic process preservation).** Accepted; a paragraph has been added to §4.3 identifying differential preservation of fine astrocytic processes as a third confound alongside region and preparation, and noting that it is not separable in the existing corpus.

**R1.6 (antibody epitope).** Partially addressed. We have added epitope information to Table S1 where the primary reports state it. For eleven of twenty-one studies it is not recoverable, and we now say so rather than leaving the domain unelaborated in the risk-of-bias table.

**R1.7–R1.10 (minor).** All accepted. Kirvell is now marked as a secondary outcome in Table 2; the Thal 2010 CAA restriction has been moved into the direction column; the Scott grading is now described as pathological severity throughout with the mapping stated; the unreferenced serum claim in §4.4 has been deleted.

## Response to Reviewer 2

**R2.1 (excess-significance assumes no bias).** Accepted; this was the most serious error in the manuscript. We implemented the reviewer's suggested correction. Results are given in new Supplementary Section S11 and summarised here:

| Null-result publication rate *w* | Implied d |
|---|---|
| 1.00 (no bias) | 0.83 |
| 0.75 | 0.73 |
| 0.50 | 0.60 |
| 0.33 | 0.48 |
| 0.25 | 0.41 |
| 0.10 | 0.21 |

The reviewer's expectation was correct. We now report d = 0.83 explicitly as an upper bound obtained under the assumption of no publication bias, with a plausible range of 0.41 to 0.83. The claimed convergence with the reuptake estimate of 0.75 is now presented as conditional on minimal bias rather than as independent corroboration, and the abstract has been rewritten. We are grateful for this comment; the original framing was indefensible.

**R2.2 (circular power benchmark).** Accepted. Recomputed across plausible abundance effects (new Supplementary Section S12):

| Assumed true abundance effect | Poirel 2018 power | Garcia-Esparcia 2018 power |
|---|---|---|
| 0.20 | 0.19 | 0.11 |
| 0.30 | 0.37 | 0.19 |
| 0.40 | 0.58 | 0.30 |
| 0.50 | 0.77 | 0.43 |
| 0.75 | 0.98 | 0.76 |

The reviewer is right that we cannot benchmark abundance studies against the functional effect size while arguing the two differ. Section 3.4 has been rewritten. We now claim only that these two studies exclude an abundance effect *as large as the functional effect*, which is a much weaker and more defensible statement. The pivotal inference in §3.6 has been correspondingly softened: the frontal homogenate result excludes a large abundance deficit but does not establish preservation.

**R2.3 (moderator dissolves under direction-specific coding).** Accepted. New Supplementary Section S13:

| Coding | Table | Fisher p |
|---|---|---|
| Any abnormality (as originally published) | [[5,0],[1,4]] | 0.048 |
| Reduction of normal transporter only | [[2,3],[1,4]] | **1.000** |
| Reduction only, insoluble studies excluded | [[2,1],[1,4]] | 0.464 |

We accept that the original coding equates an increase in aggregated transporter with a decrease in functional transporter, and that this is not defensible without argument. The claim that preparation rather than region predicts detection has been demoted from a headline finding to an observation about detection of *any* abnormality, explicitly flagged as coding-dependent and non-significant under the stricter definition. It has been removed from the abstract's list of findings and from the Highlights. Figure 2 retains the harvest plot, which is descriptive, but its subtitle no longer asserts the moderator claim.

**R2.4 (pivotal null unquantified).** Accepted and, we agree, a real gap. The source publication reports the EAAT2 result only as non-significant without a point estimate, confidence interval or contributing-study count in the text available to us. We now state this explicitly in §3.1 and in the limitations, and note that a non-significant pooled estimate with an unreported interval is weaker evidence for preservation than we originally implied. Our claim now rests primarily on the transcript-level null across approximately 1,670 AMP-AD samples, which is quantified and robust.

**R2.5 (multiplicity).** Accepted; a statement has been added to §2.4 acknowledging that at least fifteen tests are reported without adjustment, that no analysis was pre-registered, and that the two nominally significant results would not survive even modest correction.

**R2.6 (CV is estimable).** Partially addressed. We agree in principle. Beckstrøm et al. report high inter-individual variability but do not tabulate the dispersion needed to compute a CV, and figure-only reporting prevents extraction elsewhere. We have added this to §4.5 as a specific, tractable target for future work rather than leaving it implicit, and Supplementary S6 now states that the model's viability rests on an assumption that the existing literature does not permit us to test.

**R2.7–R2.11 (minor).** The vote-counting simulation now uses the noncentral t throughout, matching the power analysis; results are unchanged to two decimal places. Independence across the ten comparisons has been checked — each derives from a distinct research group — and is now stated in §2.4. Table 2 has an estimand column. The odds-ratio interval is now reported alongside the direction-specific recoding in S13 rather than in isolation. Seeds remain fixed and the accompanying code regenerates every reported value, including all new analyses.

## Summary of changes

- Title changed; "stage-stratified" removed.
- Abstract rewritten: implied effect size now reported as an upper bound with a bias-adjusted range; the preparation moderator removed from the findings list.
- Highlights revised: three deleted (the preparation-moderator claim, the adequately-powered-nulls claim and the Kobayashi resilience claim), two rewritten, two added.
- §3.1 now states that the pivotal null is unquantified in the source.
- §3.4 rewritten; the "adequately powered nulls" claim substantially weakened.
- §3.5 sign test recomputed on EAAT2-specific findings only (p = 0.031); implied effect size reported as a range.
- §3.6 moderator claim demoted and flagged as coding-dependent.
- §3.8.2 Kobayashi neuropil confound added.
- §3.9 and Figure 4 restricted to the astrocytic compartment.
- §4.3 third confound (process preservation) added.
- §4.5 limitations expanded to cover all of the above.
- New Supplementary Sections S11, S12, S13; Tables S10, S11, S12.
- Analysis script extended with the three new analyses.
