---
title: Cantor's theorem
date: 2026-05-23 15:00
---

**Theorem.** There is no bijection between a set and its power set.

**Proof.** Suppose there exists a bijective $S:X\to 2^{X}$.
1. Let $B=\{x\in X\mid x\notin S(x)\}$, and $a=S^{-1}(B)$.
2. Clearly, $a\in B$ if and only if $a\not\in S(a)$.
3. But $B=S(a)$, so $a\in S(a)$ if and only if $a\not\in S(a)$.
4. This is contradictory, so $S$ does not exist.
