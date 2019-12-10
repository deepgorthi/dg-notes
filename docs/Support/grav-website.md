# Grav Resume Website

## Setup from GitHub

1. Clone the Grav repository from [https://github.com/getgrav/grav]() to a folder in the webroot of your server, e.g. `~/webroot/grav`. Launch a **terminal** or **console** and navigate to the webroot folder:
```
   $ cd grav-resume
   $ git clone https://github.com/getgrav/grav.git
```

2. Install the **plugin** and **theme dependencies** by using the [Grav CLI application](https://learn.getgrav.org/advanced/grav-cli) `bin/grav`:
```
   $ brew install php 
   $ cd grav-resume/grav
   $ bin/grav install
```

Check out the [install procedures](https://learn.getgrav.org/basics/installation) for more information.

To have launchd start php now and restart at login:
```
    $ brew services start php
```

Use the Grav Package Manager or GPM:

```bash
# display all the available plugins
    $ bin/gpm index
# install one or more themes
    $ bin/gpm install <plugin/theme>
```

## Maintaining Grav

```bash
# To update Grav:
    $ bin/gpm selfupgrade
# To update plugins and themes:
    $ bin/gpm update
```