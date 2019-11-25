# VirtualEnv for Python

## Install Python3

*Important*: ```make altinstall``` causes it to not replace the built in python executable when installing with python source code. Ensure that `secure_path` in /etc/sudoers file includes /usr/local/bin. The line should look something like this:
```Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin```

## Using Venv for python3

**Virtualenvs** allow you to create sandboxed Python environments. In Python 2, you need to install the virtualenv package to do this, but with Python 3 it’s been worked in under the module name of venv.

To create a virtualenv, we’ll use the following command:

```bash
$ python3 -m venv <PATH FOR VIRTUALENV>
```

The -m flag loads a module as a script, so it looks a little weird, but “python3.6 -m venv” is a standalone tool. This tool can even handle its own flags.

Let’s create a directory to store our virtualenvs called venvs. From here we create an experiment virtualenv to see how they work.

```bash
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
│   ├── easy_install-3.5
│   ├── pip
│   ├── pip3
│   ├── pip3.5
│   ├── python -&gt; python3.5
│   ├── python3 -&gt; python3.5
│   └── python3.5 -&gt; /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
├── include
├── lib
│   └── python3.5
│       └── site-packages
└── pyvenv.cfg
```

Virtualenvs are local Python installations with their own site-packages, and they do absolutely nothing for us by default. To use a virtualenv, we need to activate it. We do this by sourcing an activate file in the virtualenv’s bin directory:

```bash
$ source venvs/experiment/bin/activate
(experiment) ~ $
```

Notice that our prompt changed to indicate to us what virtualenv is active. This is part of what the activate script does. It also changes our $PATH:

```bash
(experiment) ~ $ echo $PATH
/home/user/venvs/experiment/bin:/home/user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/user/.local/bin:/home/user/bin

(experiment) ~ $ which python
~/venvs/experiment/bin/python

(experiment) ~ $ python --version
Python 3.6.4

(experiment) ~ $ pip list
Package    Version
---------- -------
pip        9.0.1
setuptools 28.8.0

(experiment) ~ $ deactivate

$ which python
/usr/bin/python
```

With the virtualenv activated, the python and pip binaries point to the local Python 3 variations, so we don’t need to append the 3.6 to all of our commands. To remove the virtualenv’s contents from our $PATH, we will utilize the deactivate script that the virtualenv provided.

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

## Using `direnv` to automate

We can use a tool like `DirEnv` to do automation of our virtualenv or virtualenvwrapper tools when we enter a project directory.

For installation, on macOS, we can use 
```bash
$ brew insdtall direnv
```
We can setup and configure DirEnv for a python environment with this (in bash):

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

## Using `pipenv` to automate

Coming from pip and virtualenvs, and how they allow us to manage our dependency versions, for a development project, we will leverage a new tool to manage our project’s virtualenv and install dependencies. This tool is called **pipenv**. Let’s install pipenv for our user and create a Python 3 virtualenv for our project:

```bash
$ pip3.6 install --user pipenv
$ pipenv --python $(which python3.6)
```

Rather than creating a requirements.txt file for us, pipenv has created a Pipfile that it will use to store virtualenv and dependency information. 

To activate our new virtualenv, we use the command 

```bash
$ pipenv shell
``` 

To deactivate it we use the command 

```bash
$ exit
```

instead of ```deactivate```.


## venv vs virtualenv

The `venv` module was added to the standard library in Python 3.3. The `pyvenv` command is a wrapper around the venv module, and you should strongly consider avoiding the wrapper and just using the module directly, since it solves so many problems inherent with wrapper scripts, particularly when you have multiple versions of Python installed.

Its implementation was based heavily on virtualenv which had existed for a long time prior to that, but they are not entirely identical. venv by nature of being part of Python itself has access to the internals of Python which means it can do things the right way with far fewer hacks. For example, virtualenv has to copy the Python interpreter binary into the virtual environment to trick it into thinking it's isolated, whereas venv can just use a configuration file that is read by the Python binary in its normal location for it to know it's supposed to act like it's in a virtual environment. So venv can be thought of virtualenv done right, with the blessing and support of the Python developers.

Moreover, if you are running a version of Python that has venv in the standard library, then you can use it without having to install anything, which is another added bonus. (Or at least you can unless you're using a distribution that splits up the standard library into several optional packages.) If you're not using such a version, then you'll need to use the third party virtualenv module, hacks and all. And you can still install virtualenv under Python >= 3.3 if you really want to, but I don't see why you'd do that if you had the choice. And naturally it's impossible to use venv with Python < 3.3 since it requires those internal changes.

```bash
# Python3:
    $ python -m venv myapp
```
