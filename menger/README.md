-----------------------Menger Sponge - 2D Version----------------

Description:

This project involves writing a function that draws a 2D version of the famous **Menger Sponge** fractal. A Menger Sponge is a 3D fractal object, and this project deals with a 2D slice of it. The complexity of the sponge increases with the level parameter provided, where each level builds upon the previous one.

Menger Sponge Concept:

A Menger Sponge is created by repeatedly subdividing a cube into 27 smaller cubes, then removing the center cube and the center of each face. This process is repeated recursively. The size of a level N Menger sponge is calculated as `3^N`, where N is the level.

In the 2D version:
- A level 0 sponge is represented by a single `#` symbol.
- A level 1 sponge is a 3x3 grid of level 0 sponges, with the center being empty.
- A level 2 sponge is a 3x3 grid of level 1 sponges, with the center grid being empty.
- This pattern continues recursively.