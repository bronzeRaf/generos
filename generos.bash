#!/bin/bash



python3 dsl/run_generos_model.py $1
sudo chmod 777 -R models/generos.xmi

python3 packageGenerator.py models/generos.xmi

sudo chmod 777 -R workspace
