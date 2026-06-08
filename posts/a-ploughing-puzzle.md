---
time: 2026-04-22 14:55
title: A ploughing puzzle
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

Here is a way to reason through it.

1. Suppose you equip a device $p$ that, at any position $L_{i,j}$, says if $i+j$ is odd or even.
2. Clearly, any move from any position will flip what $p$ says.
3. We know $p$ says "odd" at $S=L_{1,4}$, because $1+4=7$ is odd.
4. To complete the plough, we must make $11=3(4)-1$ moves, and thus, flips.
5. So if an ending position $E'$ exists, $p$ must say "even" at $E'$.
6. But we know $p$ says "odd" at $E=L_{3,4}$, because $3+4=7$ is odd.
7. Thus, the task is impossible.
