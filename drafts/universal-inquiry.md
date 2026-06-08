---
time: 2026-06-06 06:00
title: Universal inquiry
---

**Metadefinition** (Formula).
1. If $a,b$ are variables, then $a\in b$ is a formula.
2. If $p$ is a formula, then $\neg p$ is a formula.
3. If $p,q$ are formulas, then $p\land q$ is a formula.
4. If $x$ is a variable, and $p$ is a formula, then $\exists x\,(p)$ is a formula.

**Notation** (Disjunction).
$$
	p\lor q
	\equiv
	\neg(\neg p\land\neg q)
$$

**Definition** (FizzBuzz Algorithm).
> FizzBuzz($n$):
>> **for** $i\in[1..n]$:  
>>> **if** $i \bmod 15 = 0$:  
>>>> print("FizzBuzz")

**Notation** (Implication).
$$
	p\Rightarrow q
	\equiv
	\neg(p\land\neg q)
$$

**Axiom** (Empty Set).
$$
	\exists n\,(
		\nexists x\,(x\in n)
	)
$$

**Definition** (Empty Set).
$$
	n=\varnothing
	\Leftrightarrow
	\nexists x\,(x\in n)
$$

**Definition** (Tuple).
Let $n\in\N\setminus\varnothing$.
$$
	(x_{1},\dots,x_{n})
	=
	\begin{cases}
	x_{1}, & \text{if}\ n=1 \\
	(x_{1},x_{2}), & \text{elif}\ n=2 \\
	((x_{1},\dots,x_{n-1}),x_{n}) & \text{otherwise}
	\end{cases}
$$
