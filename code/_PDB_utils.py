

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import Polypeptide


def read_chains(PDB_file):
    parser = PDBParser(PERMISSIVE=True, QUIET=True)
    PDB_ID = PDB_file.split('.')[0]
    structure = parser.get_structure(PDB_ID, PDB_file)
    model = structure[0]
    chains = dict()
    for chain in model:
        residues = []
        for residue in chain:
            het, resseq, icode = residue.id
            if (het == ' '):
                residues.append((residue.resname, resseq, icode))
        chains[chain.id] = residues
    return PDB_ID, chains


def write_FASTAs(PDB_ID, chains):
    polypeptide_IDs = []
    for chain_ID, residues in chains.items():
        if Polypeptide.is_aa(residues[0][0]):
            polypeptide_ID = '{}_{}'.format(PDB_ID, chain_ID)
            polypeptide_IDs.append(polypeptide_ID)
            sequence = []
            for resname, resseq, icode in residues:
                try:
                    sequence.append(Polypeptide.three_to_one(resname))
                except KeyError:
                    sequence.append('X')
            with open('{}.fasta'.format(polypeptide_ID), mode='w') as f:
                f.write('>{}\n'.format(polypeptide_ID))
                f.write('{}\n'.format(''.join(sequence)))
    return polypeptide_IDs


if __name__ == '__main__':
    from sys import argv
    PDB_ID, chains = read_chains(argv[1])
    polypeptide_IDs = write_FASTAs(PDB_ID, chains)


