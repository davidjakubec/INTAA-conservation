

import subprocess


def generate_MSAs(polypeptide_IDs, sequence_database):
    for polypeptide_ID in polypeptide_IDs:
        subprocess.run('phmmer -o /dev/null -A {}.sto --notextw {}.fasta {}'.format(polypeptide_ID, polypeptide_ID, sequence_database).split())


def calculate_sequence_weights(polypeptide_IDs):
    for polypeptide_ID in polypeptide_IDs:
        with open('{}.stow'.format(polypeptide_ID), mode='w') as f:
            subprocess.run('esl-weight {}.sto'.format(polypeptide_ID).split(), stdout=f)


if __name__ == '__main__':
    from sys import argv
    polypeptide_IDs = [i.split('.')[0] for i in argv[1:-1]]
    sequence_database = argv[-1]
    generate_MSAs(polypeptide_IDs, sequence_database)
    calculate_sequence_weights(polypeptide_IDs)


