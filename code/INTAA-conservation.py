#!/usr/bin/env python3

from sys import argv
from _PDB_utils import read_chains, write_FASTAs
from _HMMER_utils import generate_MSAs, calculate_sequence_weights


def main(PDB_file, sequence_database):
    PDB_ID, chains = read_chains(PDB_file)
    polypeptide_IDs = write_FASTAs(PDB_ID, chains)
    generate_MSAs(polypeptide_IDs, sequence_database)
    calculate_sequence_weights(polypeptide_IDs)


if __name__ == '__main__':
    main(*argv[1:])


