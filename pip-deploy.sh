#!/bin/zsh

sudo rm -rf dist
sudo rm -rf build
sudo rm -rf FairPICS.egg-info

python3 setup.py sdist
twine upload dist/*