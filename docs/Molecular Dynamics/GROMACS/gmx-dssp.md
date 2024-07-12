# Determining Secondary Structure (DSSP)

## Introduction

`gmx do_dssp` determines a protein's secondary structure based on hydrogen bonding patterns between residues. DSSP is able to determine the formation of/changes in  helices, sheets, and disordered regions (coils). This allows us to study how a protein's conformation may morph and move throughout the span of a simulation.

You should have the following files:

* Trajectory files (.xtc)
* Structure or topology file (.gro/.tpr)
* Index file (.ndx)

!!! note
    `gmx do_dssp` was changed to `gmx dssp` in the 2023 version of GROMACS. This page references the older `do_dssp` command.

## Using `gmx do_dssp`

To determine the secondary structure of your proteins:

```bash
gmx do_dssp -f trajectory.xtc -s structure.gro -n index.ndx -tu ns -o ss.xpm -sc sscount.xvg
```

GRO and TPR files may be used interchangeably for the `-s` option. If you are trying to determine the secondary structure of a multi-subunit protein with identical chains (homo-oligomers), you may need to create a [custom GRO file](#using-gmx-do_dssp-with-homo-oligomeric-proteins) to properly run this command.

`gmx do_dssp` produces the following outputs:

* `-o`: structure assignment as a function of time
* `-sc`: structure count as a function of time

Both the XPM (`-o`) and XVG (`-sc`) files can be parsed using Python or Grace for visualization. XPM files can also be processed through [`gmx xpm2ps`](https://manual.gromacs.org/current/onlinehelp/gmx-xpm2ps.html). This will transform the data into a labelled plot that may be opened through programs like [GIMP](https://www.gimp.org/).

### Using `gmx do_dssp` with homo-oligomeric proteins

Homo-oligomers have the same residue numbers designated across identical subunits. This creates issues with the DSSP algorithm, causing the command to stall at the first frame of the simulation. To get around this, you will need to create GRO and NDX files with each protein residue renumbered sequentially.

If you do not have an original GRO file, you can generate one:

```bash
gmx trjconv -f trajectory.xtc -s topology.tpr -o structure.gro
```

To edit this GRO file and renumber the protein residues:

```bash
gmx editconf -f structure.gro -resnr 1 -o renumbered.gro
```

`-resnr` indicates the residue number to start from, in this case 1.

---

If you are analyzing specific parts of your protein, you will need to create a new NDX file using the renumbered GRO file:

```bash
gmx make_ndx -f renumbered.gro -o renumbered.ndx
```

If you are unsure of how to use this command to create special atom groups, refer to the [guide on GROMACS index files](gmx-ndx.md).

---

Both renumbered files can be used as an input for the `-s` option as described in the [Using `gmx do_dssp`](#using-gmx-do_dssp) section.

## Additional Resources

* [gmx do_dssp](https://manual.gromacs.org/2022/onlinehelp/gmx-do_dssp.html)