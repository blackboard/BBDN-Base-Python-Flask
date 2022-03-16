# Base Python project

## HOW TO

### Install

We recommend the use of our [Taskfile](https://github.com/adriancooney/taskfile) to simplify the use 
```
use the

pip install -r pip-requirements.txt
```

### Setup
```
source venv/bin/activate

export PYTHONPATH='<path to project>/BBDN-LTI-Tool-Provider-Python/app'
```

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
