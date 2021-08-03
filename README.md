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

4. Download spack and configure compilers. 
The built-in spec for building UQTk with spack doesn't build 
PyUQTk, so you'll need to use the spec 
from [the spack-uqtk-PyUQTk-variant branch in padamson's fork of spack on GitHub](https://github.com/padamson/spack/blob/32a48d41110914cd827d330bd917c786a85edd67/var/spack/repos/builtin/packages/uqtk/package.py).
Just copy the above `package.py` file somewhere like `$HOME/tmp/package.py`.


```console
> git clone https://github.com/spack/spack.git
> cd spack
> cp $HOME/tmp/package.py var/spack/repos/builtin/packages/uqtk/
> . share/spack/setup-env.sh # for bash/zsh/sh (see docs if not)
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

5. Finally, build and install UQTk and PyUQTk:

```console
> spack install uqtk pyuqtk=ON %gcc@10.x.y # use x.y from above
``` 

6. Add PyUQTk to the `pyuqtk` conda environment. __Instructions TBD__

7. `spack load uqtk@3.1.0`

7. Run some examples located in `opt/spack/linux-distro-arch/gcc-10.x.y/uqtk-3.1.0-*/examples`.

