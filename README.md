# Granular
Python script used to investigate effectivity of packing different shaped granular material into a box.

## Problem
*The fraction of space occupied by granular particles depends
on their shape. Pour non-spherical particles such as rice,
matches, or M&M’s candies into a box. How do characteristics
like coordination number, orientational order, or the random
close packing fraction depend on the relevant parameters?* 

The problem was taken from the Young Physicists' Tournament 2015 (http://iypt.org/images/8/87/problems2015.pdf) which I participated in.


## Introduction to problematics
The amount of space that granules take up and the amount of unused space filled with air around them is highly dependent on the shape of granules.

The most usual indicators of the effectivity of packing are:
**Packing density(denoted as phi)**
The ratio between the volume of the granules and volume of the surrounding box in which they are packed.
**Coordination number(denoted as n)**
The average number of neighbours that an object is touching.

**Random close packing (RCP)** is an empirical parameter used to characterize the maximum packing density of solid objects when they are packed randomly.

## Approach
Aside of various physical approaches to the problem, I chose to also some 3D software and investigate the packing parametres of different shaped objects by:

- Simulating random close packing in Blender 3D software by filling a box with granules and shaking the box inside the software.
- Calculating packing density
- Calculation 

## Issues
To be able to run reasonably fast computation on my laptop, I used various approximations.


## Results
Some of the calculated packing densities and coordination numbers for common objects.

![alt text](https://github.com/padr31/Granular/blob/master/results.png "Results")
