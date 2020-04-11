

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import Polypeptide


def read_chains(PDB_file):
    parser = PDBParser(PERMISSIVE=True)
    PDB_ID = PDB_file.split('.')[0]
    structure = parser.get_structure(PDB_ID, PDB_file)
    model = structure[0]
    chains = dict()
    for chain in model:
        residues = []
        for residue in chain:
            het, resseq, icode = residue.id
            if (het == ' ') and (icode == ' '):
                residues.append((residue.resname, resseq))
        chains[chain.id] = residues
    return PDB_ID, chains


if __name__ == '__main__':
    from sys import argv
    PDB_ID, chains = read_chains(argv[1])


