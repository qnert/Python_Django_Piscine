#!/bin/bash

if [ ! -d 'Django' ]; then
    python3 -m venv ./venv

    source ./venv/bin/activate

    pip install -r requirements.txt --break-system-packages

    pip freeze
fi
