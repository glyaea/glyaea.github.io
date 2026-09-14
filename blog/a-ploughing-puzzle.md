---
date: 2026-04-22
name: A Ploughing Puzzle
---

# A Ploughing Puzzle

I recently came across the following puzzle on social media.

> Is it possible to plough a plot of land

$$
	\mathbf{L}
	=
	\begin{bmatrix}
		\square & \square & \square & S \\
		\square & \square & \square & \square \\
		\square & \square & \square & E
	\end{bmatrix}
$$

> from $S$ to $E$ using only up, down, left, and right moves without
> backtracking?

This puzzle can be solved by a simple parity argument. Suppose you equip a
device $D$ that, at any position $l_{i,j}$, says if $i+j$ is odd or even.
Clearly, any move from any position will flip what $D$ says. We know $D$ says
"odd" at $S=l_{1,4}$, because $1+4=7$ is odd. To complete the plough, we must
make $11=3(4)-1$ moves, and thus, flips. So if an ending position $E'$ exists,
$D$ must say "even" at $E'$. But we know $D$ says "odd" at $E=l_{3,4}$, because
$3+4=7$ is odd. Thus, the task is impossible.
