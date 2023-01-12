# SLAC-GRAPH
Tool to visualize human-machine collaborative writing.

## Directory Descriptions

- **scripts:** python scripts to to generate the graph and summary statistics 
- **notebooks:** python notebooks used to perform analysis on summary statistics

## Dependencies

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
`$ python3 -m pip install pandas numpy nltk pillow` <br>
A requirements file has also been included with the exact package versions used. <br>
It can be installed with: <br>
`$ python3 -m pip install -r requirements.txt`

## Instructions for Downloading the CoAuthor Dataset

A bash script has been included to help download the [CoAuthor dataset](https://coauthor.stanford.edu/). <br>
It can be run by executing the following command: <br>
`$ ./download_dataset.sh`

## Getting Started

The following instructions contain the recommended steps necessary to recreate the work. <br>
You can follow along or use any alternative methods if you prefer.

1. Install the dependencies <br>
`$ sudo apt install wget unzip git python3 python3-pip`
2. Clone the repository and `cd` into the directory <br>
`$ git clone https://github.com/srivarshan-s/SLAC-GRAPH.git` <br>
`$ cd SLAC-GRPAH/`
3. Create a new python virtual environment <br>
`$ python3 -m venv <VENV_NAME>` <br>
`$ source <VENV_NAME>/bin/activate`
4. Install the python packages <br>
`$ python3 -m pip install -r requirements.txt`
5. Download the CoAuthor dataset <br>
`$ ./download_dataset.sh`
6. Run `scripts/main.py` and pass any `JSONL` file from the dataset as an argument <br>
`$ python3 scripts/main.py coauthor-v1.0/<FILE_NAME>`
7. Done! The graph is generated as `<FILE_NAME>.png` and the summary statisitcs are printed in `stdout`