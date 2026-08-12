---
title: "Fundamentals: the diffraction phenomena"
short_title: "Fundamentals: diffraction"
---

# Fundamentals: the diffraction phenomena

:::{div}
:class: ecs-session-meta
**Day 1 · Saturday 8 August · 9:00 – 10:00** — [Andrew Stewart](../instructors.md#speaker-andrew-stewart)
:::

## Crystals

:::{figure} ../assets/day1/fundamentals/crystals.png
:alt: Real-space crystal lattice and the corresponding diffraction pattern
:width: 100%
:::

### Particle or crystal?

:::{figure} ../assets/day1/fundamentals/particle-or-crystal.png
:alt: SrTiO3 simulations: summed scattering intensity versus supercell volume
:width: 95%

SrTiO₃ simulations (unpublished, Mangan & Stewart 2022).
:::

## Inelastic scattering

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/inelastic-events.jpg
:alt: Diagram of the beam electron interacting with the atomic shell electrons
:::

:::{figure} ../assets/day1/fundamentals/inelastic-thickness.png
:alt: Fractions of unscattered, singly and doubly scattered electrons versus thickness
:::

::::

- Inelastic scatter < 1° and always incoherent
- Elastic scatter > 10° usually incoherent

### Energy filter

:::{figure} ../assets/day1/fundamentals/filter-unfiltered.jpg
:alt: Comparison of unfiltered and energy-filtered electron diffraction
:width: 70%

Unfiltered vs. filtered electron diffraction [](doi:10.1016/S0006-3495(02)75619-1).
:::

### Dynamical scattering

The measured intensity mixes several channels — coherent and incoherent, kinematic and dynamic, elastic and inelastic events — and separating them is what makes quantitative electron diffraction hard.

## Scattering

:::{figure} ../assets/day1/fundamentals/scattering.png
:alt: Wave scattering from a lattice of atoms
:width: 95%
:::

### Bragg diffraction

:::{figure} ../assets/day1/fundamentals/bragg.png
:alt: Bragg diffraction from lattice planes, with the path difference construction
:width: 100%

nλ = 2d sin θ
:::

### The reciprocal lattice

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/reciprocal-a.jpg
:alt: Reciprocal lattice basis vector definitions
:::

:::{figure} ../assets/day1/fundamentals/reciprocal-b.jpg
:alt: Real and reciprocal cell relationship
:::

::::

### The Ewald sphere construction

:::{figure} ../assets/day1/fundamentals/ewald.png
:alt: Ewald sphere construction over the reciprocal lattice
:width: 95%

The radius of the sphere is r = 1/λ.
:::

## The Fourier transform

Diffraction and the Fourier transform are equivalent (a formal proof will be circulated). The Fourier transform is representing the world in circles:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/ft-circles.mp4
:alt: Animation drawing a signal from rotating circles
:::

:::{figure} ../assets/day1/fundamentals/ft-decompose.gif
:alt: Animation decomposing a signal into frequency components
:::

::::

Moving to the complex plane, and winding the signal around the origin:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/ft-complex.gif
:alt: Animation of a signal wrapped on the complex plane
:::

:::{figure} ../assets/day1/fundamentals/ft-winding.gif
:alt: Animation winding a signal around the origin at varying frequency
:::

::::

The Fourier transform of the signal follows from the winding frequency and the boundaries:

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/ft-winding-fourier.gif
:alt: Winding animation with the resulting Fourier transform peaks
:::

:::{figure} ../assets/day1/fundamentals/ft-almost.mp4
:alt: Fourier transform of a nearly periodic signal
:::

::::

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/ft-pair-a.gif
:alt: Winding animation of a pure tone
:::

:::{figure} ../assets/day1/fundamentals/ft-pair-b.gif
:alt: Winding animation of a sum of tones
:::

::::

*Animations from [3Blue1Brown, "But what is the Fourier transform?"](https://www.3blue1brown.com/lessons/fourier-transforms).*

## Scattering factors

The atomic scattering factor is nothing but the Fourier transform of the atom's own electron density (X-rays) or electrostatic potential (electrons).

::::{grid} 2 2 2 2

:::{figure} ../assets/day1/fundamentals/sf-xray.png
:alt: X-ray atomic scattering factors versus scattering angle for all elements
X-ray scattering factors.
:::

:::{figure} ../assets/day1/fundamentals/sf-electron.png
:alt: Electron atomic scattering factors versus scattering angle for all elements
Electron scattering factors.
:::

::::

## The structure factor

The structure factor F(hkl) is the Fourier transform of the electron density / electrostatic potential in a unit cell, evaluated at a reciprocal lattice point. It tells you the amplitude and phase of the wave diffracted into the reflection hkl:

- fⱼ is the atomic scattering factor of atom j
- xⱼ, yⱼ, zⱼ — fractional coordinates in the unit cell
