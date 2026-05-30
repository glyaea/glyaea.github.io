---
title: Generalised Cantor diagonalisation
date: 2026-05-23 15:00
---

It turns out there exists no surjective function from a set to its power set.

Here is a way to reason through it!

1. Let $X$ be a set.
2. Suppose there exists surjective function $f:X\to\mathcal{P}(X)$.
2. Let $d=\{x\in X\mid x\notin f(x)\}$ be a diagonal set.
3. Now, $f$ is supposedly surjective, so it satisfies the usual definition of surjectivity:
for each codomain element $y\in\mathcal{P}(X)$,
there exists domain element $x\in X$
such that $f(x)=y$.
4. In particular, the diagonal set is a codomain element $d\in\mathcal{P}(X)$, so
there exists domain element $x\in X$
such that $f(x)=d$.
5. Consider: is $x\in d$?
If $x\in d$, then $x\notin f(x)=d$.
6. This is contradictory, so our supposition that $f$ exists must be false.
