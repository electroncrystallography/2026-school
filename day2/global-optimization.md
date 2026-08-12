---
title: "Structure solution: global optimization methods"
short_title: "Global optimization"
---

# Structure solution: global optimization methods — molecular replacement, simulated annealing

:::{div}
:class: ecs-session-meta
**Day 2 · Sunday 9 August · 14:00 – 15:00** — [Brent Nannenga](../instructors.md#speaker-brent-nannenga)
:::

## Structure solution at lower resolutions

What to do when your electron diffraction data are reasonable, but not high enough resolution for the methods already described? Use predicted structures in real space to initially solve the structure:

- **Molecular replacement**
- **Simulated annealing**

## Molecular replacement

If we know our target biomolecule is similar to a previously determined structure, we can use this information:

- A homologous model is selected and placed in the unit cell
- The model is then rotated and translated in the unit cell
- Calculate how well the model explains our experimental data

:::{figure} ../assets/day2/global-optimization/mr-cycle.png
:alt: The molecular replacement cycle: rotation search then translation search of the model in the unit cell
:width: 50%

The rotation (αβγ) and translation (xyz) searches ([rigaku.com](https://rigaku.com/products/crystallography/techniques/molecular-replacement)).
:::

### What kinds of structures can be solved by molecular replacement?

Commonly used for phasing macromolecular structures — and also peptides, small biological molecules, and small molecules:

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/global-optimization/mr-peptide.jpg
:alt: Peptide structure solved by molecular replacement
Peptide (Rodriguez *et al.*, 2015, *Nature*).
:::

:::{figure} ../assets/day2/global-optimization/mr-dna.png
:alt: Small DNA duplex electron density
Small DNA duplex (Haymaker *et al.*, 2023, *Structure*).
:::

::::

:::{figure} ../assets/day2/global-optimization/mr-smallmol.jpg
:alt: Small molecule structures solved by molecular replacement
:width: 60%

Small molecules (Zhu *et al.*, 2020, *Structure*).
:::

### How do we choose our search model?

- Sequence similarity (really want *structural* similarity)
  - Directly use a homologous model
  - Create a polyalanine model
  - Homologous model with your sequence
- Automated search (e.g. BALBES, MrBUMP)
- AlphaFold search models
- Cryo-EM maps

:::{figure} ../assets/day2/global-optimization/search-models.png
:alt: Search model choices for molecular replacement
:width: 60%

Porter *et al.* (2022), *JACS*.
:::

### What do we do with our search model?

Rotation search, then translation search, then compare with the experimental data:

- Patterson methods
- Maximum likelihood (**Phaser**)
  - LLG — "log-likelihood gain"
  - Z-score — signal-to-noise of the solution

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/global-optimization/phaser-workflow.png
:alt: The Phaser workflow
The Phaser workflow ([Phaser wiki](https://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software)).
:::

:::{figure} ../assets/day2/global-optimization/phaser-scores.png
:alt: Table of translation function Z-scores and whether the structure is likely solved
What are we looking for? TF Z-score guide.
:::

::::

### What is next?

Check the results of your top solutions — do the model and maps look right? Then begin refinement of your model.

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/global-optimization/mr-maps.jpg
:alt: Electron density maps around the placed model
:::

:::{figure} ../assets/day2/global-optimization/mr-refine.png
:alt: Refinement interface with the molecular replacement solution
:::

::::

## Simulated annealing

A global optimization strategy: accept occasional uphill moves to escape local minima, cooling over time (named for annealing in metallurgy — Hiemstra, 2013, *Geochimica et Cosmochimica Acta*).

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/global-optimization/energy-landscape.png
:alt: Energy landscape with local minima and the global minimum
An energy landscape with many local minima ([source](http://pd.chem.ucl.ac.uk/pdnn/solve1/genetic.htm)).
:::

:::{figure} ../assets/day2/global-optimization/sim-annealing.gif
:alt: Animation of simulated annealing finding the maximum of a function
Simulated annealing in action ([Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing)).
:::

::::
