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
> sudo apt install gcc-10 g++-10 gfortran-10
```

4. Download and install spack and configure compilers. 
```console
> cd $HOME/opt # or wherever you'd like to install spack
> git clone https://github.com/spack/spack.git
> cd spack
> . share/spack/setup-env.sh # for bash/zsh/sh (see docs if not)
> # you may want to add the above line to your .bashrc/.zshrc
> spack compiler find # should add gcc@10.x.y to spack
```

Update your `$HOME/.spack/linux/compilers.yaml` file to point to `gfortran-10`:

```yaml
compilers
- compiler:
    spec: gcc@10.3.0
    paths:
      cc: /usr/bin/gcc-10
      cxx: /usr/bin/g++-10
      f77: /usr/bin/gfortran-10
      fc: /usr/bin/gfortran-10
    flags: {}
    operating_system: ubuntu20.04
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
```

5. Add the [spack-ppd repo](https://github.com/NRL-Plasma-Physics-Division/spack-ppd) to spack.
The built-in spec for building UQTk with spack doesn't build 
PyUQTk, so you'll need to use the spec 
from [the spack-ppd repo](https://github.com/NRL-Plasma-Physics-Division/spack-ppd).

```console
> cd $HOME/opt # or wherever
> git clone https://github.com/NRL-Plasma-Physics-Division/spack-ppd
```
Add `spack-ppd` to your `~/.spack/repos.yaml` file:
```yaml
repos:
  - $HOME/opt/spack-ppd # or wherever you put it
  - $spack/var/spack/repos/builtin
```

6. Finally, build and install UQTk and PyUQTk:

```console
> spack install uqtk pyuqtk=ON %gcc@10.x.y # use x.y from above
``` 

If successful, UQTk and PyUQTk will be built in a folder within spack named `opt/spack/linux-[distro]-[arch]/gcc-10.[x].[y]/uqtk-3.1.0-[hash]`, where:
- distro: your linux distro, probably ubuntu20.04
- arch: your hardware architecture, perhaps skylake
- 10.x.y: the subversion of gcc, probably 10.3.0
- hash: some unique hash associated with the UQTk build

7. Add PyUQTk to the `pyuqtk` conda environment. 
Add the following basic `setup.py` file to the spack `uqtk-3.1.0-[hash]` build directory:
```console
from setuptools import setup

setup(
    name="PyUQTk",
    version="1.0",
    packages=["PyUQTk"],
)
```
Now, with the pyuqtk conda environment still activated, 
run `pip install .` (note the period at the end) inside the spack `uqtk-3.1.0-[hash]` 
build directory. This command installs the python code in the PyUQTk folder into your active pyuqtk conda environment using `pip`.

8. Load the uqtk spack package that you built with the command `spack load uqtk@3.1.0`.

9. Go through the [UQTk User Guide](https://www.sandia.gov/uqtoolkit/manual/) and run some examples located in `uqtk-3.1.0-[hash]/examples`.

