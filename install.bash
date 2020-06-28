#!/bin/bash

# Unzip Install
sudo apt install unzip

# Python 3.8 install
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt install python3-pip

# PyEcore install
pip3 install pyecore

# RyEcoreGen install
pip3 install pyecoregen

# Jinja2 install
pip3 install -U Jinja2

# TextX install
pip3 install textX

# Matplotlib install
#~ python -m pip3 install -U pip
python -m pip3 install -U matplotlib

# NetworkX install
pip3 install networkx

# Weasyprint install
pip3 install weasyprint

# Download and extract Generos
wget https://github.com/bronzeRaf/generos/archive/master.zip
unzip master.zip
