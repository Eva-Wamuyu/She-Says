#!/bin/bash


python3 -m venv venv

. venv/bin/activate


if [ -x "$(command -v pipenv)" ]; then

pipenv install - r requirements.txt

else

pip install -r requirements.txt

fi

python3 app.py
