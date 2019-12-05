# VirtualEnv for Python

## Install Python3

*Important*: ```make altinstall``` causes it to not replace the built in python executable when installing with python source code. Ensure that `secure_path` in /etc/sudoers file includes /usr/local/bin. The line should look something like this:
```Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin```


## pipenv (Preferred)

Coming from pip and virtualenvs, and how they allow us to manage our dependency versions, for a development project, `pipenv` is a new tool to manage the  project’s virtualenv and install dependencies. Rather than creating a requirements.txt file for us, pipenv creates a `Pipfile` that it will use to store virtualenv and dependency information. Full guide to `pipenv` from [Real Python](https://realpython.com/pipenv-guide/)

```bash
# install pipenv
    $ pip3 install pipenv
# activate our new virtualenv
    $ pipenv shell
# Install 3rd party package
    $ pipenv install numpy
# Install dependency for development only
    $ pipenv install pytest --dev
# To show dependency graph
    $ pipenv graph
# deactivate the virtualenv
    $ exit
```

To use pipenv with specific versions of either python or 3rd party packges:
```bash
# create a virtualenv with specific python version
    $ pipenv --python $(which python3)
# Install 3rd party package with specific version
    $ pipenv install flask==0.12.1
# Install requests library directly from git
    $ pipenv install -e 'git+https://github.com/requests/requests.git#egg=requests'
```

Once everthing is working in the local environment and ready to push to production, our environment must be locked to ensure you have the same one in production:
```bash
    $ pipenv lock
```

To install last successful environment, we need to use Pipfile.lock instead of Pipfile for a production environment:
```bash
    $ pipenv install --ignore-pipfile
```

To install all dependencies and to modify prod code after downloading it to a different dev environment:
```bash
# Prod environment
    $ pipenv install
# Dev environment with dev dependencies
    $ pipenv install --dev
```

To uninstall either one unwanted package or all packages:
```bash
# Uninstall 3rd party package
    $ pipenv uninstall numpy
# Uninstall All packages
    $ pipenv uninstall --all
```

## venv vs virtualenv

The `venv` module was added to the standard library in Python3.3. The `pyvenv` command is a wrapper around the venv module, and you should strongly consider avoiding the wrapper and just using the module directly, since it solves so many problems inherent with wrapper scripts, particularly when you have multiple versions of Python installed.

venv, which is part of Python itself, has access to internals of Python. It can do things the right way with far fewer hacks. For example, virtualenv has to copy the Python interpreter binary into the virtual environment to trick it into thinking it's isolated, whereas venv can just use a configuration file that is read by the Python binary in its normal location for it to know it's supposed to act like it's in a virtual environment. If you are running a version of Python that has venv in the standard library, you can use it without having to install anything, which is another added bonus.

## Venv for python3

Virtualenvs allow us to create sandboxed Python environments. In Python2, we need to install the virtualenv package to do this, but with Python3 it has been worked in under the module name of venv.

To create a virtualenv, use the following command:

```bash
# python3 -m venv <PATH FOR VIRTUALENV>
# -m flag loads a module as a script.

    $ mkdir venvs
    $ python3 -m venv venvs/experiment
    
```

This command creates a directory called env, which contains a directory structure similar to this:
```
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── pip
│   ├── pip3
│   ├── pip3.5
│   ├── python -> python3.7
│   ├── python3 -> python3.7
│   └── python3.5 -> /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
├── include
├── lib
│   └── python3.7
│       └── site-packages
└── pyvenv.cfg
```

Virtualenvs are local Python installations with their own site-packages. To use a virtualenv, we need to activate it by sourcing an activate file in the virtualenv’s bin directory:

```bash
$ source venvs/experiment/bin/activate
(experiment) ~ $
```

With the virtualenv activated, the python and pip binaries point to the local Python 3 variations, so we don’t need to append the 3.7 to all of our commands. 

```bash
(experiment) ~ $ echo $PATH
/home/user/venvs/experiment/bin:/home/user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/user/.local/bin:/home/user/bin

(experiment) ~ $ which python
~/venvs/experiment/bin/python

(experiment) ~ $ pip list
Package    Version
---------- -------
pip        19.3.1
setuptools 42.0.2
```

To remove the virtualenv’s contents from our $PATH, we will utilize the deactivate script that the virtualenv provided.

```bash
(experiment) ~ $ deactivate
```

## Virtualenvwrapper

```bash
# install
    $ pip install virtualenvwrapper

# setup workon area
    $ mkdir -p ~/.virtualenvs
    $ export WORKON_HOME=~/.virtualenvs

# add wrapper functions
    $ source ~/.local/bin/virtualenvwrapper.sh

# using virtualenvwrapper
    $ mkvirtualenv mynewproj
    $ workon mynewproj

# example of python3 project (virtualenvwrappers)
    $ mkvirtualenv --python=$(which python2) site2
    $ workon site2
    $ pip install django==2.1.3
```


## DirEnv

We can use a tool like `dirEnv` to automate virtualenv or virtualenvwrapper tools when we enter a project directory.

For installation on macOS:

```bash
$ brew install direnv
```

Setup and configuring DirEnv for a python environment in bash:

```bash
cat <<-'DIRENV_CONFIG' > ~/.direnvrc
layout_virtualenv() {
  local venv_path="$1"
  source ${venv_path}/bin/activate
}

layout_virtualenvwrapper() {
  local venv_path="${WORKON_HOME}/$1"
  layout_virtualenv $venv_path
}
DIRENV_CONFIG

eval "$(direnv hook bash)"
```

```bash
# setup 
    $ export WORKON_HOME=~/.virtualenvs
    $ source ~/.local/bin/virtualenvwrapper.sh
# create virtualenv 
    $ mkvirtualenv deployprojs
# configuring and allowing direnv
    $ mkdir -p myweb && cd myweb
    $ echo 'layout virtualenv $HOME/.virtualenvs/deployprojs' > .envrc
    $ direnv allow
```
Save the packages in a package manifests for future use on another machine, we can run:

```bash
    $ pip freeze > requirements.txt
```

This will capture our packages for future use in a requirements.txt file. On a new system, we can switch to the appropriate virtualenv, and then install the packages again:

```bash
    $ pip install -r requirements.txt
```
