---
date: 2026-05-23
name: Cantor's Theorem
---

There exists no surjective function from a set to its power set. To see why,
let $X$ be a set and assume there exists such a $f:X\to\mathcal{P}(X)$.
Further, let $D=\{x\in X\mid x\notin f(x)\}$. Since $f$ is surjective, we have:

$$
	\forall y\in\mathcal{P}(X),
	\exists x\in X
	:
	f(x)=y
$$

Since $D\in\mathcal{P}(X)$, we have:

$$
	\exists x\in X
	:
	f(x)=D
$$

Let $d\in X$. Then, we have:

$$
	f(d)=D
$$

If $d\in D$, then we have:

$$
	d\notin(f(d)=D)
$$

Since $d\notin D$ contradicts $d\in D$, the assumption that $f$ exists is
false.
