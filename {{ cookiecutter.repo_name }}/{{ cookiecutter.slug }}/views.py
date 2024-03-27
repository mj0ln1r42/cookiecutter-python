from {{ cookiecutter.slug }} import app

@app.route('/')
def index():
    return '{{ cookiecutter.project_description }}'
