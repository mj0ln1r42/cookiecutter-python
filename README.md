# [`/cookiecutter-python`](https://github.com/mj0ln1r42/cookiecutter-python)

Welcome to my Python template project!

This is a cookiecutter template project used to create the rest of our project repos. The project generated comes already set up with its own readme, directory structure, dev container, and tooling

## Setup
To generate a project with this template you first need to [install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter):
```
pipx install cookiecutter
```

## Usage
Follow these steps to create a new project using this template!
- Create a new repo in github
- Clone the empty repo to your local
- From a shell terminal in the cloned directory: ```cookiecutter --output-dir .. --overwrite-if-exists git+ssh://git@github.com/mj0ln1r42/cookiecutter-python repo_name=${PWD##*/}```
- Enter a Project Name! The rest of the parameters are defaulted for you!
- Push changes! The commit has already been created for you!
