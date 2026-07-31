---
date: 2026-05-04
name: BatchNorm and LayerNorm
---

Suppose you have data as follows.

|       | Age | Points |
| ----- | --- | ------ |
| Alice | $1$ | $2$    |
| Bob   | $3$ | $4$    |

BatchNorm (resp. LayerNorm) maps each $X\in\{\{1,3\},\{2,4\}\}$ (resp.
$X\in\{\{1,2\},\{3,4\}\}$) to

$$
	\gamma
	\left(
		\frac{x-\mu}{\sigma}
		\;\middle|\;
		x\in X
	\right)
	+
	\beta
$$

where $\gamma\in\mathbb{R}$ is a learned scale parameter of $X$, and
$\beta\in\mathbb{R}$ is a learned shift parameter of $X$, and
$\mu\in\mathbb{R}$ is the mean of $X$, and $\sigma\in\mathbb{R}$ is the
standard deviation of $X$.
