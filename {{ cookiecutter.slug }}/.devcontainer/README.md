# [`{{ cookiecutter.project_name }}`]({{ cookiecutter.repo_url }})
## [`/.devcontainer`]({{ cookiecutter.repo_url }}/.devcontainer)

## {{ cookiecutter.project_name }} Dev Container
Welcome to the {{ cookiecutter.project_name }} Dev Container!

This project is configured to construct a uniform development environment in the form of a docker container, specifically set up to develop, build, and run this project.  This process can be a bit hefty, so we make strides to be as redundant with the bare-metal development environment as well - that is, all extensions installed in the dev container should be recommended in the bare-bones project and vice-versa. You know, in case you were saving all your system resources for bot nets, cyrpto mining, or distributed crowd-sourcing RNA protein folding, idk it's honestly none of my business. 

## Initial Setup
To begin developing in this container, you'll first need to seolve these two riddles:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/), or [Rancher Desktop](https://rancherdesktop.io) (and make sure it's running.)
2. Install the "Remote Development" extension pack by Microsoft in VSCode. (It should have been recommended to you already by VSCode itself.)

## Running the Dev Container
Running the container is easy, just click on the green box in the bottom left of the VSCode IDE and click "Reopen in Container". Boom, bam, you're ready to go.
