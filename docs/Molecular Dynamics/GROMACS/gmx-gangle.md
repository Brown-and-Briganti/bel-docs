# Measuring Angles

## Introduction

`gmx gangle` can be used to calculate the angles between groups of vectors. Specifically, `gmx gangle` can compute angles between a vector or plane and another vector, plane, the z-axis, or the normal vector of a sphere. It can also compute angles and dihedrals, similar to `gmx angle`.

Like the [`gmx distance` command](gmx-dist.md), this command allows us to study movement of features, like protein hinges.

!!! note
    You will need to use a [custom index file](gmx-ndx.md) if you are measuring angles between custom groups of atoms.

You should have the following files:

* Trajectory files (.xtc)
* Topology file (.tpr)
* Index file (.ndx)

## Using `gmx gangle`

To calculate angles:

```bash
gmx gangle -f trajectory.xtc -s topology.tpr -n index.ndx -tu ns -oav all-angles.xvg -oall all-angles.xvg  -oh angle-hist.xvg -g1 vector -group1 <group> -g2 vector -group2 <group> 
```

`-g1` and `-g2` indicate the type of angle that should be analyzed (`vector`, `plane`, `angle`, or `dihedral`). These options are closely tied to the `-group1` and `-group2` options, which specify the atom positions to be analyzed. The groups to be analyzed are taken from the index file supplied with `-n`.

As the inputs for these options are highly dependent on the system, refer to the [`gmx gangle` documentation page](https://manual.gromacs.org/current/onlinehelp/gmx-gangle.html) for valid `-g1/g2` and `-group1/group2` combinations.

This produces the following outputs:

* `-oav`: average angles as a function of time
* `-oall`: all angles as a function of time
* `-oh`: histogram of angles

These XVG files can be visualized using Python or Grace to produce a plots of angle versus time, or to generate a heat-map from histogram data.

## Additional Resources

* [gmx gangle](https://manual.gromacs.org/current/onlinehelp/gmx-gangle.html)
* [Bonds/distances, angles and dihedrals (GROMACS reference manual)](https://manual.gromacs.org/current/reference-manual/analysis/bond-angle-dihedral.html)