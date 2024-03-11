## Introduction

Placeholder text :)

## Data visualization and analysis


The outputs of `gmx do_dssp` will be processed and visualized using a Jupyter Notebook. The notebook is mean to be ran on ARC on the `bevanlab` allocation. For more information on running Jupyter Notebooks on ARC, see the documentation (here - a link will exist). Download the notebook [`dssp.ipynb`](https://github.com/kelsieking23) and upload to ARC. 

### DSSP Per-Residue

To create plots of DSSP per residue over time, do the following for *each chain* in your system:

- Run the first cell of the notebook to import the relevant packages
- Find **Section 1: DSSP Per Residue**
- Edit the variable names for controlling the data to be plotted:
    - `xpm`: path to an .xpm file containing DSSP-per-residue data over time
    - `pdb`: path to a .pdb file containing the residues analyzed with `gmx do_dssp`
    - `ocsv`: path to output for a .csv file of data transformed from .xpm
    - `opng`: path to output for the graph
    - `chain_id`: chain ID to visualize as an integer (e.g. Chain A = 0, Chain B = 1, etc...)
- In the following cell, edit the variable names in the notebook to control the plot:
    - `colors`: colors in RGB format for coil, helix, and sheet. Defaults are:
        - `0 (coil)` : `[255,255,255] (white)`, 
        - `1 (helix)` : `[247,148,29] (orange)`, 
        - `2 (b-sheet)` : `[0,165,165] (teal)` 
        - `title`: title for the plot. Default "DSSP Per Residue"
        - `legend`: whether to display a legend or not. can be True or False
    - `major_xticks` (int or None): Interval for major x ticks. Leave as None to use matplotlib default
    - `major_yticks` (int or None): Interval for major y ticks. Leave as None to use matplotlib default
    - `minor_xticks` (int or None): Interval for minor x ticks. Leave as None to use matplotlib default
    - `minor_yticks` (int or None): Interval for minor y_ticks. Leave as None to use matplotlib default
- Finally, run the cell below the variable definitions to create the plot.

