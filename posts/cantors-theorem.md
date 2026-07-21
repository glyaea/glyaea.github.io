---
date: 2026-05-23
name: Cantor's theorem
---

There exists no surjective function from a set to its power set.
To see why, let $X$ be a set, and assume there exists such a magical surjective function:

$$
f:X\to\mathcal{P}(X)
$$

Further, let $D=\{x\in X\mid x\notin f(x)\}$.
Since $f$ is surjective, by definition of surjectivity:

$$
	\forall y\in\mathcal{P}(X),
	\exists x\in X(
		f(x)=y
	)
$$

Since $D\in\mathcal{P}(X)$:

$$
	\exists x\in X(f(x)=D)
$$

Let $d\in X$. Then:

$$
	f(d)=D
$$

Now consider: is $d\in D$?
If $d\in D$, then by definition of $D$:

$$
	d\notin(f(d)=D)
$$

Since $d\notin D$ contradicts $d\in D$, the assumption that $f$ exists is false.
