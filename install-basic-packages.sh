#!/bin/bash

set -ex

sudo dnf install -y virtualenv python3.8

rm -rf ~/venvs/learn

virtualenv --system-site-packages -p python3.8 ~/venvs/learn
source ~/venvs/learn/bin/activate
pip install --upgrade \
    -r requirements.txt \
    -r requirements-dev.txt
