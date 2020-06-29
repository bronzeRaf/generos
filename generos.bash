#!/bin/bash

# Count arguments
if [ $# -eq 0 ]; then
    echo "No arguments provided. Please give the GRS Filename"
    exit 1
fi

# Run the DSL
python3 dsl/run_generos_model.py $1
sudo chmod 777 -R models/generos.xmi

# Run the Generator
python3 packageGenerator.py models/generos.xmi
sudo chmod 777 -R workspace
