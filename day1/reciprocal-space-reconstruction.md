---
title: "Data reduction: reciprocal space reconstruction and unit cell determination"
short_title: "Reciprocal space & unit cell"
---

# Data reduction: reciprocal space reconstruction and unit cell determination

:::{div}
:class: ecs-session-meta
**Day 1 · Saturday 8 August · 11:30 – 12:30** — [Tatiana Gorelik](../instructors.md#speaker-tatiana-gorelik)
:::

… many years ago… around 2006…

## From a series of patterns to reciprocal space

We have now collected a series of patterns, and:

- We know the ED camera length
- We know the starting stage angle, the final stage angle, and the stage increment

**We need to map the set of 2D patterns onto the 3D reciprocal space.**

:::{figure} ../assets/day1/reciprocal-space/acquisition-stack.png
:alt: Diffraction data acquisition as a fan of planes about the goniometer axis, and the same data as a stack of frames
:width: 90%

Diffraction data acquisition (left) and the recorded data stack (right), sharing the goniometer axis.
:::

## Pattern centering

Every frame must first be centered — the position of the direct beam has to be known precisely.

::::{grid} 1 2 3 3

:::{figure} ../assets/day1/reciprocal-space/centering-a.jpg
:alt: Diffraction pattern with a well-defined central beam
:::

:::{figure} ../assets/day1/reciprocal-space/centering-b.jpg
:alt: Two diffraction patterns whose centers differ between frames
:::

:::{figure} ../assets/day1/reciprocal-space/centering-c.jpg
:alt: Diffraction pattern recorded with a beam stopper covering the central beam
:::

::::

Ways to find the center:

- Friedel pairs of reflections
- Shape of the central beam / center of mass of the pattern (beam stopper!)
- Analysis of the background gradient…

Large jumps between frames are unusual; for 3D 4D-STEM data the pattern shift can be modelled.

## Bragg peak positions

:::{figure} ../assets/day1/reciprocal-space/pattern-inverted.jpg
:alt: Electron diffraction pattern, inverted contrast, with weak reflections and a streak from the central beam
:width: 65%
:::

Peak finding and background correction, some of the tools:

- Morphological background removal + adaptive thresholding
- Matched filtering / normalized cross-correlation (FFT-based)
- Local maxima detection + non-maximum suppression
- (SNR) thresholding / peak significance test: noise level, detector gain, peak size, and a threshold in number of sigmas
- …

:::{figure} ../assets/day1/reciprocal-space/intensity-profile.jpg
:alt: Intensity profile along a line through the diffraction pattern, with sharp Bragg peaks over a structured background
:width: 100%

Intensity profile through a pattern: sharp Bragg peaks on a structured background.
:::

### How flat are electron diffraction patterns?

:::{figure} ../assets/day1/data-collection/ewald-sphere-rotation.mp4
:alt: Animation of the Ewald sphere cutting through the reciprocal lattice, with the resulting diffraction pattern on the detector
:width: 100%

The Ewald sphere is nearly — but not exactly — flat at electron wavelengths.
:::

For a typical detector format the curvature stays below the pixel size, so each pattern can be treated as a planar section: with 1024 × 1024 pixels, 1 pixel ≈ 0.002 Å⁻¹, and the sphere deviates from the plane by less than a pixel out to about 1 Å⁻¹ (512 pixels).

## Tilt axis position

The orientation of the tilt axis in the frames must be determined. Diffraction patterns can rotate:

- when you change the camera length
- when you focus them (diffraction lens focus)

Reflections **on** the tilt axis should stay the same throughout the series.

:::{figure} ../assets/day1/reciprocal-space/pattern-rotation.mp4
:alt: Movie of a diffraction pattern rotating as microscope settings change
:width: 65%
:::

Assume we know where the axis is — then each frame can be assigned its plane in 3D:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/cylinder-mapping.png
:alt: Diagram: the tilt axis angle phi in the frame, and the frames arranged about the axis in 3D
The frames arranged about the tilt axis in 3D.
:::

:::{figure} ../assets/day1/reciprocal-space/wedge-stack-blender.jpg
:alt: Rendering of the frames fanned about the common tilt axis
The frames fanned about the common tilt axis.
:::

::::

:::{figure} ../assets/day1/reciprocal-space/peak-cloud.mp4
:alt: Rotating cloud of extracted peak positions filling reciprocal space
:width: 70%

The extracted peaks assembled into a 3D point cloud.
:::

With the tilt axis in the **correct position**, the projections of the peak cloud show a regular lattice:

:::{figure} ../assets/day1/reciprocal-space/axis-ok-a.jpg
:alt: Peak cloud in the reconstruction program with the tilt axis set correctly: rows of sharp lattice lines
:width: 100%

Correct axis position: the cloud collapses onto sharp lattice rows.
:::

With the axis **wrong by 5°** the lattice rows bend into arcs:

:::{figure} ../assets/day1/reciprocal-space/axis-5deg-b.jpg
:alt: Peak cloud with the tilt axis wrong by 5 degrees: rows bend into arcs
:width: 100%
:::

And **wrong by 10°** the cloud smears out completely:

:::{figure} ../assets/day1/reciprocal-space/axis-10deg-b.jpg
:alt: Peak cloud with the tilt axis wrong by 10 degrees: strongly smeared arcs
:width: 100%
:::

:::{figure} ../assets/day1/reciprocal-space/axis-compare.png
:alt: Two reconstructed sections a and b showing sharp spots versus azimuthally smeared spots
:width: 90%

Sections through the reconstructed volume: a correct axis gives sharp spots (a); a wrong axis smears them azimuthally (b).
:::

### Finding the axis with the cylindrical projection

The full sphere of directions can be summarized in a cylindrical (θ–φ) projection of the reconstructed data:

:::{figure} ../assets/day1/reciprocal-space/sphere-coverage.png
:alt: Sphere of directions and its cylindrical theta-phi projection, computed for the data
:width: 75%

The reciprocal-space directions mapped onto a θ–φ cylindrical projection.
:::

:::{figure} ../assets/day1/reciprocal-space/cylproj-scan.mp4
:alt: Cylindrical projection changing as the assumed tilt-axis angle is scanned
:width: 100%

Scanning the assumed axis angle: the projection sharpens when the axis is right.
:::

The sharpness criterion also settles whether the axis points "up or down" in the frames:

::::{grid} 1 1 1 1

:::{figure} ../assets/day1/reciprocal-space/cylproj-up.png
:alt: Cylindrical projection computed with one choice of axis direction
:::

:::{figure} ../assets/day1/reciprocal-space/cylproj-down.png
:alt: Cylindrical projection computed with the opposite axis direction
:::

::::

## Unit cell determination

### Reduced cells

A lattice can be described by infinitely many cells; a unique, standard choice is made by cell reduction:

- Niggli's reduction for 3D lattices
- Delaunay (Delone) reduction

### The difference vector space

Unit cell parameter determination works in the **difference vector space (DVS)** — the autocorrelation of the lattice, which enhances the lattice basis vectors:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/dvs-ideal-lattice.png
:alt: Measured reciprocal lattice points with the missing cone regions marked
Reciprocal lattice (with missing cone).
:::

:::{figure} ../assets/day1/reciprocal-space/dvs-ideal-dvs.png
:alt: Difference vector space of the same lattice: a complete, denser lattice
Its difference vector space (DVS).
:::

::::

### Why reflections are not ideal points

:::{figure} ../assets/day1/reciprocal-space/relrod-excitation.png
:alt: Ewald sphere construction with the relrod and the observed intensity as a function of excitation error
:width: 65%

The excitation error: the Ewald sphere samples the relrod away from its center, so the observed position and intensity of a reflection shift.
:::

Reflections are not sharp 3D points, and their positions may be imprecise, because of:

- Excitation error
- Crystal shape — thin-foil effect
- Stacking faults / disorder in the crystal
- Crystal bending
- Numerical error during processing
- Undersampling at high resolution

The DVS tolerates these deviations — as the lattice becomes less perfect, its DVS still concentrates on the basis vectors:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/dvs-n2-lattice.png
:alt: Reciprocal lattice with displaced points
Non-perfect reciprocal lattice…
:::

:::{figure} ../assets/day1/reciprocal-space/dvs-n2-dvs.png
:alt: DVS of the displaced lattice, still showing concentrated clusters
…and its DVS.
:::

:::{figure} ../assets/day1/reciprocal-space/dvs-n3-lattice.png
:alt: Reciprocal lattice with strongly displaced points
Stronger deviations…
:::

:::{figure} ../assets/day1/reciprocal-space/dvs-n3-dvs.png
:alt: DVS of the strongly displaced lattice with broadened clusters
…broaden the DVS clusters.
:::

::::

### Clustering the difference vectors

The DVS clusters are found by **data clustering** — grouping the data based on proximity (how close the vectors are to each other):

:::{figure} ../assets/day1/reciprocal-space/clustering.png
:alt: Diagram: a point set D is separated by clustering into clusters C1 and C2
:width: 70%

Clustering parameters: the neighborhood ε and minPts — if there are more than minPts elements within the neighborhood ε, this is a cluster.
:::

### Mapping the 3D unit cell back onto the 2D frames

The refined cell is projected back onto each frame to verify the indexing:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/peak-model-3d.png
:alt: 3D peak-shape model surface
The peak model fitted in 3D.
:::

:::{figure} ../assets/day1/reciprocal-space/cell-on-frame.jpg
:alt: PETS2 window with the predicted cell positions overlaid on a measured frame
The predicted positions overlaid on a measured frame.
:::

::::

## 3D reconstruction

The reconstruction grid is set by the measurement: with 512 pixels to 1 Å⁻¹ and a 1° tilt increment, neighbouring frames are separated by 57 pixels at 0.5 Å⁻¹ and 114 pixels at 1 Å⁻¹ — the volume between the measured planes is not sampled.

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/recon-1deg.jpg
:alt: Reconstructed volume section with 1 degree tilt increment showing gaps between measured planes
1° tilt increment.
:::

:::{figure} ../assets/day1/reciprocal-space/recon-05deg.jpg
:alt: Reconstructed volume section with 0.5 degree tilt increment with smaller gaps
0.5° tilt increment.
:::

::::

:::{figure} ../assets/day1/reciprocal-space/recon-bowtie.jpg
:alt: Section through a reconstructed reciprocal-space volume: measured wedges meet at the tilt axis
:width: 70%

Section through the reconstructed volume: the measured wedges meet at the tilt axis; the missing wedge stays empty.
:::

:::{figure} ../assets/day1/reciprocal-space/recon-rotating.mp4
:alt: Rotating view of the reconstructed reciprocal-space volume
:width: 65%
:::

### Sections

Sections through the reconstructed volume are the tool for reading off symmetry:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/section-0kl.jpg
:alt: The 0kl section of the reconstructed reciprocal space
The 0kl section.
:::

:::{figure} ../assets/day1/reciprocal-space/section-1kl.jpg
:alt: The 1kl section of the reconstructed reciprocal space
The 1kl section.
:::

::::

### Examples

:::{figure} ../assets/day1/reciprocal-space/extinctions.mp4
:alt: Animated sections through a reconstructed volume showing systematically absent reflections
:width: 90%

Glide planes (zonal) and screw axis (serial) extinctions.
:::

:::{figure} ../assets/day1/reciprocal-space/tase2-superstructure.mp4
:alt: Animated sections showing superstructure reflections appearing between the main reflections
:width: 90%

Low-temperature superstructure of 1T-TaSe₂.
:::

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/reciprocal-space/tise2-rt.jpg
:alt: Diffraction pattern of TiSe2 at room temperature
Room temperature.
:::

:::{figure} ../assets/day1/reciprocal-space/tise2-ln2.jpg
:alt: Diffraction pattern of TiSe2 at liquid nitrogen temperature with superstructure reflections
Liquid-nitrogen temperature.
:::

::::

Superstructures of TiSe₂.

:::{figure} ../assets/day1/reciprocal-space/recon-large.mp4
:alt: Rotating reconstructed reciprocal-space volume of a large unit cell
:width: 90%
:::
