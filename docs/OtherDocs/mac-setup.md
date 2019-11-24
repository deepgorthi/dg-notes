# MacOS Setup

## Install Homebrew

Make sure Xcode Command Line tools are installed
```
xcode-select --install
```

Install Homebrew by running this command
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Install Docker

```
brew install docker
```


## Install Python3
```
brew install python3
```


## Install wget with IRI support.
```
brew install wget --with-iri
```


## Install AWS CLI and Shell

Install awscli and configure AWS with Secret Access Keys
```
pip3 install awscli
aws configure
```

Install boto
```
pip3 install boto
```

Install [AWS Shell](https://github.com/awslabs/aws-shell)
```
pip3 install aws-shell
```


## Virtualenv
Virtualenv is a tool that creates an isolated Python environment for each of your projects. For a particular project, instead of installing required packages globally, it is best to install them in an isolated folder in the project (say a folder named venv), that will be managed by virtualenv. The advantage is that different projects might require different versions of packages, and it would be hard to manage that if you install packages globally.

**Installation**
```
pip3 install virtualenv
```

**Usage**

Let's say you have a project in a directory called myproject. To set up virtualenv for that project:
```
cd myproject/
virtualenv venv --distribute
```
If you want your virtualenv to also inherit globally installed packages (like IPython or Numpy mentioned above), use:
```
virtualenv venv --distribute --system-site-packages
```
These commands create a venv subdirectory in your project where everything is installed. You need to activate it first though (in every terminal where you are working on your project):
```
source venv/bin/activate
```
You should see a (venv) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv. Now when you install something:
```
pip3 install <package>
```
It will get installed in the venv folder, and not conflict with other projects.
*Important*: Remember to add venv to your project's .gitignore file so you don't include all of that in your source code!

## Virtualenvwrapper
Virtualenvwrapper is a set of extensions that includes wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

Main features include:

- Organizes all of your virtual environments in one place.
- Wrappers for managing your virtual environments (create, delete, copy).
- Use a single command to switch between environments.
- Tab completion for commands that take a virtual environment as argument.

**Installation**
```
pip3 install virtualenvwrapper
```

**Usage**

Create a new virtual environment. When you create a new environment it automatically becomes the active environment:
```
mkvirtualenv [env name]
```
Remove an existing virtual environment. The environment must be deactivated (see below) before it can be removed:
```
rmvirtualenv [env name]
```
Activate a virtual environment. Will also list all existing virtual environments if no argument is passed:
```
workon [env name]
```
Deactivate the currently active virtual environment. Note that workonwill automatically deactivate the current environment before activating a new one:
```
deactivate
```


## Adding SSH key to GitHub 

To generate and add SSH keys to github, first create a ssh key with passphrase and it will be placed in ~/.ssh 
```
Pradeeps-MBP:github-repos pradeepgorthi$ ssh-keygen -t rsa -b 4096 -C "my@email.com"
```

Run `ssh-agent` in the background
``` 
Pradeeps-MBP:github-repos pradeepgorthi$ eval "$(ssh-agent -s)"
```

Create a config file and add the following lines to the file for automatically loading keys and storing passphrase in keychain
```
Pradeeps-MBP:github-repos pradeepgorthi$ vi ~/.ssh/config
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
```

Add SSH private key to ssh-agent
```
Pradeeps-MBP:github-repos pradeepgorthi$ ssh-add -K ~/.ssh/id_rsa
Enter passphrase for /Users/pradeepgorthi/.ssh/id_rsa:
Identity added: /Users/pradeepgorthi/.ssh/id_rsa
```

Copy the public key to add it to GitHub account via the website in the Settings section. 
```
Pradeeps-MBP:github-repos pradeepgorthi$ pbcopy < ~/.ssh/id_rsa.pub
```

Check if it is working
```
Pradeeps-MBP:github-repos pradeepgorthi$ ssh -T git@github.com
The authenticity of host 'github.com (192.30.253.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.253.112' (RSA) to the list of known hosts.
Hi deepgorthi! You've successfully authenticated, but GitHub does not provide shell access.
```


## VSCode

After installing VSCode, need to change the user settings to support CloudFormation and easy coding!

Press F1 to search for User settings and open settings.json file to add the following lines. 

```json
{
    "python.dataScience.askForKernelRestart": false,
    "files.autoSave": "afterDelay",
    "gitlens.views.repositories.files.layout": "tree",
    "window.zoomLevel": 1,
    "yaml.schemas": {
        "file:///Users/pradeepgorthi/.vscode/extensions/docsmsft.docs-yaml-0.2.3/schemas/toc.schema.json": "/toc\\.yml/i"
    },
    "yaml.customTags": [
        "!And",
        "!If",
        "!Not",
        "!Equals",
        "!Or",
        "!FindInMap sequence",
        "!Base64",
        "!Cidr",
        "!Ref",
        "!Sub",
        "!GetAtt",
        "!GetAZs",
        "!ImportValue",
        "!Select",
        "!Select sequence",
        "!Split",
        "!Join sequence"
    ],
    "yaml.format.enable": true,
    "aws.telemetry": "Disable",
    "aws.profile": "default",
    "aws.onDefaultRegionMissing": "add",
    "indenticator.inner.showHighlight": true,
}
```