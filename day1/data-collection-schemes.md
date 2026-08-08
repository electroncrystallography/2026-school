---
title: "3D ED: core idea & data collection schemes"
short_title: "3D ED data collection"
---

# 3D ED: core idea & data collection schemes

:::{div}
:class: ecs-session-meta
**Day 1 · Saturday 8 August · 10:00 – 11:00** — T. Gorelik  
Lecture
:::

:::{note}
This page is converted from Tatiana Gorelik's lecture slides. The figures and animations are taken directly from the deck.
:::

## A bit of history

… many years ago… around 2004…

Electron diffraction was used to pre-orient crystals for high-resolution TEM imaging.

:::{figure} ../assets/day1/data-collection/hrtem-quasicrystal.jpg
:alt: High-resolution TEM image of a dodecagonal quasicrystal with an inset diffraction pattern
:width: 75%

High-resolution TEM imaging guided by electron diffraction. Krumeich *et al.*, *Journal of Solid State Chemistry* **194** (2012) 106–112; image: Chuvilin, nanoGUNE, San Sebastián.
:::

### Tilt series — zonal patterns

A tilt series of zonal patterns, recorded by tilting the crystal on the goniometer:

::::{grid} 2 2 4 4

:::{figure} ../assets/day1/data-collection/holder-double-tilt.jpg
:alt: Double-tilt specimen holder
Double-tilt
:::

:::{figure} ../assets/day1/data-collection/holder-tilt-rotation.jpg
:alt: Dual-axis tilt-rotation specimen holder
Dual-axis: tilt-rotation
:::

::::

::::{grid} 2 3 3 3

:::{figure} ../assets/day1/data-collection/zonal-000.png
:alt: Zonal diffraction pattern at 0 degrees, zone [001]
0°
:::

:::{figure} ../assets/day1/data-collection/zonal-017.png
:alt: Zonal diffraction pattern at 17 degrees
17°
:::

:::{figure} ../assets/day1/data-collection/zonal-023.png
:alt: Zonal diffraction pattern at 23 degrees
23°
:::

:::{figure} ../assets/day1/data-collection/zonal-032.png
:alt: Zonal diffraction pattern at 32 degrees
32°
:::

:::{figure} ../assets/day1/data-collection/zonal-040.png
:alt: Zonal diffraction pattern at 40 degrees
40°
:::

:::{figure} ../assets/day1/data-collection/zonal-051.png
:alt: Zonal diffraction pattern at 51 degrees
51°
:::

::::

The zonal patterns of a tilt series share the common tilt axis, and can be assembled into a **Vainshtein plot** of the reciprocal lattice (here with rows indexed along a₁\*, a₂\*, a₃\*).

The same tilt-series approach appears in the discovery of quasicrystals:

:::{figure} ../assets/day1/data-collection/quasicrystal-tilt-series.jpg
:alt: Selected-area electron diffraction patterns from a single grain of the icosahedral phase at a series of rotation angles
:width: 85%

"Selected-area electron diffraction patterns taken from a single grain of the icosahedral phase. Rotations match those in Fig. 1." — Shechtman *et al.*, "Metallic Phase with Long-Range Orientational Order and No Translational Symmetry", *Physical Review Letters* (1984). The discovery of quasicrystals was awarded the Nobel Prize in Chemistry 2011 (Dan Shechtman).
:::

## What is wrong with zonal patterns?

- Data completeness
- Dynamical effects
- Intensity partiality
- Crystal alignment
- Automation

:::{figure} ../assets/day1/data-collection/ewald-sphere-rotation.mp4
:alt: Animation of the Ewald sphere cutting through reciprocal lattice spots, with the resulting diffraction pattern on the detector
:width: 90%

Ewald sphere and diffraction spots (left), and the resulting diffraction pattern on the detector (right).
:::

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/watermelon.jpg
:alt: Watermelon with cut slices
:::

:::{figure} ../assets/day1/data-collection/needle-crystals.jpg
:alt: Rendering of many needle-shaped crystals lying on a substrate
Crystals on a support.
:::

::::

### Dynamical scattering of electrons

:::{figure} ../assets/day1/data-collection/dynamical-pattern.jpg
:alt: Zone-axis electron diffraction pattern with strong dynamical intensities
:width: 55%
:::

### Reflection intensity

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/extinctions-zonal.png
:alt: Zonal diffraction pattern showing rows of reflections including extinct ones
Extinctions due to the 6₁ screw axis.
:::

:::{figure} ../assets/day1/data-collection/extinctions-offzone.png
:alt: Off-zone diffraction patterns where the extinct reflections vanish
"Off-zone" patterns.
:::

::::

Courtesy of P. Oleynikov.

### Electron beam precession

> Double conical beam-rocking system for measurement of integrated electron diffraction intensities.
> — Vincent, Midgley, *Ultramicroscopy* **53**, 271 (1994).

The beam is rotating very fast, avoiding the exact in-zone orientation (scan above the specimen, de-scan below).

:::{figure} ../assets/day1/data-collection/precession-geometry.png
:alt: Diagram of the precessing incident beam, the Ewald sphere, and the precession wedge sweeping through relrods
:width: 60%

The precessing incident beam sweeps the Ewald sphere through a wedge of reciprocal space.
:::

:::{figure} ../assets/day1/data-collection/precession-pattern-series.mp4
:alt: Animation of a diffraction pattern as the beam precesses
:width: 80%

Courtesy of C.S. Own, L. Marks (Northwestern Univ., USA).
:::

## 3D ED — the idea

### Towards 3D data

Record diffraction patterns at many stage tilts, and treat them together as a sampling of the 3D reciprocal space.

::::{grid} 3 3 3 3

:::{figure} ../assets/day1/data-collection/disc-single.jpg
:alt: A single flat disc representing one diffraction pattern in reciprocal space
:::

:::{figure} ../assets/day1/data-collection/disc-few.jpg
:alt: A few discs at different tilts sharing a common axis
:::

:::{figure} ../assets/day1/data-collection/disc-sphere.jpg
:alt: Many discs at many tilts filling a sphere of reciprocal space
:::

::::

:::{figure} ../assets/day1/data-collection/pattern-cred.jpg
:alt: Electron diffraction pattern of an arbitrarily oriented crystal
:width: 55%

Irregularly spaced 3D reciprocal data.
:::

Systematic sampling of the reciprocal space within the available tilting range of the goniometer, e.g. −60°… 60°, tilt step 1°:

:::{figure} ../assets/day1/data-collection/tilt-series-patterns.mp4
:alt: Animation stepping through the diffraction patterns of a systematic tilt series
:width: 65%
:::

:::{figure} ../assets/day1/data-collection/wedge-stack.jpg
:alt: Stack of tilted planes forming a wedge of sampled reciprocal space
:width: 55%
:::

- Arbitrary tilt axis ⇒ not-oriented diffraction patterns
- Data processing needs dedicated methods

### 3D ED data collection

- Electron diffraction patterns in transmission mode
- Arbitrary crystallographic axis
- Stage tilt with a fine (1°) step
- High total tilt range (±60°)

Data geometry: common axis (the tilt axis).

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/wedge-a.jpg
:alt: Rendering of the sampled reciprocal-space wedge, side view
:::

:::{figure} ../assets/day1/data-collection/wedge-b.jpg
:alt: Rendering of the sampled reciprocal-space wedge, viewed along the tilt axis
:::

::::

## Electron diffraction in a (S)TEM

### Ray diagram: convex lens

:::{figure} ../assets/day1/data-collection/lens-ray-diagram.gif
:alt: Ray diagram of a convex lens with object, focal points, and image
:width: 70%

<http://hyperphysics.phy-astr.gsu.edu/hbase/geoopt/image.html#c1>
:::

### Geometry: electron diffraction

:::{figure} ../assets/day1/data-collection/tem-ray-paths.jpg
:alt: Ray paths through a TEM column in imaging mode and diffraction mode, from electron source to screen
:width: 80%

Column ray paths for imaging and diffraction: SAED, nano/micro-ED, STEM.
:::

### 4D-STEM (x, y, k<sub>x</sub>, k<sub>y</sub>)

:::{figure} ../assets/day1/data-collection/phase-retrieval-abcs.png
:alt: Overview figure of TEM phase contrast imaging, nanobeam 4D-STEM, and large-convergence-angle 4D-STEM geometries
:width: 70%

Varnavides, G., Kleijne, W.P.M.d. & Ribet, S.M. The ABCs of phase retrieval: Connecting the acronyms of scanning transmission electron microscopy. *MRS Bulletin* **51**, 897–912 (2026).
:::

:::{figure} ../assets/day1/data-collection/convergence-angles.jpg
:alt: Schematic of beams with decreasing convergence angle focused by the objective lens onto the back focal plane
:width: 80%

Convergent Beam Electron Diffraction (CBED): the convergence angle sets whether Bragg disks overlap in the back focal plane of the objective lens (the 1st diffraction pattern).
:::

::::{grid} 3 3 3 3

:::{figure} ../assets/day1/data-collection/cbed-disks.jpg
:alt: CBED pattern with large overlapping disks
:::

:::{figure} ../assets/day1/data-collection/nanobeam-pattern-a.jpg
:alt: Nanobeam diffraction pattern with small disks
:::

:::{figure} ../assets/day1/data-collection/nanobeam-pattern-b.jpg
:alt: Nanobeam diffraction pattern with sharp spots
:::

::::

## ADT — automated diffraction tomography

The starting problem: **small crystals**, **beam sensitive** — what is the crystal structure?

- Combined imaging (STEM) and diffraction (nanodiffraction)
- Collect diffraction data
- Track the crystal

:::{figure} ../assets/day1/data-collection/adt-kolb-2007.png
:alt: Figure from Kolb et al. 2007 showing a microprobe STEM image used for crystal tracking and the diffraction patterns of a tilt series
:width: 90%

Microprobe STEM imaging used for tracking, with selected diffraction patterns from the tilt series. U. Kolb *et al.*, *Ultramicroscopy* **107** (2007) 507–513.
:::

### 3D ED data

The data is collected in a cylindrical coordinate system (approximation).

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/cylindrical-sampling.jpg
:alt: View along the tilt axis showing recorded reflections in red and missing reflections in blue
View along the tilt axis: recorded reflections (red), missing reflections (blue).
:::

:::{figure} ../assets/day1/data-collection/tilt-fan.jpg
:alt: Fan of measurement planes about the tilt axis
The fan of measured planes about the tilt axis.
:::

::::

### Missing cone / missing wedge

::::{grid} 3 3 3 3

:::{figure} ../assets/day1/data-collection/grid-tweezers-a.jpg
:alt: TEM grid held in tweezers, viewed edge-on at low tilt
:::

:::{figure} ../assets/day1/data-collection/grid-tweezers-b.jpg
:alt: TEM grid held in tweezers, tilted to high angle
:::

:::{figure} ../assets/day1/data-collection/grid-loading.jpg
:alt: TEM grid viewed through the binocular while loading
:::

::::

:::{figure} ../assets/day1/data-collection/reciprocal-volume-wedge.mp4
:alt: Rotating reconstructed reciprocal-space volume showing the missing wedge of unmeasured data
:width: 85%

Reconstructed reciprocal-space volume: the unmeasured region forms the missing cone / missing wedge.
:::

## Reflection partiality

### 3D ED reflections' intensities

- Tilt increment — how fine can we sample the [3D space]⁻¹
- Experimentally 0.2° is the limit
- Still patterns within the range 0° … 0.2° … 1°

:::{figure} ../assets/day1/data-collection/still-pattern-streaks.jpg
:alt: Still diffraction pattern of a crystal showing partially recorded reflections
:width: 60%
:::

:::{figure} ../assets/day1/data-collection/rocking-curve-alq3.mp4
:alt: Animation stepping the tilt of an AlQ3 crystal in 0.2 degree increments; the intensity profile of two reflections changes strongly from frame to frame
:width: 90%

AlQ₃, still patterns at tilt positions between 0° and 1°: the reflection intensities change strongly from one tilt position to the next.
:::

### Filling the gaps — precession

Tilt step 1°, precession angle 0.5° or larger → **precession-assisted 3D ED (ADT)**.

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/precession-geometry.png
:alt: Precession wedge diagram
Incident beam, Ewald sphere, and precession wedge.
:::

:::{figure} ../assets/day1/data-collection/petal-sampling.jpg
:alt: Rendering of the reciprocal-space volume swept by precession at successive tilts
The volume swept at successive stage tilts.
:::

::::

Away from "static" patterns — combined stage / beam tilt, "linear precession":

:::{figure} ../assets/day1/data-collection/linear-precession-laue.jpg
:alt: Figure showing Laue circles for beam tilt offsets of 0, 1.75, and -1.95 degrees
:width: 85%
:::

### Filling the gaps — beam tilt

Combined stage tilt (step ~2°) + high-precision beam tilt (step 0.05°) → **rotation 3D ED (RED)**.

:::{figure} ../assets/day1/data-collection/beam-tilt-series.jpg
:alt: High-precision beam-tilt series performed in 0.05 degree intervals by the rotation method
:width: 80%

*Z. Kristallogr.* **225** (2010) 94–102.
:::

## Fast detectors — digital integration

### Filling the gaps — continuous rotation

Rotate the stage continuously while the detector reads out frames → **continuous-rotation 3D ED (microED)**.

:::{figure} ../assets/day1/data-collection/still-vs-continuous.jpg
:alt: Comparison of the still-diffraction method and the continuous-rotation method, with the resulting diffraction patterns
:width: 90%

Still-diffraction method vs. continuous-rotation method. *Nature Methods* **11**, 927–930 (2014).
:::

### Integration geometry

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/integration-continuous.mp4
:alt: Animation of the reciprocal-space volume integrated by continuous rotation
Continuous rotation geometry.
:::

:::{figure} ../assets/day1/data-collection/integration-precession.mp4
:alt: Animation of the reciprocal-space volume integrated by precession
Precession geometry.
:::

::::

### Instrumental solutions — SerialEM

:::{figure} ../assets/day1/data-collection/serialem-workflow.png
:alt: SerialEM workflow: find crystals on the grid, store coordinates in the Navigator, set eucentric height, set batch parameters, start script
:width: 85%

MicroED data collection with SerialEM (SerialEM / Gunter Resch). M.J. de la Cruz *et al.*, *Ultramicroscopy* **201** (2019) 77–80.
:::

### Instrumental solutions — Tecnai scripting + CETA dynamic control

Sequence:

1. Setup for ED, go to the starting angle
2. Blank the beam
3. Start the script — it has a 3 s delay
4. Start the recording
5. The script will unblank the beam and start rotation
6. After the end-tilt position is reached, the script will blank the beam
7. Stop recording

Parameters to play with are the **integration time** and the **rotation speed**.

:::{figure} ../assets/day1/data-collection/rotation-speed-control.png
:alt: Home-built rotation speed control interface with Search, Acquire, and Record panels
:width: 85%
:::

:::{figure} ../assets/day1/data-collection/ceta-rotation-movie.mp4
:alt: Continuous-rotation diffraction movie of Cu chloro-phthalocyanine recorded on a CETA camera
:width: 70%

Cu chloro-phthalocyanine.
:::

## New problem — crystal tracking

### Beam size

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/beam-size-needles.png
:alt: Needle crystals in the microscope with the illuminated area marked
:::

:::{figure} ../assets/day1/data-collection/beam-size-disc.jpg
:alt: The illuminated beam disc on the specimen
:::

::::

### Beam size — continuous rotation

- The sphere of confusion is typically 1–1.5 microns
- This sets the typical beam diameter
- If the crystal is smaller — it effectively becomes a smaller fraction of the scattering volume

Smaller beam ⇒ crystal tracking ⇒ pre-tilt.

:::{figure} ../assets/day1/data-collection/crystal-drift.mp4
:alt: Movie of a crystal drifting out of the illuminated area during continuous rotation
:width: 60%
:::

### Crystal tracking in continuous rotation?

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/beam-rings.jpg
:alt: Defocused diffraction rings used to monitor the crystal position
:::

:::{figure} ../assets/day1/data-collection/stage-calibration.png
:alt: Tomography stage calibration curves: X and Y stage offsets versus stage tilt angle
Tomo stage calibration curves.
:::

::::

### Instrumental solutions — Instamatic

Instamatic — Stef Smeets, Daniel Tchoń.

:::{figure} ../assets/day1/data-collection/cred-pattern-stream.mp4
:alt: Continuous-rotation electron diffraction data stream recorded with Instamatic
:width: 60%

Data: Stef Smeets, <https://doi.org/10.5281/zenodo.2633052>.
:::

:::{figure} ../assets/day1/data-collection/instamatic-github.png
:alt: The instamatic-dev organization on GitHub, with the instamatic and edtools repositories
:width: 80%
:::

### Instrumental solutions — Fast ADT

Fast ADT — Sergi Plana Ruiz. A DigitalMicrograph plug-in, with pre-tilt routines.

:::{figure} ../assets/day1/data-collection/fast-adt-flowchart.png
:alt: Fast ADT acquisition flowchart covering both sequential and continuous acquisition, with crystal tracking
:width: 60%
:::

### 3D 4D-STEM

- Amount of data
- Acquisition time
- Processing (alignment)
- Precess or not precess?

::::{grid} 3 3 3 3

:::{figure} ../assets/day1/data-collection/stem4d-scan.mp4
:alt: 4D-STEM scan animation
:::

:::{figure} ../assets/day1/data-collection/nanoparticle-cluster.jpg
:alt: STEM image of an agglomerate of nanocrystals, 500 nm scale
500 nm field of view.
:::

:::{figure} ../assets/day1/data-collection/tensor-instrument.jpg
:alt: The Tescan TENSOR instrument
TENSOR (Tescan).
:::

::::

## Data collection options

### Commercial solutions

4 commercial solutions (all continuous rotation):

- **Complete instruments**
  - RIGAKU / JEOL (Synergy-ED)
  - ELDICO (ED-1)
- **Plug-ins**
  - TFS — EPU-D
  - GATAN — Latitude-D

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/data-collection/synergy-ed.png
:alt: Rigaku/JEOL Synergy-ED instrument
Rigaku / JEOL Synergy-ED.
:::

:::{figure} ../assets/day1/data-collection/eldico-ed1.png
:alt: ELDICO ED-1 instrument
ELDICO ED-1.
:::

::::

### Custom solutions

Custom solutions (depending on the instrument setup):

| Hardware | Communication protocol |
| --- | --- |
| Precession? | … |
| Detector? | |
| … | |

### Summary: data collection schemes

| Still patterns | Precession-assisted data collection | Continuous rotation |
| --- | --- | --- |
| (small tilt increments) | | (crystal tracking?) |

## References

As cited in the slides:

- R. Vincent, P.A. Midgley, "Double conical beam-rocking system for measurement of integrated electron diffraction intensities", *Ultramicroscopy* **53**, 271 (1994).
- U. Kolb *et al.*, *Ultramicroscopy* **107** (2007) 507–513.
- D. Shechtman *et al.*, "Metallic Phase with Long-Range Orientational Order and No Translational Symmetry", *Physical Review Letters* (1984).
- F. Krumeich *et al.*, *Journal of Solid State Chemistry* **194** (2012) 106–112.
- "Collecting 3D electron diffraction data by the rotation method", *Z. Kristallogr.* **225** (2010) 94–102.
- *Nature Methods* **11**, 927–930 (2014).
- M.J. de la Cruz *et al.*, "MicroED data collection with SerialEM", *Ultramicroscopy* **201** (2019) 77–80.
- G. Varnavides, W.P.M.d. Kleijne, S.M. Ribet, "The ABCs of phase retrieval: Connecting the acronyms of scanning transmission electron microscopy", *MRS Bulletin* **51**, 897–912 (2026).
- Test dataset: Stef Smeets, <https://doi.org/10.5281/zenodo.2633052>.
