---
title: Embedding and unembedding layers
date: 2026-05-24 15:30
---

An embedding layer is often a function
$$
	\begin{aligned}
		f
		&:
		\mathbb{R}^{V}\times\mathbb{R}^{n\times V}
		\to
		\mathbb{R}^{n}
		\\
		f(\bm{x};\bm{E})
		&=
		\bm{E}\bm{x}
	\end{aligned}
$$
where $V,n\in\mathbb{N}_{\geq 1}$.
Intuitively, an embedding layer can be seen as a function
that maps a one-hot vector to its embedding.

An unembedding layer is often a function
$$
	\begin{aligned}
		g
		&:
		\mathbb{R}^{n}\times\mathbb{R}^{V\times n}
		\to
		\mathbb{R}^{V}
		\\
		g(\bm{x};\bm{U})
		&=
		\bm{U}\bm{x}
	\end{aligned}
$$
where $n,V\in\mathbb{N}_{\geq 1}$.
Intuitively, an unembedding layer can be seen as a function
that maps an embedding to its one-hot vector.
