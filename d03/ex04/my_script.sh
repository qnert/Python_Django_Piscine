#!/bin/bash

if [ ! -d 'Django' ]; then
    python3 -m venv ./Django
fi

source ./Django/bin/activate

pip3 install -r requirements.txt --break-system-packages

deactivate
