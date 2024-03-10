
ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG USER="vscode"
ARG USER_HOME="/home/${USER}"

RUN apt-get update \
	&& ACCEPT_EULA=Y apt-get install --no-install-recommends -y dos2unix

# Install our python dependencies in our container
COPY requirements.txt /tmp/pip/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip/requirements.txt \
	&& rm -rf /tmp/pip

# Copy user specific .bash_aliases and make it linux friendly
COPY .devcontainer/.bash_aliases ${USER_HOME}/.bash_aliases
RUN dos2unix ${USER_HOME}/.bash_aliases \
	&& apt-get --purge remove -y dos2unix
