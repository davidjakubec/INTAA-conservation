#!/usr/bin/env python3

from sys import argv
from _PDB_utils import read_chains


def main(PDB_file, sequence_database):
    PDB_ID, chains = read_chains(PDB_file)


if __name__ == '__main__':
    main(*argv[1:])


