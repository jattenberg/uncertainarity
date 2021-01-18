#!/bin/bash

set -e

if ! command -v virtualenv &> /dev/null 
then
    echo "virtualenv could not be found"
    pip install pipx;
else
  venv_path=$(which virtualenv);
  echo "using venv located at $venv_path"
fi

venv="venv"
echo "making virtualenv: $venv"

virtualenv $venv

$venv/bin/pip install --upgrade pip
#$venv/bin/pip install --upgrade numpy pandas sklearn statsmodels numba
#$venv/bin/pip install -Iv cython==0.29.17
$venv/bin/pip install -e .
