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
The analysis involves three main steps:
### 1. Generate Key Frequency File
First, you need to generate a frequency file that will create the input CSV for the clustering, the key frequency files can be created from the triplets file which we create from the Nuclotide section (https://github.com/KrishnaRauniyar/TSR_NUCLEOTIDE_PACKAGE.git). We just need to specify the acutual directory path of the triplets keys. Use the following command to generate the input file:

```bash
python key_frequency_drug.py -p triplets_directory -H yes
```

#### Parameters:
- -p: Path to the directory containing protein files
- -H: Set to 'no' not to include headers in the output CSV (This is necessary for jaccard similarity calculation)

This will generate an input CSV file with the frequency of triplet keys for each protein.

#### CSV file information as input (input_csv_file.csv)
input_csv_file.csv will have the following format.

|               |            |             |                        |  
|---------------|------------|-------------|------------------------|
| 4NGF_H_15_U   | 4          | 0           | 0                      |
| 5VM9_D_3_A    | 1          | 5           | 9                      |

Here the first column is the protein, second, third and so on are the key1, key2 respectively.



The Jaccard Similarity should have the following format.

```
2R92_P_10_A; 0.000, 0.704, 0.740, 0.555, ...
2R92_P_11_C; 0.704, 0.000, 0.668, 0.719, ...
2R92_P_12_C; 0.740, 0.668, 0.000, 0.757, ...
2R92_P_13_A; 0.555, 0.719, 0.757, 0.000, ...
```

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