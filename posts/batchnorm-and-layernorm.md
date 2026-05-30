---
title: BatchNorm and LayerNorm
date: 2026-05-04 16:30
---

<!-- ![Image](https://miro.medium.com/v2/1*V4rbfeod7qAj7b7x5MuGbg.png) -->

Suppose you have data as follows.

| Sample | Age | Points |
|--------|-----|--------|
| Alice  | $1$ | $2$    |
| Bob    | $3$ | $4$    |

BatchNorm (resp. LayerNorm) maps each $\bm{x}\in\{(1,3),(2,4)\}$ (resp. $\bm{x}\in\{(1,2),(3,4)\}$) to
$$
\gamma_{\bm{x}}\left(\frac{x-\mu_{\bm{x}}}{\sigma_{\bm{x}}}\ \middle\vert\ x\in\bm{x}\right)+\beta_{\bm{x}}
$$
where $\gamma_{\bm{x}}\in\mathbb{R}$ is a learned scale parameter of $\bm{x}$,
and $\beta_{\bm{x}}\in\mathbb{R}$ is a learned shift parameter of $\bm{x}$,
and $\mu_{\bm{x}}\in\mathbb{R}$ is the mean of $\bm{x}$,
and $\sigma_{\bm{x}}\in\mathbb{R}$ is the standard deviation of $\bm{x}$.
