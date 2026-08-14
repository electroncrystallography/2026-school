---
title: "Structure refinement: kinematical"
short_title: "Kinematical refinement"
---

# Structure refinement: kinematical

:::{div}
:class: ecs-session-meta
**Day 2 · Sunday 9 August · 15:00 – 16:00** — [Corrado Cuocci](../instructors.md#speaker-corrado-cuocci)
:::

## Reasons for performing refinement

- To improve phasing
- To try to verify that the structure is 'correct'
- To obtain the 'best' values for the parameters in the model

Refinement takes a **trial model** to **the model that best represents the data**. The trial model may suffer from:

- Incorrect atom type assignments for some coordinates
- Atomic coordinates not very accurate
- Missing structural details: groups of lighter atoms not yet located
- Disorder not yet identified or modeled
- Hydrogen positions not yet determined

## Principles of least squares

A set of $N$ observations $y_1, y_2, \ldots y_n$ with weights $w_1, w_2, \ldots w_N$ assigned to them, and the quantity to minimise:

$$
S = \sum_{i=1}^{n} w_i \left[ y_{i,obs} - y_{i,calc} \right]^2
$$

The $p$ unknown parameters are $x_1, x_2, \ldots x_p$, and each calculated observation is a model function of them:

$$
y_{1,calc} = M_1(x_1, x_2, \ldots, x_p), \quad
y_{2,calc} = M_2(x_1, x_2, \ldots, x_p), \quad \ldots \quad
y_{N,calc} = M_N(x_1, x_2, \ldots, x_p)
$$

Writing $y_{i,calc} = M_i(\mathbf{x})$ for $i = 1, 2, \ldots n$:

$$
S = \sum_{i=1}^{n} w_i \left[ y_{i,obs} - M_i(\mathbf{x}) \right]^2
$$

In matrix form:

$$
S = \left[ \mathbf{y} - \mathbf{M}(\mathbf{x}) \right]^T \mathbf{W} \left[ \mathbf{y} - \mathbf{M}(\mathbf{x}) \right]
$$

$\mathbf{W}$ is a diagonal square matrix representing individual weights:

$$
\mathbf{W} = \begin{pmatrix}
w_1 & 0 & \cdots & 0 \\
0 & w_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & w_n
\end{pmatrix}
$$

The condition for $S$ to be a minimum gives the **normal equations**:

$$
\frac{\partial S}{\partial x_j} = -2 \sum_{i=1}^{n} w_i \left[ y_{i,obs} - M_i(\mathbf{x}) \right] \frac{\partial M_i(\mathbf{x})}{\partial x_j} = 0,
\qquad j = 1, \ldots p
$$

The model functions $M_i(\mathbf{x})$ are, in general, nonlinear.

## Linear least squares

$$
y_{i,calc} = M_i(\mathbf{x}) = b_i + \sum_{j=1}^{p} a_{ij} x_j, \qquad i = 1, \ldots n
$$

In matrix form $\mathbf{M}(\mathbf{x}) = \mathbf{b} + \mathbf{A}\mathbf{x}$, with the design matrix

$$
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1p} \\
a_{21} & a_{22} & \cdots & a_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
a_{N1} & a_{N1} & \cdots & a_{np}
\end{pmatrix}
$$

Since $\partial M_i(\mathbf{x}) / \partial x_j = a_{ij}$, the minimum condition becomes

$$
\sum_{i=1}^{n} w_i \left[ y_{i,obs} - b_i - \sum_{k=1}^{p} a_{ik} x_k \right] a_{ij} = 0
$$

$$
\sum_{i=1}^{n} a_{ij} w_i \sum_{k=1}^{p} a_{ik} x_k = \sum_{i=1}^{n} a_{ij} w_i (y_{i,obs} - b_i), \qquad j = 1, \ldots p
$$

The normal equations of the weighted linear least-squares problem:

$$
\sum_{k=1}^{p} \left( \sum_{i=1}^{n} a_{ij} w_i a_{ik} \right) x_k = \sum_{i=1}^{n} a_{ij} w_i (y_{i,obs} - b_i)
$$

The two bracketed quantities are $(\mathbf{A}^T \mathbf{W} \mathbf{A})_{jk}$ and $\left[ \mathbf{A}^T \mathbf{W} (\mathbf{y} - \mathbf{b}) \right]_j$, so in matrix notation

$$
\mathbf{A}^T \mathbf{W} \mathbf{A}\, \mathbf{x} = \mathbf{A}^T \mathbf{W} (\mathbf{y} - \mathbf{b})
$$

The solution is

$$
\mathbf{x} = \left( \mathbf{A}^T \mathbf{W} \mathbf{A} \right)^{-1} \mathbf{A}^T \mathbf{W} (\mathbf{y} - \mathbf{b})
$$

but the explicit computation of the inverse $(\mathbf{A}^T\mathbf{W}\mathbf{A})^{-1}$ is avoided in practice. Writing

$$
\mathbf{N} = \mathbf{A}^T \mathbf{W} \mathbf{A}, \qquad \mathbf{q} = \mathbf{A}^T \mathbf{W} (\mathbf{y} - \mathbf{b})
\qquad \Longrightarrow \qquad
\mathbf{N} \mathbf{x} = \mathbf{q}
$$

$\mathbf{N}$ is a symmetric positive-definite matrix. The system is solved using:

- Cholesky decomposition
- QR decomposition

### Cholesky factorisation

$$
\mathbf{N} = \mathbf{L}\mathbf{L}^T
$$

$$
\mathbf{N} = \begin{pmatrix}
l_{11} & 0 & 0 & \cdots & 0 \\
l_{21} & l_{22} & 0 & \cdots & 0 \\
l_{31} & l_{32} & l_{33} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
l_{m1} & l_{m2} & l_{m3} & \cdots & l_{pp}
\end{pmatrix}
\begin{pmatrix}
l_{11} & l_{21} & l_{31} & \cdots & l_{p1} \\
0 & l_{22} & l_{32} & \cdots & l_{p2} \\
0 & 0 & l_{33} & \cdots & l_{p3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & l_{pp}
\end{pmatrix}
$$

:::{figure} ../assets/day2/kinematical/cholesky-blocks.jpg
:alt: Block diagram showing the symmetric positive-definite matrix N as the product of a lower triangular matrix L and its transpose
:width: 70%
:::

The system $\mathbf{N}\mathbf{x} = \mathbf{q}$ is solved in two triangular steps:

$$
\mathbf{L}\mathbf{L}^T \mathbf{x} = \mathbf{q}
\quad \rightarrow \quad
\mathbf{L}\mathbf{z} = \mathbf{q} \;\; \text{(forward substitution)} \;\; \rightarrow \;\; \mathbf{z}
$$

$$
\mathbf{L}^T \mathbf{x} = \mathbf{z} \;\; \text{(back substitution)} \;\; \rightarrow \;\; \mathbf{x}
$$

**Limitations:** it requires forming $\mathbf{N} = \mathbf{A}^T\mathbf{W}\mathbf{A}$ explicitly, which squares the condition number. This can cause loss of accuracy.

### QR factorization

Instead of forming the normal equations ($\mathbf{N}\mathbf{x} = \mathbf{q}$) explicitly, this approach works directly on the weighted data matrix:

$$
\tilde{\mathbf{A}} = \mathbf{W}^{\frac{1}{2}} \mathbf{A},
\qquad
\tilde{\mathbf{r}} = \mathbf{W}^{\frac{1}{2}} (\mathbf{y} - \mathbf{b})
\qquad \Longrightarrow \qquad
\tilde{\mathbf{A}}^T \tilde{\mathbf{A}} \mathbf{x} = \tilde{\mathbf{A}} \tilde{\mathbf{r}}
$$

so the weighted least-squares problem is equivalent to an unweighted one on $\tilde{\mathbf{A}}$, and

$$
\tilde{\mathbf{A}} = \mathbf{Q}\mathbf{R}
$$

:::{figure} ../assets/day2/kinematical/qr-blocks.png
:alt: Block diagram showing the design matrix as the product of an N by p matrix with orthonormal columns and a p by p upper triangular matrix
:width: 80%

$\tilde{\mathbf{A}}$ is the $N \times p$ design matrix, $\mathbf{Q}$ has orthonormal columns ($N \times p$), and $\mathbf{R}$ is upper triangular ($p \times p$).
:::

Substituting the factorization reduces the problem to a single back substitution:

$$
(\mathbf{Q}\mathbf{R})^T (\mathbf{Q}\mathbf{R}) \mathbf{x} = (\mathbf{Q}\mathbf{R})^T \tilde{\mathbf{r}}
\quad \rightarrow \quad
\mathbf{R}^T \mathbf{Q}^T \mathbf{Q} \mathbf{R} \mathbf{x} = \mathbf{R}^T \mathbf{Q}^T \tilde{\mathbf{r}}
$$

$$
\mathbf{R}^T \mathbf{R} \mathbf{x} = \mathbf{R}^T \mathbf{Q}^T \tilde{\mathbf{r}}
\quad \rightarrow \quad
\mathbf{R}\mathbf{x} = \mathbf{Q}^T \tilde{\mathbf{r}}
\quad \rightarrow \quad
\mathbf{x}
$$

using $\mathbf{Q}^T\mathbf{Q} = \mathbf{I}_m$ and $(\mathbf{R}^T)^{-1}\mathbf{R}^T = \mathbf{I}_m$.

- QR avoids the explicit formation of the normal matrix $\mathbf{N}$
- Numerically more stable when parameters are highly correlated or the matrix is ill-conditioned

## Nonlinear least squares

Expanding the model function $\mathbf{M}(\mathbf{x})$ around the starting point $\mathbf{x}_0$ in Taylor's series and retaining only the linear terms we obtain the equation:

$$
M_i(\mathbf{x}) = M_i(\mathbf{x}_0) + \sum_{j=1}^{p} J_{ij}(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0)_j
$$

In matrix form:

$$
\mathbf{M}(\mathbf{x}) = \mathbf{M}(\mathbf{x}_0) + \mathbf{J}(\mathbf{x}_0) \Delta\mathbf{x}
$$

- $\Delta\mathbf{x} = (\mathbf{x} - \mathbf{x}_0)$ — the vector of parameter shifts
- $\mathbf{J}(\mathbf{x}_0) \in \mathbb{R}^{N \times p}$, $\left[ \mathbf{J}(\mathbf{x}_0) \right]_{ij} = \left. \dfrac{\partial M_i}{\partial x_j} \right|_{\mathbf{x}_0}$ — the Jacobian matrix

### The Gauss-Newton algorithm

For each $k$ iteration:

1. Compute the search direction $\Delta\mathbf{x}$ as the solution of the linear system

   $$
   \mathbf{J}^T \mathbf{W} \mathbf{J} \Delta\mathbf{x} = \mathbf{J}^T \mathbf{W} \left[ \mathbf{y} - \mathbf{M}(\mathbf{x}) \right]
   $$

2. Set $\mathbf{x}_k = \mathbf{x}_{k-1} + \Delta\mathbf{x}$

3. If not converged go to (1), else stop.

### Gauss-Newton-type methods

**Gauss-Newton method with a line search.** Set $\mathbf{x}_{k-1} = \mathbf{x}_k + \alpha \Delta\mathbf{x}$, where $\alpha$, called the step length, is such that the algorithm is in descendant condition:

$$
S(\mathbf{x}_k + \alpha \Delta\mathbf{x}) < S(\mathbf{x}_k)
$$

$\alpha$ is chosen by a line-search procedure.

**Levenberg–Marquardt** algorithms modify the normal equations to

$$
\left( \mathbf{J}^T \mathbf{W} \mathbf{J} + \lambda \mathbf{I} \right) \Delta\mathbf{x} = \mathbf{J}^T \mathbf{W} \left[ \mathbf{y} - \mathbf{M}(\mathbf{x}) \right]
$$

where $\mathbf{I}$ is the identity matrix and $\lambda$ is a damping factor.

## Standard deviations

Variance-covariance matrix:

$$
\mathbf{V}_x = \left( \mathbf{J}^T \mathbf{W} \mathbf{J} \right)^{-1}
$$

$$
\sigma(x_j) = \sqrt{ \frac{(V_x)_{jj}\, S}{n - p} }
$$

- $n$ is the number of observations
- $p$ is the number of unknown parameters
- $(V_x)_{jj}$ is the corresponding diagonal element of the variance-covariance matrix

Inversion via Cholesky:

$$
\mathbf{N}^{-1} = (\mathbf{L}^T\mathbf{L})^{-1} = \mathbf{L}^{-1}(\mathbf{L}^T)^{-1} = \mathbf{L}^{-1}(\mathbf{L}^{-1})^T
$$

Inversion via QR:

$$
\mathbf{N}^{-1} = (\mathbf{R}^T\mathbf{R})^{-1} = \mathbf{R}^{-1}(\mathbf{R}^T)^{-1} = \mathbf{R}^{-1}(\mathbf{R}^{-1})^T
$$

## Newton-like methods

Quadratic approximation $q(\Delta x)$ to $S$ at the current point $x_k$:

$$
S(\mathbf{x}_k + \Delta\mathbf{x}) \approx S(\mathbf{x}_k) + \nabla S_k^T \Delta\mathbf{x} + \frac{1}{2} \Delta\mathbf{x}^T \mathbf{H}_k \Delta\mathbf{x} = q(\Delta\mathbf{x})
$$

- $\nabla S_k$ is the gradient at $x_k$, a column vector of dimension $p$
- $H_k$ is the Hessian matrix at $x_k$, $p \times p$ symmetric, $H_{ij} = \dfrac{\partial^2 S}{\partial x_i\, \partial x_j}$

$$
\frac{\partial q}{\partial (\Delta\mathbf{x})} = \nabla S_k + \mathbf{H}_k \Delta\mathbf{x} = \mathbf{0}
\qquad \Longrightarrow \qquad
\mathbf{H}_k \Delta\mathbf{x} = -\nabla S_k
$$

**Advantages:** very fast convergence near the solution.

## Quasi-Newton methods

$$
\mathbf{H}_k = 2\mathbf{J}_k^T \mathbf{W} \mathbf{J}_k - 2\mathbf{B}_k,
\qquad
(\mathbf{B}_k)_{ij} = \sum_{i}^{N} w_h \left( y_i - M_i(x_k) \right) \frac{\partial^2 M_i(x_k)}{\partial x_i\, \partial x_j}
$$

The Gauss-Newton approximation is $\mathbf{B}_k \approx 0$.

Since computing $H_k$ exactly is prohibitively expensive, quasi-Newton methods iteratively approximate it using only gradient information. **BFGS** and **L-BFGS** directly update an approximation of $H_k$, avoiding the computation of $J_k$ and requiring only gradient evaluations.

Programs using L-BFGS: Phenix, CNS, Rosetta, GROMACS/AMBER/CHARMM, SciPy.

## Conjugate-gradients methods

At each iteration

$$
\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{p}_k
$$

with the step length $\alpha_k$ found by line search and the search direction

$$
\mathbf{p}_k = -\mathbf{g}_k + \beta_k \mathbf{p}_{k-1}
$$

Several formulas exist for $\beta_k$. The most common are **Fletcher–Reeves** and **Polak–Ribière**. It is chosen to make $\mathbf{p}_k$ and $\mathbf{p}_{k+1}$ conjugate:

$$
\mathbf{p}_i^\top A\, \mathbf{p}_j = 0 \qquad (i \neq j)
$$

:::{figure} ../assets/day2/kinematical/conjugate-gradient-contours.png
:alt: Two contour plots comparing a zig-zagging steepest descent path with a conjugate gradient path that reaches the minimum in two steps
:width: 85%

Steepest descent (left): each step undoes part of the last — many zig-zags. Conjugate gradient (right): two A-conjugate steps reach the exact minimum.
:::

**Advantages:** no Hessian is required, low memory consumption, particularly suitable for very large optimization problems, each iteration is computationally inexpensive.

**Disadvantages:** rarely competitive with Gauss–Newton / Levenberg–Marquardt.

### The conjugate gradient method for solving linear systems

The Gauss-Newton system

$$
\left( \mathbf{J}^\top \mathbf{W} \mathbf{J} \right) \Delta\mathbf{x} = -\mathbf{J}^\top \mathbf{W} \mathbf{r}
$$

has the form $\mathbf{A}\mathbf{x} = \mathbf{b}$. Solving $\mathbf{A}\mathbf{x} = \mathbf{b}$ is equivalent to minimizing the quadratic function

$$
f(\mathbf{x}) = \frac{1}{2} \mathbf{x}^T \mathbf{A} \mathbf{x} - \mathbf{b}^T \mathbf{x}
$$

:::{figure} ../assets/day2/kinematical/conjugate-gradient-algorithm.jpg
:alt: The conjugate gradient algorithm written as a sequence of update formulas for the residual, step length, solution and search direction
:width: 40%

The algorithm.
:::

This approach combines improved convergence properties with the low memory requirements and computational efficiency of iterative solvers, making it particularly attractive for large-scale optimization problems.

## Maximum likelihood

For each observation $y_i$, we can write the probability of observing it given the model $\mathbf{x}$ as a conditional distribution $p(y_i \mid \mathbf{x})$. If the errors are Gaussian with standard deviation $\sigma_i$:

$$
p(y_i \mid \mathbf{x}) = \frac{1}{\sigma_i \sqrt{2\pi}} \exp\!\left( -\frac{\left( y_i - M_i(\mathbf{x}) \right)^2}{2\sigma_i^2} \right)
$$

Common distributions: Gaussian, Poisson, Rice, Wilson, Cauchy (Lorentzian), Laplace.

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/kinematical/likelihood-gaussian-a.jpg
:alt: Gaussian probability density centred on the calculated value with the observed value marked on the flank of the curve
:::

:::{figure} ../assets/day2/kinematical/likelihood-gaussian-b.jpg
:alt: Gaussian probability density with the observed value close to the peak, giving a higher likelihood
:::

::::

Assuming the observations are mutually independent, the joint probability of all observations is the product — the **likelihood function**:

$$
L(\mathbf{x}) = \prod_i p(y_i \mid \mathbf{x})
$$

The ML estimate consists in finding the $\mathbf{x}$ that maximises this sum:

$$
\ln L(\mathbf{x}) = \sum_i \ln p(y_i \mid \mathbf{x})
$$

The quantity that is actually minimised:

$$
-\ln L(\mathbf{x}) = - \sum_i \ln p(y_i \mid \mathbf{x})
$$

ML refinement is available in programs such as REFMAC5 and Phenix.refine.

With a Gaussian error distribution this reduces to

$$
S = \sum_{i=1}^{n} \frac{\left( y_{i,obs} - y_{i,calc} \right)^2}{\sigma_i^2}
$$

so **ML with Gaussian errors coincides with least squares**.

## Functions to minimize

$$
S = \sum_{i=1}^{n} w_i \left[ y_{i,obs} - y_{i,calc} \right]^2
$$

becomes, for diffraction data,

$$
S = \sum_\mathbf{h} w_\mathbf{h} \left( F_\mathbf{h}^{o\,2} - F_\mathbf{h}^{c\,2} \right)^2
\qquad
S' = \sum_\mathbf{h} w'_\mathbf{h} \left( F_\mathbf{h}^{o} - F_\mathbf{h}^{c} \right)^2
$$

The first is currently the most widely used method, and the only one implemented in SHELX — the measured quantity being $I_{hkl} = C\,|F_{hkl}|^2$.

## Weights

$$
w_i = \frac{1}{\sigma^2(y_{i,obs})}
$$

$$
w_\mathbf{h} = \frac{1}{\sigma^2 \left( F_\mathbf{h}^{o\,2} \right)} \;\leftarrow\; \sigma(I_h)
\qquad
w'_\mathbf{h} = \frac{1}{\sigma^2 \left( F_\mathbf{h}^{o} \right)},
\qquad
\sigma^2 \left( F_\mathbf{h}^{o} \right) = \frac{\sigma^2 \left( F_\mathbf{h}^{o\,2} \right)}{4 F_\mathbf{h}^{o\,2}}
$$

## Model and parameters

$$
F^c_\mathbf{h} = K \sum_{j=1}^{n} O_j\, t_j(s)\, f_j(s) \exp\!\left[ 2\pi i (h x_j + k y_j + l z_j) \right]
$$

- $s$ is $\sin\theta_\mathbf{h} / \lambda$
- $n$ is the total number of atoms in the unit cell
- $f_j$ is the atomic scattering factor, determined by the atom type
- $x_j, y_j, z_j$ are the fractional coordinates of the $j$th atom in the unit cell
- $t_j$ is the temperature factor (atomic displacement parameters)
- $O_j$ is the occupation factor
- $K$ is a scale factor
- Flack parameter

Each atom is described by 9–10 parameters, and about 8–10 reflections per parameter are needed.

### Isotropic displacement parameter

$$
t_j(s) = \exp\!\left( -B_j \frac{\sin^2\theta}{\lambda^2} \right) = \exp\!\left( -B_j s^2 \right)
$$

$B_j$ is the displacement parameter of the $j$th atom,

$$
B_j = 8\pi \left< \bar{u}^2 \right>_j,
\qquad
U_j = B_j / 8\pi
$$

where $\left< \bar{u}^2 \right>_j$ is the root mean square deviation in Å.

:::{figure} ../assets/day2/kinematical/adp-isotropic.jpg
:alt: Sphere with arrows of equal length pointing outwards from the atom centre in all directions
:width: 30%

One independent parameter per atom.
:::

### Anisotropic displacement parameters

$$
\begin{aligned}
t_j = \exp\Big[ -\big( & B^j_{11} h^2 a^{*2} + B^j_{22} k^2 b^{*2} + B^j_{33} l^2 c^{*2} \\
& + 2B^j_{12} hk\, a^* b^* + 2B^j_{13} hl\, a^* c^* + 2B^j_{23} kl\, b^* c^* \big) \Big]
\end{aligned}
$$

$$
\begin{aligned}
t_j = \exp\Big[ -2\pi^2 \big( & U^j_{11} h^2 a^{*2} + U^j_{22} k^2 b^{*2} + U^j_{33} l^2 c^{*2} \\
& + 2U^j_{12} hk\, a^* b^* + 2U^j_{13} hl\, a^* c^* + 2U^j_{23} kl\, b^* c^* \big) \Big]
\end{aligned}
$$

$$
t_j = \exp\!\left[ -\mathbf{h}^{*\top} \mathbf{B}^j \mathbf{h}^* \right],
\qquad
\mathbf{h}^* = \begin{pmatrix} h\,a^* \\ k\,b^* \\ l\,c^* \end{pmatrix},
\qquad
\mathbf{B}^j = \begin{pmatrix}
B^j_{11} & B^j_{12} & B^j_{13} \\
B^j_{21} & B^j_{22} & B^j_{23} \\
B^j_{31} & B^j_{32} & B^j_{33}
\end{pmatrix}
$$

:::{figure} ../assets/day2/kinematical/adp-anisotropic.jpg
:alt: Ellipsoid with arrows of different lengths along its principal axes
:width: 35%

Six independent parameters per atom.
:::

## Residual factors

The weighted R-factor based on $F^2$ (*wR*, *wR2*):

$$
wR_f = \left[ \frac{\displaystyle\sum_\mathbf{h} w_\mathbf{h} \left( F_\mathbf{h}^{o\,2} - F_\mathbf{h}^{c\,2} \right)^2}{\displaystyle\sum_\mathbf{h} w_\mathbf{h} F_\mathbf{h}^{o\,2}} \right]^{1/2}
$$

The unweighted R-factor based on $F$ (*R*, *R1*):

$$
R_f = \frac{\displaystyle\sum_\mathbf{h} \left| F_\mathbf{h}^{o} - F_\mathbf{h}^{c} \right|}{\displaystyle\sum_\mathbf{h} F_\mathbf{h}^{o}}
$$

Goodness of fit (GooF, GoF, S):

$$
GoF = \left[ \frac{\displaystyle\sum_\mathbf{h} w_\mathbf{h} \left( F_\mathbf{h}^{o} - F_\mathbf{h}^{c} \right)^2}{n - p} \right]^{1/2}
$$

## Constraints

Constraints are mathematical relationships between parameters.

**Symmetry constraints** are mandatory and automatically imposed by the program.

- An atom on the special position $(\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2})$ should not be refined
- An atom on the special position $(x, x, x)$ in space group $P23$ should have equal shifts on $x$, $y$, $z$

**Constraints imposed by the user** to reduce the number of parameters:

- Riding model (move H atoms synchronously with the C atoms)
- Occupation factor — e.g. A, B atoms in the same site: $occ_A + occ_B = 1$
- Rigid groups
- Constraints on ADPs (TLS groups)

## Restraints

$$
S = \sum_\mathbf{h} w_\mathbf{h} \left( |F^o_\mathbf{h}|^2 - |F^c_\mathbf{h}|^2 \right)^2 + \sum_j w_j \left( T^o_j - T^c_j \right)^2
$$

- $T^c_j$ is the value of some target function computed from the structural parameters
- $T^o_j$ is the corresponding value taken from some other source (databases, similar structures, computational chemistry, …)

Restraints are generally applied under one (or both) of two situations:

- The starting model is very poor
- Normal refinement has produced an unacceptable structure

## Refinement strategies

### Adapt strategy to model quality

**Very good model** — full anisotropic refinement straight away.

**Unreliable model or poor/scarce data** — a more cautious approach is required:

- Initialize the scale factor and average isotropic ADP from the Wilson plot.
- Refine atomic positions first.
- Perform a few isotropic refinement cycles before introducing anisotropic ADPs.
- For structures with heavy atoms, refine heavy atoms anisotropically before extending to all atoms.
- Don't refine each stage to completion.

### ADPs flag misassigned atom types

Inspect ADPs carefully, they are powerful indicators of model errors.

- Unusually large ADPs may indicate an incorrectly assigned atom type. For example, if a C atom (six electrons) is erroneously assigned as an N atom (seven electrons), least squares will try to dissipate the extra electron by increasing the ADP.
- Extremely large ADPs often reveal spurious atoms that should be removed.
- Least-squares refinement can eliminate false atoms, but it cannot create missing ones.

### Elongated ADPs

Highly elongated (cigar-shaped) ADPs usually indicate atom disorder or misidentified positions. Split the atom into two partially occupied sites with refined positions.

:::{figure} ../assets/day2/kinematical/adp-split.png
:alt: One elongated displacement ellipsoid on the left, split on the right into two smaller ellipsoids at half occupancy each
:width: 100%

Left: least squares stretched one ellipsoid across two atomic positions. Right: the atom split into two partially occupied sites, with positions and site occupation factors refined, $occ(A') + occ(A'') = 1$.
:::

### Finding missing atoms

- Use chemical knowledge (e.g. complete a phenyl ring geometrically)
- Or locate them in a Fourier synthesis

### Hydrogen atoms

- Locate by difference Fourier maps at the end of isotropic ADP refinement
- Place H geometrically, refine the bonded (heavier) atoms anisotropically

Three strategies for hydrogen atom refinement:

- Refine the H atoms with riding constraints
- Refine them with restraints
- Recompute their positions geometrically after each cycle of refinement

X–H (X-ray) < X–H (neutrons):

::::{grid} 1 2 2 2

:::{figure} ../assets/day2/kinematical/oh-xray.jpg
:alt: Ball-and-stick O-H unit with a short O to H distance
0.80–0.85 Å (X-ray).
:::

:::{figure} ../assets/day2/kinematical/oh-neutron.jpg
:alt: Ball-and-stick O-H unit with a longer O to H distance
~0.96–0.98 Å (neutrons, electrons).
:::

::::

## References

- Watkin, D. J. (2008). Structure refinement: some background theory and practical strategies. *J. Appl. Cryst.* **41**, 491–522. [10.1107/S0021889808007279](https://doi.org/10.1107/S0021889808007279)
- Clegg, W., Blake, A. J., Gould, R. O. & Main, P. (2001). *Crystal Structure Analysis: Principles and Practice*. Oxford University Press, Oxford.
- Giacovazzo, C., Monaco, H. L., Artioli, G., Viterbo, D., Ferraris, G., Gilli, G., Zanotti, G. & Catti, M. (2002). *Fundamentals of Crystallography*, 2nd edn. IUCr/Oxford University Press, Oxford.
- Müller, P., Herbst-Irmer, R., Spek, A. L., Schneider, T. R. & Sawaya, M. R. (2006). *Crystal Structure Refinement: A Crystallographer's Guide to SHELXL*. Oxford University Press, Oxford. [10.1093/acprof:oso/9780198570769.001.0001](https://doi.org/10.1093/acprof:oso/9780198570769.001.0001)
- Massa, W. (2004). Structure Refinement (Cap. 9). In *Crystal Structure Determination*, 2nd edn., Springer, Berlin/Heidelberg. [10.1007/978-3-662-06431-3_9](https://doi.org/10.1007/978-3-662-06431-3_9)
- Hendrickson, W. A. (1985). Stereochemically Restrained Refinement of Macromolecular Structures. *Methods in Enzymology* **115**, 252–270. [10.1016/0076-6879(85)15021-4](<https://doi.org/10.1016/0076-6879(85)15021-4>)
- Tronrud, D. E. (2004). Introduction to macromolecular refinement. *Acta Cryst.* **D60**, 2156–2168. [10.1107/S090744490402356X](https://doi.org/10.1107/S090744490402356X)
- Prince, E. & Boggs, P. T. (2006). Least squares (Cap. 8.1, pp. 678–688). In *International Tables for Crystallography*, Vol. C. [10.1107/97809553602060000609](https://doi.org/10.1107/97809553602060000609)
- Shmueli, U. (2007). Refinement of Structural Parameters (Cap. 10). In *Theories and Techniques of Crystal Structure Determination*, IUCr/Oxford University Press. [10.1093/oso/9780199213504.001.0001](https://doi.org/10.1093/oso/9780199213504.001.0001)
- van der Maelen Uría, J. F. (1999). Current Methods and Optimization Algorithms for the Refinement of X-Ray Crystal Structures. *Crystallography Reviews* **7**(2), 125–180. [10.1080/08893119908039929](https://doi.org/10.1080/08893119908039929)
