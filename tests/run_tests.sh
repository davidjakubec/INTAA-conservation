#!/bin/bash

SEQUENCE_DATABASE="../database/uniprot_sprot.fasta"

for PDB_FILE in *.pdb
do
	echo "Processing file:" ${PDB_FILE}
	../code/INTAA-conservation.py ${PDB_FILE} ${SEQUENCE_DATABASE}
done


