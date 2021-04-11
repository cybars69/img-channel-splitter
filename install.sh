#!/bin/sh
pip uninstall pillow -y
pip3 uninstall pillow -y
sudo apt-get install libjpeg-dev
pip3 install --no-cache-dir -I pillow
pip3 install numpy

echo
echo

./main.py -h