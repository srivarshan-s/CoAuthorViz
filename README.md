# SLAC-GRAPH
Tool to visualize human-machine collaborative writing.

## Directory descriptions

- **scripts:** python scripts to to generate the graph and summary statistics 
- **notebooks:** python notebooks used to perform analysis on summary statistics

## Pre-requisites

### System utils

- wget
- unzip
- git
- python
- pip

If using a Debian-based development environment (Ubuntu/Debian/WSL) the user can install the packages using the following command: <br>
`$ sudo apt install wget unzip git python3 python3-pip`

### Python packages

- pandas
- numpy
- nltk
- pillow

The python packages can be installed using the following command: <br>
`$ pip3 install pandas numpy nltk pillow` <br>
A requirements file has also been included with the exact package versions used. <br>
It can be installed with: <br>
`$ pip3 install -r requirements.txt`

## Instructions for downloading the CoAuthor dataset

A bash script has been included to help download the CoAuthor dataset. <br>
It can be run by executing the following command: <br>
`$ ./download_dataset.sh`
