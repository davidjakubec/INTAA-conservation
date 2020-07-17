# INTAA-conservation

## About

INTAA-conservation implements the evolutionary conservation calculations featured in the [Amino Acid Interactions (INTAA) web server](https://bioinfo.uochb.cas.cz/INTAA/); however, it can also be used as a stand-alone tool.

## Installation

Extract the archive, then install the Python dependencies: `python3 -m pip install -r requirements.txt`. The script `database/download_Swiss-Prot.sh` can be used to download an example sequence database.

### Requirements

The [HMMER](http://hmmer.org/) software package, including the Easel tools, must be installed and the programs available in the `$PATH`. All development and testing is done using HMMER 3.3.

## Usage

Use
```
code/INTAA-conservation.py PDB_file sequence_database
```
to calculate the information content for the amino acid residues in the `PDB_file` using the `sequence_database` to construct the multiple sequence alignments.
