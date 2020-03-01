# MkDocs Website Setup

## Installation

Install MkDocs using:

    pip3 install mkdocs

Once MkDocs is installed, this material theme can be installed using:

    pip install mkdocs mkdocs-material pymdown-extensions pygments mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin

Alternatively, we can use Docker by pulling the image with all dependencies included from Docker repo and running the Docker image locally in the root folder of the project:

    docker pull squidfunk/mkdocs-material
    docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material

## Build and Serve

After the site is configured, it can be served using:

    mkdocs serve

The site can be accessed locally using:

    http://localhost:8000

## Deployment
To deploy the site to GH pages, we can run this:

    mkdocs gh-deploy

For further configuration and other support related documentaiton, here is the [best source](https://squidfunk.github.io/mkdocs-material/getting-started/)


## TravisCI

The site is built using TravisCI.

```YAML
language: python

python: 3.6

branches: master

install:
    - pip install mkdocs mkdocs-material pymdown-extensions pygments mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin  # Install the required dependencies

script: true

before_deploy:
    - mkdocs build --verbose --clean --strict

deploy:
    provider: pages
    skip_cleanup: true
    github_token: $github_token
    local_dir: site
    on:
        branch: master
```