# Support Documentation

## Installation

Install MkDocs using:

    pip3 install mkdocs

Once MkDocs is installed, this material can be installed using:

    pip3 install mkdocs-material

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

For further configuration and other support related documentaiton, here is the [best source:](https://squidfunk.github.io/mkdocs-material/getting-started/)
