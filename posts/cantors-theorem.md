---
title: Cantor's theorem
date: 2026-05-23 15:00
---

**Lemma 1**. There exists an injection from a set to its power set.

*Proof*. Let $X$ be a set.
1. There exists a function $f:X\to 2^{X}$ such that $f(x)=\{x\}$.
2. Clearly, $f(x)=f(y)$ implies $\{x\}=\{y\}$, which implies $x=y$.
3. Thus, $f$ is injective.

**Lemma 2**. There exists no bijection between a set and its power set.

*Proof*. Let $X$ be a set, and suppose there exists a bijective $f:X\to 2^{X}$.
1. Let $B=\{x\in X\mid x\notin f(x)\}$, and $a=f^{-1}(B)$.
2. Clearly, $a\in B$ if and only if $a\not\in f(a)$.
3. But $B=f(a)$, so $a\in f(a)$ if and only if $a\not\in f(a)$.
4. This is contradictory, so $f$ does not exist.

**Theorem**. A set is smaller than its power set.

*Proof*. Let $X$ be a set.
1. By Lemma 1, $|X|\leq|2^{X}|$.
2. By Lemma 2, $|X|\neq|2^{X}|$.
3. Thus, $|X|<|2^{X}|$.
