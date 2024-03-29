# [`{{ cookiecutter.project_name }}`]({{ cookiecutter.repo_url }})

{{ cookiecutter.project_description }}

## Setup
To set up your project for development, first we need `pipx` and `poetry`
```
pip install pipx
pipx ensurepath
pipx install poetry
```

## Installing
Easy.
```
poetry install
```

## Tooling
This project is set up to use the following development utilities to make all of our lives just a little bit easier:
- **[Black](https://black.readthedocs.io/en/stable/)** - Linting & Formatting:
This is defined as VSCode's default formatter, and is automatically invoked when you save a file.
- **[iSort](https://pycqa.github.io/isort/)** - Import Statement Ordering:
This sorts our import statements into distinctive layers and keeps things clean for us. Invoked automatically on file save.
- **[Poetry](https://python-poetry.org/)** - Package Management:
This lets us manage our dependencies and packaging needs gracefully.
- **[MyPy](https://mypy-lang.org/)** - Static Type Checking:
We highly encourage using typed code as much as possible to allow for explicit programming. (the [py.typed]({{ cookiecutter.repo_url }}/src/{{ cookiecutter.slug }}/py.typed) file in /src/{{ cookiecutter.slug }} lets MyPy know this package is typed.)
- **[PyTest](https://docs.pytest.org/)** - Test Execution:
It's important to keep our code tested, so we're using PyTest integrated directly with VSCode to make sure things keep working. Check out our [/tests]({{ cookiecutter.repo_url }}/tests)

---
This project was created from my cookiecutter python repo, [`mj0ln1r42/cookiecutter-python`](https://github.com/mj0ln1r42/cookiecutter-python)