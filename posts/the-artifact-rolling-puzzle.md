---
date: 2026-09-29
name: The Artifact Rolling Puzzle
---

# The Artifact Rolling Puzzle

Suppose a carnival has games $A_{1},A_{2}$, and exactly one must be played.
Game $A_{i}$ has:

1. A four-sided die with $F_{i}\in\{1,2,3,4\}$ good faces.
2. A starter score $S_{i}\in\{0,1,2,3,4\}$.

Playing game $A_{i}$ requires one to:

1. Roll its die exactly four times.
2. Exit the carnival with score $\max(S,S_{i})+S_{3-i}$, where $S$ is the number
   of rolls that landed on good faces.

When should one play either game?
