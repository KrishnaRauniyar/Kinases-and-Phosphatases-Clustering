# Kinases and Phosphatases Clustering

**Kinases and Phosphatases Clustering** helps to cluster the Kinases and Phosphatases dataset into n number of clusters.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

### Cloning the Repository

To get started with the `Kinases and Phosphatases Clustering`, clone the repository from GitHub:

```bash
git clone https://github.com/KrishnaRauniyar/Kinases-and-Phosphatases-Clustering.git
cd Kinases-and-Phosphatases-Clustering/clustermap
```

### Installing the Package
1. It's recommended to create a virtual environment:

```bash
python3 -m venv tsrenv
source tsrenv/bin/activate  # Mac/Linux
tsrenv\Scripts\activate  # Windows
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage
### Using a CSV file as Input
You can pass a CSV file as input to process key generation and then you can use the key generation frequency file to generate Jaccard Similarity. The CSV file should have the following format:

|protein         |chain        |
|----------------|-------------|
|1GTA            |A            |
|1GTB            |A            |
|1LBE            |A            |

The Jaccard Similarity should have the following format.

|----------------------------------|
|2R92_P_10_A;0,0,0,0,0,3,2,2,......|
|2R92_P_11_C;0,0,0,0,0,4,0,0,......|
|2R92_P_12_C;0,0,0,0,0,2,1,0,......|
|2R92_P_13_A;0,0,0,0,0,4,1,2,......|

To run the code:

```python
python clustermap_n.py -p (jaccard input csv file) -n (number of clusters)
```

Example code:

```python
python clustermap_n.py -p jaccard.csv -n 5
```

## Result
- Two files will be generated
    1. clustermap.png (This is the clustermap created with n number of cluster color)
    2. clustermap.csv (This contains the number of clusters with their rows containing kinases and phosphatases)