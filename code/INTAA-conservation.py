#!/usr/bin/env python3

from sys import argv
from _PDB_utils import read_chains, write_FASTAs


def main(PDB_file, sequence_database):
    PDB_ID, chains = read_chains(PDB_file)
    polypeptide_IDs = write_FASTAs(PDB_ID, chains)


if __name__ == '__main__':
    main(*argv[1:])


