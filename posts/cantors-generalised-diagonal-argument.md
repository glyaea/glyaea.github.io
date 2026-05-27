---
title: Cantor's generalised diagonal argument
date: 2026-05-23 15:00
---

It turns out that there exists no surjective function from a set to its power set.
To see why, let $X$ be a set, and suppose there exists a surjective function $f:X\to\mathcal{P}(X)$.
Then, define:
$$
	d=\{x\in X\mid x\notin f(x)\}
$$
Now, $f$ is supposedly surjective, so the usual definition of surjectivity applies: for each $y\in\mathcal{P}(X)$, there exists $x\in X$ such that $f(x)=y$.
In particular, $d\in\mathcal{P}(X)$, so there exists $x\in X$ such that $f(x)=d$.
Now, consider: is $x\in d$?
If $x\in d$, then $x\notin f(x)=d$.
This is impossible, so our supposition that $f$ exists must be false.
