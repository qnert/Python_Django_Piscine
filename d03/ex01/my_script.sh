#!/bin/bash

if ! which pip3 > /dev/null
then
  brew install python3
fi

pip3 --version

if [ ! -d ./local_lib ]; then
  mkdir ./local_lib
  pip3 install --target ./local_lib/ git+https://github.com/jaraco/path.py.git > ./local_lib/install.log
fi;

python3 my_programm.py
