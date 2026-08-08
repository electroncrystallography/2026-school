---
title: Software
short_title: Software
---

# Software

The hands-on [practical session](./day2/practical-session.md) on the afternoon of Day 2 used two software tracks. Pick whichever fits your samples — you do not need both.

| Track | Use it for | Programs |
| --- | --- | --- |
| **PETS2 + Jana2020** | Small-molecule and inorganic crystals | Data extraction (PETS2), structure solution and refinement (Jana2020) |
| **DIALS + Phenix** | Macromolecular compounds | Data processing (DIALS), structure solution and refinement (Phenix) |

If you work on macromolecules, DIALS + Phenix is the better fit. For small-molecule or inorganic crystals, either track works.

:::{admonition} Downloads are large
:class: note
The tutorial datasets run to several gigabytes. Download them over a connection you trust, and give the installers time to finish before you start working through the tutorials.
:::

(track-pets2)=
## PETS2 + Jana2020

### Installing PETS2

PETS2 handles data extraction. Go to [pets-login.fzu.cz](https://pets-login.fzu.cz), register, and download the installer. Run the installer — an executable — to install the standalone program.

### Installing Jana2020

Jana2020 handles structure solution and refinement. Go to [jana.fzu.cz](https://jana.fzu.cz), log in with the same credentials you used for PETS2, and download the installer. Run the installer to install the standalone program.

Download the **latest version of both programs** even if you already have older versions installed — improvements and bug fixes are released frequently.

### Datasets

Two datasets are processed in this track: **Tyrosine** (cRED dataset) and **Slotaite** (PED dataset). Both are in the [Jana cookbook](https://jana.fzu.cz/#cookbook-section), under sections **13.10** and **13.11**. Each section provides the data (a single zip file) and a tutorial text with all the steps to process the raw diffraction data through to structure refinement in PETS2 and Jana2020.

(track-dials)=
## DIALS + Phenix

### Installing DIALS

The easiest way to get DIALS is from the [DIALS installation page](https://dials.github.io/installation.html), which has installers for Linux, macOS, and Windows. If you would rather build from source, follow the [developer install instructions](https://dials.github.io/documentation/installation_developer.html).

### Installing Phenix

Download links are at [phenix-online.org/download](https://phenix-online.org/download), and installation instructions at [phenix-online.org/documentation/install-setup-run.html](https://phenix-online.org/documentation/install-setup-run.html).

(dials-datasets)=
### Datasets

The datasets are on Zenodo, where you will also find notes on how to process them.

**Small molecules**

- [Hybrid pixel data](https://zenodo.org/records/21359216)
- [CMOS data (K2)](https://zenodo.org/records/13742284)

**Macromolecules**

- [Protein lamella on Ceta-D](https://zenodo.org/records/20086111)
- [Small protein crystal, K2 small wedge](https://zenodo.org/records/15691475)

## Other software mentioned in the school

Software introduced in the lectures, beyond the two practical tracks.

| Package | What it does | Links |
| --- | --- | --- |
| PETS2 | 3D ED data extraction and processing | [pets-login.fzu.cz](https://pets-login.fzu.cz) |
| Jana2020 | Structure solution and refinement, including dynamical refinement | [jana.fzu.cz](https://jana.fzu.cz) |
| DIALS | Diffraction integration and data reduction | [dials.github.io](https://dials.github.io/) |
| Phenix | Macromolecular structure solution and refinement | [phenix-online.org](https://phenix-online.org/) |
| SIR / Il Milione | Direct methods for structure solution | [crystal.ic.cnr.it](https://www.ba.ic.cnr.it/softwareic/) |
| py4DSTEM | 4D-STEM data analysis | [GitHub](https://github.com/py4dstem/py4DSTEM) |
