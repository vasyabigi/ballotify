Ballotify 2.0
==============

## Installation ##

### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv ballotify
```

#### For virtualenv ####
```bash
virtualenv ballotify
source ballotify/bin/activate
```

### Clone the code ###

```bash
git clone YOUR-CUSTOM-REPO-LINK/ballotify.git
```

### Install requirements ###
```bash
cd ballotify
pip install -r reqs/dev.txt
```

### Configure project ###
```bash
cp ballotify/settings/dev.py.example ballotify/settings/dev.py
vi ballotify/settings/dev.py
```

### Sync/migrate database ###
```bash
python manage.py migrate
```

## Running Django ##
```bash
python manage.py runserver
```
