---
time: 2026-05-04 16:30
title: BatchNorm and LayerNorm
---

Suppose you have data as follows.

|       | Age | Points |
|-------|-----|--------|
| Alice | $1$ | $2$    |
| Bob   | $3$ | $4$    |

BatchNorm (resp. LayerNorm) maps each $X\in\{\{1,3\},\{2,4\}\}$ (resp. $X\in\{\{1,2\},\{3,4\}\}$) to
$$
\gamma_{X}
\left(
	\frac{x-\mu_{X}}{\sigma_{X}}
	\;\middle|\;
	x\in X
\right)
+
\beta_{X}
$$
where $\gamma_{X}\in\R$ is a learned scale parameter of $X$,
and $\beta_{X}\in\R$ is a learned shift parameter of $X$,
and $\mu_{X}\in\R$ is the mean of $X$,
and $\sigma_{X}\in\R$ is the standard deviation of $X$.
