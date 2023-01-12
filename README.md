# SLAC-GRAPH
Tool to visualize human-machine collaborative writing.

## Directory descriptions
- **notebooks:** python notebooks used to generate the graph and summary statistics
- **scripts:** python scripts to to generate the graph and summary statistics 

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
`$ pip3 install pandas numpy nltk pillow`

## Instructions for downloading the CoAuthor dataset

A bash script has been included to help download the CoAuthor dataset. <br>
It can be run by executing the following command: <br>
`$ ./download_dataset.sh`
