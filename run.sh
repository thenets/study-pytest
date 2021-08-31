#!/bin/bash

source ~/venvs/learn/bin/activate

cd src/

uvicorn main:app --reload
