# Measuring Eccentricity

## Introduction

**Eccentricity** is a measure of how much a protein or complex's shape deviates from a sphere, or its roundness.

Eccentricity (*e*) is calculated using the moments of inertia (*I*) from the three principal axes (x, y, z). Values of *e* closer to 0 are considered more spherical, while values closer to 1 are more ellipsoid.

*e* can be calculated using the following equation[^1]:
<figure markdown="span">
  ![Equation for eccentricity. Eccentricity = sqrt(1 - ((Ix + Iy - Iz) / (-Ix + Iy + Iz)))](../../assets/GROMACS/gyrate-sasa/gmx_gyrate_moi_2.png){ width="300" }
</figure>

[^1]: This is the equation used in the lab to determine *e*. Occasionally, you will find literature that also uses a more simplified equation of *e* = 1 - (I~min~/I~avg~).

*I* for each axis can be calculated using `gmx gyrate` with the `-moi` option. Note that `gmx principal` may also be used to determine *I*, but `gmx gyrate` is currently supported in scripts used by our lab.

You should have the following files:

* Trajectory files (.xtc)
* Topology file (.tpr)

!!! note
    `gmx gyrate` was changed in the 2024 version of GROMACS. This page references the command as it was in prior releases.

## Using `gmx gyrate`

To calculate moments of inertia using `gmx gyrate`:

```
gmx gyrate -f trajectory.xtc -s topology.tpr -o moi.xvg -moi
```

???+ tip "Other options you may find useful"

    * `-n`: index file to be used (see [Creating Index Files](gmx-ndx.md))
    * `-b` and `-e`: the frames to <ins>b</ins>egin and <ins>e</ins>nd

!!! warning
    You **MUST** use the `-moi` option, otherwise GROMACS will calculate [radius of gyration](gmx-gyrate.md) instead.
  
When prompted, select the atom group you wish to analyze. Special groups will require a custom index file to be supplied with `-n`.

This will output an XVG file of *I* versus time. This file can be processed to extract each value and calculate the eccentricity of your protein. Alternatively, it can also be visualized using Grace or Python, as is.

## Additional Resources

* [gmx gyrate](https://manual.gromacs.org/2023-current/onlinehelp/gmx-gyrate.html)