# Base Template Python project

This is a template repository with the essentials to build a Python project using Flask.

## HOW TO

### Install

We recommend the use of our [Taskfile](https://github.com/adriancooney/taskfile)

You can check the [Contributing](.github/contributing.md)

### Run

```
python app.py
```

### Configuration

If you want to modify your configuration it's best to create a `.env` file. These are the possible values you can change:

```
PORT='5000'
DOMAIN='localhost'
AWS_KEY_ID = 'whatever'
AWS_KEY_ID_SECRET = 'key'
```

### Docker

To build the docker image run the following command on the root folder

```
docker build . -f docker/Dockerfile -t <name-for-container>
```

### MKDocs

We suggest the use of [Mkdocs](https://www.mkdocs.org/getting-started/) for documentation.

#### Install

```
pip install mkdocs
```

#### Serve

```
mkdocs serve
```

#### Pre-commit hooks

This project has a set of hooks for [pre-commit](https://pre-commit.com/) for formatting.

To install this hooks into your repo, run.

```
pre-commit install
```
