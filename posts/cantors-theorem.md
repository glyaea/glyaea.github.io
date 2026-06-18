---
time: 2026-05-23 15:00
title: Cantor's theorem
---

**Theorem**. There exists no surjective function from a set to its power set.

*Proof*. Suppose there exists such a magical surjective function
$$
	f:X\to\mathcal{P}(X)
$$
where $X$ is a set.
Then, let $D=\{x\in X\mid x\notin f(x)\}$.
By the definition of surjectivity:
$$
	\forall y\in\mathcal{P}(X),\,
	\exists x\in X\,(
		f(x)=y
	)
$$
In particular, since $D\in\mathcal{P}(X)$:
$$
	\exists c\in X\,(
		f(c)=D
	)
$$
Is $c\in D$?
By the definition of $D$, if $c\in D$, then $c\notin f(c)=D$.
This is contradictory, so our original supposition is false.
