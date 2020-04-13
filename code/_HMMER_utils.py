

import subprocess


def generate_MSAs(polypeptide_IDs, sequence_database):
    for polypeptide_ID in polypeptide_IDs:
        subprocess.run('phmmer -o /dev/null -A {}.sto --notextw {}.fasta {}'.format(polypeptide_ID, polypeptide_ID, sequence_database).split())


if __name__ == '__main__':
    from sys import argv
    polypeptide_IDs = [i.split('.')[0] for i in argv[1:-1]]
    sequence_database = argv[-1]
    generate_MSAs(polypeptide_IDs, sequence_database)


