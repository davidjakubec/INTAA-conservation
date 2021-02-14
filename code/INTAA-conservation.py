#!/usr/bin/env python3

from sys import argv
from _PDB_utils import read_chains, write_FASTAs
from _HMMER_utils import generate_MSAs, calculate_sequence_weights, calculate_information_content
from os import remove


def write_PDB_information_content(PDB_ID, chains, polypeptide_IDs):
    with open('{}.ic'.format(PDB_ID), mode='w') as fo:
        for polypeptide_ID in polypeptide_IDs:
            chain_ID = polypeptide_ID.split('_')[-1]
            try:
                with open('{}.ic'.format(polypeptide_ID)) as fi:
                    chain_information_content = [i.strip().split()[3] for i in fi if (i[0] != '#') and (i[0] != '/') and (i.lstrip()[0] != '-')]
                with open('{}.r'.format(polypeptide_ID)) as fi:
                    chain_freqgap = [i.strip().split()[5] for i in fi if (i[0] != '#') and (i[0] != '/') and (i.lstrip()[0] != '-')]
            except FileNotFoundError:
                continue
            assert len(chains[chain_ID]) == len(chain_information_content) == len(chain_freqgap)
            for (resname, resseq, icode), information_content, freqgap in zip(chains[chain_ID], chain_information_content, chain_freqgap):
                fo.write('\t'.join((chain_ID, resname, str(resseq), icode, information_content, freqgap)) + '\n')


def clean_up(polypeptide_IDs):
    for polypeptide_ID in polypeptide_IDs:
        for ext in ('fasta', 'sto', 'stow', 'ic', 'r'):
            try:
                remove('{}.{}'.format(polypeptide_ID, ext))
            except FileNotFoundError:
                continue


def main(PDB_file, sequence_database):
    PDB_ID, chains = read_chains(PDB_file)
    polypeptide_IDs = write_FASTAs(PDB_ID, chains)
    generate_MSAs(polypeptide_IDs, sequence_database)
    calculate_sequence_weights(polypeptide_IDs)
    calculate_information_content(polypeptide_IDs)
    write_PDB_information_content(PDB_ID, chains, polypeptide_IDs)
    clean_up(polypeptide_IDs)


if __name__ == '__main__':
    main(*argv[1:])


