---
title: A ploughing puzzle
date: 2026-04-22 14:55
---

I recently came across the following problem on social media.

> Is it possible to plough a plot of land
$$
\bm{L}
=
\begin{bmatrix}
\square & \square & \square & S \\
\square & \square & \square & \square \\
\square & \square & \square & E
\end{bmatrix}
$$
> from $S$ to $E$ using only up, down, left, and right moves without backtracking?

Here is a way to reason through it!

1. Imagine that, while ploughing, you wear a magical device $p$ that, at any position $L_{i,j}$, tells you the parity of $i+j$ (i.e. whether $i+j$ is odd or even).
2. We know $p$ is odd at $S$.
3. Clearly, any move from any position will flip $p$.
4. To complete the plough, we must make $11=3(4)-1$ moves, and thus, flips.
5. So if an ending position $E'$ exists, $p$ would be even at $E'$.
6. But we know $p$ is odd at $E$.
7. Thus, the task is impossible.
