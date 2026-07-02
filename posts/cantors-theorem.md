---
time: 2026-05-23 15:00
title: Cantor's theorem
---

It turns out there is no surjective function from a set to its power set.

To see why, assume there exists such a magical surjective function
$$
	f:X\to\mathcal{P}(X)
$$
where $X$ is a set. Further, let $D=\{x\in X\mid x\notin f(x)\}$.

Since $f$ is surjective, by the definition of surjectivity, we have:
$$
	\forall y\in\mathcal{P}(X),\,
	\exists x\in X\,(
		f(x)=y
	)
$$

Since $D\in\mathcal{P}(X)$, we simply have:
$$
	\exists x\in X\,(
		f(x)=D
	)
$$

Let $d\in X$. Then, we have:
$$
	f(d)=D
$$

Now consider: is $d\in D$?

If $d\in D$, then by the definition of $D$, we have:
$$
	d\notin f(d)
$$

Since $f(d)=D$, we have:
$$
	d\notin D
$$

It is impossible to have $d\notin D$ if $d\in D$, so our assumption that $f$ exists is false.
