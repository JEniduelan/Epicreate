#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Oops!
You might need to install the latest python to play the application!
To install Python3, just go to https://www.python.org/downloads/" >&2
    exit 1
fi

# Create virtual environment 
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# Install packages from requirements.txt
pip3 install -r requirements.txt

# run application
python3 main.py