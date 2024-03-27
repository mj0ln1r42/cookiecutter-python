# [`cookiecutter-python (flask)`](https://github.com/mj0ln1r42/cookiecutter-python/tree/flask)

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
- From a shell terminal in the cloned directory:
```
cookiecutter --output-dir .. --overwrite-if-exists git+ssh://git@github.com/mj0ln1r42/cookiecutter-python --checkout flask project_name=${PWD##*/} repo_name=${PWD##*/}
```
- Enter a Project Name! The rest of the parameters are defaulted for you!

### Local Use
To use this template locally (ie for development), repeat the steps above but use this instead, changing the path to match your local project repo path.

```
cookiecutter --output-dir .. --overwrite-if-exists /mnt/c/Dev/mj0ln1r42/cookiecutter-python project_name=${PWD##*/} repo_name=${PWD##*/}
```

### Replay Generation
Previously generated projects can be regenerated without having to type in everything again

Remote (standard):
```
cookiecutter --output-dir .. --overwrite-if-exists --replay git+ssh://git@github.com/mj0ln1r42/cookiecutter-python --checkout flask
```

Local (for development):
```
cookiecutter --output-dir .. --overwrite-if-exists --replay /mnt/c/Dev/mj0ln1r42/cookiecutter-python
```
