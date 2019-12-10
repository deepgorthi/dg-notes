# Hugo Website Setup

## Installation

Install Hugo using:

    $ brew install hugo

Once Hugo is installed, new site can be created using:

    $ hugo new site hugo-resume

To apply a specific theme, like devresume, in the root of Hugo webroot folder,

    $ cd themes
    $ git clone https://github.com/deepgorthi/hugo-resume-custom.git


Once that is done, copy config.toml to the webroot folder and change the data as needed:

    $ cp hugo-resume-custom/exampleSite/config.toml

## Build and Serve

After the site is configured, it can be served using:

    hugo server

The site can be accessed locally using:

    http://localhost:1313

## Deployment

To deploy the site to GH pages, we can run this:

    $ ./publish.sh

For further configuration and other support related documentaiton, here is the [best source](https://github.com/cowboysmall-tools/hugo-devresume-theme)