# CoAuthorViz
Tool to visualize human-machine collaborative writing using the CoAuthor Dataset

**Paper to cite this work**: Shibani, A., Rajalakshmi, R., Mattins, F., Selvaraj, S & Knight, S. (2023). Visual representation of co-authorship with GPT-3: Studying human-machine interaction for effective writing. In Proceedings of the 16th international conference on educational data mining (pp. xx).  International Educational Data Mining Society.

## Directory Descriptions

- **scripts:** python scripts that generate the CoAuthorViz graph and summary statistics 
- **notebooks:** python notebooks that perform analysis on summary statistics
- **csv:** comma seperated value files of the analysis results
- **plots:** plots generated from the analysis performed
- **CoAuthorViz-dataset:** new dataset based on the [CoAuthor dataset](https://coauthor.stanford.edu/).

## Dependencies

### System utils

- wget
- unzip
- git
- python
- pip

If using a Debian-based development environment (Ubuntu/Debian/WSL), users can install packages using the following command: <br>
`$ sudo apt install wget unzip git python3 python3-pip`

### Python packages

- pandas
- numpy
- nltk
- pillow
- scipy

Python packages can be installed using the following command: <br>
`$ python3 -m pip install pandas numpy nltk pillow` <br>
A requirements file has been included with the exact package versions used in the code. <br>
This can be installed with: <br>
`$ python3 -m pip install -r requirements.txt`

## Instructions for Downloading the CoAuthor Dataset

A bash script has been included to help download the CoAuthor dataset. <br>
This can be run by executing the following command: <br>
`$ ./download_dataset.sh`

## Getting Started

The following instructions contain recommended steps to recreate the work. <br>
You can follow along or use other alternatives.

1. Install the dependencies <br>
`$ sudo apt install wget unzip git python3 python3-pip`

2. Clone the repository and `cd` into the directory <br>
`$ git clone <REPO_URL>` <br>
`$ cd <REPO_NAME>/`

3. Create a new python virtual environment <br>
`$ python3 -m venv <VENV_NAME>` <br>
`$ source <VENV_NAME>/bin/activate`

4. Install the python packages <br>
`$ python3 -m pip install -r requirements.txt`

5. Download the CoAuthor dataset <br>
`$ ./download_dataset.sh`

6. Run `scripts/main.py` and pass any `jsonl` file from the dataset as an argument <br>
`$ python3 scripts/main.py coauthor-v1.0/<FILE_NAME>.jsonl`

7. Done! The graph is generated as `<FILE_NAME>.png` and the summary statistics are printed in `stdout`.
