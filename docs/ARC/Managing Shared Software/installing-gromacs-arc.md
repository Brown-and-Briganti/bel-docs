# GROMACS Version Management & Installation

## Introduction
**GROMACS** is the main simulation engine used in our lab for performing MD simulations. Separate installations are required for both different clusters (*i.e.* Tinkercliffs, Infer) and for different partitions (*i.e.* v100, p100, *etc.*). This page documents how GROMACS installations and versions are managed and installed. 

### GROMACS Version List
To load any GROMACS version, the `$MODULEPATH` environment variable must be modified as follows:
* Infer: `export MODULEPATH=$MODULEPATH:/projects/bevanlab/software/infer/modules/modules/infer-skylake/all`
* Tinkercliffs: `export MODULEPATH=$MODULEPATH:/projects/bevanlab/software/tinkercliffs/modules/modules/tinkercliffs-rome/all`
* OWL: `export MODULEPATH=$MODULEPATH:/projects/bevanlab/software/tinkercliffs/modules/modules/owl-genoa/all`
<table>
    <tr>
        <th>Cluster</th>
        <th>Partition</th>
        <th>Load Syntax</th>
        <th>Versions</th>
        <th>GPU-Enabled?</th>
        <th>MDRun executable</th>
    </tr>
    <tr>
        <td>Infer</td>
        <td>v100_normal_q<br>v100_dev_q</td>
        <td><code>module load gromacs-v100/20XX.X</code></td>
        <td>2018.1<br>2019.1<br>2020.3<br>2020.4<br>2024.4</td>
        <td>Yes</td>
        <td><code>gmx mdrun</code></td>
    </tr>
    <tr>
        <td>Infer</td>
        <td>p100_normal_q<br>p100_dev_q</td>
        <td><code>module load gromacs-p100/20XX.X</code></td>
        <td>2019.3<br>2020.4<br>2020.4</td>
        <td>Yes</td>
        <td><code>gmx mdrun</code></td>
    </tr>
    <tr>
        <td>Infer</td>
        <td>t4_normal_q<br>t4_dev_q</td>
        <td><code>module load gromacs-t4/20XX.X</code></td>
        <td>2019.3<br>2020.3<br>2020.4</td>
        <td>Yes</td>
        <td><code>gmx mdrun</code></td>
    </tr>
    <tr>
        <td>Infer</td>
        <td>Login Node</td>
        <td><code>module load gromacs/2020.4</code></td>
        <td>2020.4</td>
        <td>No</td>
        <td>--</td>
    </tr>
    <tr>
        <td>Tinkercliffs</td>
        <td>a100_normal_q<br>a100_dev_q</td>
        <td><code>module load gromacs/a100/20XX.X<code></td>
        <td>2020.4<br>2024.4</td>
        <td>Yes</td>
        <td><code>mdrun_gpu</code>(2020.4)<br><code>gmx mdrun</code>(2024.4)</td>
    </tr>
    <tr>
        <td>Tinkercliffs</td>
        <td>normal_q<br>dev_q</td>
        <td><code>module load gromacs/normal_q/2024.4<code></td>
        <td>2024.4</td>
        <td>No</td>
        <td>--</td>
    </tr>
    <tr>
        <td>OWL</td>
        <td>normal_q<br>dev_q</td>
        <td><code>module load gromacs/2024.4<code></td>
        <td>2024.4</td>
        <td>No</td>
        <td>--</td>
    </tr>
</table>

### File Structure
The base folder for all shared software on ARC is `/projects/bevanlab/software`. 
As of writing, the Brown Lab has access to two clusters through ARC: [Infer](https://www.docs.arc.vt.edu/resources/compute/01infer.html) and [Tinkercliffs](https://www.docs.arc.vt.edu/resources/compute/00tinkercliffs.html). Cluster-specific software, like GROMACS installations, are maintained in separate folders: `/projects/bevanlab/software/infer` and `/projects/bevanlab/software/tinkercliffs`. Partition-specific installs (modules) are maintained through using ARC's `setup_app` tool. `setup_app` automates the creation of file structures for specific apps that can be loaded modularly. Modules for Infer and Tinkercliffs are stored in `/projects/bevanlab/software/infer/modules` and `/projects/bevanlab/software/tinkercliffs/modules`, respectively. 

## Example Installation Protocols
Note: **for future GROMACS versions, the protocol as described here may not be exactly congruent** in terms of module versions and CMake syntax.

## Infer Installation: GPU-Enabled GROMACS

### Downloading GROMACS source-files
First, move into the Tinkercliffs software directory:
```bash
[kelsieking23@infer1 ~]$ cd /projects/bevanlab/software/infer
```

Download GROMACS source files with `wget` and uncompress:
```bash
[kelsieking23@infer1 infer]$ wget http://ftp.gromacs.org/pub/gromacs/gromacs-2024.4.tar.gz
[kelsieking23@infer1 infer]$ tar -xzvf gromacs-2024.4.tar.gz
```


### Setting up with `setup_app`
To set up the initial file structure for install, we will run the `setup_app` tool. Make sure that you are still on the *log-in node* and that you have not yet requested an interactive session. This is important to keep consistency in the automatic generation of file paths.
```bash
[kelsieking23@infer1 infer]$ setup_app --base /projects/bevanlab/software/infer/modules gromacs 2024.4
```
`setup_app` will then prompt for user input. Type `y` for yes:
```
Create directories /projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4 and /projects/bevanlab/software/infer/modules/modules/infer-skylake/all/gromacs-v100?
```
After confirming, the following will be printed to the console:
```
Done. To finish your build:
 1. Install your app in /projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4/
 2. Edit the modulefile in /projects/bevanlab/software/infer/modules/modules/infer-skylake/all/gromacs-v100/2024.4.lua
    - Set or remove modules to load in the load() line
    - Edit description and URL
    - Check the variable names
    - Edit paths (some packages don't have, e.g., an include/)

Note: You specified a non-standard directory. You will need to add
/projects/bevanlab/software/infer/modules/modules/infer-skylake/all
to MODULEPATH to be able to load the module.
This can be done by adding, e.g.,
  export MODULEPATH="/projects/bevanlab/software/infer/modules/modules/infer-skylake/all:$MODULEPATH"
to your ~/.bashrc

Note: You may need to refresh the cache, e.g.,
  module --ignore_cache spider gromacs-v100
to find the module the first time.
```
Here, we have created a file structure for our GROMACS install, allowing the creation of an isolated GROMACS install for a specific Infer partition. In this example, we will be installing on the **V100 partition**. 



### Building GROMACS
First, we must request an interactive session:
```bash
[kelsieking23@infer1 infer]$ interact -p v100_normal_q -t 6:00:00 -N1 --ntasks=1 --cpus-per-task 24 -A bevanlab --gres=gpu:1
```

#### Loading dependencies

To install GROMACS, we will need to load the correct versions of `CMake`, `CUDA`, and `GCC`. For each of these modules, there are several versions availble for loading on Infer. To see a list of available versions, we can use the command `module spider`. For example, the available versions for `CMake` are as follows:

```
[kelsieking23@inf092 infer]$ module spider CMake
----------------------------------------------------------------------------------------------------------------------
  CMake:
----------------------------------------------------------------------------------------------------------------------
    Description:
      CMake, the cross-platform, open-source build system. CMake is a family of tools designed to build, test and package software.

     Versions:
        CMake/3.15.3-GCCcore-8.3.0
        CMake/3.16.4-GCCcore-9.3.0
        CMake/3.18.4-GCCcore-10.2.0
        CMake/3.20.1-GCCcore-10.3.0
        CMake/3.21.1-GCCcore-11.2.0
        CMake/3.22.1-GCCcore-11.2.0

----------------------------------------------------------------------------------------------------------------------
  For detailed information about a specific "CMake" package (including how to load the modules) use the module's full name. Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider CMake/3.22.1-GCCcore-11.2.0
----------------------------------------------------------------------------------------------------------------------
```
Note that each `CMake` version has an associated `GCCCore` version. `CUDA` also has an associated `GCC` version, whcih **needs to match the** `CMAKE`-associated `GCCCore` **version**. We can check these versions by using `module spider` to inspect the available `CUDA` modules:
```
[kelsieking23@inf092 infer]$ module spider CUDA
----------------------------------------------------------------------------------------------------------------------
  CUDA:
----------------------------------------------------------------------------------------------------------------------
    Description:
      CUDA (formerly Compute Unified Device Architecture) is a parallel computing platform and programming model created by NVIDIA and
      implemented by the graphics processing units (GPUs) that they produce. CUDA gives developers access to the virtual instruction
      set and memory of the parallel computational elements in CUDA GPUs.

     Versions:
        CUDA/8.0.61
        CUDA/9.0.176-GCC-6.4.0-2.28
        CUDA/10.1.243-GCC-8.3.0
        CUDA/10.1.243-iccifort-2019.5.281
        CUDA/11.0.2-GCC-9.3.0
        CUDA/11.0.2-iccifort-2020.1.217
        CUDA/11.1.1-GCC-10.2.0
        CUDA/11.1.1-iccifort-2020.4.304
        CUDA/11.4.1
        CUDA/11.7.0
        CUDA/12.1.1
        CUDA/12.3.2
     Other possible modules matches:
        CUDAcore  UCX-CUDA  chainer-py37-cuda10.1-gcc  chainer-py37-cuda10.2-gcc  cub-cuda10.1  cub-cuda10.2  cuda-dcgm  cuda10.1/blas  ...
----------------------------------------------------------------------------------------------------------------------
```
For this install, we will select `CMake/3.18.4-GCCcore-10.2.0` and `CUDA/11.1.1-GCC-10.2.0`. The minimum requirement for GROMACS 20204.4 is `CMake 3.18.4` or later, and `CUDA/11.1.1-GCC-10.2.0` has a matching `GCC` version available. 

Now, load the required modules:

```bash
[kelsieking23@inf092 infer]$ module reset
[kelsieking23@inf092 infer]$ module load site/infer/easybuild/setup
[kelsieking23@inf092 infer]$ module load CMake/3.18.4-GCCcore-10.2.0
[kelsieking23@inf092 infer]$ module load CUDA/11.1.1-GCC-10.2.0
[kelsieking23@inf092 infer]$ module load GCC/10.2.0
```
#### GROMACS build

Earlier, we un-tarred `gromacs-2024.4.tar.gz`. The uncompressed folder, `gromacs-2024.4` should now be present in `/projects/bevanlab/software/infer`. Now, we need to create a folder for build files in `gromacs-2024.4` and move there:
```bash
[kelsieking23@inf092 infer]$ cd /projects/bevanlab/software/infer/gromacs-2024.4
[kelsieking23@inf092 gromacs-2024.4]$ mkdir build
[kelsieking23@inf092 gromacs-2024.4]$ cd build
```

Create an initial build with `CMake`:
```bash
[kelsieking23@inf092 build]$ cmake .. -DGMX_GPU=CUDA -DGMX_BUILD_OWN_FFTW=ON -DCMAKE_INSTALL_PREFIX=/projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4/
```
Breaking down the command:
* `..` : A positional argument. Indicates the  path to `CMake` set-up files relative to the current working directory (*i.e.* in the parent directory to `build`)
* `-DGMX_GPU` : Toggles GROMACS installation with GPU support. `-DGMX_GPU=CUDA` enables CUDA support. 
* `-DGMX_BUILD_OWN_FFTW` : `FFTW` is an important GROMACS dependency. `-DGMX_BUILD_OWN_FFTW=ON` toggles `CMake` to build a special `FFTW` library specifically for the GROMACS build, which is better for performance and software compatability. 
* `-DCMAKE_INSTALL_PREFIX` : This specifies where to install GROMACS. The `setup_app` command from earlier instructed that the application be installed in `/projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4/`.

For more information on `CMake` commands for building GROMACS, see the official [GROMACS Installation Guide](https://manual.gromacs.org/current/install-guide/index.html).


Upon completion, we can start the build:
```bash
[kelsieking23@inf092 build]$ make -j 12
```
* `-j 12` : parallelizes the build process (12 threads) and is considerably faster. 

After the build completes, we can install the build:
```bash
[kelsieking23@inf092 build]$ make install
```

### Modifying module files
The `setup_app` command created a `.lua` module file. In this file, we can specify module dependencies (*i.e.*, CMake, CUDA, and GCC modules) that will be automatically loaded when the GROMACS installation is loaded. The file, `/projects/bevanlab/software/infer/modules/modules/infer-skylake/all/gromacs-v100/2024.4.lua`, was specified in the output of `setup_app` (see [Setting up with `setup_app`](#setting-up-with-setup_app)). Open the file with `vi`:
```bash
[kelsieking23@inf092 build]$ vi /projects/bevanlab/software/infer/modules/modules/infer-skylake/all/gromacs-v100/2024.4.lua
```
The last line in the file stores information for dependencies. The default line should be:

```
load("foss/2020b")
```
Using the text-editor, we will change the line as follows:
```
load("apps","fosscuda/2020b","GCC/10.2.0", "GCCcore/10.2.0", "CMake/3.18.4-GCCcore-10.2.0", "CUDA/11.1.1-GCC-10.2.0")
```
### Loading and testing new install
To check that the install functions correctly, reset all modules and load:
```bash
[kelsieking23@inf092 infer]$ module reset
[kelsieking23@inf092 infer]$ export MODULEPATH=$MODULEPATH:/projects/bevanlab/software/infer/modules/modules/infer-skylake/all
[kelsieking23@inf092 infer]$ module load gromacs-v100/2024.4
[kelsieking23@inf092 infer]$ gmx
                         :-) GROMACS - gmx, 2024.4 (-:

Executable:   /projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4/bin/gmx
Data prefix:  /projects/bevanlab/software/infer/modules/apps/infer-skylake/gromacs-v100/2024.4
Working dir:  /projects/bevanlab/software/infer
Command line:
  gmx

...
```



