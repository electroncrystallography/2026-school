---
title: "Beyond typical 3D ED: 4D-STEM"
short_title: "4D-STEM"
---

# Beyond typical 3D ED: 4D-STEM

:::{div}
:class: ecs-session-meta
**Day 2 · Sunday 9 August · 9:00 – 10:00** — [Colin Ophus](../instructors.md#speaker-colin-ophus)
:::

:::{admonition} Hands-on tutorial
:class: tip
The web-based 4D-STEM tutorials for this block run in Google Colab — no installation needed: [tinyurl.com/nanobeam2026](https://tinyurl.com/nanobeam2026)
:::

## STEM & 4D-STEM

In scanning transmission electron microscopy, a converged electron probe is scanned over the sample. A conventional annular dark field (ADF) detector integrates the scattered signal to one number per probe position — but a pixelated detector can record the full diffraction pattern at every position: **2D images recorded over a 2D grid of probe positions — four-dimensional scanning transmission electron microscopy (4D-STEM)**.

The two signals of interest:

- **Crystalline scattering** — the position and intensity of the Bragg disks in each pattern act as a fingerprint for the local structure and orientation.
- **Amorphous scattering** — the position and shape of the amorphous halos act as a fingerprint for the local structure factor (the mean atomic arrangement).

### A complex sample, one dataset

:::{figure} ../assets/day2/four-d-stem/gto-overview.png
:alt: A 4D-STEM scan across an ion-irradiated and annealed gadolinium titanate sample, with regions labeled single crystal pyrochlore, recrystallized fluorite, mixed, polycrystalline fluorite, and amorphous
:width: 80%

One 4D-STEM experiment across ion-irradiated, annealed Gd₂Ti₂O₇ (pyrochlore) captures single-crystal, recrystallized, polycrystalline, mixed, and amorphous regions in a single scan [](doi:10.1017/S1431927621000477).
:::

### Choosing the probe convergence angle

The probe convergence semiangle controls the trade between real-space and diffraction-space resolution:

:::{figure} ../assets/day2/four-d-stem/conv-20mrad.jpg
:alt: 20 mrad semiangle: diffraction space probe, real space probe, crystalline scattering, and amorphous scattering
:width: 100%

**20 mrad semiangle** — atomic-resolution imaging, DPC, ptychography. (Left to right: diffraction-space probe, real-space probe, crystalline scattering, amorphous scattering.)
:::

:::{figure} ../assets/day2/four-d-stem/conv-2mrad.jpg
:alt: 2 mrad semiangle: diffraction space probe, real space probe, crystalline scattering, and amorphous scattering
:width: 100%

**2 mrad semiangle** — crystal strain mapping, polarization, superlattice ordering, amorphous medium-range order.
:::

:::{figure} ../assets/day2/four-d-stem/conv-02mrad.jpg
:alt: 0.2 mrad semiangle: diffraction space probe, real space probe, crystalline scattering, and amorphous scattering
:width: 100%

**0.2 mrad semiangle** — phase / orientation mapping, lattice parameters, amorphous short-range order.
:::

:::{figure} ../assets/day2/four-d-stem/aunp-convergence.jpg
:alt: Mean and individual diffraction patterns of gold nanoparticles on amorphous carbon, for convergence angles from 24 down to 1.5 mrad
:width: 100%

Gold nanoparticles on amorphous carbon: mean (top) and individual (bottom) diffraction patterns as the convergence angle steps from 24 to 1.5 mrad.
:::

In 4D-STEM, the probe size (via the convergence semiangle) and the step size between adjacent probe positions can be set **independently**. Guidelines:

- Feature/sample dependent — and beam damage must be considered
- Beam-sensitive samples: 5–500 nm probes
- Strain / orientation / FEM / RDF: 1–500 nm
- DPC / ptychography / imaging: 0.1–5 nm

:::{figure} ../assets/day2/four-d-stem/probe-step-guide.png
:alt: Diagram of undersampling and oversampling of probe positions relative to the probe size
:width: 55%
:::

### Electron beam damage

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/damage-timeseries.jpg
:alt: Diffraction pattern of a polymer at 0, 2, and 4 seconds of exposure, losing long-range order
Loss of long-range order with exposure time (defined-area diffraction of a polyethylene; Yan *et al.*, *Polymer* **135**, 2018).
:::

:::{figure} ../assets/day2/four-d-stem/damage-map.png
:alt: Grid of probe positions in a polymer electrolyte showing beam damage at each measured position
Probe positions showing damage: polymer electrolyte, 4D-STEM, 50×50 positions at 10 nm steps [](doi:10.1126/sciadv.adc9721).
:::

::::

We must either keep the total (local) exposure well below the critical dose, or take steps large enough to always probe undamaged material.

## 4D-STEM of crystals: phase, orientation, and strain

### Orientation mapping of organic molecular crystals

Bragg peaks are detected in each diffraction pattern: a template (from a vacuum reference probe or a synthetic disk) is matched against each pattern by image correlation, and the detected peaks are recorded.

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/nbed-schematic.png
:alt: Schematic of scanning nanobeam diffraction over a thin film, with example patterns
:::

:::{figure} ../assets/day2/four-d-stem/disk-detection.png
:alt: Diffraction pattern with detected Bragg peaks circled
:::

::::

:::{figure} ../assets/day2/four-d-stem/orientation-maps.jpg
:alt: Orientation maps of an organic semiconductor film without and with DIO additive, showing large continuously-turning domains versus small single-orientation domains
:width: 100%

Two film morphologies resolved by orientation mapping: without additive, single orientation through the thickness in large, continuously turning domains; with DIO additive, multiple orientations through the thickness in small single-orientation domains [](doi:10.1038/s41563-019-0387-3).
:::

### Strain mapping

A lattice in compression spreads the diffraction spots apart; a lattice in tension pulls them together — measuring the Bragg disk positions in each pattern maps the local reciprocal lattice, and from it the strain tensor. Note the sign change: we work in reciprocal space.

:::{figure} ../assets/day2/four-d-stem/strain-concept.png
:alt: Diagram of a probe on a strained lattice with the resulting change in diffraction spot spacing
:width: 55%
:::

Disk positions come from correlation template matching:

:::{figure} ../assets/day2/four-d-stem/correlation-method.png
:alt: Correlation of the measured pattern with a probe template, comparing cross, hybrid, and phase correlation with and without noise
:width: 95%

The correlation is calculated by convolution; cross-, hybrid-, and phase-correlation respond differently to noise [](doi:10.1017/S1431927621000477).
:::

:::{figure} ../assets/day2/four-d-stem/template-matching.png
:alt: Vacuum probe template, bright field image, and template matching by cross correlation with detected disks
:width: 100%
:::

:::{figure} ../assets/day2/four-d-stem/gto-strain-maps.png
:alt: Mean diffraction image and strain component maps of single-crystal pyrochlore and recrystallized fluorite
:width: 100%

Strain measured across the single-crystal pyrochlore / recrystallized fluorite interface of the Gd₂Ti₂O₇ sample.
:::

### Enhancing strain precision with patterned apertures

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/bullseye-method.png
:alt: Schematic of a bullseye-patterned condenser aperture producing patterned diffraction disks
"Bullseye" apertures, fabricated with FIB and installed in the second condenser aperture, imprint a sharp pattern on every diffraction disk [](doi:10.1016/j.ultramic.2019.112890).
:::

:::{figure} ../assets/day2/four-d-stem/bullseye-litho.png
:alt: TEM image of lithographically fabricated bullseye apertures from 2 to 20 micrometers
Lithographic bullseye apertures (2–20 μm). Want one for your TEM? We are giving them away — email <cophus@stanford.edu>.
:::

::::

### Automated crystal orientation mapping (ACOM)

Scanning nanobeam diffraction over polycrystalline samples, then matching each pattern against a **library of simulated diffraction patterns** over the unique orientations, yields phase and orientation maps ([](doi:10.1017/S1431927619000497); E. Rauch *et al.*, *Arch. Metall. Mater.* **50**, 87, 2005; [](doi:10.1021/cm201783z)).

:::{figure} ../assets/day2/four-d-stem/orientation-library.png
:alt: Diffraction pattern library calculated over the unique crystal orientations
:width: 70%

The diffraction-pattern library over the orientation sphere [](doi:10.1017/S1431927622000101).
:::

::::{grid} 1 1 1 1

:::{figure} ../assets/day2/four-d-stem/acom-matching.png
:alt: AuAgPd nanowire dataset: mean diffraction pattern, Bragg vector map, HAADF image, and Bragg peak histogram
The AuAgPd nanowire test dataset: mean diffraction pattern, Bragg vector map, simultaneous HAADF image, and Bragg peak histogram.
:::

:::{figure} ../assets/day2/four-d-stem/acom-maps.png
:alt: In-plane and out-of-plane orientation maps of the AuAgPd nanowire, with the orientation color legend
In-plane and out-of-plane orientation maps of the nanowire. Try it yourself: `py4DSTEM` notebook `orientation_01_AuAgPd_wire.ipynb`.
:::

::::

### Improving ACOM and strain: precession 4D-STEM

Like precession in 3D ED, tilting the beam during 4D-STEM acquisition — or acquiring a beam-tilt series of scans and summing them after cross-correlation alignment — integrates through the rocking curves and fills in the diffraction patterns:

:::{figure} ../assets/day2/four-d-stem/precession-4dstem.png
:alt: Data acquisition of a 5-scan beam tilt series with descan alignment and cross correlation of the scans
:width: 100%

Multi-beam-tilt 4D-STEM acquisition (S. Ribet *et al.*, [arXiv:2506.11327](https://arxiv.org/abs/2506.11327)).
:::

:::{figure} ../assets/day2/four-d-stem/precession-results.png
:alt: Single and mean diffraction patterns and strain maps comparing conventional and multi-beam-tilt acquisition
:width: 95%
:::

### Phase mapping of ferroelectric HZO

:::{figure} ../assets/day2/four-d-stem/hzo-structures.png
:alt: The candidate HZO crystal structures: monoclinic, tetragonal, and centrosymmetric and ferroelectric orthorhombic phases
:width: 100%

Hafnium–zirconium oxide (HZO) films can crystallize in several phases — the ferroelectric orthorhombic phase (Pca2₁) among them [](doi:10.1093/mam/ozaf019).
:::

:::{figure} ../assets/day2/four-d-stem/hzo-confusion.png
:alt: Simulated classification results for the HZO phases including silicon and titanium nitride
:width: 80%

Dynamical Bloch-wave simulations of the four HZO phases plus Si and TiN test the phase classification — good accuracy, with room for improvement (future: ML classification, dynamical inversion).
:::

:::{figure} ../assets/day2/four-d-stem/hzo-stack.jpg
:alt: The HZO film stack and the resulting dark field, reliability, and phase maps
:width: 90%

Phase and orientation mapping of the functional HZO layer between TiN electrodes on silicon.
:::

## 4D-STEM of disordered materials

Ideally, the diffracted signal is simply a 2D Fourier transform of the projected potential, multiplied by the probe intensity. The position and shape of the amorphous halos fingerprint the local structure factor. Interpretation is complicated by multiple/dynamical scattering (thickness effects) and background — more so than for crystal diffraction.

### The electron pair distribution function (PDF)

P(r): the probability of finding an atom inside a radial shell, normalized to the mean density.

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/ata-structure.png
:alt: Simulation cell of amorphous tantalum
Amorphous tantalum, abTEM multislice simulation (coordinates from Jun Ding and Mark Asta, *Scientific Reports* **5**, 2015).
:::

:::{figure} ../assets/day2/four-d-stem/pdf-groundtruth.png
:alt: Ground-truth pair distribution function of the simulated structure
The ground-truth PDF of the simulated structure.
:::

::::

From the measured patterns, the analysis runs radial mean → reduced structure factor → sine transform to the PDF:

:::{figure} ../assets/day2/four-d-stem/radial-mean.jpg
:alt: Log radial mean of the diffraction signal for elastic scattering only, and with a synthetic inelastic background at low angles
:width: 100%

Log radial mean: elastic scattering only (left) vs. with a synthetic inelastic background at low angles (right).
:::

:::{figure} ../assets/day2/four-d-stem/structure-factor.jpg
:alt: Reduced structure factors for the elastic-only and with-background cases
:width: 100%

The reduced structure factor for both cases.
:::

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/pdf-elastic.png
:alt: PDF computed from elastic scattering only
PDF from elastic scattering only.
:::

:::{figure} ../assets/day2/four-d-stem/pdf-background.png
:alt: PDF computed with the synthetic inelastic background present
PDF with the inelastic background present.
:::

::::

The PDF magnitude is quantitatively correct **with energy filtering**.

## Ptychography and phase contrast in 4D-STEM

Phase-contrast HRTEM resolves light-atom structures — for example grain boundaries in suspended polycrystalline graphene [](doi:10.1186/s40679-016-0030-1):

:::{figure} ../assets/day2/four-d-stem/graphene-gb.jpg
:alt: HRTEM images of grain boundaries in polycrystalline graphene
:width: 95%
:::

STEM phase-contrast measurements reach the same contrast mechanisms — sample Coulomb potential [](doi:10.1038/nphys2337), electric fields [](doi:10.1038/srep10040), magnetic fields [](doi:10.1016/j.ultramic.2016.03.006).

### Differential phase contrast (DPC)

If we can measure the shift of the disk-shaped probe in diffraction space, we can estimate the derivative of the potential (the field). The shift can come from a segmented detector (top/bottom, left/right differences) or from the probe's center of mass on a pixelated camera. A grid of these measurements lets us numerically reconstruct the 2D sample potential — phase-contrast imaging.

:::{figure} ../assets/day2/four-d-stem/dpc-infinite.jpg
:alt: Center-of-mass DPC reconstructions at infinite dose for 2, 6, and 32 mrad probes
:width: 100%

CoM-DPC at **infinite dose**, for 2, 6, and 32 mrad probes: small convergence angles fail to recover high spatial frequencies; large angles recover them.
:::

:::{figure} ../assets/day2/four-d-stem/dpc-500e.jpg
:alt: Center-of-mass DPC reconstructions at 500 electrons per probe for 2, 6, and 32 mrad probes
:width: 100%

The same reconstructions at **500 electrons/probe**: now the large-angle probe suffers significant low-spatial-frequency errors, while the small-angle probe has almost none — the optimum depends on dose.
:::

### Iterative ptychography

Ptychography reconstructs the object wave by gradient descent, alternating forward- and back-projections between real space and diffraction space — with either focused or defocused probes:

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/four-d-stem/ptycho-focused.png
:alt: Schematic of focused-probe ptychography
"Focused probe" ptychography.
:::

:::{figure} ../assets/day2/four-d-stem/ptycho-defocused.png
:alt: Schematic of defocused-probe ptychography
"Defocused probe" ptychography (G. Varnavides\*, S. Ribet\* *et al.*, [arXiv:2309.05250](https://arxiv.org/abs/2309.05250)).
:::

::::

:::{figure} ../assets/day2/four-d-stem/phase-comparison.png
:alt: Comparison of STEM phase contrast methods on gold nanoparticles on a carbon support with a highly defocused probe
:width: 100%

STEM phase-contrast method comparison: Au nanoparticles on carbon, highly defocused probe — dark field, DPC, parallax, and ptychography after 5 and 150 iterations.
:::

## Beyond 4D-STEM: in situ and 5D-STEM

### In situ mechanical testing + 4D-STEM

CrCoNi-based medium/high-entropy alloys — single-phase equiatomic mixtures of 3+ metals with the highest fracture toughnesses ever recorded — deform through long, thin planar defects ([](doi:10.1126/science.abp8070); [](doi:10.1126/sciadv.adf8602)).

:::{figure} ../assets/day2/four-d-stem/hea-defects.png
:alt: STEM images of long thin planar defects in a deformed high-entropy alloy
:width: 85%
:::

:::{figure} ../assets/day2/four-d-stem/insitu-setup.png
:alt: In situ push-to-pull mechanical testing setup combined with energy-filtered 4D-STEM, with HAADF imaging, virtual-image defect maps, and bullseye strain mapping
:width: 90%

In situ cyclic loading combined with energy-filtered 4D-STEM (Gatan K3): HAADF imaging, defect mapping from virtual images, and bullseye strain mapping [](doi:10.1038/s41467-024-45696-z).
:::

:::{figure} ../assets/day2/four-d-stem/insitu-cycles.png
:alt: Stacking fault maps of CrCoNi over cyclic deformation at t = 0, T/2, T, and 1000T, compared with pure Ni
:width: 100%

Deformation of the CrCoNi medium-entropy alloy creates *reversible* stacking faults — which become irreversible after ~1000 cycles, indicating lower stacking-fault energy and rejuvenation.
:::

### Ptychographic atomic electron tomography

:::{figure} ../assets/day2/four-d-stem/aet-modes.png
:alt: HAADF, DPC, and ptychography images of a ZrTe nanowire encapsulated in a double-walled carbon nanotube
:width: 100%

A ZrTe-sandwich nanowire encapsulated in a double-walled carbon nanotube, imaged by HAADF (50–120 mrad), DPC, and ptychography [](doi:10.1038/s41467-023-43634-z).
:::

:::{figure} ../assets/day2/four-d-stem/aet-result.png
:alt: 3D atomic model of the ZrTe nanowire reconstructed by ptychographic atomic electron tomography
:width: 80%

Ptychographic tilt-series tomography resolves the full 3D atomic structure — including a previously unobserved ZrTe₂ phase.
:::

## Resources

- **4D-STEM review**: [](doi:10.1017/S1431927619000497)
- **py4DSTEM**: [github.com/py4DSTEM](https://www.github.com/py4dstem) — paper: [](doi:10.1017/S1431927621000477)
- **Dose-aware phase retrieval metrics**: G. Varnavides *et al.*, [arXiv:2507.19476](https://arxiv.org/abs/2507.19476)
- **quantEM** — open-source quantitative electron microscopy spanning diffraction, imaging, tomography, and spectroscopy: [github.com/electronmicroscopy/quantem](https://github.com/electronmicroscopy/quantem) · [tutorials](https://github.com/electronmicroscopy/quantem-tutorials)
- **Colab tutorials for this block**: [tinyurl.com/nanobeam2026](https://tinyurl.com/nanobeam2026)
