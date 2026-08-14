---
title: "Structure solution: the phasing problem & direct methods"
short_title: "Direct methods"
---

# Structure solution: the phasing problem & direct methods

:::{div}
:class: ecs-session-meta
**Day 2 · Sunday 9 August · 10:30 – 11:30** — [Corrado Cuocci](../instructors.md#speaker-corrado-cuocci)
:::

## The phase problem

A 3D ED experiment gives a set of measured intensities $I_\mathbf{h}$. Turning them into a structure requires something the experiment does not record.

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/phase-problem-collection.jpg
:alt: Diffraction geometry, a tilt series of patterns, the sampled wedge of reciprocal space and the missing cone
Data collection: a tilt series of patterns samples a wedge of reciprocal space [](doi:10.1016/j.micromeso.2013.11.040).
:::

:::{figure} ../assets/day2/direct-methods/phase-problem-structure.jpg
:alt: Electron density isosurface of a porous framework structure with atoms
The goal: the structure.
:::

::::

## Structure factor

$$
F_\mathbf{h} = \int_V \varrho(\mathbf{r})\, \exp\!\left[2\pi i\,(\mathbf{h}\cdot\mathbf{r})\right] d\mathbf{r}
$$

$$
F_\mathbf{h} = \sum_{j=1}^{N} f_j \exp\!\left(2\pi i\, \mathbf{h}\cdot\mathbf{r}_j\right)
$$

where $N$ is the total number of atoms in the unit cell and $f_j$ is the atomic scattering factor. With

$$
\mathbf{h}\cdot\mathbf{r}_j = (h \; k \; l) \times \begin{pmatrix} x_j \\ y_j \\ z_j \end{pmatrix} = h x_j + k y_j + l z_j
$$

this becomes

$$
F_\mathbf{h} = \sum_{j=1}^{n} f_j \exp\!\left[2\pi i (h x_j + k y_j + l z_j)\right]
$$

Two further per-atom factors enter:

$$
F_\mathbf{h} = \sum_{j=1}^{n} O_j\, t_j(s)\, f_j(s) \exp\!\left[2\pi i (h x_j + k y_j + l z_j)\right],
\qquad s = \sin\theta_\mathbf{h}/\lambda
$$

- $O_j$ — the occupation factor
- $t_j(s)$ — the temperature factor (atomic displacement parameters)

## Phase angle

$$
F_\mathbf{h} = |F_\mathbf{h}| \exp\!\left(i \varphi_\mathbf{h}\right)
$$

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/phase-angle-cell.jpg
:alt: Molecular structure drawn inside its unit cell
:::

:::{figure} ../assets/day2/direct-methods/phase-angle-argand.jpg
:alt: Argand diagram showing the structure factor as a vector of length |F| at angle phi
:::

::::

## Fourier transform

Direct space and reciprocal space are related by a Fourier transform:

$$
F(\mathbf{h}) = FT\left[\varrho(\mathbf{r})\right]
\qquad
\varrho(\mathbf{r}) = FT^{-1}\left[F(\mathbf{h})\right]
$$

$$
F(\mathbf{h}) = \int_V \varrho(\mathbf{r}) \exp\!\left[2\pi i (\mathbf{h}\cdot\mathbf{r})\right] d\mathbf{r}
\qquad
\varrho(\mathbf{r}) = \int_{V^*} F(\mathbf{h}) \exp\!\left[-2\pi i (\mathbf{h}\cdot\mathbf{r})\right] d\mathbf{h}
$$

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/ft-reciprocal-space.jpg
:alt: Simulated three-dimensional diffraction volume
Reciprocal space.
:::

:::{figure} ../assets/day2/direct-methods/ft-direct-space.jpg
:alt: Electron density isosurface of a molecule
Direct space.
:::

::::

## The electron-density equation

$$
\rho(\mathbf{r}) = FT^{-1}\left[F_\mathbf{h}\right] = \frac{1}{V_{cell}} \sum_\mathbf{h} F_\mathbf{h} \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}\right)
$$

$$
\rho(x,y,z) = \frac{1}{V_{cell}} \sum_h \sum_k \sum_l F_{hkl} \exp\!\left[-2\pi i (hx + ky + lz)\right]
$$

$$
F_{hkl} = |F_{hkl}| \exp\!\left(i\varphi_{hkl}\right) = |F_{hkl}| \left(\cos\varphi_{hkl} + i \sin\varphi_{hkl}\right)
$$

$$
\rho(x,y,z) = \frac{1}{V_{cell}} \sum_h \sum_k \sum_l |F_{hkl}| \cos\!\left[2\pi (hx + ky + lz) - \varphi_{hkl}\right]
$$

The experiment measures

$$
I_{hkl} = C\,|F_{hkl}|^2
$$

so the amplitudes $|F_{hkl}|$ are available — but the phases $\varphi_{hkl}$ are not.

:::{admonition} The phase problem
:class: important
Accurate structure determination requires **both** the amplitudes and phases of the structure factors. This difficulty is known as the **phase problem**, as the phase information is missing from diffraction data.

Phases must be estimated and refined using appropriate **phasing methods**, which give approximate positions of atoms.
:::

## Phasing methods

Traditional approaches:

- direct methods
- Patterson methods

Direct space methods — alternative expressions: real space, global optimization, global search.

Other methods:

- charge flipping
- molecular replacement

## Direct methods: the theoretical basis

Direct methods emerged in 1948, achieving full theoretical and practical maturity by the 1970s.

Key points in DM development include:

- Sayre's equation (1952)
- Structure invariants by Hauptman and Karle (1953)
- Cochran's three-phase probability distribution (1955)
- Hauptman and Karle's **tangent formula** (1956)

Automated direct methods software:

- MULTAN (Main, 1980)
- SIMPEL (Schenk, 1988)
- SHELX-76 (Sheldrick, 1976)
- SIR (Giacovazzo, 1982)

::::{grid} 2 2 2 2

:::{figure} ../assets/day2/direct-methods/hauptman.jpg
:alt: Portrait photograph of Herbert A. Hauptman
Herbert A. Hauptman
:::

:::{figure} ../assets/day2/direct-methods/karle.jpg
:alt: Portrait photograph of Jerome Karle
Jerome Karle
:::

::::

Direct methods practically solved the phase problem for small molecules, earning H. Hauptman and J. Karle the 1985 Nobel Prize in Chemistry.

## Constraints on the electron density

**Discrete atoms (atomicity).** The inverse transform of $F_\mathbf{h}$ gives $\rho(\mathbf{r})$; the inverse transform of the *normalized* structure factor $E_\mathbf{h}$ gives a point-atom structure:

$$
|E_\mathbf{h}|^2 = \frac{|F_\mathbf{h}|^2}{\left\langle |F_\mathbf{h}|^2 \right\rangle},
\qquad
\left\langle |F_\mathbf{h}|^2 \right\rangle = \epsilon_\mathbf{h} \sum_{i=1}^{N} f_i^2
$$

**Non-negative electron density (positivity):**

$$
\rho(\mathbf{r}) > 0
$$

## Scaling and normalization of the structure factors

The first step of a typical direct methods procedure: $F_\mathbf{h} \rightarrow E_\mathbf{h}$.

$$
|F_\mathbf{h}|^2_{obs} = K\,|F_\mathbf{h}|^2 = K \left|F^0_\mathbf{h}\right|^2 \exp(-2Bs^2)
$$

$$
\ln\!\left( \frac{\left\langle |F_\mathbf{h}|^2_{obs} \right\rangle_s}{\sum_s^0} \right) = \ln K - 2B \left\langle s^2 \right\rangle
$$

with $s = \sin(\theta)/\lambda$ and $\sum_s^0 = \sum_{j=1}^{N} (f_j^0)^2$, giving

$$
|E_\mathbf{h}|^2 = \frac{|F_\mathbf{h}|^2_{obs}}{\left\langle |F_\mathbf{h}|^2_{obs} \right\rangle}
= \frac{|F_\mathbf{h}|^2_{obs}}{K \exp(-2Bs^2)\, \epsilon_\mathbf{h} \sum_{j=1}^{N} (f_j^0)^2}
$$

:::{figure} ../assets/day2/direct-methods/wilson-plot.jpg
:alt: Wilson plot, logarithm of the mean intensity ratio against s squared, with a straight-line fit
:width: 60%

Wilson plot for cimetidine.
:::

## Normalized structure factors

Centric structures:

$$
P_{\bar{1}}(|E|) = \sqrt{\frac{2}{\pi}}\, \exp\!\left(-|E|^2/2\right)
$$

Acentric structures:

$$
P_{1}(|E|) = 2\,|E|\, \exp\!\left(-|E|^2\right)
$$

Normalization helps to reveal underlying symmetry (i.e. inversion centre) in the data.

:::{figure} ../assets/day2/direct-methods/e-value-distributions.png
:alt: Probability distributions of normalized structure factor magnitudes for centric and acentric structures, with the two regions where they differ most circled
:width: 60%

The centric and acentric distributions of $|E_\mathbf{h}|$ differ most at low $|E|$ and in the tail.
:::

:::{figure} ../assets/day2/direct-methods/e-value-table.jpg
:alt: Table comparing experimental and theoretical moments of the E distribution for acentric, centric and hypercentric cases
:width: 80%

Comparison of theoretical and experimental distribution functions.
:::

## Structure invariants

Move the origin by a general vector $\mathbf{r}_0$:

$$
F_\mathbf{h} = |F_\mathbf{h}| \exp(i\varphi_\mathbf{h}) = \sum_{j=1}^{n} f_j \exp\!\left(2\pi i\, \mathbf{h}\cdot\mathbf{r}_j\right)
$$

$$
\begin{aligned}
F'_\mathbf{h} &= |F'_\mathbf{h}| \exp(i\varphi'_\mathbf{h}) = \sum_{j=1}^{n} f_j \exp\!\left[2\pi i\, \mathbf{h}\cdot(\mathbf{r}_j - \mathbf{r}_0)\right] \\
&= \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}_0\right) \sum_{j=1}^{n} f_j \exp\!\left(2\pi i\, \mathbf{h}\cdot\mathbf{r}_j\right) \\
&= \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}_0\right) F_\mathbf{h}
\end{aligned}
$$

Shifting the origin by a vector $\mathbf{r}_0$ therefore gives

$$
|F'_\mathbf{h}| = |F_\mathbf{h}|
\qquad
\varphi'_\mathbf{h} = \varphi_\mathbf{h} - 2\pi\, \mathbf{h}\cdot\mathbf{r}_0
$$

$|F_\mathbf{h}|$ is a structure-invariant quantity, i.e. independent of the choice of origin, whereas $\varphi_\mathbf{h}$ is not.

A **structure invariant** is a product of structure factors whose phase is independent of the choice of origin. The most general structure invariant is represented by the product

$$
F_{\mathbf{h}_1} F_{\mathbf{h}_2} \ldots F_{\mathbf{h}_m} = \left| F_{\mathbf{h}_1} F_{\mathbf{h}_2} \ldots F_{\mathbf{h}_m} \right| \exp\!\left[ i\left(\varphi_{\mathbf{h}_1} + \varphi_{\mathbf{h}_2} + \cdots + \varphi_{\mathbf{h}_m}\right) \right]
$$

when

$$
\mathbf{h}_1 + \mathbf{h}_2 + \cdots + \mathbf{h}_m = 0
$$

Every structure invariant must satisfy the condition that the sum of the Miller indices equals **zero**.

Triplet invariants:

$$
F_\mathbf{h} F_\mathbf{k} F_\mathbf{-h-k} = \left| F_\mathbf{h} F_\mathbf{k} F_\mathbf{-h-k} \right| \exp\!\left[ i \left( \varphi_\mathbf{h} + \varphi_\mathbf{k} + \varphi_\mathbf{-h-k} \right) \right]
$$

Quartet invariants:

$$
F_\mathbf{h} F_\mathbf{k} F_\mathbf{l} F_\mathbf{-h-k-l} = \left| F_\mathbf{h} F_\mathbf{k} F_\mathbf{l} F_\mathbf{-h-k-l} \right| \exp\!\left[ i \left( \varphi_\mathbf{h} + \varphi_\mathbf{k} + \varphi_\mathbf{l} + \varphi_\mathbf{-h-k-l} \right) \right]
$$

## Probability methods

$$
\Phi_\mathbf{hk} = \varphi_\mathbf{h} + \varphi_\mathbf{-k} + \varphi_\mathbf{k-h}
$$

Friedel's law gives $|F_\mathbf{h}| = |F_\mathbf{-h}| \rightarrow I_\mathbf{h} = I_\mathbf{-h}$ and $\varphi_\mathbf{h} = -\varphi_\mathbf{-h}$, so

$$
\Phi_\mathbf{hk} = \varphi_\mathbf{h} + \varphi_\mathbf{-k} + \varphi_\mathbf{k-h} = \varphi_\mathbf{h} - \varphi_\mathbf{k} - \varphi_\mathbf{h-k}
$$

The probability formulae for triplet invariants derived by Cochran:

$$
P(\Phi_\mathbf{hk}) = \frac{1}{2\pi I_0 G_\mathbf{hk}} \exp\!\left( G_\mathbf{hk} \cos(\Phi_\mathbf{hk}) \right)
$$

Equal atoms:

$$
G_\mathbf{hk} = \frac{2}{\sqrt{N}} \left| E_\mathbf{h} E_\mathbf{k} E_\mathbf{h-k} \right|
$$

Non-equal atoms:

$$
G_\mathbf{hk} = 2 \sigma_3 \sigma_2^{-3/2} \left| E_\mathbf{h} E_\mathbf{k} E_\mathbf{h-k} \right|,
\qquad
\sigma_n = \sum_{J=1}^{N} Z_j^n
$$

$I_0$ is the modified Bessel function of zero order and $Z$ is the atomic number.

$P(\Phi_\mathbf{hk})$ is a so-called **von Mises distribution**, and

$$
\Phi_\mathbf{hk} = \varphi_\mathbf{h} - \varphi_\mathbf{k} - \varphi_\mathbf{h-k} \approx 0
$$

where $\approx$ indicates 'is distributed about'. Hence

$$
\varphi_\mathbf{h} \approx \varphi_\mathbf{k} + \varphi_\mathbf{h-k}
$$

which shows that if the phases of two structure factors are known then the phase of the third one may be estimated.

:::{figure} ../assets/day2/direct-methods/cochran-distributions.jpg
:alt: Family of von Mises probability distributions of the triplet phase for increasing values of the concentration parameter G
:width: 55%

Probability distributions based on Cochran's formula for different values of the parameter $G$.
:::

## Structure factor phase estimate: the tangent formula

If more than one pair of phases

$$
\varphi_\mathbf{h} \approx \varphi_{\mathbf{k}_j} + \varphi_{\mathbf{h}-\mathbf{k}_j}, \qquad j = 1, 2, \ldots, r
$$

is known, all defining the same phase $\varphi_\mathbf{h}$ through triplet relations, then

$$
\tan \varphi_\mathbf{h} \approx \frac{\displaystyle\sum_j^r G_j \sin(\varphi_j)}{\displaystyle\sum_j^r G_j \cos(\varphi_j)} = \frac{A_\mathbf{h}}{B_\mathbf{h}},
\qquad
G_j = G_{\mathbf{hk}_j}
$$

gives the most probable value of $\varphi_\mathbf{h}$. The reliability parameter is

$$
\alpha_\mathbf{h} = \sqrt{A_\mathbf{h}^2 + B_\mathbf{h}^2}
$$

:::{figure} ../assets/day2/direct-methods/tangent-argand.jpg
:alt: Argand-plane construction of the tangent formula as the vector sum of five complex contributions
:width: 55%

Graphical representation of the tangent formula: it is visualized in the Argand plane as the resultant of the sum of five complex vectors $G_j \exp(i\vartheta_j)$.
:::

## A typical direct methods procedure

:::{figure} ../assets/day2/direct-methods/dm-procedure-tangent.png
:alt: Flowchart of the tangent formula procedure, from scaling and normalization through random phase assignment, phase extension and refinement, to a trial phase set
:width: 100%

Inside the tangent formula procedure: random phase assignment, phase extension, phase refinement, and a figure of merit for each of $N_{max}$ trials.
:::

:::{figure} ../assets/day2/direct-methods/dm-procedure-full.png
:alt: Flowchart of the full direct methods procedure ending in E-map calculation, structure refinement and completion, and the structure model
:width: 100%

The full procedure: the most reliable trials are selected, an E-map is calculated, and the model is refined and completed until it is suitable.
:::

## DSR — direct space refinement

:::{figure} ../assets/day2/direct-methods/dsr-edm.png
:alt: Diagram of the direct space refinement cycle from starting phases to an electron density map, an EDM step and updated phases, with typical EDM operators listed below
:width: 100%
:::

## Completing and refining the structure

Errors in the model: missing atoms, position errors, errors in the thermal parameters.

A Fourier series having as coefficients $F^c_\mathbf{h}$ gives the positions of the atoms of the given model:

$$
\rho_c(\mathbf{r}) = \frac{1}{V} \sum_\mathbf{h} F^c_\mathbf{h} \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}\right)
$$

A Fourier series having as coefficients $F^o_\mathbf{h} = |F^o_\mathbf{h}| \exp(i\varphi_{\text{true}})$ gives the true structure:

$$
\rho_o(\mathbf{r}) = \frac{1}{V} \sum_\mathbf{h} F^o_\mathbf{h} \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}\right)
$$

Their difference shows how much the initial model deviates from the real structure:

$$
\Delta\rho(\mathbf{r}) = \rho_o(\mathbf{r}) - \rho_c(\mathbf{r}) = \frac{1}{V} \sum_\mathbf{h} \left( F^o_\mathbf{h} - F^c_\mathbf{h} \right) \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r}\right)
$$

### Difference Fourier synthesis method

$\varphi_{\text{true}}$ are unknown, so the approximation $\varphi_{\text{true}} \approx \varphi^c_\mathbf{h}$ is used:

$$
\Delta\rho(\mathbf{r}) = \frac{1}{V} \sum_\mathbf{h} \left( |F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right) \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r} + i\varphi^c_\mathbf{h}\right)
$$

$$
\rho_{\text{best}}(\mathbf{r}) = \frac{1}{V} \sum_\mathbf{h} \left( 2|F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right) \exp\!\left(-2\pi i\, \mathbf{h}\cdot\mathbf{r} + i\varphi^c_\mathbf{h}\right)
$$

## Completion of the crystal structure and preliminary refinement

::::{grid} 1 3 3 3

:::{figure} ../assets/day2/direct-methods/completion-flowchart.png
:alt: Flowchart from a partial atomic model through difference Fourier, adding atoms and least-squares refinement, looping back until the structure is complete
:::

:::{figure} ../assets/day2/direct-methods/emap-model.jpg
:alt: Ball-and-stick model of a structure obtained directly from an E-map, with spurious and misplaced atoms
E-map.
:::

:::{figure} ../assets/day2/direct-methods/refined-model.jpg
:alt: The same structure after kinematical model refinement, with a clean and chemically sensible geometry
After kinematical model refinement.
:::

::::

## Least-squares method

Functions to minimize:

$$
M = \sum_\mathbf{h} w_\mathbf{h} \left( |F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right)^2
\qquad
M' = \sum_\mathbf{h} w'_\mathbf{h} \left( |F^o_\mathbf{h}|^2 - |F^c_\mathbf{h}|^2 \right)^2
$$

Residual factors (R-factors):

$$
wR_f = \left[ \frac{\displaystyle\sum_\mathbf{h} w_\mathbf{h} \left( |F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right)^2}{\displaystyle\sum_\mathbf{h} w_\mathbf{h} |F^o_\mathbf{h}|^2} \right]^{1/2}
\qquad
R_f = \frac{\displaystyle\sum_\mathbf{h} \left| |F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right|}{\displaystyle\sum_\mathbf{h} |F^o_\mathbf{h}|}
$$

$$
S = \left[ \frac{\displaystyle\sum_\mathbf{h} w_\mathbf{h} \left( |F^o_\mathbf{h}| - |F^c_\mathbf{h}| \right)^2}{N_R - N_P} \right]^{1/2}
$$

## Correct solution identification

For X-ray data, the correct solution is marked by an outstanding value of the FOM ($R_f \ll 25\%$).

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/sir-fom.jpg
:alt: SIR graphical interface showing the solved structure, the final FOM versus R-factor plot, and the trial list with the best solution highlighted
$R_f = 9.06$ for the best trial.
:::

:::{figure} ../assets/day2/direct-methods/carbamate-formula.png
:alt: Chemical structure diagram of the gold carbamate complex
:::

::::

:::{admonition} Electron diffraction is different
:class: warning
This is not always true for electron diffraction data. The lowest value of $R_f$ does not necessarily indicate the best solution.
:::

## Main parameters in the phasing process

### Data resolution

When data resolution is around 1 Å or better, phase determination can normally be obtained *ab initio* by direct methods.

### Data completeness

- **>70–80% completeness** — structure solution is often feasible
- **<60% completeness** — solution becomes difficult or unstable, depending also on resolution and data quality

#### Akermanite, PED data

Data up to 0.4 Å, completeness ≈ 23%.

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/akermanite-sir.jpg
:alt: SIR session for akermanite showing the trial list, FOM histogram and scatter plot, and the solved structure
:::

:::{figure} ../assets/day2/direct-methods/akermanite-completeness.jpg
:alt: Table of the distribution of reflections against resolution for akermanite, with the per-shell completeness column highlighted
23.46% completeness to 0.40 Å.
:::

::::

Data from Gemmi et al., *Amer. Miner.* **92**, 408 (2007).

#### Orthocetamol, STEM-3DED data

Data up to 0.78 Å, completeness ≈ 80%.

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/orthocetamol-sir.jpg
:alt: SIR session for orthocetamol showing the trial list, FOM histogram and scatter plot, and the solved molecular structure
:::

:::{figure} ../assets/day2/direct-methods/orthocetamol-completeness.png
:alt: Table of the distribution of reflections against resolution for orthocetamol, with the per-shell completeness column highlighted
79.90% completeness to 0.78 Å.
:::

::::

Data from [](doi:10.1002/anie.201904564).

## Structure solution of the complex silicate Ca₂FeAl₂Si₃O₁₃ by direct methods

Cell: 8.86 5.62 10.11 90 115.3 90 — space group $P2_1/m$. Resolution 0.77 Å, $R_{int} = 14.27\%$.

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/direct-methods/silicate-structure.jpg
:alt: Polyhedral model of the solved silicate structure
:::

:::{figure} ../assets/day2/direct-methods/silicate-pattern.jpg
:alt: Reconstructed diffraction pattern of the silicate
:::

::::

::::{grid} 1 3 3 3

:::{figure} ../assets/day2/direct-methods/silicate-fom.png
:alt: Early FOM histogram and final FOM versus R-factor scatter plot for the silicate solution
FOM statistics.
:::

:::{figure} ../assets/day2/direct-methods/silicate-rint.png
:alt: Table of the number of reflections and Rint per resolution shell
Merging statistics.
:::

:::{figure} ../assets/day2/direct-methods/silicate-completeness.jpg
:alt: Table of the distribution of reflections against resolution with the per-shell completeness column
88.58% completeness to 0.77 Å.
:::

::::

The merging residual value:

$$
R_{int} = \frac{\sum \left| F_o^2 - \left\langle F_o^2 \right\rangle \right|}{\sum F_o^2}
$$

## Recommended reading on direct methods

- Woolfson, M. M. & Fan Hai-Fu. *Physical and Non-Physical Methods of Solving Crystal Structures*, 1st edition.
- Giacovazzo, C., Monaco, H. L., Artioli, G., Viterbo, D. and others. *Fundamentals of Crystallography* (International Union of Crystallography Texts on Crystallography), 3rd edition.
- Shmueli, U. *Theories and Techniques of Crystal Structure Determination*.
- Main, P., Clegg, W., Blake, A. J. & Gould, R. O. *Crystal Structure Analysis: Principles and Practice*.
- Giacovazzo, C. *Phasing in Crystallography: A Modern Perspective*.
