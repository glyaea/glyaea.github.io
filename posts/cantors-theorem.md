---
date: 2026-05-23
name: Cantor's Theorem
---

There exists no surjective function from a set to its power set. To see why,
let $X$ be a set and assume there exists such a $f:X\to\mathcal{P}(X)$.
Since $f$ is surjective, we have:

$$
	\forall y\in\mathcal{P}(X):(
		\exists x\in X:(
			f(x)=y
		)
	)
$$

Let $D=\{x\in X\mid x\notin f(x)\}$. Since $D\in\mathcal{P}(X)$, we have:

$$
	\exists x\in X:(
		f(x)=D
	)
$$

Let $d\in X$. Then, we have:

$$
	f(d)=D
$$

Clearly, either $d\in D$ or $d\notin D$. If $d\in D$, then $d\notin f(d)$.
Otherwise, $d\in f(d)$. Overall, since $f(d)=D$, we have:

$$
	d\in D
	\iff
	d\notin D
$$

Since this is a contradiction, the assumption that $f$ exists is false.
