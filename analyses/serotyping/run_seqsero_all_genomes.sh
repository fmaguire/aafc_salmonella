#!/bin/bash

for genome in ../genomes/*.fasta;
do
    zcat $genome > $(basename $genome).fasta;
    python2.7 SeqSero.py -m 4 -i $(basename $genome).fasta
    rm $(basename $genome).fasta
done
