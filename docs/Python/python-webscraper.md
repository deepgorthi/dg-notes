# Web Scraping

Creating a folder and initializing the project with

??? "pipenv install --python python3.7 scrapy"
    ```bash
    $ pipenv install --python python3.7 scrapy
        Virtualenv already exists!
        Removing existing virtualenv…
        Creating a virtualenv for this project…
        Pipfile: /Users/pradeepgorthi/Documents/github-repos/webscraper-python/Pipfile
        Using /usr/local/bin/python3.7 (3.7.5) to create virtualenv…
        ⠇ Creating virtual environment...Already using interpreter /usr/local/opt/python/bin/python3.7
        Using base prefix '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7'
        New python executable in /Users/pradeepgorthi/.local/share/virtualenvs/webscraper-python-TotDRkD-/bin/python3.7
        Also creating executable in /Users/pradeepgorthi/.local/share/virtualenvs/webscraper-python-TotDRkD-/bin/python
        Installing setuptools, pip, wheel...
        done.
        Running virtualenv with interpreter /usr/local/bin/python3.7

        ✔ Successfully created virtual environment! 
        Virtualenv location: /Users/pradeepgorthi/.local/share/virtualenvs/webscraper-python-TotDRkD-
        Installing scrapy…
        Adding scrapy to Pipfile's [packages]…
        ✔ Installation Succeeded 
        Pipfile.lock not found, creating…
        Locking [dev-packages] dependencies…
        Locking [packages] dependencies…
        ✔ Success! 
        Updated Pipfile.lock (00acc2)!
        Installing dependencies from Pipfile.lock (00acc2)…
        🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 25/25 — 00:00:03
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
    ```

Activating the pipenv shell using:
```bash
$ pipenv shell
    Launching subshell in virtual environment…
    bash-5.0$  . /Users/pradeepgorthi/.local/share/virtualenvs/webscraper-python-TotDRkD-/bin/activate
    (webscraper-python) bash-5.0$
```