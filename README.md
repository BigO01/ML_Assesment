## Pre-requisite

- pyenv
- python 3.10.6
    - To install python with pyenv on linux, follow [this](https://devcamp.com/trails/development-environments/campsites/python-development-environment/guides/how-to-install-work-pipenv-linux) blog
    - To install python with pyenv on Mac OS, follow [this](https://codinggear.blog/how-to-install-fastapi-on-computer-using-pip/) blog

`Pipenv` is a tool that aims to bring the best of all packaging worlds
(bundler, composer, npm, cargo, yarn, etc.) to the Python world.

It automatically creates and manages a virtualenv for your projects, as
well as adds/removes packages from your `Pipfile` as you
install/uninstall packages. It also generates the ever-important
`Pipfile.lock`, which is used to produce deterministic builds.

### Installation
If you\'re using Mac OS:

    brew install pipenv
    
Or, if you\'re using Linux:

    # pip install --user pipenv
## Setup

Enable pipenv shell

    $ pipenv shell

Install all dependencies locked in ***pipfile.lock***

    $ pipenv install
## Run Server

    $ python main.py 
    
   It runs the main.py file containing basic code to test FASTAPI server
