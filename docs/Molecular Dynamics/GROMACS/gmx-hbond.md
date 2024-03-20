# Hydrogen Bonds (H-bond)

## Introduction

`gmx hbond` allows us to determine the number and angle of hydrogen bonds between groups of H-bond acceptors and donors.

You should have the following files:

* Trajectory files (.xtc)
* Topology file (.tpr)
* Index file (.ndx)

!!! note
    `gmx hbond` was changed in the 2024 version of GROMACS. This page references the command as it was in prior releases.

## Using `gmx hbond`

To calculate H-bond properties:

```
gmx hbond -f trajectory.xtc -s topology.tpr -n index.ndx -tu ns -num hbnum.xvg -g hbond.log
```

???+ tip "Other options you may find useful"

    * `-b` and `-e`: the frames to <ins>b</ins>egin and <ins>e</ins>nd
    * `-r`: the distance cutoff for H-bonds
    * `-dist`: outputs the distance distribution of all H-bonds
    * `-ang`: outputs the angle distribution of all H-bonds

You will be prompted to select two groups. Select the groups you want to analyze. Note that special groups will require a custom index file to be supplied with `-n`.

This produces the following outputs:

* `-num`: number of H-bonds as a function of time
* `-g`: information on H-bond acceptor-donor pairs

## Additional Resources

* [gmx hbond](https://manual.gromacs.org/2023-current/onlinehelp/gmx-hbond.html)