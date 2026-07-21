---
date: 2026-04-22
name: A ploughing puzzle
---

I recently came across the following puzzle on social media.

> Is it possible to plough a plot of land

$$
	\mathbf{L}
	=
	\begin{bmatrix}
	\square & \square & \square & S
	\\
	\square & \square & \square & \square
	\\
	\square & \square & \square & E
	\end{bmatrix}
$$

> from $S$ to $E$ using only up, down, left, and right moves without backtracking?

Here is a solution.

1. Suppose you equip a device $D$ that, at any position $l_{i,j}$, says if $i+j$ is odd or even.
2. Clearly, any move from any position will flip what $D$ says.
3. We know $D$ says "odd" at $S=l_{1,4}$, because $1+4=7$ is odd.
4. To complete the plough, we must make $11=3(4)-1$ moves, and thus, flips.
5. So if an ending position $E'$ exists, $D$ must say "even" at $E'$.
6. But we know $D$ says "odd" at $E=l_{3,4}$, because $3+4=7$ is odd.
7. Thus, the task is impossible.
