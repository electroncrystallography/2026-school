---
title: "Practical demonstration: DIALS"
short_title: "Demo: DIALS"
---

# Practical demonstration: DIALS

:::{div}
:class: ecs-session-meta
**Day 1 · Saturday 8 August · 16:30 – 17:30** — [Marcus Gallagher-Jones](../instructors.md#speaker-marcus-gallagher-jones)
:::

An introduction to DIALS for 3D ED / MicroED. This tutorial covers: an introduction to the DIALS software suite, key features important to 3D ED/MicroED, getting started and installation, and a worked example.

## Introduction to the DIALS package

**DIALS** — *Diffraction Integration for Advanced Light Sources* ([dials.github.io](https://dials.github.io/)):

- A decade and a half of development; international open-source software collaboration
- General framework and toolkit
- Single crystal rotation and stills, MX and CX
- X-rays, electrons, neutrons

:::{figure} ../assets/day1/demo-dials/workflow.png
:alt: The general workflow of data processing in DIALS from images to merged data
:width: 95%

The general workflow of data processing in DIALS.
:::

DIALS is driven from the command line — `dials.import`, `dials.find_spots`, `dials.find_rotation_axis`, `dials.index`, `dials.refine_bravais_settings`, `dials.refine`, `dials.integrate`, `dials.symmetry`, `dials.scale`, `dials.export`, … about 90 `dials.*` commands in version 3.29.0.

## DIALS for 3D ED / MicroED

Since 2018, features added for MicroED [](doi:10.1107/S2059798318007726) include the distortion correction map, beam drift modelling, refinement diagnostics, image format readers, spot finding for Ceta-D, rotation axis determination, serial ED indexing, and beam centre determination.

General strengths: open-source extensible framework · scripting · multi-crystal analysis · familiarity for structural biologists · support from DLS/CCP4/LBNL.

### Challenges for electron diffraction

- Almost flat Ewald sphere, high detector distance, low diffraction angle
- Joint refinement of detector and unit cell may not be possible; refined parameters may be poor
- Indexing from a single image is challenging; even the rotation direction can be ambiguous
- The beam centre may be unknown, and can drift
- Lens distortions may introduce systematic error in observed positions

**The biggest headache remains handling image formats!** Many EM formats lack the diffraction metadata needed for automatic processing. DIALS handles formats via plugins (`dxtbx.install_format`, [dxtbx_ED_formats](https://github.com/dials/dxtbx_ED_formats)), or the metadata can be supplied by hand at import.

:::{figure} ../assets/day1/demo-dials/format-zoo.png
:alt: The many electron microscopy image formats
:width: 55%

The format zoo.
:::

Incorrect imports can lose chiral information — be particularly wary with MRC files:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/chirality-a.png
:alt: Structure solution in one detector orientation
:::

:::{figure} ../assets/day1/demo-dials/chirality-b.png
:alt: Mirrored structure solution from a flipped detector orientation
Which orientation is correct?
:::

::::

A solution may come from following the X-ray world: HDF5 ← NeXus ← NXmx — a standardised format with metadata embedded at collection time [](doi:10.1016/j.str.2023.07.004):

:::{figure} ../assets/day1/demo-dials/nexus.png
:alt: Standard data format proposal for 3D ED and MicroED
:width: 60%
:::

## Key DIALS functions for ED data

Post-specimen lenses can induce ellipticity, rotation of the diffraction plane, and displacement of the central beam — DIALS has tools for all of these.

### Elliptical distortion correction

:::{figure} ../assets/day1/demo-dials/distortion.png
:alt: The elliptical distortion tool in the dials image viewer
:width: 70%

Built into `dials.image_viewer`: click points around a powder ring to fit the ellipse, then `dials.generate_distortion_map` writes the dx/dy displacement maps. Most modern microscopes have ellipticities of ~1% or better. (Thanks to David Waterman and Takanori Nakane.)
:::

### Spot finding

The default algorithm was optimized for photon-counting detectors, and works well for hybrid pixel array detectors. For CMOS/integrating detectors, a structured background throws it off — use the **radial average** algorithm instead (`dials.image_viewer` → threshold settings):

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/spotfind-cmos.png
:alt: Structured background confusing the default spot finding threshold
Default algorithm on CMOS data.
:::

:::{figure} ../assets/day1/demo-dials/spotfind-radial.png
:alt: Radial average threshold cleanly separating spots from background
Radial average algorithm.
:::

::::

### Rotation axis determination

Changes to the projection optics rotate the diffraction plane relative to the detector; an incorrect rotation axis makes it impossible to find the reciprocal lattice. `dials.find_rotation_axis` runs a coarse then fine search (sub-degree precision), scoring each step on a cylindrical projection of difference vectors (algorithm from Kolb *et al.*, *MRS Symp. Proc.* **1184**, 2009):

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/rotaxis-a.png
:alt: Cylindrical projection with a wrong rotation axis
:::

:::{figure} ../assets/day1/demo-dials/rotaxis-b.png
:alt: Cylindrical projection with the correct rotation axis
:::

::::

### Beam centre determination

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/beamcentre-line.png
:alt: Line tool bisecting Friedel pairs to find the beam centre
The line tool in the image viewer: bisect a line between two Friedel mates.
:::

:::{figure} ../assets/day1/demo-dials/beamcentre-algo.png
:alt: Inversion and midpoint beam centre algorithms
Inversion and midpoint algorithms, designed for 3D ED data with high background or visible Friedel pairs.
:::

::::

The projector lenses can also drift during slow acquisitions, moving the pattern across the detector — shifts can be applied during data conversion ([split_and_shift](https://github.com/dagewa/split_and_shift)):

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/drift-a.png
:alt: Beam centre drift along the fast axis over the scan
:::

:::{figure} ../assets/day1/demo-dials/drift-b.png
:alt: Beam centre drift along the slow axis over the scan
:::

::::

### Detector distance

In MicroED the Ewald sphere is flat, so the effective detector distance and the unit cell cannot be refined simultaneously. Fix the detector distance to a properly calibrated value (though <1% error is hard), or — if the cell is known — restrain to the target unit cell ([MyD88 tutorial](https://dials.github.io/documentation/tutorials/3DED/MyD88.html)).

### Multi-crystal methods

:::{figure} ../assets/day1/demo-dials/multi-crystal.png
:alt: Reciprocal lattice viewer showing reflections from multiple lattices
:width: 70%

DIALS handles multiple crystals simultaneously: multi-lattice indexing, joint refinement (better cells), joint scaling (better completeness, averaged-out systematics).
:::

## Installing DIALS

:::{figure} ../assets/day1/demo-dials/install.png
:alt: The DIALS installation page with graphical and shell installers per platform
:width: 90%

Installers for Linux, macOS (Intel and Apple silicon), and Windows: [dials.github.io/installation](https://dials.github.io/installation.html). See also the [software page](../software.md#track-dials).
:::

## Worked example — biotin on a Merlin (Timepix4)

### 1. Import

```
dials.import data1.mrc geometry.scan.oscillation=0,0.88 distance=400 \
  geometry.beam.wavelength=0.025079 pixel_size=0.055,0.055 \
  fast_slow_beam_centre=219,259 panel.gain=4.84
```

The oscillation defines the angular wedge per frame; the gain matters for PADs; distance and wavelength define the scattering vectors; with no beamstop the beam centre is easy to determine. This creates `imported.expt` — check it with `dials.show imported.expt`, and view the frames:

:::{figure} ../assets/day1/demo-dials/wx-viewer.png
:alt: The dials image viewer showing a biotin diffraction frame
:width: 90%

`dials.image_viewer` after import.
:::

### 2. Find spots

Build the spot-finding parameters interactively in the image viewer, save them as a `find_spots.phil`, then run:

```
dials.find_spots imported.expt find_spots.phil min_spot=2
```

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-phil.png
:alt: The saved find_spots.phil parameters
:::

:::{figure} ../assets/day1/demo-dials/wx-findspots.png
:alt: Terminal output of dials find_spots with the per-image spot count histogram
:::

::::

Check the found spots sit on real reflections:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-spots-a.png
:alt: Image viewer with found spots marked on the diffraction frame
`dials.image_viewer imported.expt strong.refl`
:::

:::{figure} ../assets/day1/demo-dials/wx-spots-b.png
:alt: Image viewer display options for checking spots
:::

::::

### 3. Find the rotation axis

The default rotation axis is almost certainly wrong:

```
dials.find_rotation_axis imported.expt strong.refl
```

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-rotaxis-plot.png
:alt: Rotation axis search score versus azimuth
:::

:::{figure} ../assets/day1/demo-dials/wx-rotaxis-proj.png
:alt: Cylindrical projection at the optimal rotation axis
:::

::::

:::{figure} ../assets/day1/demo-dials/wx-rotaxis-out.png
:alt: Terminal output with the found rotation axis
:width: 60%

Check the update with `dials.show optimised.expt`.
:::

### 4. Index

```
dials.index optimised.expt strong.refl detector.fix=distance
```

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-index-initial.png
:alt: Initial indexing solution
Initial solution (already very good).
:::

:::{figure} ../assets/day1/demo-dials/wx-index-final.png
:alt: Final indexing solution with more spots indexed
Final solution — more spots indexed. Default behaviour proceeds in P1.
:::

::::

:::{figure} ../assets/day1/demo-dials/wx-rmsd.png
:alt: RMSD in x, y, and z per experiment
:width: 75%

RMSDs — generally want each of these below one (pixel, pixel, image).
:::

Check the indexing in the reciprocal lattice viewer (`dials.reciprocal_lattice_viewer`, or `dials.rlv`) — points should lie on flat Bragg planes, not curves:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-rlv-a.png
:alt: Reciprocal lattice viewer view down a zone axis
:::

:::{figure} ../assets/day1/demo-dials/wx-rlv-b.png
:alt: Reciprocal lattice viewer showing flat reciprocal lattice planes
:::

::::

Optionally check the symmetry now:

:::{figure} ../assets/day1/demo-dials/wx-bravais.png
:alt: dials refine_bravais_settings table of candidate lattices
:width: 100%

`dials.refine_bravais_settings indexed.{expt,refl}` — high confidence in an orthorhombic cell here, but we continue in P1.
:::

### 5. Refine

```
dials.refine indexed.{expt,refl} scan_varying=False detector.fix=distance
```

:::{figure} ../assets/day1/demo-dials/wx-refine.png
:alt: Refinement output with final RMSDs
:width: 90%

Scan-varying refinement is possible but won't change much here.
:::

### 6. Integrate, scale, and cut the resolution

```
dials.integrate refined.{expt,refl} profile.fitting=False \
  background.algorithm=simple block.size=999
```

:::{figure} ../assets/day1/demo-dials/wx-integrate.png
:alt: Integration output summary
:width: 85%

These parameters make the output more "XDS-like" and preserve hand information a bit better for dynamical refinement (thanks Mike Martynowycz).
:::

```
dials.scale integrated.{expt,refl}
dials.estimate_resolution scaled.{expt,refl} isigma=1.0
```

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/demo-dials/wx-scale.png
:alt: Scaling output with merging statistics
:::

:::{figure} ../assets/day1/demo-dials/wx-resolution.png
:alt: Resolution estimate from CC-half
:::

::::

:::{figure} ../assets/day1/demo-dials/wx-final.png
:alt: Final scaling statistics at the resolution cutoff
:width: 85%

Re-integrate and scale to the estimated cutoff (d_min = 0.66 Å).
:::

### 7. Export

- For the SHELX suite: `dials.export scaled.expt scaled.refl format=shelx composition=<your atoms>`
- For Phenix and other MX programs (merged `.mtz`): `dials.merge scaled.{expt,refl}`

## Not covered — ask me!

Importing multiple datasets and joint refinement · cosym and joint scaling · xia2 and clustering for merging large datasets · the output HTML reports.

## Datasets

The workshop datasets are on Zenodo — see the [software page](../software.md#dials-datasets) for the full list (hybrid-pixel and CMOS small-molecule data, protein lamella, and small-wedge protein data).

## Acknowledgements

David Waterman (for having the patience of a saint with DIALS questions, and for slides that informed this demo), Mike Martynowycz (DIALS/XDS reconciliation), Gloria Gao (suggestions), and all past and present DIALS developers.
