---
title: BatchNorm and LayerNorm
date: 2026-05-04 16:30
---

![Image](https://miro.medium.com/v2/1*V4rbfeod7qAj7b7x5MuGbg.png)

Suppose you have data as follows.

| Sample | Distance (m) | Time (s) |
|--------|--------------|----------|
| A      | 1            | 2        |
| B      | 3            | 4        |

BatchNorm (resp. LayerNorm)
maps each $\mathbf{x}\in\{(1,3),(2,4)\}$ (resp. $\mathbf{x}\in\{(1,2),(3,4)\}$)
to
$$
\gamma_{\mathbf{x}}\left(\frac{x-\mu_{\mathbf{x}}}{\sigma_{\mathbf{x}}}\ \middle\vert\ x\in\mathbf{x}\right)+\beta_{\mathbf{x}}
$$
where $\gamma_{\mathbf{x}}\in\mathbb{R}$ is a learned scale parameter of $\mathbf{x}$,
and $\beta_{\mathbf{x}}\in\mathbb{R}$ is a learned shift parameter of $\mathbf{x}$,
and $\mu_{\mathbf{x}}\in\mathbb{R}$ is the mean of $\mathbf{x}$,
and $\sigma_{\mathbf{x}}\in\mathbb{R}$ is the standard deviation of $\mathbf{x}$.
