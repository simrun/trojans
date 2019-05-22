# Simulation of Jupiter’s Trojan asteroids

This is my solution and [writeup](trojans.pdf) for one of the Part II Physics projects at Cambridge University.

*Health warning: likely contains bugs!*

## Abstract

The orbits of asteroids bound to Lagrange points 4 and 5 of the Sun-Jupiter system were simulated in two dimensions. A linear multistep method was used to solve the equation of motion. The stability of the region surrounding each point was assessed by observing how far an asteroid would ‘wander’ from its starting position. An asteroid placed at the point itself was found to have a range of wander of 0.14 au; it travelled in a ‘tadpole’ orbit because of the Coriolis effect. The stable region lies along and just outside Jupiter’s orbit, with a width on the order of 1 au. A quadratic empirical relation between the planet’s mass and asteroid range of wander was derived. For planet/sun mass ratios greater than 0.02 no stability at the Lagrange points was seen. This is consistent with previous analytical results.

## License

The [source code](src) is licensed under the [MIT license](src/LICENSE).

The [writeup](trojans.tex) and [figures](figures) are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), with the following exceptions:

* [potential.*](figures/potential.svg) are licensed under the [Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/) by [Xander89](https://commons.wikimedia.org/wiki/File:Lagrange_points2.svg)
* [trojans.png](figures/trojans.png) has been released into the public domain by [Mdf](https://commons.wikimedia.org/wiki/File:InnerSolarSystem-en.png)
