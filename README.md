# uqtk-playground
A place to learn UQTk and PyUQTk.

## Building UQTk and PyUQTk with spack

[Spack](https://spack.io/) is a package manager that makes installing and using scientific
codes in Linux and MacOS easy. Here are the basic steps to use spack to get a working
copy of UQTk and PyUQTk on Linux. These instructions assume you are working in Ubuntu Linux, and
will even work within Ubuntu running in Windows WSL2. (The
steps should be similar on MacOS.)

1. If you don't have a recent version of the [GNU Compiler Collection](https://gcc.gnu.org/) and other developer tools installed, install them now. (These steps should certainly work for gcc-10, and probably for versions >7.)
```console
> sudo apt update
> sudo apt upgrade # if desired, not necessarily required
> sudo apt install build-essential
> sudo apt install gcc-10 g++-10 gfortran-10
> sudo apt install unzip # also needed by spack
```

2. Download and install spack and configure compilers. 
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

3. Add the [spack-ppd repo](https://github.com/NRL-Plasma-Physics-Division/spack-ppd) to spack.
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

4. Finally, build and install UQTk and PyUQTk:

```console
> spack install uqtk pyuqtk=True %gcc@10.x.y # use x.y from above
``` 

If successful, UQTk and PyUQTk will be built in a folder within spack named `opt/spack/linux-[distro]-[arch]/gcc-10.[x].[y]/uqtk-3.1.0-[hash]`, where:
- distro: your linux distro, probably ubuntu20.04
- arch: your hardware architecture, perhaps skylake
- 10.x.y: the subversion of gcc, probably 10.3.0
- hash: some unique hash associated with the UQTk build  

Also, you will have a version of python, numpy, scipy, and matplotlib installed within spack that will be loaded alongside UQTk (and PyUQTk) when you do the next step.

5. Load the uqtk spack package with the command `spack load uqtk`. `PyUQTk` that resides in the `uqtk-3.1.0-[hash]` folder in spack will be in your `PYTHONPATH`.

6. Go through the [UQTk User Guide](https://www.sandia.gov/uqtoolkit/manual/) and run some examples located in `uqtk-3.1.0-[hash]/examples`.

