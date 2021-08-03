# uqtk-playground
A place to learn UQTk and PyUQTk.

## Building UQTk and PyUQTk with spack

[Spack](https://spack.io/) is a package manager that makes installing and using scientific
codes in Linux and MacOS easy. Here are the basic steps to use spack to get a working
copy of UQTk and PyUQTk. These instructions assume you are working in Ubuntu Linux, and
will even work within Ubuntu running in Windows WSL2.

1. Install [miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html). 
If you don't know about conda, [take some time to learn about it](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

2. Create and activate a conda environment with numpy, 
scipy, matplotlib, and swig (required by PyUQTk). An
environment.yml file is provided in this directory so you can
build a conda environment named `pyuqtk` with the required
packages (and a few others that might be helpful).
```console
> conda env create -f environment.yml
> conda activate pyuqtk
```

3. Install GCC and other development tools. If you don't have the [GNU Compiler Collection](https://gcc.gnu.org/) and other developer tools installed, install them now.
```console
> sudo apt update
> sudo apt upgrade # if desired, not necessarily required
> sudo apt install build-essential
> sudo apt install gcc-10 g++-10
```

4. Download spack and build UQTk and PyUQTk. 
The built-in spec for building UQTk with spack doesn't build 
PyUQTk, so you'll need to use the spec 
from [the spack-uqtk-PyUQTk-variant branch in padamson's fork of spack on GitHub](https://github.com/padamson/spack/tree/spack-uqtk-PyUQTk-variant). 
If you have spack installed already, you can just copy the `package.py` file from `spack/var/spack/repos/builtin/packages/uqtk`
into your copy of spack (make sure you get the version from the spack-uqtk-PyUQTk-variant branch). Or, you can clone padamson's fork of spack and checkout the dev branch:
```console
> git clone git@github.com:padamson/spack.git
> cd spack
> git checkout spack-uqtk-PyUQTk-variant
> . share/spack/setup-env.sh # for bash/zsh/sh (see docs if not)
> spack compiler find # should add gcc@10.x.y to spack
> spack install uqtk pyuqtk=ON %gcc@10.x.y # use x.y from above
``` 

5. Add PyUQTk to the `pyuqtk` conda environment. __Instructions TBD__

6. Load uqtk.
```console
> spack load uqtk
```

6. Run some examples. __Instructions TBD__

